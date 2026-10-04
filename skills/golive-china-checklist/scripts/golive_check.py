#!/usr/bin/env python3
"""golive_check.py — 上线前自动体检（只读，不提交任何表单）。

检查一个已部署站点的"agent 能自动验证"的部分：HTTPS、ICP 备案号链接、公安备案号链接、
隐私政策/用户协议入口、境外资源依赖、AI 标识/模型公示关键词。人工步骤仍需对照 SKILL.md。

用法:
    python3 golive_check.py https://www.example.com [--ai] [--json]
仅依赖 Python 3.8+ 标准库。结果为提示性质，不代表合规结论。
"""
import argparse, json, re, socket, ssl, sys, urllib.request
from datetime import datetime, timezone
from urllib.parse import urlparse

FOREIGN = ["fonts.googleapis.com", "fonts.gstatic.com", "www.google-analytics.com", "googletagmanager.com",
           "www.google.com/recaptcha", "cdn.jsdelivr.net", "unpkg.com", "cdnjs.cloudflare.com",
           "api.openai.com", "api.anthropic.com", "connect.facebook.net"]

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "golive-china-check/0.1"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.geturl(), r.status, r.read(2_000_000).decode("utf-8", "ignore")

def cert_days_left(host):
    ctx = ssl.create_default_context()
    with socket.create_connection((host, 443), timeout=10) as s:
        with ctx.wrap_socket(s, server_hostname=host) as ss:
            exp = datetime.strptime(ss.getpeercert()["notAfter"], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
    return (exp - datetime.now(timezone.utc)).days

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url"); ap.add_argument("--ai", action="store_true", help="产品含生成式 AI 功能")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    url = a.url if a.url.startswith("http") else "https://" + a.url
    host = urlparse(url).hostname
    res = []
    def add(key, ok, msg, skill):
        res.append({"check": key, "status": "PASS" if ok is True else ("WARN" if ok is None else "FAIL"), "detail": msg, "skill": skill})

    try:
        final, status, html = fetch(url)
    except Exception as e:
        add("reachable", False, f"无法访问: {e}", "china-cloud-cdn-deploy"); html = ""; final = url; status = 0
    if html:
        add("reachable", status == 200, f"HTTP {status} → {final}", "china-cloud-cdn-deploy")
        add("https", final.startswith("https://"), "最终落地为 HTTPS" if final.startswith("https://") else "未跳转到 HTTPS", "china-cloud-cdn-deploy")
    try:
        d = cert_days_left(host); add("cert", d > 14, f"证书剩余 {d} 天", "china-cloud-cdn-deploy")
    except Exception as e:
        add("cert", False, f"证书检查失败: {e}", "china-cloud-cdn-deploy")

    icp = re.search(r"[\u4e00-\u9fa5]ICP[备证]\s*\d+号(-\d+)?", html)
    add("icp_number", bool(icp), f"找到备案号: {icp.group(0)}" if icp else "页面未找到 ICP 备案号（若服务器/CDN 在内地则必需）", "icp-beian")
    add("icp_link", "beian.miit.gov.cn" in html, "备案号链接到 beian.miit.gov.cn" if "beian.miit.gov.cn" in html else "未发现指向 beian.miit.gov.cn 的链接", "icp-beian")
    ga = re.search(r"[\u4e00-\u9fa5]公网安备\s*\d+号", html)
    add("gongan", bool(ga) or None, f"找到: {ga.group(0)}" if ga else "未找到公网安备号（ICP 通过后 30 日内办理）", "gongan-beian")
    add("privacy", bool(re.search(r"隐私政策|隐私协议|个人信息保护", html)) or None, "检查首页是否有隐私政策入口", "pipl-privacy-policy")
    add("terms", bool(re.search(r"用户协议|服务协议|服务条款", html)) or None, "检查首页是否有用户协议入口", "pipl-privacy-policy")
    hits = [f for f in FOREIGN if f in html]
    add("foreign_deps", not hits or None, ("境外资源: " + ", ".join(hits)) if hits else "首页未发现常见境外资源", "china-cloud-cdn-deploy")
    if a.ai:
        add("ai_label", bool(re.search(r"AI\s*生成|人工智能生成|由\s*AI|生成合成", html)) or None, "检查 AI 生成内容显式标识", "genai-algorithm-filing")
        add("model_disclosure", bool(re.search(r"备案号|上线编号|Beijing-|网信算备", html)) or None, "检查模型名称与备案号/上线编号公示（可能在详情页）", "genai-algorithm-filing")

    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        icon = {"PASS": "✅", "WARN": "⚠️ ", "FAIL": "❌"}
        for r in res:
            print(f"{icon[r['status']]} {r['check']:<16} {r['detail']}  → {r['skill']}")
        print("\n提示：本脚本只做页面级自动检查，不代表合规结论；人工项见 skills/golive-china-checklist/SKILL.md")
    sys.exit(1 if any(r["status"] == "FAIL" for r in res) else 0)

if __name__ == "__main__":
    main()
