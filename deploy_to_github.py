import streamlit as st

# 全部系统链接配置
system_list = [
    {
        "name": "新预测模型",
        "desc": "全新升级的企业预测分析模型，提供精准趋势预测，智能分析辅助决策制定",
        "url": "https://newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app/",
        "btn_class": "btn-blue"
    },
    {
        "name": "数字经济分析",
        "desc": "专注于数字经济领域，对全球数字经济发展趋势分析，数据可视化呈现产业经济现状",
        "url": "https://digital-encomy.streamlit.app/",
        "btn_class": "btn-purple"
    },
    {
        "name": "数字经济主站",
        "desc": "整合企业多维数据资源，通过交互式图表直观展示经济指标，支持自定义筛选",
        "url": "https://digital-encomy-main.streamlit.app/",
        "btn_class": "btn-cyan"
    },
    {
        "name": "大数据作业平台",
        "desc": "学届大数据作业专用分析平台，集成多种数据清洗与建模工具，支持批量处理",
        "url": "https://xuejiededashujuzuoye.streamlit.app/",
        "btn_class": "btn-blue"
    },
    {
        "name": "大数据分析系统",
        "desc": "企业级大数据分析解决方案，支持海量数据实时处理，多维度交叉分析",
        "url": "https://big-data-hmjdjensqzboumvsvydca3.streamlit.app/",
        "btn_class": "btn-purple"
    },
    {
        "name": "ESG数字化平台",
        "desc": "专注企业环境、社会与治理数据评估，提供ESG指标追踪、评级分析",
        "url": "https://esgdigital.streamlit.app/",
        "btn_class": "btn-cyan"
    },
    {
        "name": "应用分析平台",
        "desc": "通用应用数据分析平台，支持多源数据接入与自定义仪表盘，满足个性化需求",
        "url": "https://app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app/",
        "btn_class": "btn-blue"
    },
    {
        "name": "2007-2023 数字化",
        "desc": "覆盖2007至2023年企业数字化转型历程数据，纵向对比分析演变趋势",
        "url": "https://20072023digital.streamlit.app/",
        "btn_class": "btn-purple"
    },
    {
        "name": "1999-2023 数字化",
        "desc": "更长周期的企业数字化发展数据追踪，洞察二十余年数字化变革规律",
        "url": "https://19992023digital.streamlit.app/",
        "btn_class": "btn-cyan"
    },
    {
        "name": "企业数字化指数",
        "desc": "综合评估企业数字化水平的核心指标体系，提供行业对标、排名分析",
        "url": "https://1999-2023companydeindex-tgax4uws6a7.streamlit.app/",
        "btn_class": "btn-blue"
    },
    {
        "name": "SmartBI 数据可视化",
        "desc": "基于SmartBI的企业级数据可视化平台，支持复杂报表设计与交互式数据探索",
        "url": "http://47.98.202.43/smartbi/vision/share.jsp?resid=100ef521ecf6c5860d5917a961a6e0b0",
        "btn_class": "btn-purple"
    }
]

# 拼接功能卡片HTML
feature_html_blocks = ""
qr_html_blocks = ""
for item in system_list:
    # 功能卡片（可替换background-image:url('你的图片地址')实现自定义图片）
    feature_html_blocks += f"""
    <div class="feature-card">
      <div class="card-img-box" style="background:linear-gradient(135deg,#082038,#102848);"></div>
      <div class="card-body">
        <h3>{item['name']}</h3>
        <p>{item['desc']}</p>
        <a class="card-btn {item['btn_class']}" href="{item['url']}" target="_blank" rel="noopener noreferrer">
          进入系统
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
            <polyline points="15 3 21 3 21 9"></polyline>
            <line x1="10" y1="14" x2="21" y2="3"></line>
          </svg>
        </a>
      </div>
    </div>
    """
    # 二维码卡片（前端JS自动生成）
    qr_html_blocks += f"""
    <div class="qr-card">
      <div class="qr-canvas" data-link="{item['url']}"></div>
      <h4>{item['name']}</h4>
      <p class="qr-link">{item['url']}</p>
    </div>
    """

