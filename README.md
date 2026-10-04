<div align="center">

# 🇨🇳 GoLive China Skills

**13 个 Agent Skills：让 AI 编程 Agent 陪你把产品在中国大陆合规上线**<br>
**13 Agent Skills that walk your coding agent + you through launching a product in mainland China**

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-13-8b5cf6)](#-skills--技能列表)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-ready-d97757)](#-安装)
[![Codex](https://img.shields.io/badge/Codex-ready-111111)](#-安装)
[![Cursor](https://img.shields.io/badge/Cursor-ready-2563eb)](#-安装)
[![Sources](https://img.shields.io/badge/每个%20skill-附官方来源-de2910)](#-资料来源与免责声明)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[中文](#-中文) · [English](#-english) · [Skills](#-skills--技能列表) · [免责声明 Disclaimer](#-资料来源与免责声明)

<img src="https://upload.maynor1024.live/file/1791117154492_golive-china-hero.png" alt="GoLive China Skills 上线流程图：域名实名 → ICP 备案 → 公安备案 → 云与 CDN → 隐私政策 → 微信支付 → 支付宝 → 小程序 → App 与软著 → 短信 → 国产大模型 → AI 备案 → 上线总检查" width="100%">

</div>

---

## 🇨🇳 中文

Agent 一个下午就能把产品写完，但在国内上线还有一长串"最后一公里"：**ICP 备案、公安备案、域名实名、内地服务器和 CDN、微信支付、支付宝、小程序审核、软著、隐私政策、短信签名、生成式 AI 备案/登记、国产大模型选型**……每一步都有材料、顺序和驳回坑。

这个仓库把它们拆成 13 个可单独安装的 Agent Skill。对 Claude Code / Codex / Cursor 说一句「帮我在国内上线这个项目」，agent 会按 **探测 → 计划 → 人工确认 → 执行 → 验证** 的顺序工作：能自动做的（改 footer、写回调验签、扫描隐私收集行为、起草隐私政策、去掉 Google Fonts、跑体检脚本）它直接做；必须由你本人做的（实名、人脸核验、接初审电话、24 小时内短信核验、签约、提交表单）它会列清楚、按顺序提醒你。

**和一篇"备案攻略"的区别：**

- 📎 **每条规则都附官方来源**：工信部、公安部、网信办、人大网、微信支付商户平台、支付宝开放平台、微信开放文档、阿里云/腾讯云文档。核对日期 2026-10-04。
- 🤝 **Agent / 人 分工表**：每个 skill 都有"Agent 能自动化 vs 人必须做"，agent 不代替你实名、签约或提交政府表单。
- 🚫 **常见驳回原因 + 修复**：备案、支付签约、小程序审核、短信签名、商店上架的高频驳回点。
- 🔗 **依赖顺序**：主体一致性（域名实名 = 备案主体 = 商户主体 = 小程序主体 = 短信资质）放在第一位。
- 🛠 **只读体检脚本**：`golive_check.py` 检查 HTTPS、ICP/公安备案号、隐私政策入口、境外依赖、AI 标识。
- ⚖️ **保守**：不编造费用和时效（只引用官方页面写明的数字），不确定处明确标 ⚠️。

<div align="center">
<img src="https://upload.maynor1024.live/file/1791117155495_golive-china-checklist.gif" alt="上线前总检查清单动图：Agent 自动项与 Human 人工项逐条打勾" width="720">
</div>

### 📦 安装

一行安装（[skills CLI](https://skills.sh)）：

```bash
npx skills add xianyu110/golive-china-skills
```

或者手动复制：

```bash
git clone https://github.com/xianyu110/golive-china-skills.git && cd golive-china-skills
mkdir -p ~/.claude/skills && cp -r skills/* ~/.claude/skills/   # Claude Code（或项目内 .claude/skills/）
mkdir -p ~/.codex/skills  && cp -r skills/* ~/.codex/skills/    # Codex
mkdir -p .cursor/skills   && cp -r skills/* .cursor/skills/     # Cursor（项目内）
```

Claude Code 插件市场：`/plugin marketplace add xianyu110/golive-china-skills`。只想要某一个？复制对应文件夹即可，例如 `cp -r skills/icp-beian ~/.claude/skills/`。

### 🚀 使用

```text
用 golive-china-checklist 看一下这个仓库要在国内上线还差什么，先给我计划，不要替我提交任何东西
用 icp-beian 判断我需不需要备案，列出我要准备的材料
用 wechat-pay 给 Next.js 项目接入 Native 支付，回调要验签和幂等
用 pipl-privacy-policy 扫描代码，生成隐私政策和第三方 SDK 清单
用 genai-algorithm-filing 判断我的 AI 小程序走备案还是登记
python3 skills/golive-china-checklist/scripts/golive_check.py https://你的域名 --ai
```

---

## 🧩 Skills / 技能列表

| # | Skill | 中文说明 | English |
|---|---|---|---|
| 1 | [`icp-beian`](skills/icp-beian/SKILL.md) | ICP 备案：是否需要、经营性许可 vs 非经营性备案、材料、短信核验、备案号展示 | MIIT ICP filing |
| 2 | [`gongan-beian`](skills/gongan-beian/SKILL.md) | 公安联网备案：30 日内办理、填报项、公网安备号展示 | Public-security network filing |
| 3 | [`domain-realname-dns`](skills/domain-realname-dns/SKILL.md) | 域名实名与解析：可备案后缀、实名主体一致、DNS/HTTPS | Domain real-name & DNS |
| 4 | [`china-cloud-cdn-deploy`](skills/china-cloud-cdn-deploy/SKILL.md) | 国内云服务器与 CDN：可备案服务器、CDN 与备案、境外依赖替换 | Mainland cloud & CDN deploy |
| 5 | [`wechat-pay`](skills/wechat-pay/SKILL.md) | 微信支付 APIv3：入驻材料、产品选择、回调验签解密、幂等对账 | WeChat Pay APIv3 |
| 6 | [`alipay`](skills/alipay/SKILL.md) | 支付宝：签约条件、加签、异步通知验签返回 success | Alipay |
| 7 | [`wechat-miniprogram-launch`](skills/wechat-miniprogram-launch/SKILL.md) | 微信小程序：小程序备案、隐私保护指引、对照官方拒绝情形自查 | Mini Program filing & review |
| 8 | [`app-store-ruanzhu`](skills/app-store-ruanzhu/SKILL.md) | 应用商店上架与软著：App 备案、iOS ICP 号、安卓商店版权证明、软著材料 | App stores & software copyright |
| 9 | [`pipl-privacy-policy`](skills/pipl-privacy-policy/SKILL.md) | 个保法隐私政策与用户协议：代码扫描数据清单、单独同意、注销（附模板） | PIPL privacy policy & terms |
| 10 | [`genai-algorithm-filing`](skills/genai-algorithm-filing/SKILL.md) | 生成式 AI 备案/登记/算法备案、AI 内容标识、拟人化互动新规 | GenAI & algorithm filing |
| 11 | [`sms-sign-template`](skills/sms-sign-template/SKILL.md) | 短信签名与模板：签名来源、模板写法、商业短信同意与退订 | SMS signature & templates |
| 12 | [`llm-api-in-china`](skills/llm-api-in-china/SKILL.md) | 国内调用大模型：已备案国产模型 vs API 中转的合规取舍 | Calling LLMs from China |
| 13 | [`golive-china-checklist`](skills/golive-china-checklist/SKILL.md) | 上线前总检查清单 + 总调度 + 体检脚本 | Master go-live checklist |

每个 `SKILL.md` 都包含：frontmatter（name + "Use when…" 描述）、前置条件、分步流程、检查清单、常见驳回原因与修复、Agent vs 人 分工、官方来源链接、免责声明。

---

## 🤖 开发时没有 Claude / API？

写这些代码时你可能需要一个能用的模型。下面是作者团队推荐的**开发者工具**（含推广链接），用于你本人写代码、做原型——**不是**面向中国境内用户的生产合规方案。产品上线后，生产环境请切换到已备案的国产模型，并按 [`genai-algorithm-filing`](skills/genai-algorithm-filing/SKILL.md) 完成登记/备案（取舍详见 [`llm-api-in-china`](skills/llm-api-in-china/SKILL.md)）。

- 方法一：`https://claude-opus.top/` —— Claude 国内镜像站，浏览器里直接辅助编程
- 方法二：`https://tryallapi.com/register?aff=5A6A` —— 一站式 API（OpenAI 兼容），本地开发时一个 Key 切换多家模型

> 请勿向任何第三方开发工具输入真实用户个人信息、密钥或保密代码；使用前阅读其条款，并自行评估上游服务商条款与数据出境风险。

---

## 🇺🇸 English

Your agent can build a product in an afternoon; launching it **inside mainland China** still means ICP filing, public-security filing, real-name domains, mainland servers & CDN, WeChat Pay, Alipay, Mini Program review, software copyright, a PIPL-grade privacy policy, SMS signature registration, GenAI filing/registration and picking a compliant LLM.

This repo is a **Chinese-first** set of 13 installable Agent Skills (each with an English summary). The agent follows **detect → plan → approve → apply → verify**: it automates code/config/docs (footer filing numbers, payment callback verification, privacy-data inventory, policy drafts, removing Google Fonts, a read-only health-check script) and gives you an ordered list of the steps only a human can do (real-name & face verification, the MIIT SMS check within 24 h, signing merchant contracts, submitting government/platform forms). Every rule links to an official source (MIIT, MPS, CAC, NPC, WeChat Pay, Alipay, WeChat docs, Alibaba/Tencent Cloud docs), checked on 2026-10-04; uncertain points are flagged ⚠️ and no fees or timelines are stated unless an official page states them.

```bash
npx skills add xianyu110/golive-china-skills
python3 skills/golive-china-checklist/scripts/golive_check.py https://your.domain --ai
```

**No Claude / API while developing?** The authors recommend two developer tools (affiliate link included): `https://claude-opus.top/` (Claude mirror for coding in the browser) and `https://tryallapi.com/register?aff=5A6A` (OpenAI-compatible multi-model API). They're for *your own development*, not a compliance solution for serving users in mainland China — see `llm-api-in-china`.

---

## 📚 资料来源与免责声明

- 主要官方来源：[工信部备案管理系统](https://beian.miit.gov.cn/)、[全国互联网安全管理服务平台](https://beian.mps.gov.cn/)、[网信办](https://www.cac.gov.cn/)（生成式 AI 办法、标识办法、算法推荐规定、数据跨境规定、网络数据安全管理条例）、[人大网·个人信息保护法](http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html)、[微信支付商户平台](https://pay.weixin.qq.com/)、[支付宝开放平台](https://open.alipay.com/)、[微信开放文档](https://developers.weixin.qq.com/miniprogram/product/reject.html)、阿里云/腾讯云帮助中心。具体条款链接见每个 `SKILL.md` 底部。
- ⚠️ **不是法律意见**：本仓库是开发者经验与公开资料的整理。政策、平台规则、费率与审核尺度随时变化，各省/各地执行口径也可能不同；上线前请以官方最新页面为准，涉及经营许可、支付、未成年人、跨境数据、生成式 AI 的事项请咨询专业律师或主管部门。
- 发现过时或错误？欢迎提 Issue / PR，并附上官方链接。

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=xianyu110/golive-china-skills&type=Date)](https://star-history.com/#xianyu110/golive-china-skills&Date)

## 🤝 Contributing

PR 欢迎：补充腾讯云/华为云等接入商差异、更多驳回案例、各省管局规则。请保持每个 skill 自包含（`skills/<name>/SKILL.md`），**只写能附官方链接的规则**。

## Related

- [ecommerce-image-skills](https://github.com/xianyu110/ecommerce-image-skills) — 12 个电商出图 Agent Skills

## License

MIT © xianyu110

---

<div align="center">

我是 MaynorAI 团队，分享 AI 编程、AI SaaS 工具出海、一人团队搭建经验。

</div>
