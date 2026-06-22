import streamlit as st
import qrcode
from io import BytesIO

# ---------- 页面配置 ----------
st.set_page_config(
    page_title="数字智能 · 链接导航",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- 自定义 CSS（淡蓝粉紫 · 毛玻璃 · 精美排版） ----------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    .stApp {
        background: radial-gradient(circle at 10% 20%, #f0e6ff 0%, #e0f0ff 50%, #f5e6ff 100%);
        color: #2d3a4a;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    header { display: none; }
    .main-container {
        max-width: 1300px;
        margin: 0 auto;
        padding: 0 1.8rem 2rem;
    }

    /* 顶部导航 */
    .top-nav {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 0 1.2rem;
        border-bottom: 1px solid rgba(180, 160, 220, 0.25);
        margin-bottom: 1.8rem;
        flex-wrap: wrap;
        gap: 0.8rem;
    }
    .logo {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-weight: 700;
        font-size: 1.3rem;
        color: #6a4c9c;
        letter-spacing: 0.04em;
    }
    .logo svg {
        width: 28px; height: 28px;
        stroke: #6a4c9c;
        fill: none;
        stroke-width: 2.2;
    }
    .nav-links {
        display: flex;
        gap: 2rem;
    }
    .nav-links a {
        color: #5a6a8a;
        text-decoration: none;
        font-size: 0.95rem;
        font-weight: 500;
        transition: color 0.3s;
    }
    .nav-links a:hover {
        color: #7c5cbf;
    }

    /* Hero */
    .hero {
        position: relative;
        border-radius: 28px;
        overflow: hidden;
        margin-bottom: 2.5rem;
        background: url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&h=300&fit=crop') center/cover no-repeat;
        box-shadow: 0 8px 30px rgba(100, 80, 180, 0.15);
    }
    .hero-overlay {
        background: linear-gradient(135deg, rgba(240, 230, 255, 0.75), rgba(220, 240, 255, 0.7));
        backdrop-filter: blur(3px);
        padding: 3rem 2rem;
        text-align: center;
    }
    .hero h1 {
        font-size: 2.8rem;
        font-weight: 800;
        color: #3b2a5a;
        margin-bottom: 0.4rem;
        text-shadow: 0 2px 10px rgba(255,255,255,0.3);
    }
    .hero p {
        font-size: 1.15rem;
        color: #4a3a6a;
        max-width: 700px;
        margin: 0 auto 0.8rem;
        font-weight: 500;
    }
    .hero-btn {
        display: inline-block;
        padding: 0.7rem 2.2rem;
        border-radius: 50px;
        background: linear-gradient(90deg, #b39ddb, #81d4fa);
        color: #1f2a3a;
        font-weight: 600;
        text-decoration: none;
        box-shadow: 0 4px 15px rgba(120, 100, 200, 0.25);
        transition: transform 0.2s, box-shadow 0.2s;
        border: none;
        cursor: pointer;
    }
    .hero-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(120, 100, 200, 0.4);
    }

    /* 卡片 */
    .card-wrapper {
        background: rgba(255, 255, 255, 0.55);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(120, 100, 180, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.6);
        transition: all 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .card-wrapper:hover {
        transform: translateY(-6px);
        box-shadow: 0 16px 40px rgba(120, 100, 180, 0.18);
        border-color: rgba(180, 150, 220, 0.5);
    }
    .card-img {
        width: 100%;
        height: 170px;
        object-fit: cover;
        display: block;
        border-bottom: 1px solid rgba(200, 180, 220, 0.2);
    }
    .card-body {
        padding: 1.2rem 1.2rem 1.2rem;
        flex: 1;
        display: flex;
        flex-direction: column;
    }
    .card-title {
        font-size: 1.0rem;
        font-weight: 700;
        color: #2f2a4a;
        margin-bottom: 0.3rem;
        line-height: 1.3;
        word-break: break-all;
    }
    .card-desc {
        font-size: 0.82rem;
        color: #4a4a6a;
        line-height: 1.5;
        flex: 1;
        margin-bottom: 0.8rem;
    }
    .card-footer {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.5rem;
        margin-top: auto;
    }
    .qr-container {
        display: flex;
        justify-content: center;
        margin-bottom: 0.2rem;
    }
    .qr-container img {
        border-radius: 10px;
        background: white;
        padding: 4px;
        width: 100px;
        height: 100px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    .stLinkButton button {
        width: 100%;
        padding: 0.6rem 0;
        border-radius: 40px;
        font-weight: 600;
        font-size: 0.95rem;
        border: none;
        color: #1f1a3a;
        background: linear-gradient(90deg, #b39ddb, #81d4fa);
        transition: opacity 0.25s, transform 0.2s;
        cursor: pointer;
        box-shadow: 0 2px 10px rgba(120, 100, 200, 0.15);
    }
    .stLinkButton button:hover {
        opacity: 0.9;
        transform: scale(1.02);
        box-shadow: 0 4px 18px rgba(120, 100, 200, 0.25);
    }
    .btn-alt .stLinkButton button {
        background: linear-gradient(90deg, #c9b0ff, #a8d8ff);
    }

    /* 优势 */
    .adv-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.2rem;
        margin: 2rem 0;
    }
    .adv-card {
        background: rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(8px);
        border-radius: 16px;
        padding: 1.5rem 1rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.6);
        transition: border-color 0.3s, box-shadow 0.3s;
    }
    .adv-card:hover {
        border-color: #b39ddb;
        box-shadow: 0 4px 20px rgba(120, 100, 200, 0.08);
    }
    .adv-icon {
        font-size: 2.2rem;
        margin-bottom: 0.4rem;
    }
    .adv-card h4 {
        font-size: 1rem;
        font-weight: 700;
        color: #2f2a4a;
        margin-bottom: 0.2rem;
    }
    .adv-card p {
        font-size: 0.8rem;
        color: #4a4a6a;
        line-height: 1.4;
    }

    /* 二维码集中展示 */
    .qr-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.2rem;
        margin: 1.5rem 0;
    }
    .qr-grid-item {
        background: rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(8px);
        border-radius: 16px;
        padding: 1.2rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.6);
        transition: border-color 0.3s;
    }
    .qr-grid-item:hover {
        border-color: #b39ddb;
    }
    .qr-grid-item img {
        width: 130px;
        height: 130px;
        border-radius: 10px;
        background: white;
        padding: 5px;
        margin-bottom: 0.4rem;
    }
    .qr-grid-item .qr-name {
        font-weight: 600;
        color: #2f2a4a;
        font-size: 0.9rem;
        word-break: break-all;
    }
    .qr-grid-item .qr-url {
        font-size: 0.7rem;
        color: #5a5a7a;
        word-break: break-all;
        line-height: 1.3;
    }

    /* 页脚 */
    .footer {
        text-align: center;
        border-top: 1px solid rgba(180, 160, 220, 0.2);
        padding: 2rem 1rem 1rem;
        margin-top: 2.5rem;
        color: #4a4a6a;
        font-size: 0.85rem;
    }
    .footer h3 {
        color: #2f2a4a;
        font-weight: 700;
        font-size: 1.2rem;
        margin-bottom: 0.4rem;
    }
    .footer p {
        max-width: 600px;
        margin: 0 auto 0.8rem;
        line-height: 1.6;
    }
    .footer-social {
        display: flex;
        justify-content: center;
        gap: 1.2rem;
        margin-top: 0.6rem;
    }
    .footer-social a {
        color: #4a4a6a;
        text-decoration: none;
        font-size: 1.4rem;
        transition: color 0.3s;
    }
    .footer-social a:hover {
        color: #7c5cbf;
    }

    @media (max-width: 1024px) {
        .adv-grid { grid-template-columns: repeat(2, 1fr); }
        .qr-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 640px) {
        .hero h1 { font-size: 2rem; }
        .top-nav { flex-direction: column; align-items: stretch; }
        .nav-links { justify-content: center; flex-wrap: wrap; gap: 1rem; }
        .adv-grid, .qr-grid { grid-template-columns: 1fr; }
    }
</style>
""", unsafe_allow_html=True)

# ---------- 顶部导航 ----------
st.markdown("""
<div class="top-nav">
    <div class="logo">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
        </svg>
        数字智能 · 聚合导航
    </div>
    <div class="nav-links">
        <a href="#features">功能模块</a>
        <a href="#advantages">核心优势</a>
        <a href="#qrcodes">移动端</a>
        <a href="#about">关于我们</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- Hero ----------
st.markdown("""
<div class="hero">
    <div class="hero-overlay">
        <h1>✨ 企业数据智能分析平台</h1>
        <p>整合企业数字化转型 · ESG分析 · 数据可视化，助力智能决策</p>
        <a class="hero-btn" href="#features">探索数据应用 ↓</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- 功能模块标题 ----------
st.markdown('<h2 id="features" style="text-align:center; color:#2f2a4a; margin-top:1.5rem;">系统功能介绍</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#4a4a6a; margin-bottom:1.8rem;">我们提供多个专业数据系统，满足企业不同维度的分析需求</p>', unsafe_allow_html=True)

# ---------- 链接数据：标题 = 域名/路径（完全对应） ----------
links_info = [
    {
        "name": "newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app",
        "desc": "全新升级的企业预测分析模型，提供精准趋势预测，辅助决策制定。",
        "url": "https://newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app/",
        "seed": 10
    },
    {
        "name": "digital-encomy.streamlit.app",
        "desc": "专注全球数字经济发展趋势分析，数据可视化呈现产业经济现状。",
        "url": "https://digital-encomy.streamlit.app/",
        "seed": 20
    },
    {
        "name": "digital-encomy-main.streamlit.app",
        "desc": "整合多维数据资源，交互式图表展示经济指标，支持自定义筛选。",
        "url": "https://digital-encomy-main.streamlit.app/",
        "seed": 30
    },
    {
        "name": "xuejiededashujuzuoye.streamlit.app",
        "desc": "学届大数据作业专用分析平台，集成数据清洗与建模工具。",
        "url": "https://xuejiededashujuzuoye.streamlit.app/",
        "seed": 40
    },
    {
        "name": "big-data-hmjdjensqzboumvsvydca3.streamlit.app",
        "desc": "企业级大数据解决方案，支持海量数据实时处理与交叉分析。",
        "url": "https://big-data-hmjdjensqzboumvsvydca3.streamlit.app/",
        "seed": 50
    },
    {
        "name": "esgdigital.streamlit.app",
        "desc": "企业环境、社会与治理数据评估，提供ESG指标追踪与评级。",
        "url": "https://esgdigital.streamlit.app/",
        "seed": 60
    },
    {
        "name": "app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app",
        "desc": "通用数据分析平台，支持多源接入与自定义仪表盘。",
        "url": "https://app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app/",
        "seed": 70
    },
    {
        "name": "20072023digital.streamlit.app",
        "desc": "覆盖2007-2023年企业数字化转型历程，纵向对比趋势。",
        "url": "https://20072023digital.streamlit.app/",
        "seed": 80
    },
    {
        "name": "19992023digital.streamlit.app",
        "desc": "更长周期（1999-2023）企业数字化发展数据洞察。",
        "url": "https://19992023digital.streamlit.app/",
        "seed": 90
    },
    {
        "name": "1999-2023companydeindex-tgax4uws6a7.streamlit.app",
        "desc": "综合评估企业数字化水平，提供行业对标与改进建议。",
        "url": "https://1999-2023companydeindex-tgax4uws6a7.streamlit.app/",
        "seed": 100
    },
    {
        "name": "47.98.202.43 (SmartBI)",
        "desc": "基于SmartBI的企业级可视化平台，支持复杂报表与交互探索。",
        "url": "http://47.98.202.43/smartbi/vision/share.jsp?resid=100ef521ecf6c5860d5917a961a6e0b0",
        "seed": 110
    }
]

# ---------- 二维码生成 ----------
def generate_qr(url):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=4, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#2f2a4a", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

# ---------- 渲染卡片网格（每行3个） ----------
cols_per_row = 3
for i in range(0, len(links_info), cols_per_row):
    row_items = links_info[i:i+cols_per_row]
    cols = st.columns(cols_per_row, gap="medium")
    for j, (col, item) in enumerate(zip(cols, row_items)):
        with col:
            img_url = f"https://picsum.photos/seed/{item['seed']}/400/200"
            btn_alt = "btn-alt" if (i + j) % 2 == 1 else ""
            st.markdown(f"""
            <div class="card-wrapper">
                <img class="card-img" src="{img_url}" alt="{item['name']}">
                <div class="card-body">
                    <div class="card-title">{item['name']}</div>
                    <div class="card-desc">{item['desc']}</div>
                    <div class="card-footer">
                        <div class="qr-container">
            """, unsafe_allow_html=True)
            
            # 二维码（居中）
            qr_bytes = generate_qr(item['url'])
            st.image(qr_bytes, width=100, use_column_width="never", output_format="PNG")
            
            st.markdown("""
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # 跳转按钮（全宽，位于卡片底部）
            st.link_button(f"🚀 打开", item['url'], use_container_width=True)

# ---------- 核心优势 ----------
st.markdown('<h2 id="advantages" style="text-align:center; color:#2f2a4a; margin-top:2.5rem;">平台核心优势</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#4a4a6a; margin-bottom:1.2rem;">整合多种先进技术，提供全方位数据分析解决方案</p>', unsafe_allow_html=True)

adv_data = [
    {"icon": "📊", "title": "整合多维数据", "desc": "支持多个数据源统一接入"},
    {"icon": "📈", "title": "专业算法引擎", "desc": "精准预测趋势，辅助决策"},
    {"icon": "⏱️", "title": "响应式设计", "desc": "完美支持PC与移动端"},
    {"icon": "🧩", "title": "模块化定制", "desc": "灵活组合分析模块"}
]

cols = st.columns(4)
for col, adv in zip(cols, adv_data):
    with col:
        st.markdown(f"""
        <div class="adv-card">
            <div class="adv-icon">{adv['icon']}</div>
            <h4>{adv['title']}</h4>
            <p>{adv['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------- 二维码集中展示（移动端访问） ----------
st.markdown('<h2 id="qrcodes" style="text-align:center; color:#2f2a4a; margin-top:2.5rem;">移动端访问</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#4a4a6a; margin-bottom:1.2rem;">扫描二维码，在手机上访问对应系统</p>', unsafe_allow_html=True)

for i in range(0, len(links_info), 3):
    row = links_info[i:i+3]
    cols = st.columns(3, gap="medium")
    for col, item in zip(cols, row):
        with col:
            qr_bytes = generate_qr(item['url'])
            st.image(qr_bytes, width=130, use_column_width="never", output_format="PNG")
            st.markdown(f"<div class='qr-name'>{item['name']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='qr-url'>{item['url']}</div>", unsafe_allow_html=True)

# ---------- 页脚 ----------
st.markdown("""
<div class="footer" id="about">
    <h3>✨ 关于我们</h3>
    <p>我们致力于为企业提供专业的数据智能分析工具，整合多个数据分析平台与可视化系统，通过先进的算法与模型技术，帮助企业实现数据驱动决策，优化运营流程。</p>
    <div class="footer-social">
        <a href="#" target="_blank">🐙</a>
        <a href="#" target="_blank">🐦</a>
        <a href="#" target="_blank">🔗</a>
    </div>
    <div style="margin-top:0.8rem; font-size:0.7rem; opacity:0.6;">© 2026 数字智能导航 · 淡蓝粉紫设计</div>
</div>
""", unsafe_allow_html=True)