# 完整内嵌HTML页面代码
full_html_page = f'''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>企业数据智能导航平台</title>
<!-- CDN在线二维码生成JS，无需Python图像处理 -->
<script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.1/build/qrcode.min.js"></script>
<style>
:root {{
  --bg: #050b14;
  --bg2: #0a1120;
  --text: #e8ecf1;
  --gray: #8b9bb4;
  --border: #1a2a44;
  --cyan: #00d4ff;
  --purple: #7c3aed;
  --glow: rgba(0, 212, 255, 0.3);
  --max-width: 1200px;
}}
* {{box-sizing: border-box;margin:0;padding:0;}}
html {{scroll-behavior: smooth;}}
body {{
  background: var(--bg);
  color: var(--text);
  font-family: "PingFang SC",Microsoft YaHei,sans-serif;
  line-height: 1.6;
  overflow-x: hidden;
}}
#particle-canvas {{
  position: fixed;
  width: 100%;
  height: 100%;
  top:0;left:0;
  z-index: 0;
  pointer-events: none;
}}
.wrap {{position: relative;z-index: 1;}}
/* 导航栏 */
.top-nav {{
  max-width: var(--max-width);
  margin:0 auto;
  display:flex;
  justify-content: space-between;
  align-items:center;
  padding:1.2rem 2rem;
}}
.logo {{
  display:flex;
  align-items:center;
  gap:0.6rem;
  font-weight:bold;
  font-size:1.1rem;
  color:var(--cyan);
}}
.logo svg {{width:28px;height:28px;}}
.nav-menu {{display:flex;gap:2rem;}}
.nav-menu a {{
  color:var(--gray);
  text-decoration:none;
  font-size:0.9rem;
  transition:0.3s;
}}
.nav-menu a:hover {{color:var(--cyan);}}
/* 头部Hero区域 */
.hero {{
  text-align:center;
  padding:5rem 2rem 6rem;
}}
.hero h1 {{
  font-size:2.8rem;
  background:linear-gradient(90deg,var(--cyan),#a855f7);
  -webkit-background-clip:text;
  color:transparent;
  margin-bottom:1rem;
}}
.hero p {{
  max-width:600px;
  margin:0 auto 2rem;
  color:var(--gray);
  font-size:1.1rem;
}}
.hero-btn {{
  display:inline-flex;
  align-items:center;
  gap:0.5rem;
  padding:0.85rem 2.2rem;
  border-radius:50px;
  background:linear-gradient(90deg,var(--cyan),var(--purple));
  color:#fff;
  text-decoration:none;
  font-weight:600;
  box-shadow:0 0 25px var(--glow);
  transition:0.3s;
}}
.hero-btn:hover {{transform:translateY(-2px);box-shadow:0 0 40px rgba(0,212,255,0.5);}}
/* 通用区块标题 */
.section-title {{
  text-align:center;
  font-size:1.6rem;
  font-weight:bold;
  margin-bottom:0.5rem;
}}
.section-desc {{
  text-align:center;
  color:var(--gray);
  font-size:0.9rem;
  margin-bottom:2.5rem;
}}
/* 功能卡片区域 */
.feature-box {{
  max-width:var(--max-width);
  margin:0 auto;
  padding:3rem 2rem;
}}
.feature-grid {{
  display:grid;
  grid-template-columns: repeat(3,1fr);
  gap:1.5rem;
}}
.feature-card {{
  background:var(--bg2);
  border:1px solid var(--border);
  border-radius:16px;
  overflow:hidden;
  transition:0.3s;
  display:flex;
  flex-direction:column;
}}
.feature-card:hover {{
  transform:translateY(-6px);
  box-shadow:0 12px 40px rgba(0,0,0,0.4);
  border-color:var(--cyan);
}}
.card-img-box {{
  width:100%;
  height:160px;
  /* 替换这里background为图片url即可加载图片：background:url("图片链接") center/cover; */
}}
.card-body {{padding:1.2rem 1.4rem 1.4rem;flex:1;}}
.card-body h3 {{font-size:1.05rem;margin-bottom:0.4rem;}}
.card-body p {{font-size:0.82rem;color:var(--gray);margin-bottom:1rem;}}
.card-btn {{
  display:flex;
  width:100%;
  justify-content:center;
  gap:0.4rem;
  padding:0.65rem 0;
  border-radius:8px;
  color:#fff;
  text-decoration:none;
  font-weight:600;
  font-size:0.9rem;
  transition:0.3s;
}}
.card-btn:hover {{opacity:0.9;transform:scale(1.02);}}
.btn-blue {{background:linear-gradient(90deg,#2563eb,#1d4ed8);}}
.btn-purple {{background:linear-gradient(90deg,#7c3aed,#6d28d9);}}
.btn-cyan {{background:linear-gradient(90deg,#0891b2,#0e7490);}}
/* 核心优势 */
.adv-box {{
  max-width:var(--max-width);
  margin:0 auto;
  padding:3rem 2rem;
}}
.adv-grid {{
  display:grid;
  grid-template-columns: repeat(4,1fr);
  gap:1.2rem;
}}
.adv-card {{
  background:var(--bg2);
  border:1px solid var(--border);
  border-radius:12px;
  padding:1.4rem 1.2rem;
  text-align:center;
  transition:0.3s;
}}
.adv-card:hover {{border-color:var(--cyan);box-shadow:0 0 20px rgba(0,212,255,0.1);}}
.adv-icon {{
  width:44px;height:44px;
  margin:0 auto 0.8rem;
  display:flex;
  align-items:center;
  justify-content:center;
  border-radius:10px;
  background:rgba(0,212,255,0.1);
  color:var(--cyan);
}}
.adv-card h4 {{font-size:0.95rem;margin-bottom:0.4rem;}}
.adv-card p {{font-size:0.78rem;color:var(--gray);}}
/* 二维码区域 */
.qrcode-box {{
  max-width:var(--max-width);
  margin:0 auto;
  padding:3rem 2rem 4rem;
}}
.qr-grid {{
  display:grid;
  grid-template-columns: repeat(3,1fr);
  gap:1.5rem;
}}
.qr-card {{
  background:var(--bg2);
  border:1px solid var(--border);
  border-radius:16px;
  padding:1.5rem;
  text-align:center;
  transition:0.3s;
}}
.qr-card:hover {{transform:translateY(-4px);border-color:var(--cyan);}}
.qr-canvas {{
  width:140px;height:140px;
  margin:0 auto 0.8rem;
  background:#fff;
  border-radius:10px;
  padding:6px;
}}
.qr-card h4 {{font-size:0.95rem;margin-bottom:0.3rem;}}
.qr-link {{font-size:0.72rem;color:var(--gray);word-break:break-all;}}
/* 底部 */
.footer {{
  background:#080f1c;
  border-top:1px solid var(--border);
  padding:2.5rem 2rem;
  text-align:center;
}}
.footer h3 {{font-size:1.1rem;margin-bottom:0.6rem;}}
.footer p {{max-width:600px;margin:0 auto 1rem;color:var(--gray);font-size:0.82rem;}}
.social {{display:flex;justify-content:center;gap:1rem;margin-top:1rem;}}
.social a {{
  width:36px;height:36px;
  border-radius:50%;
  border:1px solid var(--border);
  background:var(--bg2);
  display:flex;
  align-items:center;
  justify-content:center;
  color:var(--gray);
  text-decoration:none;
  transition:0.3s;
}}
.social a:hover {{border-color:var(--cyan);color:var(--cyan);box-shadow:0 0 12px var(--glow);}}
/* 响应式适配 */
@media (max-width:1024px){{
  .feature-grid, .qr-grid {{grid-template-columns: repeat(2,1fr);}}
  .adv-grid {{grid-template-columns: repeat(2,1fr);}}
}}
@media (max-width:640px){{
  .hero h1 {{font-size:2rem;}}
  .feature-grid,.adv-grid,.qr-grid {{grid-template-columns: 1fr;}}
  .top-nav {{flex-direction:column;gap:1rem;}}
}}
</style>
</head>
<body>
<canvas id="particle-canvas"></canvas>
<div class="wrap">
  <!-- 导航 -->
  <nav class="top-nav">
    <div class="logo">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
      </svg>
      企业数据智能平台
    </div>
    <div class="nav-menu">
      <a href="#feature">功能模块</a>
      <a href="#advantage">核心优势</a>
      <a href="#qrcode">移动端访问</a>
      <a href="#foot">关于我们</a>
    </div>
  </nav>

  <!-- Hero -->
  <section class="hero">
    <h1>企业数据智能分析平台</h1>
    <p>整合企业数字化转型、ESG分析与数据可视化，助力企业决策智能化</p>
    <a class="hero-btn" href="#feature">
      探索数据应用
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <polyline points="6 9 12 15 18 9"></polyline>
      </svg>
    </a>
  </section>

  <!-- 功能卡片 -->
  <section class="feature-box" id="feature">
    <h2 class="section-title">系统功能介绍</h2>
    <p class="section-desc">我们提供多个专业数据系统，满足企业不同维度的数据分析需求</p>
    <div class="feature-grid">
      {feature_html_blocks}
    </div>
  </section>

  <!-- 核心优势 -->
  <section class="adv-box" id="advantage">
    <h2 class="section-title">平台核心优势</h2>
    <p class="section-desc">我们的系统整合多种先进技术，为企业提供全方位的数据分析解决方案</p>
    <div class="adv-grid">
      <div class="adv-card">
        <div class="adv-icon">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <ellipse cx="12" cy="5" rx="9" ry="3"></ellipse>
            <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path>
            <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>
          </svg>
        </div>
        <h4>整合企业多维数据</h4>
        <p>支持多个数据源统一接入与整合</p>
      </div>
      <div class="adv-card">
        <div class="adv-icon">
          <svg width="22" height="22" viewBox="0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
          </svg>
        </div>
        <h4>专业级工具</h4>
        <p>搭载高级算法引擎，精准预测趋势</p>
      </div>
      <div class="adv-card">
        <div class="adv-icon">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 16 14"></polyline>
          </svg>
        </div>
        <h4>响应式设计</h4>
        <p>完美支持PC端与移动端无缝访问</p>
      </div>
      <div class="adv-card">
        <div class="adv-icon">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="3" y="3" width="18" height="18" rx="2"></rect>
            <line x1="3" y1="9" x2="21" y2="9"></line>
            <line x1="9" y1="21" x2="9" y2="9"></line>
          </svg>
        </div>
        <h4>模块化系统</h4>
        <p>灵活组合不同分析模块，定制专属方案</p>
      </div>
    </div>
  </section>

  <!-- 二维码区域 -->
  <section class="qrcode-box" id="qrcode">
    <h2 class="section-title">移动端访问</h2>
    <p class="section-desc">扫描下方二维码，在手机上访问对应数据系统</p>
    <div class="qr-grid">
      {qr_html_blocks}
    </div>
  </section>

  <!-- 底部 -->
  <footer class="footer" id="foot">
    <h3>关于我们</h3>
    <p>我们致力于为企业提供专业的数据智能分析工具，整合多个数据分析平台与可视化系统，通过先进的算法与模型技术，帮助企业实现数据驱动决策，优化运营流程。</p>
    <div class="social">
      <a href="#" aria-label="GitHub">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
        </svg>
      </a>
      <a href="#" aria-label="Twitter">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
        </svg>
      </a>
      <a href="#" aria-label="LinkedIn">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
          <rect x="2" y="9" width="4" height="12"></rect>
          <circle cx="4" cy="4" r="2"></circle>
        </svg>
      </a>
    </div>
  </footer>
</div>

<!-- 粒子背景JS -->
<script>
(function(){{
  const canvas = document.getElementById("particle-canvas");
  const ctx = canvas.getContext("2d");
  let w,h;
  const particles = [];
  const count = 60;
  const dist = 120;
  function resize(){{
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
  }}
  window.addEventListener("resize",resize);
  resize();
  for(let i=0;i<count;i++){{
    particles.push({{
      x:Math.random()*w,
      y:Math.random()*h,
      vx:(Math.random()-0.5)*0.5,
      vy:(Math.random()-0.5)*0.5,
      r:Math.random()*2+1
    }})
  }}
  function draw(){{
    ctx.clearRect(0,0,w,h);
    for(let i=0;i<particles;i++){{
      const p = particles[i];
      p.x += p.vx;
      p.y += p.vy;
      if(p.x<0||p.x>w)p.vx*=-1;
      if(p.y<0||p.y>h)p.vy*=-1;
      ctx.beginPath();
      ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
      ctx.fillStyle="rgba(0,212,255,0.5)";
      ctx.fill();
      for(let j=i+1;j<particles;j++){{
        const q = particles[j];
        const dx = p.x - q.x;
        const dy = p.y - q.y;
        const d = Math.sqrt(dx*dx+dy*dy);
        if(d < dist){{
          ctx.beginPath();
          ctx.moveTo(p.x,p.y);
          ctx.lineTo(q.x,q.y);
          ctx.strokeStyle=`rgba(0,212,255,${(1-d/dist)*0.2})`;
          ctx.lineWidth=1;
          ctx.stroke();
        }}
      }}
    }}
    requestAnimationFrame(draw);
  }}
  draw();
}})();

<!-- 页面加载生成二维码 -->
window.addEventListener("DOMContentLoaded",()=>{{
  const qrBoxs = document.querySelectorAll(".qr-canvas");
  qrBoxs.forEach(box=>{{
    const url = box.dataset.link;
    QRCode.toCanvas(box,url,{{width:128,color:{{dark:"#00d4ff",light:"#ffffff"}}}})
  }})
}});
</script>
</body>
</html>
'''

# Streamlit页面配置
st.set_page_config(
    page_title="企业数据智能导航平台",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 嵌入完整HTML页面，高度自适应
st.components.v1.html(
    full_html_page,
    height=2200,
    scrolling=True
)
