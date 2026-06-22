import os
import io
import qrcode
from PIL import Image

# 全部链接配置
systems = [
    {
        "name": "新预测模型",
        "description": "全新升级的企业预测分析模型，提供精准趋势预测，智能分析辅助决策制定",
        "url": "https://newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app/",
        "image": "assets/card_data.jpg",
        "btn_color": "btn-blue",
        "qr_filename": "qr_1.png"
    },
    {
        "name": "数字经济分析",
        "description": "专注于数字经济领域，对全球数字经济发展趋势分析，数据可视化呈现产业经济现状",
        "url": "https://digital-encomy.streamlit.app/",
        "image": "assets/card_digital.jpg",
        "btn_color": "btn-purple",
        "qr_filename": "qr_2.png"
    },
    {
        "name": "数字经济主站",
        "description": "整合企业多维数据资源，通过交互式图表直观展示经济指标，支持自定义筛选",
        "url": "https://digital-encomy-main.streamlit.app/",
        "image": "assets/card_data.jpg",
        "btn_color": "btn-cyan",
        "qr_filename": "qr_3.png"
    },
    {
        "name": "大数据作业平台",
        "description": "学届大数据作业专用分析平台，集成多种数据清洗与建模工具，支持批量处理",
        "url": "https://xuejiededashujuzuoye.streamlit.app/",
        "image": "assets/card_digital.jpg",
        "btn_color": "btn-blue",
        "qr_filename": "qr_4.png"
    },
    {
        "name": "大数据分析系统",
        "description": "企业级大数据分析解决方案，支持海量数据实时处理，多维度交叉分析",
        "url": "https://big-data-hmjdjensqzboumvsvydca3.streamlit.app/",
        "image": "assets/card_data.jpg",
        "btn_color": "btn-purple",
        "qr_filename": "qr_5.png"
    },
    {
        "name": "ESG数字化平台",
        "description": "专注企业环境、社会与治理数据评估，提供ESG指标追踪、评级分析",
        "url": "https://esgdigital.streamlit.app/",
        "image": "assets/card_digital.jpg",
        "btn_color": "btn-cyan",
        "qr_filename": "qr_6.png"
    },
    {
        "name": "应用分析平台",
        "description": "通用应用数据分析平台，支持多源数据接入与自定义仪表盘，满足个性化需求",
        "url": "https://app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app/",
        "image": "assets/card_data.jpg",
        "btn_color": "btn-blue",
        "qr_filename": "qr_7.png"
    },
    {
        "name": "2007-2023 数字化",
        "description": "覆盖2007至2023年企业数字化转型历程数据，纵向对比分析演变趋势",
        "url": "https://20072023digital.streamlit.app/",
        "image": "assets/card_digital.jpg",
        "btn_color": "btn-purple",
        "qr_filename": "qr_8.png"
    },
    {
        "name": "1999-2023 数字化",
        "description": "更长周期的企业数字化发展数据追踪，洞察二十余年数字化变革规律",
        "url": "https://19992023digital.streamlit.app/",
        "image": "assets/card_data.jpg",
        "btn_color": "btn-cyan",
        "qr_filename": "qr_9.png"
    },
    {
        "name": "企业数字化指数",
        "description": "综合评估企业数字化水平的核心指标体系，提供行业对标、排名分析",
        "url": "https://1999-2023companydeindex-tgax4uws6a7.streamlit.app/",
        "image": "assets/card_digital.jpg",
        "btn_color": "btn-blue",
        "qr_filename": "qr_10.png"
    },
    {
        "name": "SmartBI 数据可视化",
        "description": "基于SmartBI的企业级数据可视化平台，支持复杂报表设计与交互式数据探索",
        "url": "http://47.98.202.43/smartbi/vision/share.jsp?resid=100ef521ecf6c5860d5917a961a6e0b0",
        "image": "assets/card_data.jpg",
        "btn_color": "btn-purple",
        "qr_filename": "qr_11.png"
    }
]

# 创建目录结构
def create_folders():
    os.makedirs("assets", exist_ok=True)
    os.makedirs("_shared/fonts", exist_ok=True)
    # 生成2张占位卡片图
    if not os.path.exists("assets/card_data.jpg"):
        img1 = Image.new("RGB", (800, 400), color="#0a1120")
        img1.save("assets/card_data.jpg")
    if not os.path.exists("assets/card_digital.jpg"):
        img2 = Image.new("RGB", (800, 400), color="#0f1a30")
        img2.save("assets/card_digital.jpg")

# 批量生成二维码
def build_qr_images():
    for item in systems:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        qr.add_data(item["url"])
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="#00d4ff", back_color="#050b14")
        qr_img.save(os.path.join("assets", item["qr_filename"]))

