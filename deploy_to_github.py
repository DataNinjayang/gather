"""
企业数据智能分析平台 - 链接导航主页 (Streamlit 深度优化版)
========================================================
部署方式: streamlit run app.py
特性: 17张AI配图 / 粒子动画背景 / 滚动渐入动画 / 悬停交互
"""

import streamlit as st
import base64
from pathlib import Path

# ============================================================
# 页面基础配置
# ============================================================
st.set_page_config(
    page_title="企业数据智能分析平台",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# 系统数据定义（每个系统对应独立配图，标题与URL严格对应）
# ============================================================
SYSTEMS = [
    {
        "id": 1,
        "name": "New Prediction - 新预测模型",
        "short_name": "新预测模型系统",
        "desc": "全新升级的企业预测分析模型，融合机器学习与深度学习算法，提供精准趋势预测与智能决策辅助，助力企业数字化战略规划。",
        "url": "https://newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app/",
        "icon": "📈",
        "color": "#00d4ff",
        "gradient": "linear-gradient(135deg, #00d4ff, #0099cc)",
        "img": "img_prediction.jpg",
        "tag": "AI 预测",
        "tag_color": "#00d4ff",
    },
    {
        "id": 2,
        "name": "Digital Economy - 数字经济分析",
        "short_name": "数字经济分析平台",
        "desc": "专注于全球数字经济发展趋势分析，涵盖产业数字化、数字贸易与数字金融等领域，数据可视化呈现经济全貌。",
        "url": "https://digital-encomy.streamlit.app/",
        "icon": "🌐",
        "color": "#a855f7",
        "gradient": "linear-gradient(135deg, #a855f7, #7c3aed)",
        "img": "img_digital_economy.jpg",
        "tag": "经济分析",
        "tag_color": "#a855f7",
    },
    {
        "id": 3,
        "name": "Digital Economy Main - 数字经济主站",
        "short_name": "数字经济综合门户",
        "desc": "整合企业多维数据资源的数字经济综合门户，通过交互式图表直观展示经济指标，支持自定义筛选与深度数据挖掘。",
        "url": "https://digital-encomy-main.streamlit.app/",
        "icon": "🏛️",
        "color": "#06b6d4",
        "gradient": "linear-gradient(135deg, #06b6d4, #0891b2)",
        "img": "img_digital_economy.jpg",
        "tag": "综合门户",
        "tag_color": "#06b6d4",
    },
    {
        "id": 4,
        "name": "Big Data Homework - 大数据作业平台",
        "short_name": "大数据学术作业平台",
        "desc": "学术大数据作业专用分析平台，集成多种数据清洗、特征工程与建模工具，支持批量处理与自动化分析流程。",
        "url": "https://xuejiededashujuzuoye.streamlit.app/",
        "icon": "📝",
        "color": "#3b82f6",
        "gradient": "linear-gradient(135deg, #3b82f6, #2563eb)",
        "img": "img_bigdata.jpg",
        "tag": "学术平台",
        "tag_color": "#3b82f6",
    },
    {
        "id": 5,
        "name": "Big Data Analysis - 大数据分析系统",
        "short_name": "大数据分析系统",
        "desc": "企业级大数据分析解决方案，支持海量数据实时处理、多维度交叉分析与可视化报表，助力业务增长与运营优化。",
        "url": "https://big-data-hmjdjensqzboumvsvydca3.streamlit.app/",
        "icon": "🧮",
        "color": "#8b5cf6",
        "gradient": "linear-gradient(135deg, #8b5cf6, #7c3aed)",
        "img": "img_data_warehouse.jpg",
        "tag": "数据分析",
        "tag_color": "#8b5cf6",
    },
    {
        "id": 6,
        "name": "ESG Digital - ESG数字化平台",
        "short_name": "ESG数字化评估平台",
        "desc": "专注企业环境(Environment)、社会(Social)与治理(Governance)数据评估，提供ESG指标追踪、评级分析与可持续发展报告。",
        "url": "https://esgdigital.streamlit.app/",
        "icon": "🌱",
        "color": "#10b981",
        "gradient": "linear-gradient(135deg, #10b981, #059669)",
        "img": "img_esg.jpg",
        "tag": "ESG 评估",
        "tag_color": "#10b981",
    },
    {
        "id": 7,
        "name": "App Analysis - 应用分析平台",
        "short_name": "应用数据分析平台",
        "desc": "通用应用数据分析平台，支持多源数据接入与自定义仪表盘搭建，满足个性化业务分析场景需求。",
        "url": "https://app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app/",
        "icon": "📱",
        "color": "#f59e0b",
        "gradient": "linear-gradient(135deg, #f59e0b, #d97706)",
        "img": "img_app.jpg",
        "tag": "应用平台",
        "tag_color": "#f59e0b",
    },
    {
        "id": 8,
        "name": "2007-2023 Digital Transformation",
        "short_name": "2007-2023 数字化转型",
        "desc": "覆盖2007至2023年企业数字化转型历程数据，纵向对比分析企业数字化成熟度演变趋势与关键里程碑。",
        "url": "https://20072023digital.streamlit.app/",
        "icon": "📅",
        "color": "#ec4899",
        "gradient": "linear-gradient(135deg, #ec4899, #db2777)",
        "img": "img_digitization.jpg",
        "tag": "数字化转型",
        "tag_color": "#ec4899",
    },
    {
        "id": 9,
        "name": "1999-2023 Digital Transformation",
        "short_name": "1999-2023 数字化转型",
        "desc": "更长周期的企业数字化发展数据追踪，从1999年至2023年，洞察二十余年数字化变革规律与演进趋势。",
        "url": "https://19992023digital.streamlit.app/",
        "icon": "📊",
        "color": "#06b6d4",
        "gradient": "linear-gradient(135deg, #06b6d4, #0e7490)",
        "img": "img_automation.jpg",
        "tag": "长期追踪",
        "tag_color": "#06b6d4",
    },
    {
        "id": 10,
        "name": "Company Digital Index - 企业数字化指数",
        "short_name": "企业数字化指数评估",
        "desc": "综合评估企业数字化水平的核心指标体系，提供行业对标分析、排名评估与数字化改进建议。",
        "url": "https://1999-2023companydeindex-tgax4uws6a7.streamlit.app/",
        "icon": "📋",
        "color": "#f97316",
        "gradient": "linear-gradient(135deg, #f97316, #ea580c)",
        "img": "img_analytics.jpg",
        "tag": "指数评估",
        "tag_color": "#f97316",
    },
    {
        "id": 11,
        "name": "SmartBI - 数据可视化平台",
        "short_name": "SmartBI 数据可视化",
        "desc": "基于SmartBI的企业级数据可视化平台，支持复杂报表设计、交互式数据探索与多维分析，助力决策层洞察业务全貌。",
        "url": "http://47.98.202.43/smartbi/vision/share.jsp?resid=100ef521ecf6c5860d5917a961a6e0b0",
        "icon": "🖥️",
        "color": "#a855f7",
        "gradient": "linear-gradient(135deg, #a855f7, #9333ea)",
        "img": "img_smartbi.jpg",
        "tag": "BI 可视化",
        "tag_color": "#a855f7",
    },
]

# ============================================================
# 图片展示画廊数据（展示更多AI配图）
# ============================================================
GALLERY = [
    {"img": "img_tech_network.jpg", "title": "智能网络架构", "desc": "全域互联的数据传输网络"},
    {"img": "img_data_warehouse.jpg", "title": "数据仓储中心", "desc": "海量数据安全存储与管理"},
    {"img": "img_ai_brain.jpg", "title": "AI 智能引擎", "desc": "深度学习驱动的智能分析"},
    {"img": "img_cloud_compute.jpg", "title": "云端算力平台", "desc": "弹性扩展的云计算基础设施"},
    {"img": "img_security.jpg", "title": "数据安全防护", "desc": "企业级数据安全保障体系"},
    {"img": "img_automation.jpg", "title": "流程自动化引擎", "desc": "智能化的业务流程自动化"},
    {"img": "img_analytics.jpg", "title": "多维数据分析", "desc": "全方位数据洞察与可视化"},
    {"img": "img_blockchain.jpg", "title": "分布式信任网络", "desc": "区块链驱动的数据可信交换"},
    {"img": "img_iot.jpg", "title": "万物互联生态", "desc": "IoT设备数据采集与协同"},
]

# ============================================================
# 自定义 CSS 样式（科技感深色主题 - 深度优化版）
# ============================================================
CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    /* ===== 全局 ===== */
    * { box-sizing: border-box; }
    .stApp {
        background: #030712;
        color: #e0e7ef;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    #MainMenu, footer, header { visibility: hidden; }
    .block-container {
        padding-top: 0;
        padding-bottom: 4rem;
        max-width: 1400px;
    }

    /* ===== 粒子动画背景 ===== */
    .particles-bg {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        z-index: -1;
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

    /* ===== 顶部导航条 ===== */
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
        position: relative;
        padding-bottom: 0.3rem;
    }
    .top-bar .nav-links a::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0;
        width: 0; height: 2px;
        background: linear-gradient(90deg, #00d4ff, #a855f7);
        transition: width 0.3s;
    }
    .top-bar .nav-links a:hover { color: #00d4ff; }
    .top-bar .nav-links a:hover::after { width: 100%; }

    /* ===== Hero 区域 ===== */
    .hero-section {
        position: relative;
        text-align: center;
        padding: 5rem 2rem 4rem;
        overflow: hidden;
        border-radius: 24px;
        margin: 1.5rem 0 2rem;
        border: 1px solid rgba(0, 212, 255, 0.08);
    }
    .hero-bg {
        position: absolute;
        inset: 0;
        background: url("data:image/jpeg;base64,HERO_B64") center/cover no-repeat;
        opacity: 0.25;
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
        font-size: 3.2rem !important;
        font-weight: 900 !important;
        background: linear-gradient(90deg, #00d4ff, #a855f7, #ec4899, #00d4ff);
        background-size: 300% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: shimmer 6s ease-in-out infinite;
        margin-bottom: 1.2rem !important;
        letter-spacing: 0.04em;
        line-height: 1.15;
    }
    @keyframes shimmer {
        0%, 100% { background-position: 0% center; }
        50% { background-position: 300% center; }
    }
    .hero-sub {
        font-size: 1.1rem !important;
        color: #8b9bb4 !important;
        max-width: 750px;
        margin: 0 auto 2.5rem;
        line-height: 1.8;
    }
    .hero-stats {
        display: flex;
        justify-content: center;
        gap: 3.5rem;
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

    /* ===== 分隔线 ===== */
    .section-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(0,212,255,0.2), rgba(168,85,247,0.2), transparent);
        margin: 3rem 0;
    }

    /* ===== 章节标题 ===== */
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
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        color: #f0f4f8 !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: 0.02em;
    }
    .section-sub {
        color: #6b7fa3 !important;
        font-size: 0.9rem !important;
        max-width: 600px;
        margin: 0 auto;
    }

    /* ===== 系统卡片网格 ===== */
    .card-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
    }
    .sys-card {
        background: linear-gradient(165deg, rgba(15,23,42,0.9), rgba(8,15,30,0.95));
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 18px;
        overflow: hidden;
        transition: all 0.45s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        position: relative;
    }
    .sys-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: var(--card-accent, #00d4ff);
        opacity: 0;
        transition: opacity 0.4s;
        z-index: 2;
    }
    .sys-card::after {
        content: '';
        position: absolute;
        inset: 0;
        border-radius: 18px;
        padding: 1px;
        background: linear-gradient(135deg, transparent, rgba(0,212,255,0.1), transparent);
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 0;
        transition: opacity 0.4s;
        pointer-events: none;
    }
    .sys-card:hover {
        transform: translateY(-10px) scale(1.01);
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.5), 0 0 40px rgba(0, 212, 255, 0.06);
        border-color: rgba(0, 212, 255, 0.15);
    }
    .sys-card:hover::before { opacity: 1; }
    .sys-card:hover::after { opacity: 1; }
    .sys-card .card-img-wrap {
        position: relative;
        overflow: hidden;
        height: 180px;
    }
    .sys-card .card-img-wrap img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    .sys-card:hover .card-img-wrap img { transform: scale(1.1); }
    .sys-card .card-img-overlay {
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 70%;
        background: linear-gradient(transparent, rgba(8,15,30,0.95));
        pointer-events: none;
    }
    .sys-card .card-id {
        position: absolute;
        top: 12px; left: 12px;
        width: 32px; height: 32px;
        border-radius: 8px;
        background: rgba(0,0,0,0.5);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75rem;
        font-weight: 700;
        color: #fff;
    }
    .sys-card .card-tag {
        position: absolute;
        top: 12px; right: 12px;
        padding: 0.3rem 0.8rem;
        border-radius: 8px;
        font-size: 0.68rem;
        font-weight: 600;
        color: #fff;
        background: rgba(0,0,0,0.45);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.08);
    }
    .sys-card .card-body {
        padding: 1.3rem 1.5rem 1.5rem;
    }
    .sys-card .card-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #f0f4f8;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }
    .sys-card .card-title .icon {
        font-size: 1.3rem;
        filter: drop-shadow(0 0 6px rgba(0,212,255,0.3));
    }
    .sys-card .card-desc {
        font-size: 0.8rem;
        color: #6b7fa3;
        line-height: 1.7;
        margin-bottom: 1.2rem;
    }
    .sys-card .card-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.6rem;
        width: 100%;
        padding: 0.75rem 0;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.88rem;
        color: #fff;
        text-decoration: none;
        border: none;
        cursor: pointer;
        transition: all 0.35s;
        letter-spacing: 0.04em;
        position: relative;
        overflow: hidden;
    }
    .sys-card .card-btn::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(255,255,255,0.1), transparent);
        opacity: 0;
        transition: opacity 0.3s;
    }
    .sys-card .card-btn:hover::before { opacity: 1; }
    .sys-card .card-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        filter: brightness(1.1);
    }
    .sys-card .card-btn svg {
        width: 16px; height: 16px;
        transition: transform 0.3s;
    }
    .sys-card .card-btn:hover svg { transform: translateX(4px); }

    /* ===== 图片画廊 ===== */
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
    .gallery-card .gallery-overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(transparent 40%, rgba(3,7,18,0.9));
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        padding: 1.2rem;
    }
    .gallery-card .gallery-overlay h4 {
        font-size: 0.95rem;
        font-weight: 700;
        color: #f0f4f8;
        margin-bottom: 0.2rem;
    }
    .gallery-card .gallery-overlay p {
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
    .adv-card:hover::before { opacity: 1; }
    .adv-card:hover {
        border-color: rgba(0, 212, 255, 0.15);
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.05);
        transform: translateY(-5px);
    }
    .adv-icon-wrap {
        width: 56px; height: 56px;
        margin: 0 auto 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 16px;
        font-size: 1.6rem;
        position: relative;
    }
    .adv-card h4 {
        font-size: 0.95rem;
        font-weight: 700;
        color: #f0f4f8;
        margin-bottom: 0.4rem;
    }
    .adv-card p {
        font-size: 0.76rem;
        color: #6b7fa3;
        line-height: 1.6;
    }

    /* ===== 二维码区域 ===== */
    .qr-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.2rem;
    }
    .qr-card {
        background: linear-gradient(165deg, rgba(15,23,42,0.8), rgba(8,15,30,0.9));
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 1.4rem 1rem;
        text-align: center;
        transition: all 0.4s;
        position: relative;
    }
    .qr-card:hover {
        transform: translateY(-5px);
        border-color: rgba(0, 212, 255, 0.2);
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.05);
    }
    .qr-card .qr-img-wrap {
        width: 120px; height: 120px;
        margin: 0 auto 0.8rem;
        border-radius: 12px;
        background: #fff;
        padding: 8px;
        position: relative;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .qr-card .qr-img-wrap img {
        width: 100%;
        height: 100%;
        border-radius: 6px;
    }
    .qr-card .qr-scan-hint {
        position: absolute;
        top: -8px; right: -8px;
        width: 24px; height: 24px;
        border-radius: 50%;
        background: linear-gradient(135deg, #00d4ff, #a855f7);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.6rem;
        box-shadow: 0 2px 8px rgba(0,212,255,0.4);
    }
    .qr-card .qr-name {
        font-size: 0.82rem;
        font-weight: 700;
        color: #f0f4f8;
        margin-bottom: 0.2rem;
    }
    .qr-card .qr-tag {
        display: inline-block;
        padding: 0.15rem 0.5rem;
        border-radius: 4px;
        font-size: 0.65rem;
        font-weight: 600;
        background: rgba(0,212,255,0.08);
        color: #00d4ff;
        border: 1px solid rgba(0,212,255,0.12);
    }

    /* ===== Footer ===== */
    .footer-section {
        text-align: center;
        padding: 3rem 2rem 1.5rem;
        color: #6b7fa3;
        font-size: 0.82rem;
    }
    .footer-section h3 {
        color: #f0f4f8;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.6rem;
    }
    .footer-section .footer-desc {
        max-width: 650px;
        margin: 0 auto;
        line-height: 1.8;
        color: #6b7fa3;
    }
    .footer-links {
        display: flex;
        justify-content: center;
        gap: 2.5rem;
        margin-top: 1.2rem;
    }
    .footer-links a {
        color: #6b7fa3;
        text-decoration: none;
        font-size: 0.8rem;
        font-weight: 500;
        transition: all 0.3s;
    }
    .footer-links a:hover { color: #00d4ff; }
    .footer-copy {
        margin-top: 2rem;
        padding-top: 1.2rem;
        border-top: 1px solid rgba(255,255,255,0.05);
        color: #4b5e7a;
        font-size: 0.75rem;
        letter-spacing: 0.03em;
    }

    /* ===== 滚动条美化 ===== */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #030712; }
    ::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #334155; }

    /* ===== 响应式 ===== */
    @media (max-width: 1024px) {
        .card-grid { grid-template-columns: repeat(2, 1fr); }
        .qr-grid { grid-template-columns: repeat(3, 1fr); }
        .adv-grid { grid-template-columns: repeat(2, 1fr); }
        .gallery-grid { grid-template-columns: repeat(2, 1fr); }
        .hero-stats { gap: 2rem; }
        .hero-title { font-size: 2.5rem !important; }
    }
    @media (max-width: 640px) {
        .card-grid, .qr-grid, .adv-grid, .gallery-grid { grid-template-columns: 1fr; }
        .hero-title { font-size: 2rem !important; }
        .hero-stats { flex-direction: column; gap: 1rem; align-items: center; }
        .top-bar { flex-direction: column; gap: 1rem; }
        .top-bar .nav-links { gap: 1.2rem; flex-wrap: wrap; justify-content: center; }
        .hero-section { padding: 3rem 1rem 2.5rem; }
    }
</style>
"""

# ============================================================
# 辅助函数
# ============================================================
def get_asset_path(filename: str) -> str:
    return str(Path(__file__).parent / "assets" / filename)


def img_to_base64(image_path: str) -> str:
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except FileNotFoundError:
        return ""


def b64_img_tag(b64: str, cls: str = "") -> str:
    if b64:
        return f'<img class="{cls}" src="data:image/jpeg;base64,{b64}" alt="">'
    return ""


def load_b64(filename: str) -> str:
    return img_to_base64(get_asset_path(filename))


# ============================================================
# 粒子背景 HTML
# ============================================================
def particles_html():
    particles = []
    import random
    for i in range(40):
        left = random.randint(0, 100)
        size = random.randint(1, 3)
        dur = random.randint(8, 20)
        delay = random.randint(0, 15)
        particles.append(
            f'<div class="particle" style="left:{left}%;width:{size}px;height:{size}px;'
            f'animation-duration:{dur}s;animation-delay:{delay}s;"></div>'
        )
    return f'<div class="particles-bg">{"".join(particles)}</div>'


# ============================================================
# 主程序
# ============================================================
def main():
    # 加载 hero 背景图
    hero_b64 = load_b64("hero_bg.jpg")
    css = CUSTOM_CSS.replace("HERO_B64", hero_b64)
    st.markdown(css, unsafe_allow_html=True)

    # 粒子背景
    st.markdown(particles_html(), unsafe_allow_html=True)

    # ====== 顶部导航 ======
    st.markdown("""
    <div class="top-bar">
        <div class="logo">
            <div class="logo-icon">📊</div>
            DATA INTELLIGENCE
        </div>
        <div class="nav-links">
            <a href="#systems">功能模块</a>
            <a href="#gallery">技术架构</a>
            <a href="#advantages">核心优势</a>
            <a href="#qrcodes">移动访问</a>
            <a href="#about">关于</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ====== Hero 区域 ======
    st.markdown("""
    <div class="hero-section">
        <div class="hero-bg"></div>
        <div class="hero-content">
            <div class="hero-badge">
                <div class="dot"></div>
                DATA INTELLIGENCE HUB v3.0
            </div>
            <h1 class="hero-title">企业数据智能分析平台</h1>
            <p class="hero-sub">
                整合企业数字化转型、ESG 环境社会治理评估与多维数据可视化，
                构建一站式数据分析决策中枢，以 AI 驱动企业智能化升级。
            </p>
            <div class="hero-stats">
                <div class="hero-stat">
                    <div class="num">11</div>
                    <div class="label">专业分析系统</div>
                </div>
                <div class="hero-stat">
                    <div class="num">6+</div>
                    <div class="label">数据分析维度</div>
                </div>
                <div class="hero-stat">
                    <div class="num">24/7</div>
                    <div class="label">全天候在线访问</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # ====== 系统功能介绍 ======
    st.markdown("""
    <div class="section-header" id="systems">
        <div class="section-tag">SYSTEM MODULES</div>
        <h2 class="section-title">系统功能介绍</h2>
        <p class="section-sub">涵盖预测分析、数字经济、大数据处理、ESG评估等 11 个专业数据系统</p>
    </div>
    """, unsafe_allow_html=True)

    cards_html = '<div class="card-grid">'
    for sys in SYSTEMS:
        img_b64 = load_b64(sys["img"])
        img_tag = b64_img_tag(img_b64, "card-img") if img_b64 else ""
        cards_html += f"""
        <div class="sys-card" style="--card-accent: {sys['color']};">
            <div class="card-img-wrap">
                {img_tag}
                <div class="card-img-overlay"></div>
                <div class="card-id">{sys['id']:02d}</div>
                <div class="card-tag" style="border-left: 3px solid {sys['tag_color']};">{sys['tag']}</div>
            </div>
            <div class="card-body">
                <div class="card-title">
                    <span class="icon">{sys['icon']}</span>
                    {sys['short_name']}
                </div>
                <div class="card-desc">{sys['desc']}</div>
                <a href="{sys['url']}" target="_blank" rel="noopener"
                   class="card-btn"
                   style="background: {sys['gradient']};">
                    进入系统
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path>
                    </svg>
                </a>
            </div>
        </div>
        """
    cards_html += '</div>'
    st.markdown(cards_html, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # ====== 技术架构画廊 ======
    st.markdown("""
    <div class="section-header" id="gallery">
        <div class="section-tag">TECH ARCHITECTURE</div>
        <h2 class="section-title">技术能力展示</h2>
        <p class="section-sub">基于前沿技术栈构建的企业级数据智能基础设施</p>
    </div>
    """, unsafe_allow_html=True)

    gallery_html = '<div class="gallery-grid">'
    for item in GALLERY:
        img_b64 = load_b64(item["img"])
        img_tag = b64_img_tag(img_b64) if img_b64 else ""
        gallery_html += f"""
        <div class="gallery-card">
            {img_tag}
            <div class="gallery-overlay">
                <h4>{item['title']}</h4>
                <p>{item['desc']}</p>
            </div>
        </div>
        """
    gallery_html += '</div>'
    st.markdown(gallery_html, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # ====== 核心优势 ======
    st.markdown("""
    <div class="section-header" id="advantages">
        <div class="section-tag">CORE ADVANTAGES</div>
        <h2 class="section-title">平台核心优势</h2>
        <p class="section-sub">融合先进技术与专业方法论，为企业提供全方位数据智能解决方案</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="adv-grid">
        <div class="adv-card">
            <div class="adv-icon-wrap" style="background: rgba(0,212,255,0.08); border: 1px solid rgba(0,212,255,0.12);">🗄️</div>
            <h4>多维数据整合</h4>
            <p>支持多个数据源统一接入、清洗与整合，构建企业数据资产全景图</p>
        </div>
        <div class="adv-card">
            <div class="adv-icon-wrap" style="background: rgba(168,85,247,0.08); border: 1px solid rgba(168,85,247,0.12);">⚡</div>
            <h4>智能算法引擎</h4>
            <p>搭载机器学习与深度学习模型，精准预测趋势与异常检测</p>
        </div>
        <div class="adv-card">
            <div class="adv-icon-wrap" style="background: rgba(6,182,212,0.08); border: 1px solid rgba(6,182,212,0.12);">📱</div>
            <h4>全端响应式</h4>
            <p>PC / 平板 / 手机多端无缝适配，随时随地访问分析结果</p>
        </div>
        <div class="adv-card">
            <div class="adv-icon-wrap" style="background: rgba(37,99,235,0.08); border: 1px solid rgba(37,99,235,0.12);">🧩</div>
            <h4>模块化架构</h4>
            <p>灵活组合分析模块，按需定制企业专属数据分析方案</p>
        </div>
        <div class="adv-card">
            <div class="adv-icon-wrap" style="background: rgba(236,72,153,0.08); border: 1px solid rgba(236,72,153,0.12);">🔒</div>
            <h4>数据安全防护</h4>
            <p>企业级数据加密与权限管理，确保敏感信息安全可控</p>
        </div>
        <div class="adv-card">
            <div class="adv-icon-wrap" style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.12);">🌱</div>
            <h4>ESG 合规评估</h4>
            <p>内置 ESG 评估框架，助力企业可持续发展与合规运营</p>
        </div>
        <div class="adv-card">
            <div class="adv-icon-wrap" style="background: rgba(245,158,11,0.08); border: 1px solid rgba(245,158,11,0.12);">🔄</div>
            <h4>实时数据更新</h4>
            <p>支持实时数据流接入，确保分析结果始终反映最新业务状态</p>
        </div>
        <div class="adv-card">
            <div class="adv-icon-wrap" style="background: rgba(139,92,246,0.08); border: 1px solid rgba(139,92,246,0.12);">🎯</div>
            <h4>精准决策辅助</h4>
            <p>智能推荐与预警机制，帮助管理层快速做出数据驱动的决策</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # ====== 二维码区域 ======
    st.markdown("""
    <div class="section-header" id="qrcodes">
        <div class="section-tag">MOBILE ACCESS</div>
        <h2 class="section-title">移动端快速访问</h2>
        <p class="section-sub">使用手机扫描下方二维码，即可在移动端访问对应数据系统</p>
    </div>
    """, unsafe_allow_html=True)

    qr_html = '<div class="qr-grid">'
    for sys in SYSTEMS:
        qr_b64 = load_b64(f"qr_{sys['id']}.png")
        qr_img = (
            f'<img src="data:image/png;base64,{qr_b64}" alt="{sys["short_name"]}">'
            if qr_b64 else ""
        )
        qr_html += f"""
        <div class="qr-card">
            <div class="qr-img-wrap">
                {qr_img}
                <div class="qr-scan-hint">📱</div>
            </div>
            <div class="qr-name">{sys['icon']} {sys['short_name']}</div>
            <div class="qr-tag">{sys['tag']}</div>
        </div>
        """
    qr_html += '</div>'
    st.markdown(qr_html, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # ====== Footer ======
    st.markdown("""
    <div class="footer-section" id="about">
        <h3>关于我们</h3>
        <p class="footer-desc">
            我们致力于为企业提供专业的数据智能分析工具，整合预测分析、数字经济研究、
            大数据处理、ESG评估与BI可视化等多个平台，通过先进的算法与模型技术，
            帮助企业实现数据驱动决策，优化运营流程，加速数字化转型。
        </p>
        <div class="footer-links">
            <a href="#systems">功能模块</a>
            <a href="#gallery">技术架构</a>
            <a href="#advantages">核心优势</a>
            <a href="#qrcodes">移动访问</a>
        </div>
        <div class="footer-copy">
            &#169; 2026 企业数据智能分析平台 &nbsp;&bull;&nbsp; Powered by Streamlit &nbsp;&bull;&nbsp; All Rights Reserved
        </div>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
