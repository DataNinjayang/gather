import streamlit as st
import qrcode
from io import BytesIO
import base64

# ---------- 页面配置 ----------
st.set_page_config(
    page_title="数字书籍 · 科技导航",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- 自定义CSS（书籍风格 + 科技感） ----------
st.markdown("""
<style>
    /* 全局字体和背景 */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    .stApp {
        background: #0a0e1a;
        background-image: 
            radial-gradient(ellipse at 10% 30%, rgba(120, 80, 255, 0.08) 0%, transparent 50%),
            radial-gradient(ellipse at 90% 70%, rgba(0, 200, 255, 0.06) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 50%, rgba(255, 100, 200, 0.03) 0%, transparent 70%);
        color: #d8e6ff;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    header { display: none; }
    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 1.5rem 3rem;
    }

    /* ===== 书籍封面 ===== */
    .book-cover {
        background: linear-gradient(135deg, #1a1f35, #0f1a2e);
        border-radius: 48px 48px 24px 24px;
        padding: 2.2rem 2rem 1.8rem;
        margin-bottom: 2.5rem;
        border: 1px solid rgba(120, 180, 255, 0.15);
        box-shadow: 0 20px 60px rgba(0,0,0,0.7), inset 0 1px 0 rgba(255,255,255,0.05);
        position: relative;
        overflow: hidden;
        text-align: center;
    }
    .book-cover::before {
        content: '';
        position: absolute;
        top: -30%; left: -10%;
        width: 60%; height: 140%;
        background: radial-gradient(ellipse, rgba(79, 172, 254, 0.10) 0%, transparent 70%);
        transform: rotate(-10deg);
        pointer-events: none;
    }
    .book-cover::after {
        content: '';
        position: absolute;
        bottom: -40%; right: -10%;
        width: 50%; height: 130%;
        background: radial-gradient(ellipse, rgba(180, 80, 255, 0.08) 0%, transparent 70%);
        transform: rotate(15deg);
        pointer-events: none;
    }
    .book-icon {
        font-size: 4.2rem;
        display: block;
        margin-bottom: 0.2rem;
        filter: drop-shadow(0 0 20px rgba(79, 172, 254, 0.3));
    }
    .book-title {
        font-size: 3.8rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        background: linear-gradient(135deg, #b8d4ff, #4facfe, #a78bfa, #00d4ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 60px rgba(79, 172, 254, 0.15);
        position: relative;
        z-index: 1;
    }
    .book-sub {
        font-size: 1.1rem;
        color: #8aa3c9;
        letter-spacing: 12px;
        text-transform: uppercase;
        border-top: 1px solid rgba(79, 172, 254, 0.15);
        padding-top: 1rem;
        margin-top: 0.5rem;
        display: inline-block;
    }
    .book-decoration {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-top: 0.8rem;
        opacity: 0.4;
        font-size: 1.8rem;
        letter-spacing: 20px;
    }

    /* ===== 分类章节标题 ===== */
    .chapter-header {
        display: flex;
        align-items: center;
        gap: 14px;
        margin: 2.8rem 0 1.5rem 0;
        border-bottom: 2px solid rgba(79, 172, 254, 0.10);
        padding-bottom: 0.6rem;
    }
    .chapter-number {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #4facfe, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        opacity: 0.6;
    }
    .chapter-name {
        font-size: 1.8rem;
        font-weight: 600;
        color: #c2d6ff;
        letter-spacing: 2px;
    }
    .chapter-line {
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, rgba(79,172,254,0.3), transparent);
    }

    /* ===== 书页卡片 ===== */
    .book-page {
        background: rgba(16, 28, 48, 0.65);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-radius: 20px 8px 20px 8px;
        padding: 20px 16px 16px;
        border-left: 4px solid;
        box-shadow: 0 8px 30px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.04);
        transition: all 0.25s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 100%;
        min-height: 270px;
        position: relative;
    }
    .book-page:hover {
        transform: translateY(-6px) scale(1.01);
        box-shadow: 0 16px 48px rgba(0,0,0,0.7), 0 0 0 1px rgba(79,172,254,0.2);
    }
    /* 不同分类的左边框颜色（在Python中动态设置） */
    .page-title {
        font-size: 0.95rem;
        font-weight: 500;
        color: #d0e2ff;
        text-align: center;
        word-break: break-all;
        line-height: 1.4;
        margin-bottom: 12px;
        padding: 0 2px;
        border-bottom: 1px dashed rgba(255,255,255,0.06);
        padding-bottom: 10px;
        width: 100%;
    }
    .qr-wrapper {
        background: white;
        border-radius: 14px;
        padding: 5px;
        box-shadow: 0 0 25px rgba(79, 172, 254, 0.12);
        margin: 4px 0 12px;
        line-height: 0;
        transition: 0.2s;
    }
    .qr-wrapper:hover {
        box-shadow: 0 0 35px rgba(79, 172, 254, 0.3);
    }
    .stLinkButton button {
        width: 100%;
        background: linear-gradient(135deg, #4facfe, #00d4ff);
        color: #0a0e1a;
        font-weight: 700;
        border: none;
        border-radius: 60px;
        padding: 0.55rem 0;
        transition: 0.2s;
        box-shadow: 0 4px 20px rgba(79, 172, 254, 0.25);
        font-size: 0.95rem;
        letter-spacing: 0.5px;
        margin-top: 4px;
    }
    .stLinkButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 35px rgba(79, 172, 254, 0.5);
        background: linear-gradient(135deg, #5fb8ff, #1ad6ff);
    }

    /* ===== 脚注 ===== */
    .footer {
        text-align: center;
        color: #3f5a7a;
        font-size: 0.85rem;
        margin-top: 4rem;
        padding-top: 2rem;
        border-top: 1px solid #1a2640;
        letter-spacing: 1px;
    }

    /* ===== 装饰图片（页面顶部和底部） ===== */
    .deco-image {
        border-radius: 30px;
        margin: 1.2rem 0;
        opacity: 0.5;
        filter: grayscale(0.4) brightness(0.7);
        transition: 0.3s;
    }
    .deco-image:hover {
        opacity: 0.8;
        filter: grayscale(0) brightness(0.9);
    }

    /* 响应式 */
    @media (max-width: 720px) {
        .book-title { font-size: 2.6rem; }
        .chapter-name { font-size: 1.4rem; }
        .book-page { min-height: 220px; }
    }
</style>
""", unsafe_allow_html=True)

# ---------- 辅助函数：生成二维码 ----------
def generate_qr(url):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=4, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0a0e1a", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

# ---------- 装饰图片（Unsplash 科技风） ----------
# 这些图片将作为分隔装饰，增强色彩
deco_url_1 = "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&h=200&fit=crop"
deco_url_2 = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&h=200&fit=crop"

# ---------- 书籍封面 ----------
st.markdown("""
<div class="book-cover">
    <span class="book-icon">📘</span>
    <div class="book-title">数字书籍 · 聚合导航</div>
    <div class="book-sub">✦ 预测 · 经济 · 大数据 · ESG · 索引 ✦</div>
    <div class="book-decoration">◈ ◆ ◈ ◆ ◈</div>
</div>
""", unsafe_allow_html=True)

# ---------- 装饰图片 1 ----------
st.image(deco_url_1, use_column_width=True, caption="数据流 · 科技脉络")

# ---------- 分类数据 ----------
# 每个分类：名称，颜色（边框），链接列表（元组：显示名称，URL）
# 显示名称使用域名/路径，但可以添加简短描述（这里保持原样）
categories = [
    {
        "name": "🔮 预测与人工智能",
        "color": "#4facfe",
        "links": [
            ("newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app", 
             "https://newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app/"),
        ]
    },
    {
        "name": "📊 数字经济",
        "color": "#00d4ff",
        "links": [
            ("digital-encomy.streamlit.app", 
             "https://digital-encomy.streamlit.app/"),
            ("digital-encomy-main.streamlit.app", 
             "https://digital-encomy-main.streamlit.app/"),
        ]
    },
    {
        "name": "🧠 大数据与分析",
        "color": "#a78bfa",
        "links": [
            ("xuejiededashujuzuoye.streamlit.app", 
             "https://xuejiededashujuzuoye.streamlit.app/"),
            ("big-data-hmjdjensqzboumvsvydca3.streamlit.app", 
             "https://big-data-hmjdjensqzboumvsvydca3.streamlit.app/"),
        ]
    },
    {
        "name": "🌿 ESG 可持续",
        "color": "#34d399",
        "links": [
            ("esgdigital.streamlit.app", 
             "https://esgdigital.streamlit.app/"),
        ]
    },
    {
        "name": "📱 应用与平台",
        "color": "#f472b6",
        "links": [
            ("app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app", 
             "https://app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app/"),
        ]
    },
    {
        "name": "📆 时间序列索引",
        "color": "#fbbf24",
        "links": [
            ("20072023digital.streamlit.app", 
             "https://20072023digital.streamlit.app/"),
            ("19992023digital.streamlit.app", 
             "https://19992023digital.streamlit.app/"),
            ("1999-2023companydeindex-tgax4uws6a7.streamlit.app", 
             "https://1999-2023companydeindex-tgax4uws6a7.streamlit.app/"),
        ]
    },
    {
        "name": "📈 商业智能 (BI)",
        "color": "#fb923c",
        "links": [
            ("47.98.202.43 (SmartBI)", 
             "http://47.98.202.43/smartbi/vision/share.jsp?resid=100ef521ecf6c5860d5917a961a6e0b0"),
        ]
    },
]

# ---------- 渲染分类及卡片 ----------
for idx, cat in enumerate(categories, start=1):
    # 章节标题
    st.markdown(f"""
    <div class="chapter-header">
        <span class="chapter-number">0{idx}</span>
        <span class="chapter-name">{cat['name']}</span>
        <span class="chapter-line"></span>
    </div>
    """, unsafe_allow_html=True)
    
    links = cat["links"]
    cols_per_row = 3
    # 按行显示卡片
    for i in range(0, len(links), cols_per_row):
        row = links[i:i+cols_per_row]
        cols = st.columns(cols_per_row, gap="medium")
        for col, (display_name, url) in zip(cols, row):
            with col:
                # 卡片带左边框颜色
                border_color = cat["color"]
                st.markdown(f"""
                <div class="book-page" style="border-left-color: {border_color};">
                    <div class="page-title">{display_name}</div>
                """, unsafe_allow_html=True)
                
                # 二维码
                qr_bytes = generate_qr(url)
                st.image(qr_bytes, width=130, use_column_width="never", output_format="PNG")
                
                # 按钮
                st.link_button("🚀 打开", url, use_container_width=True)
                
                st.markdown("</div>", unsafe_allow_html=True)

    # 分类之间的装饰分隔（小图片）
    if idx < len(categories):
        st.image(deco_url_2, use_column_width=True, caption="— 章节分隔 —")

# ---------- 页脚 ----------
st.markdown("""
<div class="footer">
    <span>✦ 数据驱动 · 智能互联 · 未来已来 ✦</span><br>
    <span style="font-size:0.75rem; opacity:0.5;">版本 3.0 · 数字书籍设计 · 2026</span>
</div>
""", unsafe_allow_html=True)