# 生成完整HTML页面
def build_html():
    feature_html = ""
    qr_html = ""
    # 拼接功能卡片
    for s in systems:
        feature_html += f'''
        <div class="feature-card">
          <img class="card-img" src="{s['image']}" alt="{s['name']}">
          <div class="card-body">
            <h3>{s['name']}</h3>
            <p>{s['description']}</p>
            <a class="card-btn {s['btn_color']}" href="{s['url']}" target="_blank" rel="noopener">
              进入系统
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
            </a>
          </div>
        </div>
        '''
    # 拼接二维码卡片
    for s in systems:
        qr_html += f'''
        <div class="qr-card">
          <img src="assets/{s['qr_filename']}" alt="{s['name']}二维码">
          <h4>{s['name']}</h4>
          <p class="qr-url">{s['url']}</p>
        </div>
        '''
    # 完整HTML模板
    html_template = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>数字智能分析平台 - 链接导航主页</title>
  <style>
    @font-face {
      font-family: 'NotoSans';
      src: url('./_shared/fonts/NotoSansSC-Regular.ttf') format('truetype');
      font-weight: 400;
    }
    @font-face {
      font-family: 'NotoSans';
      src: url('./_shared/fonts/NotoSansSC-Bold.ttf') format('truetype');
      font-weight: 700;
    }
    :root {
      --bg: #050b14;
      --bg2: #0a1120;
      --ink: #e8ecf1;
      --muted: #8b9bb4;
      --rule: #1a2a44;
      --accent: #00d4ff;
      --accent2: #7c3aed;
      --accent-glow: rgba(0, 212, 255, 0.3);
      --font: 'NotoSans', 'PingFang SC', 'Microsoft YaHei', sans-serif;
      --max: 1200px;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { font-size: 16px; scroll-behavior: smooth; }
    body {
      font-family: var(--font);
      color: var(--ink);
      background: var(--bg);
      line-height: 1.6;
      overflow-x: hidden;
    }
    #particles-canvas {
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      z-index: 0;
      pointer-events: none;
    }
    .page { position: relative; z-index: 1; }
    .top-nav {
      display: flex;
      align-items: center;
      justify-content: space-between;
      max-width: var(--max);
      margin: 0 auto;
      padding: 1.2rem 2rem;
    }
    .logo {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-weight: 700;
      font-size: 1.1rem;
      color: var(--accent);
      letter-spacing: 0.05em;
    }
    .logo svg { width: 28px; height: 28px; }
    .nav-links { display: flex; gap: 2rem; }
    .nav-links a {
      color: var(--muted);
      text-decoration: none;
      font-size: 0.9rem;
      transition: color 0.3s;
    }
    .nav-links a:hover { color: var(--accent); }
    .hero {
      position: relative;
      text-align: center;
      padding: 5rem 2rem 6rem;
      overflow: hidden;
    }
    .hero-bg {
      position: absolute;
      inset: 0;
      background: url('assets/hero_banner.jpg') center/cover no-repeat;
      opacity: 0.35;
      z-index: 0;
    }
    .hero-bg::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(5,11,20,0.3) 0%, var(--bg) 100%);
    }
    .hero-content { position: relative; z-index: 1; max-width: 800px; margin: 0 auto; }
    .hero h1 {
      font-size: 2.8rem;
      font-weight: 700;
      margin-bottom: 1rem;
      background: linear-gradient(90deg, var(--accent), #a855f7);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      letter-spacing: 0.04em;
    }
    .hero p {
      color: var(--muted);
      font-size: 1.1rem;
      margin-bottom: 2rem;
      max-width: 600px;
      margin-left: auto;
      margin-right: auto;
    }
    .hero-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.85rem 2.2rem;
      border-radius: 50px;
      background: linear-gradient(90deg, var(--accent), var(--accent2));
      color: #fff;
      font-weight: 600;
      font-size: 1rem;
      text-decoration: none;
      box-shadow: 0 0 25px var(--accent-glow);
      transition: transform 0.3s, box-shadow 0.3s;
      border: none;
      cursor: pointer;
    }
    .hero-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 0 40px rgba(0, 212, 255, 0.5);
    }
    .section-title {
      text-align: center;
      font-size: 1.6rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
      color: var(--ink);
    }
    .section-sub {
      text-align: center;
      color: var(--muted);
      font-size: 0.9rem;
      margin-bottom: 2.5rem;
    }
    .features {
      max-width: var(--max);
      margin: 0 auto;
      padding: 3rem 2rem;
    }
    .feature-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
    }
    .feature-card {
      background: var(--bg2);
      border: 1px solid var(--rule);
      border-radius: 16px;
      overflow: hidden;
      transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s;
      display: flex;
      flex-direction: column;
    }
    .feature-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 12px 40px rgba(0,0,0,0.4);
      border-color: var(--accent);
    }
    .feature-card .card-img {
      width: 100%;
      height: 160px;
      object-fit: cover;
      display: block;
    }
    .feature-card .card-body {
      padding: 1.2rem 1.4rem 1.4rem;
      flex: 1;
      display: flex;
      flex-direction: column;
    }
    .feature-card h3 {
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 0.4rem;
      color: var(--ink);
    }
    .feature-card p {
      font-size: 0.82rem;
      color: var(--muted);
      line-height: 1.6;
      margin-bottom: 1rem;
      flex: 1;
    }
    .feature-card .card-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
      width: 100%;
      padding: 0.65rem 0;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.9rem;
      text-decoration: none;
      color: #fff;
      transition: opacity 0.3s, transform 0.3s;
      border: none;
      cursor: pointer;
    }
    .feature-card .card-btn:hover { opacity: 0.9; transform: scale(1.02); }
    .btn-blue { background: linear-gradient(90deg, #2563eb, #1d4ed8); }
    .btn-purple { background: linear-gradient(90deg, #7c3aed, #6d28d9); }
    .btn-cyan { background: linear-gradient(90deg, #0891b2, #0e7490); }
    .advantages {
      max-width: var(--max);
      margin: 0 auto;
      padding: 3rem 2rem;
    }
    .adv-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.2rem;
    }
    .adv-card {
      background: var(--bg2);
      border: 1px solid var(--rule);
      border-radius: 12px;
      padding: 1.4rem 1.2rem;
      text-align: center;
      transition: border-color 0.3s, box-shadow 0.3s;
    }
    .adv-card:hover {
      border-color: var(--accent);
      box-shadow: 0 0 20px rgba(0, 212, 255, 0.1);
    }
    .adv-icon {
      width: 44px; height: 44px;
      margin: 0 auto 0.8rem;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 10px;
      background: rgba(0, 212, 255, 0.1);
      color: var(--accent);
    }
    .adv-card h4 {
      font-size: 0.95rem;
      font-weight: 700;
      margin-bottom: 0.4rem;
      color: var(--ink);
    }
    .adv-card p {
      font-size: 0.78rem;
      color: var(--muted);
      line-height: 1.5;
    }
    .qr-section {
      max-width: var(--max);
      margin: 0 auto;
      padding: 3rem 2rem 4rem;
    }
    .qr-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
    }
    .qr-card {
      background: var(--bg2);
      border: 1px solid var(--rule);
      border-radius: 16px;
      padding: 1.5rem;
      text-align: center;
      transition: transform 0.3s, border-color 0.3s;
    }
    .qr-card:hover {
      transform: translateY(-4px);
      border-color: var(--accent);
    }
    .qr-card img {
      width: 140px;
      height: 140px;
      border-radius: 10px;
      margin-bottom: 0.8rem;
      background: #fff;
      padding: 6px;
    }
    .qr-card h4 {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--ink);
      margin-bottom: 0.3rem;
    }
    .qr-card .qr-url {
      font-size: 0.72rem;
      color: var(--muted);
      word-break: break-all;
      line-height: 1.4;
    }
    .site-footer {
      background: #080f1c;
      border-top: 1px solid var(--rule);
      padding: 2.5rem 2rem;
      text-align: center;
    }
    .site-footer h3 {
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 0.6rem;
      color: var(--ink);
    }
    .site-footer p {
      font-size: 0.82rem;
      color: var(--muted);
      max-width: 600px;
      margin: 0 auto 1rem;
      line-height: 1.6;
    }
    .footer-social {
      display: flex;
      justify-content: center;
      gap: 1rem;
      margin-top: 1rem;
    }
    .footer-social a {
      width: 36px; height: 36px;
      border-radius: 50%;
      background: var(--bg2);
      border: 1px solid var(--rule);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--muted);
      text-decoration: none;
      transition: all 0.3s;
    }
    .footer-social a:hover {
      border-color: var(--accent);
      color: var(--accent);
      box-shadow: 0 0 12px var(--accent-glow);
    }
    @media (max-width: 1024px) {
      .feature-grid { grid-template-columns: repeat(2, 1fr); }
      .adv-grid { grid-template-columns: repeat(2, 1fr); }
      .qr-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 640px) {
      .hero h1 { font-size: 2rem; }
      .feature-grid, .adv-grid, .qr-grid { grid-template-columns: 1fr; }
      .top-nav { flex-direction: column; gap: 1rem; }
    }
  </style>
</head>
<body>
  <canvas id="particles-canvas"></canvas>
  <div class="page">
    <nav class="top-nav">
      <div class="logo">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
        </svg>
        企业数据智能平台
      </div>
      <div class="nav-links">
        <a href="#features">功能模块</a>
        <a href="#advantages">核心优势</a>
        <a href="#qrcodes">移动端访问</a>
        <a href="#about">关于我们</a>
      </div>
    </nav>
    <section class="hero">
      <div class="hero-bg"></div>
      <div class="hero-content">
        <h1>企业数据智能分析平台</h1>
        <p>整合企业数字化转型、ESG分析与数据可视化，助力企业决策智能化</p>
        <a class="hero-btn" href="#features">
          探索数据应用
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </a>
      </div>
    </section>
    <section class="features" id="features">
      <h2 class="section-title">系统功能介绍</h2>
      <p class="section-sub">我们提供多个专业数据系统，满足企业不同维度的数据分析需求</p>
      <div class="feature-grid">
        {feature_cards}
      </div>
    </section>
    <section class="advantages" id="advantages">
      <h2 class="section-title">平台核心优势</h2>
      <p class="section-sub">我们的系统整合多种先进技术，为企业提供全方位的数据分析解决方案</p>
      <div class="adv-grid">
        <div class="adv-card">
          <div class="adv-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path></svg>
          </div>
          <h4>整合企业多维数据</h4>
          <p>支持多个数据源统一接入与整合</p>
        </div>
        <div class="adv-card">
          <div class="adv-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
          </div>
          <h4>专业级工具</h4>
          <p>搭载高级算法引擎，精准预测趋势</p>
        </div>
        <div class="adv-card">
          <div class="adv-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          </div>
          <h4>响应式设计</h4>
          <p>完美支持PC端与移动端无缝访问</p>
        </div>
        <div class="adv-card">
          <div class="adv-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
          </div>
          <h4>模块化系统</h4>
          <p>灵活组合不同分析模块，定制专属方案</p>
        </div>
      </div>
    </section>
    <section class="qr-section" id="qrcodes">
      <h2 class="section-title">移动端访问</h2>
      <p class="section-sub">扫描下方二维码，在手机上访问对应数据系统</p>
      <div class="qr-grid">
        {qr_cards}
      </div>
    </section>
    <footer class="site-footer" id="about">
      <h3>关于我们</h3>
      <p>我们致力于为企业提供专业的数据智能分析工具，整合多个数据分析平台与可视化系统，通过先进的算法与模型技术，帮助企业实现数据驱动决策，优化运营流程。</p>
      <div class="footer-social">
        <a href="#" aria-label="GitHub">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
        </a>
        <a href="#" aria-label="Twitter">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>
        </a>
        <a href="#" aria-label="LinkedIn">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
        </a>
      </div>
    </footer>
  </div>
  <script>
    (function(){const canvas=document.getElementById("particles-canvas");const ctx=canvas.getContext("2d");let width,height;const particles=[];const PARTICLE_COUNT=60;const CONNECTION_DIST=120;function resize(){width=canvas.width=window.innerWidth;height=canvas.height=window.innerHeight}window.addEventListener("resize",resize);resize();for(let i=0;i<PARTICLE_COUNT;i++){particles.push({x:Math.random()*width,y:Math.random()*height,vx:(Math.random()-0.5)*0.5,vy:(Math.random()-0.5)*0.5,radius:Math.random()*2+1})}function draw(){ctx.clearRect(0,0,width,height);for(let i=0;i<particles;i++){const p=particles[i];p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>width)p.vx*=-1;if(p.y<0||p.y>height)p.vy*=-1;ctx.beginPath();ctx.arc(p.x,p.y,p.radius,0,Math.PI*2);ctx.fillStyle="rgba(0, 212, 255, 0.5)";ctx.fill();for(let j=i+1;j<particles.length;j++){const q=particles[j];const dx=p.x-q.x;const dy=p.y-q.y;const dist=Math.sqrt(dx*dx+dy*dy);if(dist<CONNECTION_DIST){ctx.beginPath();ctx.moveTo(p.x,p.y);ctx.lineTo(q.x,q.y);ctx.strokeStyle=`rgba(0, 212, 255, ${(1-dist/CONNECTION_DIST)*0.2})`;ctx.lineWidth=1;ctx.stroke()}}}requestAnimationFrame(draw)}draw()})();
  </script>
</body>
</html>
'''
    html_out = html_template.replace("{feature_cards}", feature_html).replace("{qr_cards}", qr_html)
    with open("link-hub.html", "w", encoding="utf-8") as f:
        f.write(html_out)

# 程序入口
if __name__ == "__main__":
    create_folders()
    build_qr_images()
    build_html()
    print("✅ 全部文件生成完成：")
    print("1. link-hub.html 导航主页")
    print("2. assets/ 二维码+占位图片目录")
    print("3. _shared/fonts 字体存放目录")
