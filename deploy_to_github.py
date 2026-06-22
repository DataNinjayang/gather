import streamlit as st
import qrcode
from io import BytesIO
import base64

# ---------- 页面配置 ----------
st.set_page_config(
    page_title="数字智能分析平台 · 链接导航",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- 自定义CSS（完全参考HTML风格） ----------
st.markdown("""
<style>
    /* 全局重置 & 字体 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    .stApp {
        background: #050b14;
        color: #e8ecf1;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    header { display: none; }
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1.5rem 2rem;
    }

    /* ----- 顶部导航（模拟） ----- */
    .top-nav {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1.2rem 0;
        border-bottom: 1px solid #1a2a44;
        margin-bottom: 2rem;
        flex-wrap: wrap;
        gap: 1rem;
    }
    .logo {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-weight: 700;
        font-size: 1.2rem;
        color: #00d4ff;
        letter-spacing: 0.05em;
    }
    .logo svg {
        width: 28px;
        height: 28px;
        stroke: #00d4ff;
        fill: none;
        stroke-width: 2;
    }
    .nav-links {
        display: flex;
        gap: 2rem;
    }
    .nav-links a {
        color: #8b9bb4;
        text-decoration: none;
        font-size: 0.9rem;
        transition: color 0.3s;
    }
    .nav-links a:hover {
        color: #00d4ff;
    }

    /* ----- Hero 区域 ----- */
    .hero {
        position: relative;
        text-align: center;
        padding: 4rem 1rem 5rem;
        margin-bottom: 2rem;
        border-radius: 24px;
        overflow: hidden;
        background: url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&h=400&fit=crop') center/cover no-repeat;
    }
    .hero::after {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(5,11,20,0.4) 0%, #050b14 100%);
        z-index: 0;
    }
    .hero-content {
        position: relative;
        z-index: 1;
        max-width: 800px;
        margin: 0 auto;
    }
    .hero h1 {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(90deg, #00d4ff, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.8rem;
    }
    .hero p {
        color: #8b9bb4;
        font-size: 1.1rem;
        max-width: 600px;
        margin: 0 auto 1.8rem;
    }

    /* ----- 卡片样式（玻璃态 + 悬停） ----- */
    .card-wrapper {
        background: #0a1120;
        border: 1px solid #1a2a44;
        border-radius: 16px;
        overflow: hidden;
        transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .card-wrapper:hover {
        transform: translateY(-6px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.5);
        border-color: #00d4ff;
    }
    .card-img {
        width: 100%;
        height: 160px;
        object-fit: cover;
        display: block;
    }
    .card-body {
        padding: 1.2rem 1.2rem 1.4rem;
        flex: 1;
        display: flex;
        flex-direction: column;
    }
    .card-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #e8ecf1;
        margin-bottom: 0.3rem;
    }
    .card-desc {
        font-size: 0.82rem;
        color: #8b9bb4;
        line-height: 1.5;
        flex: 1;
        margin-bottom: 1rem;
    }
    .card-footer {
        display: flex;
        flex-direction: column;
        gap: 0.6rem;
        margin-top: auto;
    }
    .qr-container {
        display: flex;
        justify-content: center;
        margin: 0.2rem 0;
    }
    .qr-container img {
        border-radius: 8px;
        background: white;
        padding: 4px;
        width: 100px;
        height: 100px;
    }
    .stLinkButton button {
        width: 100%;
        padding: 0.6rem 0;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.9rem;
        border: none;
        color: #fff;
        background: linear-gradient(90deg, #2563eb, #1d4ed8);
        transition: opacity 0.3s, transform 0.3s;
        cursor: pointer;
    }
    .stLinkButton button:hover {
        opacity: 0.9;
        transform: scale(1.02);
    }
    /* 不同按钮颜色（按顺序循环） */
    .btn-purple .stLinkButton button { background: linear-gradient(90deg, #7c3aed, #6d28d9); }
    .btn-cyan .stLinkButton button { background: linear-gradient(90deg, #0891b2, #0e7490); }

    /* ----- 核心优势 ----- */
    .adv-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.2rem;
        margin: 2rem 0;
    }
    .adv-card {
        background: #0a1120;
        border: 1px solid #1a2a44;
        border-radius: 12px;
        padding: 1.4rem 1rem;
        text-align: center;
        transition: border-color 0.3s;
    }
    .adv-card:hover {
        border-color: #00d4ff;
    }
    .adv-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        color: #00d4ff;
    }
    .adv-card h4 {
        font-size: 0.95rem;
        font-weight: 700;
        color: #e8ecf1;
        margin-bottom: 0.3rem;
    }
    .adv-card p {
        font-size: 0.78rem;
        color: #8b9bb4;
        line-height: 1.4;
    }

    /* ----- 页脚 ----- */
    .footer {
        text-align: center;
        border-top: 1px solid #1a2a44;
        padding: 2rem 1rem 1rem;
        margin-top: 3rem;
        color: #8b9bb4;
        font-size: 0.82rem;
    }
    .footer h3 {
        color: #e8ecf1;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    .footer p {
        max-width: 600px;
        margin: 0 auto 1rem;
        line-height: 1.6;
    }
    .footer-social {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 0.8rem;
    }
    .footer-social a {
        color: #8b9bb4;
        text-decoration: none;
        font-size: 1.2rem;
        transition: color 0.3s;
    }
    .footer-social a:hover {
        color: #00d4ff;
    }

    /* 响应式 */
    @media (max-width: 1024px) {
        .adv-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 640px) {
        .hero h1 { font-size: 2rem; }
        .top-nav { flex-direction: column; align-items: stretch; }
        .nav-links { justify-content: center; flex-wrap: wrap; gap: 1rem; }
        .adv-grid { grid-template-columns: 1fr; }
    }
</style>
""", unsafe_allow_html=True)

# ---------- 顶部导航（HTML模拟） ----------
st.markdown("""
<div class="top-nav">
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
</div>
""", unsafe_allow_html=True)

# ---------- Hero 区域 ----------
st.markdown("""
<div class="hero">
    <div class="hero-content">
        <h1>企业数据智能分析平台</h1>
        <p>整合企业数字化转型、ESG分析与数据可视化，助力企业决策智能化</p>
    </div>
</div>
""", unsafe_allow_html=True)

# 在 Hero 下方放一个 CTA 按钮（用 st.link_button 实现）
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.link_button("🚀 探索数据应用", "#features", use_container_width=True)

# ---------- 功能模块（卡片网格） ----------
st.markdown('<h2 style="text-align:center; margin-top:2.5rem;">系统功能介绍</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#8b9bb4; margin-bottom:2rem;">我们提供多个专业数据系统，满足企业不同维度的数据分析需求</p>', unsafe_allow_html=True)

# ---------- 链接数据（名称、描述、URL、图片种子） ----------
# 描述和名称参考 HTML 内容，可自由修改
links_info = [
    {
        "name": "新预测模型",
        "desc": "全新升级的企业预测分析模型，提供精准趋势预测，智能分析辅助决策制定，助力企业数字化战略选择。",
        "url": "https://newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app/",
        "seed": 1
    },
    {
        "name": "数字经济分析",
        "desc": "专注于数字经济领域，对全球数字经济发展趋势分析，数据可视化呈现产业经济现状，支持一键导出报告。",
        "url": "https://digital-encomy.streamlit.app/",
        "seed": 2
    },
    {
        "name": "数字经济主站",
        "desc": "整合企业多维数据资源，通过交互式图表直观展示经济指标，支持自定义筛选与深度数据挖掘。",
        "url": "https://digital-encomy-main.streamlit.app/",
        "seed": 3
    },
    {
        "name": "大数据作业平台",
        "desc": "学届大数据作业专用分析平台，集成多种数据清洗与建模工具，支持批量处理与自动化分析流程。",
        "url": "https://xuejiededashujuzuoye.streamlit.app/",
        "seed": 4
    },
    {
        "name": "大数据分析系统",
        "desc": "企业级大数据分析解决方案，支持海量数据实时处理，多维度交叉分析，助力业务增长与运营优化。",
        "url": "https://big-data-hmjdjensqzboumvsvydca3.streamlit.app/",
        "seed": 5
    },
    {
        "name": "ESG数字化平台",
        "desc": "专注企业环境、社会与治理数据评估，提供ESG指标追踪、评级分析与可持续发展报告生成服务。",
        "url": "https://esgdigital.streamlit.app/",
        "seed": 6
    },
    {
        "name": "应用分析平台",
        "desc": "通用应用数据分析平台，支持多源数据接入与自定义仪表盘，满足个性化业务分析场景需求。",
        "url": "https://app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app/",
        "seed": 7
    },
    {
        "name": "2007-2023 数字化",
        "desc": "覆盖2007至2023年企业数字化转型历程数据，纵向对比分析企业数字化成熟度演变趋势。",
        "url": "https://20072023digital.streamlit.app/",
        "seed": 8
    },
    {
        "name": "1999-2023 数字化",
        "desc": "更长周期的企业数字化发展数据追踪，从1999年至2023年，洞察二十余年数字化变革规律。",
        "url": "https://19992023digital.streamlit.app/",
        "seed": 9
    },
    {
        "name": "企业数字化指数",
        "desc": "综合评估企业数字化水平的核心指标体系，提供行业对标、排名分析与改进建议。",
        "url": "https://1999-2023companydeindex-tgax4uws6a7.streamlit.app/",
        "seed": 10
    },
    {
        "name": "SmartBI 数据可视化",
        "desc": "基于SmartBI的企业级数据可视化平台，支持复杂报表设计与交互式数据探索，助力决策层洞察业务。",
        "url": "http://47.98.202.43/smartbi/vision/share.jsp?resid=100ef521ecf6c5860d5917a961a6e0b0",
        "seed": 11
    }
]

# ---------- 二维码生成函数 ----------
def generate_qr(url):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=4, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#050b14", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

# ---------- 渲染卡片网格（每行3个） ----------
cols_per_row = 3
for i in range(0, len(links_info), cols_per_row):
    row_items = links_info[i:i+cols_per_row]
    cols = st.columns(cols_per_row, gap="medium")
    for col, item in zip(cols, row_items):
        with col:
            # 卡片图片（使用 picsum 随机图片，根据 seed 固定）
            img_url = f"https://picsum.photos/seed/{item['seed']}/400/200"
            # 按钮颜色循环：根据索引 mod 3
            btn_class = ""
            if i % 3 == 0:
                btn_class = ""  # 默认蓝色
            elif i % 3 == 1:
                btn_class = "btn-purple"
            else:
                btn_class = "btn-cyan"
            
            # 构建卡片
            st.markdown(f"""
            <div class="card-wrapper">
                <img class="card-img" src="{img_url}" alt="{item['name']}">
                <div class="card-body">
                    <div class="card-title">{item['name']}</div>
                    <div class="card-desc">{item['desc']}</div>
                    <div class="card-footer">
                        <div class="qr-container">
            """, unsafe_allow_html=True)
            
            # 插入二维码
            qr_bytes = generate_qr(item['url'])
            st.image(qr_bytes, width=100, use_column_width="never", output_format="PNG")
            
            st.markdown("""
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # 按钮（放在卡片外部，但使用 link_button 会另起一行，我们放在卡片内部用 markdown 模拟按钮？）
            # 为了保持卡片内按钮，我们使用 st.link_button 放在卡片外面，但会破坏结构。
            # 解决：用 st.markdown 加一个容器，然后放 link_button，但 link_button 会占据整行，我们可用 columns 控制。
            # 或者使用 st.button 配合 js 跳转？但推荐 link_button。
            # 我们简单在卡片下方放 link_button，但会超出卡片。更佳：在卡片内用 st.link_button 放在容器内，但 streamlit 的组件不能放在 markdown 内。
            # 替代方案：使用 st.button 并利用 st.markdown 的 meta refresh 或使用 st.experimental_rerun？不推荐。
            # 稳妥方案：使用 st.link_button 放在卡片下方，视觉上仍属于卡片。
            # 我们将 link_button 放在卡片容器外，但通过相同列来对齐。
            # 由于我们已经在 with col 中，我们可以在 markdown 后直接调用 st.link_button，它会在卡片下方。
            # 但为了保持卡片整体，我们将 link_button 放在卡片 markdown 后面，并设置样式为全宽。
            # 我们可以为 link_button 包裹一个 div，但 link_button 本身是块级。
            # 我们直接放置，它会出现在卡片下方，但我们可以调整样式使间距紧凑。
            
            # 放置按钮（使用 link_button）
            st.link_button(f"进入 {item['name']}", item['url'], use_container_width=True)

# ---------- 核心优势（四个特点） ----------
st.markdown('<h2 style="text-align:center; margin-top:3rem;">平台核心优势</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#8b9bb4; margin-bottom:2rem;">我们的系统整合多种先进技术，为企业提供全方位的数据分析解决方案</p>', unsafe_allow_html=True)

adv_data = [
    {"icon": "📊", "title": "整合企业多维数据", "desc": "支持多个数据源统一接入与整合"},
    {"icon": "📈", "title": "专业级工具", "desc": "搭载高级算法引擎，精准预测趋势"},
    {"icon": "⏱️", "title": "响应式设计", "desc": "完美支持PC端与移动端无缝访问"},
    {"icon": "🧩", "title": "模块化系统", "desc": "灵活组合不同分析模块，定制专属方案"}
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

# ---------- 二维码集中展示区（可选，为了更接近HTML） ----------
st.markdown('<h2 style="text-align:center; margin-top:3rem;">移动端访问</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#8b9bb4; margin-bottom:2rem;">扫描下方二维码，在手机上访问对应数据系统</p>', unsafe_allow_html=True)

# 每行3个二维码卡片
for i in range(0, len(links_info), 3):
    row = links_info[i:i+3]
    cols = st.columns(3, gap="medium")
    for col, item in zip(cols, row):
        with col:
            qr_bytes = generate_qr(item['url'])
            st.image(qr_bytes, width=140, use_column_width="never", output_format="PNG")
            st.markdown(f"<div style='text-align:center; font-weight:600;'>{item['name']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align:center; font-size:0.7rem; color:#8b9bb4; word-break:break-all;'>{item['url']}</div>", unsafe_allow_html=True)

# ---------- 页脚 ----------
st.markdown("""
<div class="footer" id="about">
    <h3>关于我们</h3>
    <p>我们致力于为企业提供专业的数据智能分析工具，整合多个数据分析平台与可视化系统，通过先进的算法与模型技术，帮助企业实现数据驱动决策，优化运营流程。</p>
    <div class="footer-social">
        <a href="#" target="_blank">🐙</a>
        <a href="#" target="_blank">🐦</a>
        <a href="#" target="_blank">🔗</a>
    </div>
    <div style="margin-top:1rem; font-size:0.7rem; opacity:0.6;">© 2026 企业数据智能平台 · 链接导航</div>
</div>
""", unsafe_allow_html=True)