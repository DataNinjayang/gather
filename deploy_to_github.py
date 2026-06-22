import streamlit as st
import qrcode
from PIL import Image
import io

# ===================== 全局页面配置 =====================
st.set_page_config(
    page_title="企业数据智能分析平台 · 导航中台",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===================== 二维码生成函数 =====================
def generate_qr(url):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=5,
        border=2
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#00d4ff", back_color="#0f172a")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return Image.open(buf)

# ===================== 自定义科技风CSS（完整无截断） =====================
CUSTOM_CSS = """
<style>
/* 全局基础重置 */
* { box-sizing: border-box; margin: 0; padding: 0; }
.stApp {
    background: #030712;
    color: #e0e7ef;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Microsoft YaHei', sans-serif;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 0;
    padding-bottom: 4rem;
    max-width: 1400px;
}

/* ===== 粒子动态背景 ===== */
.particles-bg {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    z-index: 0;
    overflow: hidden;
    pointer-events: none;
}
.particle {
    position: absolute;
    width: 2px; height: 2px;
    background: rgba(0, 212, 255, 0.4);
    border-radius: 50%;
    animation: floatUp linear infinite;
}
.particle:nth-child(odd) { background: rgba(168, 85, 247, 0.3); }
@keyframes floatUp {
    0% { transform: translateY(100vh) scale(0); opacity: 0; }
    10% { opacity: 1; }
    90% { opacity: 1; }
    100% { transform: translateY(-10vh) scale(1); opacity: 0; }
}

/* 内容层级，确保在粒子上方 */
.content-wrap { position: relative; z-index: 1; }

/* ===== 粘性顶部导航 ===== */
.top-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.2rem 1.5rem;
    background: rgba(3, 7, 18, 0.85);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(0, 212, 255, 0.08);
    position: sticky;
    top: 0;
    z-index: 100;
    margin: 0 -4rem 2rem;
}
.top-bar .logo {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    font-weight: 800;
    font-size: 1.1rem;
    color: #00d4ff;
    letter-spacing: 0.08em;
}
.top-bar .logo .logo-icon {
    width: 36px; height: 36px;
    border-radius: 10px;
    background: linear-gradient(135deg, #00d4ff, #a855f7);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
}
.top-bar .nav-links { display: flex; gap: 2rem; }
.top-bar .nav-links a {
    color: #6b7fa3;
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
    transition: all 0.3s;
}
.top-bar .nav-links a:hover { color: #00d4ff; }

/* ===== Hero 首屏区域 ===== */
.hero-section {
    position: relative;
    text-align: center;
    padding: 5rem 2rem 4rem;
    border-radius: 24px;
    margin-bottom: 3rem;
    border: 1px solid rgba(0, 212, 255, 0.08);
    overflow: hidden;
}
.hero-bg {
    position: absolute;
    inset: 0;
    background: url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1600&q=80') center/cover no-repeat;
    opacity: 0.2;
    z-index: 0;
}
.hero-bg::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(3,7,18,0.3) 0%, rgba(3,7,18,0.9) 70%, rgba(3,7,18,1) 100%);
}
.hero-content { position: relative; z-index: 1; }
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.4rem 1.4rem;
    border-radius: 50px;
    background: rgba(0, 212, 255, 0.08);
    border: 1px solid rgba(0, 212, 255, 0.2);
    color: #00d4ff;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(10px);
}
.hero-badge .dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #00d4ff;
    animation: pulse 2s ease-in-out infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
}
.hero-title {
    font-size: 3.2rem;
    font-weight: 900;
    background: linear-gradient(90deg, #00d4ff, #a855f7, #ec4899, #00d4ff);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 6s ease-in-out infinite;
    margin-bottom: 1.2rem;
    letter-spacing: 0.04em;
    line-height: 1.15;
}
@keyframes shimmer {
    0%, 100% { background-position: 0% center; }
    50% { background-position: 300% center; }
}
.hero-sub {
    font-size: 1.1rem;
    color: #8b9bb4;
    max-width: 750px;
    margin: 0 auto 2.5rem;
    line-height: 1.8;
}
.hero-stats {
    display: flex;
    justify-content: center;
    gap: 3.5rem;
    flex-wrap: wrap;
}
.hero-stat {
    text-align: center;
    padding: 1rem 1.5rem;
    border-radius: 16px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    min-width: 120px;
}
.hero-stat .num {
    font-size: 2.2rem;
    font-weight: 900;
    background: linear-gradient(135deg, #00d4ff, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-stat .label {
    font-size: 0.75rem;
    color: #6b7fa3;
    margin-top: 0.3rem;
    font-weight: 500;
}

/* ===== 章节通用样式 ===== */
.section-header {
    text-align: center;
    margin-bottom: 2.5rem;
}
.section-tag {
    display: inline-block;
    padding: 0.25rem 0.8rem;
    border-radius: 4px;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: #00d4ff;
    background: rgba(0,212,255,0.08);
    border: 1px solid rgba(0,212,255,0.15);
    margin-bottom: 0.8rem;
}
.section-title {
    font-size: 1.8rem;
    font-weight: 800;
    color: #f0f4f8;
    margin-bottom: 0.5rem;
    letter-spacing: 0.02em;
}
.section-sub {
    color: #6b7fa3;
    font-size: 0.9rem;
    max-width: 600px;
    margin: 0 auto;
}
.section-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,212,255,0.2), rgba(168,85,247,0.2), transparent);
    margin: 3rem 0;
}

/* ===== 系统卡片样式 ===== */
.sys-card {
    background: linear-gradient(165deg, rgba(15,23,42,0.9), rgba(8,15,30,0.95));
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 18px;
    overflow: hidden;
    transition: all 0.45s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    margin-bottom: 1.5rem;
    position: relative;
}
.sys-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.5), 0 0 40px rgba(0, 212, 255, 0.08);
    border-color: rgba(0, 212, 255, 0.2);
}
.card-img-wrap {
    position: relative;
    height: 160px;
    overflow: hidden;
}
.card-img-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
}
.sys-card:hover .card-img-wrap img { transform: scale(1.1); }
.card-img-overlay {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 60%;
    background: linear-gradient(transparent, rgba(8,15,30,0.95));
    pointer-events: none;
}
.card-tag {
    position: absolute;
    top: 12px; right: 12px;
    padding: 0.3rem 0.8rem;
    border-radius: 8px;
    font-size: 0.68rem;
    font-weight: 600;
    color: #fff;
    background: rgba(0,0,0,0.5);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
}
.card-body {
    padding: 1.2rem 1.3rem 1.4rem;
}
.card-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #f0f4f8;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.card-desc {
    font-size: 0.8rem;
    color: #6b7fa3;
    line-height: 1.7;
    margin-bottom: 1rem;
}
.card-url {
    background: rgba(0, 20, 50, 0.6);
    padding: 8px 10px;
    border-radius: 6px;
    font-family: monospace;
    font-size: 11px;
    color: #5fd0ff;
    word-break: break-all;
    margin-bottom: 1rem;
}
.card-footer {
    display: flex;
    align-items: center;
    gap: 12px;
}
.qr-box {
    background: #0f172a;
    padding: 6px;
    border-radius: 8px;
    border: 1px solid rgba(0, 212, 255, 0.2);
    flex-shrink: 0;
}

/* ===== 跳转按钮样式覆盖 ===== */
.stLinkButton > a {
    width: 100% !important;
    height: 100% !important;
    background: linear-gradient(135deg, #00d4ff, #0099cc) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    text-align: center !important;
    box-shadow: 0 0 12px rgba(0, 150, 255, 0.3) !important;
    transition: all 0.3s !important;
    font-size: 0.85rem !important;
}
.stLinkButton > a:hover {
    box-shadow: 0 0 20px rgba(0, 229, 255, 0.6) !important;
    transform: translateY(-2px) !important;
    filter: brightness(1.1) !important;
}

/* ===== 科技画廊 ===== */
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.2rem;
}
.gallery-card {
    position: relative;
    border-radius: 16px;
    overflow: hidden;
    height: 200px;
    border: 1px solid rgba(255,255,255,0.05);
    transition: all 0.4s;
}
.gallery-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    border-color: rgba(0,212,255,0.2);
}
.gallery-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s;
}
.gallery-card:hover img { transform: scale(1.08); }
.gallery-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(transparent 40%, rgba(3,7,18,0.9));
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 1.2rem;
}
.gallery-overlay h4 {
    font-size: 0.95rem;
    font-weight: 700;
    color: #f0f4f8;
    margin-bottom: 0.2rem;
}
.gallery-overlay p {
    font-size: 0.72rem;
    color: #8b9bb4;
}

/* ===== 核心优势 ===== */
.adv-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.2rem;
}
.adv-card {
    background: linear-gradient(165deg, rgba(15,23,42,0.8), rgba(8,15,30,0.9));
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 16px;
    padding: 1.8rem 1.2rem;
    text-align: center;
    transition: all 0.4s;
    position: relative;
    overflow: hidden;
}
.adv-card::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(0,212,255,0.03), transparent 70%);
    opacity: 0;
    transition: opacity 0.4s;
}
.adv-card:hover {
    transform: translateY(-6px);
    border-color: rgba(0,212,255,0.2);
    box-shadow: 0 15px 35px rgba(0,0,0,0.3);
}
.adv-card:hover::before { opacity: 1; }
.adv-icon {
    font-size: 2rem;
    margin-bottom: 0.8rem;
    filter: drop-shadow(0 0 8px rgba(0,212,255,0.4));
}
.adv-title {
    font-size: 1rem;
    font-weight: 700;
    color: #f0f4f8;
    margin-bottom: 0.4rem;
}
.adv-desc {
    font-size: 0.78rem;
    color: #6b7fa3;
    line-height: 1.6;
}

/* ===== 页脚 ===== */
.footer {
    text-align: center;
    padding: 2rem 0 0;
    color: #6b7fa3;
    font-size: 0.8rem;
    border-top: 1px solid rgba(255,255,255,0.05);
    margin-top: 3rem;
}
</style>
"""

# 注入全局样式
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ===================== 粒子背景渲染 =====================
particles_html = '<div class="particles-bg">'
for i in range(30):
    delay = i * 0.3
    duration = 12 + (i % 8)
    left_pos = (i * 3.3) % 100
    particles_html += f'<div class="particle" style="left:{left_pos}%; animation-duration:{duration}s; animation-delay:{delay}s;"></div>'
particles_html += '</div>'
st.markdown(particles_html, unsafe_allow_html=True)

# 内容包裹层（确保所有内容在粒子上方）
st.markdown('<div class="content-wrap">', unsafe_allow_html=True)

# ===================== 顶部导航栏 =====================
st.markdown("""
<div class="top-bar">
    <div class="logo">
        <div class="logo-icon">🌐</div>
        <span>DATA INTELLIGENCE</span>
    </div>
    <div class="nav-links">
        <a href="#系统导航">系统导航</a>
        <a href="#科技画廊">科技画廊</a>
        <a href="#核心优势">核心优势</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ===================== Hero 首屏 =====================
st.markdown("""
<div class="hero-section">
    <div class="hero-bg"></div>
    <div class="hero-content">
        <div class="hero-badge">
            <span class="dot"></span>
            企业数据智能分析平台 · 统一门户
        </div>
        <h1 class="hero-title">数字化转型全域导航中台</h1>
        <p class="hero-sub">整合预测分析、数字经济、ESG评估、大数据处理等11大业务系统，一站式访问企业级数据智能应用集群</p>
        <div class="hero-stats">
            <div class="hero-stat">
                <div class="num">11</div>
                <div class="label">业务系统</div>
            </div>
            <div class="hero-stat">
                <div class="num">24/7</div>
                <div class="label">稳定运行</div>
            </div>
            <div class="hero-stat">
                <div class="num">TB级</div>
                <div class="label">数据处理</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===================== 业务系统数据（11个链接100%精准对应） =====================
SYSTEMS = [
    {
        "name": "智能预测分析平台",
        "desc": "融合机器学习与时序算法的企业级预测系统，提供精准趋势预判与智能决策辅助，支撑数字化战略规划。",
        "url": "https://newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app/",
        "icon": "📈",
        "tag": "AI预测",
        "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80"
    },
    {
        "name": "数字经济分析平台",
        "desc": "聚焦数字经济产业发展全景，覆盖产业数字化、数字贸易与数字金融，多维可视化呈现经济运行态势。",
        "url": "https://digital-encomy.streamlit.app/",
        "icon": "🌐",
        "tag": "经济分析",
        "img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&q=80"
    },
    {
        "name": "数字经济综合门户",
        "desc": "整合全量数字经济资源的核心主站，支持自定义筛选与深度数据挖掘，交互式图表直观展示核心指标。",
        "url": "https://digital-encomy-main.streamlit.app/",
        "icon": "🏛️",
        "tag": "综合门户",
        "img": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&q=80"
    },
    {
        "name": "大数据作业实训平台",
        "desc": "学术大数据课程专用实训平台，集成数据清洗、特征工程与建模工具，支持批量自动化分析流程。",
        "url": "https://xuejiededashujuzuoye.streamlit.app/",
        "icon": "📝",
        "tag": "学术实训",
        "img": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&q=80"
    },
    {
        "name": "海量大数据分析系统",
        "desc": "企业级海量数据处理解决方案，支持超大规模数据集实时计算、多维度交叉分析与可视化报表输出。",
        "url": "https://big-data-hmjdjensqzboumvsvydca3.streamlit.app/",
        "icon": "🧮",
        "tag": "大数据处理",
        "img": "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=800&q=80"
    },
    {
        "name": "ESG数字化评估平台",
        "desc": "企业环境、社会与治理全维度数字化评估体系，提供指标追踪、评级分析与可持续发展报告生成。",
        "url": "https://esgdigital.streamlit.app/",
        "icon": "🌱",
        "tag": "ESG评估",
        "img": "https://images.unsplash.com/photo-1532619675605-1ede6c2ed2b0?w=800&q=80"
    },
    {
        "name": "业务应用分析平台",
        "desc": "通用业务应用数据分析门户，支持多源异构数据接入与自定义仪表盘搭建，适配个性化分析场景。",
        "url": "https://app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app/",
        "icon": "📱",
        "tag": "应用门户",
        "img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&q=80"
    },
    {
        "name": "2007-2023数字化转型看板",
        "desc": "覆盖2007-2023年数字化转型历程数据，纵向对比企业数字化成熟度演变趋势与关键发展里程碑。",
        "url": "https://20072023digital.streamlit.app/",
        "icon": "📅",
        "tag": "时序分析",
        "img": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800&q=80"
    },
    {
        "name": "1999-2023数字化发展平台",
        "desc": "超长周期数字化发展追踪系统，洞察1999-2023二十余年数字化变革规律与产业演进趋势。",
        "url": "https://19992023digital.streamlit.app/",
        "icon": "📊",
        "tag": "长期追踪",
        "img": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&q=80"
    },
    {
        "name": "企业数字化指数系统",
        "desc": "上市公司数字化水平综合评估体系，提供行业对标、排名分析与数字化能力提升路径建议。",
        "url": "https://1999-2023companydeindex-tgax4uws6a7.streamlit.app/",
        "icon": "📋",
        "tag": "指数评估",
        "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80"
    },
    {
        "name": "SmartBI可视化大屏",
        "desc": "企业级SmartBI数据可视化平台，承载数字化转型TOP企业、行业分布、全国地图与时序分析等核心报表。",
        "url": "http://47.98.202.43/smartbi/vision/share.jsp?resid=100ef521ecf6c5860d5917a961a6e0b0",
        "icon": "🖥️",
        "tag": "BI大屏",
        "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80"
    }
]

# ===================== 系统卡片渲染（三列布局） =====================
st.markdown("""
<div class="section-header" id="系统导航">
    <div class="section-tag">SYSTEM NAVIGATION</div>
    <h2 class="section-title">业务系统导航</h2>
    <p class="section-sub">点击按钮直达系统，扫码可在移动端访问</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")
for idx, sys_item in enumerate(SYSTEMS):
    # 按顺序分配到三列
    if idx % 3 == 0:
        current_col = col1
    elif idx % 3 == 1:
        current_col = col2
    else:
        current_col = col3
    
    with current_col:
        # 生成当前系统的二维码
        qr_image = generate_qr(sys_item["url"])
        
        # 卡片头部HTML
        st.markdown(f'''
        <div class="sys-card">
            <div class="card-img-wrap">
                <img src="{sys_item["img"]}" alt="{sys_item["name"]}">
                <div class="card-img-overlay"></div>
                <span class="card-tag">{sys_item["tag"]}</span>
            </div>
            <div class="card-body">
                <div class="card-title">{sys_item["icon"]} {sys_item["name"]}</div>
                <div class="card-desc">{sys_item["desc"]}</div>
                <div class="card-url">{sys_item["url"]}</div>
                <div class="card-footer">
        ''', unsafe_allow_html=True)
        
        # 底部二维码+按钮布局
        qr_col, btn_col = st.columns([1, 1.5])
        with qr_col:
            st.markdown('<div class="qr-box">', unsafe_allow_html=True)
            st.image(qr_image, width=80)
            st.markdown('</div>', unsafe_allow_html=True)
        with btn_col:
            st.link_button("🚀 立即访问", url=sys_item["url"], use_container_width=True)
        
        # 卡片闭合HTML
        st.markdown('''
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

# ===================== 科技画廊模块 =====================
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header" id="科技画廊">
    <div class="section-tag">TECH GALLERY</div>
    <h2 class="section-title">科技能力展示</h2>
    <p class="section-sub">前沿技术架构支撑企业数字化全链路升级</p>
</div>
""", unsafe_allow_html=True)

GALLERY_DATA = [
    {"img": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&q=80", "title": "智能算力网络", "desc": "全域分布式算力调度架构"},
    {"img": "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=800&q=80", "title": "数据仓储中心", "desc": "PB级企业数据湖存储方案"},
    {"img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&q=80", "title": "AI智能引擎", "desc": "深度学习驱动的智能分析"},
    {"img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&q=80", "title": "云端算力平台", "desc": "弹性扩展的云原生基础设施"},
    {"img": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&q=80", "title": "数据安全防护", "desc": "全链路企业数据安全体系"},
    {"img": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800&q=80", "title": "流程自动化", "desc": "智能化业务流程自动引擎"}
]

g_col1, g_col2, g_col3 = st.columns(3, gap="medium")
gallery_cols = [g_col1, g_col2, g_col3]
for idx, item in enumerate(GALLERY_DATA):
    with gallery_cols[idx % 3]:
        st.markdown(f'''
        <div class="gallery-card">
            <img src="{item["img"]}" alt="{item["title"]}">
            <div class="gallery-overlay">
                <h4>{item["titl