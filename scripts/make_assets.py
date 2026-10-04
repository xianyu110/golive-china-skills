from PIL import Image, ImageDraw, ImageFont
B="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"; R="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
import os
if not os.path.exists(R): R=B
def F(p,s): return ImageFont.truetype(p,s,index=2)  # SC
W,H=1600,860
img=Image.new("RGB",(W,H)); d=ImageDraw.Draw(img)
for y in range(H):
    t=y/H; d.line([(0,y),(W,y)],fill=(int(12+10*t),int(18+14*t),int(38+30*t)))
# red accent band
d.rectangle([0,0,W,8],fill=(222,41,16))
d.text((70,50),"GoLive China Skills",font=F(B,64),fill=(255,255,255))
d.text((70,135),"13 个 Agent Skills · 把 AI 写的产品在中国大陆合规上线",font=F(B,36),fill=(255,214,102))
d.text((70,190),"ICP 备案 · 公安备案 · 云与 CDN · 微信支付 · 支付宝 · 小程序 · 软著 · 个保法 · 生成式 AI 备案 · 短信 · 国产大模型",font=F(R,24),fill=(190,200,225))
steps=[("域名实名","domain-realname-dns","H"),("ICP 备案","icp-beian","H"),("公安备案","gongan-beian","H"),("云 + CDN","china-cloud-cdn-deploy","A"),("隐私政策","pipl-privacy-policy","A"),
       ("微信支付","wechat-pay","B"),("支付宝","alipay","B"),("小程序审核","wechat-miniprogram-launch","B"),("App + 软著","app-store-ruanzhu","B"),("短信签名","sms-sign-template","B"),
       ("国产大模型","llm-api-in-china","A"),("AI 备案/登记","genai-algorithm-filing","H")]
col={"A":(52,211,153),"H":(251,146,60),"B":(129,140,248)}
bw,bh,gx=230,108,60; x0=70; ys=[280,450,620]
pos=[]
for i,(t,slug,o) in enumerate(steps):
    r,c=divmod(i,5) if i<10 else (2,i-10)
    if r==1: c=4-c  # snake
    x=x0+c*(bw+gx); y=ys[r]; pos.append((x,y))
    d.rounded_rectangle([x,y,x+bw,y+bh],radius=18,fill=(30,41,74),outline=col[o],width=4)
    d.text((x+18,y+14),f"{i+1:02d}  {t}",font=F(B,28),fill=(255,255,255))
    d.text((x+18,y+62),slug,font=F(R,16),fill=(160,172,205))
def arrow(a,b):
    (x1,y1),(x2,y2)=a,b
    if y1==y2:
        if x2>x1: s,e=(x1+bw,y1+bh//2),(x2,y2+bh//2)
        else: s,e=(x1,y1+bh//2),(x2+bw,y2+bh//2)
    else: s,e=(x1+bw//2,y1+bh),(x2+bw//2,y2)
    d.line([s,e],fill=(230,230,240),width=4)
    import math; ang=math.atan2(e[1]-s[1],e[0]-s[0]); L=16
    d.polygon([e,(e[0]-L*math.cos(ang-0.45),e[1]-L*math.sin(ang-0.45)),(e[0]-L*math.cos(ang+0.45),e[1]-L*math.sin(ang+0.45))],fill=(230,230,240))
for i in range(len(pos)-1):
    if i==9: arrow(pos[9],(pos[10][0],pos[10][1])) if False else None
    arrow(pos[i],pos[i+1])
# final checklist box
x=x0+2*(bw+gx); y=ys[2]
d.rounded_rectangle([x,y,x+2*bw+gx,y+bh],radius=18,fill=(222,41,16))
d.text((x+22,y+14),"13  上线前总检查 ✓",font=F(B,32),fill=(255,255,255))
d.text((x+22,y+62),"golive-china-checklist · golive_check.py",font=F(R,18),fill=(255,230,225))
arrow(pos[11],(x,y))
# legend
lx,ly=70,790
for k,name in [("A","Agent 可自动化"),("H","必须由人完成"),("B","Agent + 人协作")]:
    d.rounded_rectangle([lx,ly,lx+26,ly+26],radius=6,outline=col[k],width=4); d.text((lx+36,ly-4),name,font=F(R,22),fill=(220,225,240)); lx+=260
d.text((W-560,ly-4),"探测 → 计划 → 人工确认 → 执行 → 验证",font=F(B,24),fill=(255,214,102))
img.save("assets/hero.png")  # run from repo root: python3 scripts/make_assets.py; print("hero ok")

# GIF
items=[("auto","HTTPS + 证书剩余 93 天"),("auto","ICP 备案号 → beian.miit.gov.cn"),("auto","公网安备号已展示"),("auto","隐私政策 / 用户协议入口"),
       ("auto","无 Google Fonts / 境外 CDN"),("human","微信支付 / 支付宝 真实小额支付+退款"),("human","小程序备案 + 隐私保护指引"),
       ("human","短信签名运营商报备成功"),("auto","AI 内容显式 + 隐式标识"),("human","模型名称 + 备案号/上线编号 公示")]
frames=[]; GW,GH=960,640
for k in range(len(items)+3):
    im=Image.new("RGB",(GW,GH),(15,23,42)); g=ImageDraw.Draw(im)
    g.rounded_rectangle([20,20,GW-20,GH-20],radius=16,fill=(17,24,39),outline=(55,65,81),width=2)
    for i,c in enumerate([(239,68,68),(234,179,8),(34,197,94)]): g.ellipse([44+i*26,40,60+i*26,56],fill=c)
    g.text((140,34),"golive-china-checklist  ·  上线前总检查",font=F(B,22),fill=(203,213,225))
    g.text((50,80),"$ python3 golive_check.py https://your.domain --ai",font=F(R,20),fill=(52,211,153))
    for i,(who,t) in enumerate(items):
        y=124+i*42; done=i<k
        box="✅" if done else "⬜"
        g.text((60,y),"[x]" if done else "[ ]",font=F(B,22),fill=(52,211,153) if done else (100,116,139))
        g.text((120,y),t,font=F(R,22),fill=(241,245,249) if done else (148,163,184))
        tag="Agent" if who=="auto" else "Human"
        g.rounded_rectangle([GW-170,y+2,GW-60,y+32],radius=8,fill=(6,78,59) if who=="auto" else (124,45,18))
        g.text((GW-152,y+2),tag,font=F(B,20),fill=(255,255,255))
    n=min(k,len(items)); bar=int((GW-120)*n/len(items))
    g.rounded_rectangle([60,GH-62,GW-60,GH-42],radius=8,fill=(30,41,59)); 
    if bar: g.rounded_rectangle([60,GH-62,60+bar,GH-42],radius=8,fill=(222,41,16) if n<len(items) else (34,197,94))
    g.text((60,GH-100),f"{n}/{len(items)} 已完成" + ("  · Ready to go live" if n==len(items) else ""),font=F(B,22),fill=(255,214,102))
    frames.append(im.convert("P",palette=Image.ADAPTIVE,colors=128))
dur=[700]*(len(frames)-3)+[700,1500,2500]
frames[0].save("assets/checklist.gif",save_all=True,append_images=frames[1:],duration=dur,loop=0,optimize=True)
print("gif ok")
