import streamlit as st
import qrcode
from io import BytesIO

# ---------- 页面配置 ----------
st.set_page_config(
    page_title="数字枢纽 · 企业导航",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- 自定义CSS（高科技企业风格） ----------
st.markdown("""
<style>
    /* 全局背景 + 字体 */
    .stApp {
        background: #0a0e1a;
        background-image: radial-gradient(ellipse at 20% 50%, rgba(10, 80, 200, 0.08) 0%, transparent 60%),
                          radial-gradient(ellipse at 80% 50%, rgba(0, 200, 255, 0.06) 0%, transparent 60%);
        color: #d0dfff;
        font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
    }
    /* 顶栏隐藏 */
    header { display: none; }
    /* 主容器 */
    .main-content {
        max-width: 1400px;
        margin: 0 auto;
        padding: 1rem 2rem 3rem;
    }
    /* 标题区域 */
    .hero-title {
        font-size: 4.2rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        background: linear-gradient(135deg, #a0d0ff 0%, #4facfe 40%, #00d4ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 60px rgba(79, 172, 254, 0.25);
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .hero-sub {
        text-align: center;
        font-size: 1.2rem;
        color: #7a8bb0;
        letter-spacing: 8px;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(79, 172, 254, 0.15);
        padding-bottom: 1.5rem;
        margin-bottom: 2rem;
    }
    /* 卡片容器 */
    .card {
        background: rgba(18, 30, 51, 0.55);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 28px;
        padding: 24px 18px 18px;
        border: 1px solid rgba(79, 172, 254, 0.20);
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255,255,255,0.04);
        transition: all 0.25s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 100%;
        min-height: 280px;
        position: relative;
        overflow: hidden;
    }
    .card::before {
        content: '';
        position: absolute;
        top: -2px; left: -2px; right: -2px; bottom: -2px;
        border-radius: 30px;
        background: linear-gradient(135deg, rgba(79,172,254,0.2), rgba(0,212,255,0.05), rgba(79,172,254,0.2));
        z-index: -1;
        opacity: 0;
        transition: opacity 0.4s;
    }
    .card:hover::before {
        opacity: 1;
    }
    .card:hover {
        transform: translateY(-8px);
        border-color: #4facfe;
        box-shadow: 0 20px 60px rgba(79, 172, 254, 0.20), inset 0 1px 0 rgba(255,255,255,0.08);
    }
    /* 卡片标题 —— 显示完整名称（域名/路径） */
    .card-title {
        font-size: 0.95rem;
        font-weight: 500;
        color: #b8ceff;
        text-align: center;
        word-break: break-all;
        line-height: 1.4;
        margin-bottom: 16px;
        padding: 0 4px;
        flex: 0 0 auto;
        width: 100%;
        border-bottom: 1px dashed rgba(79, 172, 254, 0.15);
        padding-bottom: 12px;
    }
    /* 二维码容器 */
    .qr-wrapper {
        background: white;
        border-radius: 16px;
        padding: 6px;
        box-shadow: 0 0 30px rgba(79, 172, 254, 0.15);
        margin: 6px 0 12px;
        line-height: 0;
        transition: all 0.2s;
    }
    .qr-wrapper:hover {
        box-shadow: 0 0 40px rgba(79, 172, 254, 0.35);
    }
    /* 按钮覆盖 Streamlit 默认 */
    .stLinkButton button {
        width: 100%;
        background: linear-gradient(135deg, #4facfe 0%, #00d4ff 100%);
        color: #0a0e1a;
        font-weight: 700;
        font-size: 1rem;
        border: none;
        border-radius: 60px;
        padding: 0.6rem 0;
        transition: all 0.2s;
        box-shadow: 0 4px 20px rgba(79, 172, 254, 0.30);
        letter-spacing: 0.5px;
        margin-top: 4px;
    }
    .stLinkButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 32px rgba(79, 172, 254, 0.55);
        background: linear-gradient(135deg, #5fb8ff, #1ad6ff);
    }
    /* 脚注 */
    .footer {
        text-align: center;
        color: #3f5a7a;
        font-size: 0.85rem;
        margin-top: 3.5rem;
        padding-top: 1.8rem;
        border-top: 1px solid #1e2b44;
        letter-spacing: 2px;
    }
    /* 响应式 */
    @media (max-width: 720px) {
        .hero-title { font-size: 2.8rem; }
        .card { min-height: 240px; }
    }
</style>
""", unsafe_allow_html=True)

# ---------- 标题 Banner （使用纯色科技感装饰，不依赖外部图片） ----------
st.markdown("""
<div style="background: linear-gradient(135deg, #0f1a2e, #162033); border-radius: 32px; padding: 0.4rem 0; margin-bottom: 1.8rem; border: 1px solid rgba(79,172,254,0.10);">
    <div style="display: flex; justify-content: center; align-items: center; gap: 12px; flex-wrap: wrap; padding: 0.8rem 1.5rem;">
        <span style="font-size: 2.2rem; opacity: 0.7;">⟡</span>
        <span style="font-size: 1.1rem; color: #7a9bcb; letter-spacing: 6px; font-weight: 300;">ENTERPRISE · DIGITAL HUB</span>
        <span style="font-size: 2.2rem; opacity: 0.7;">⟡</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="hero-title">⚡ 数字枢纽 · 聚合入口</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">AI · 大数据 · ESG · 商业智能</div>', unsafe_allow_html=True)

# ---------- 链接数据（标题 = 完整域名/路径，保证准确） ----------
# 您可以将每个元组的第一个元素替换为任意正式名称，第二个元素为 URL
links = [
    ("newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app", 
     "https://newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app/"),
    ("digital-encomy.streamlit.app", 
     "https://digital-encomy.streamlit.app/"),
    ("digital-encomy-main.streamlit.app", 
     "https://digital-encomy-main.streamlit.app/"),
    ("xuejiededashujuzuoye.streamlit.app", 
     "https://xuejiededashujuzuoye.streamlit.app/"),
    ("big-data-hmjdjensqzboumvsvydca3.streamlit.app", 
     "https://big-data-hmjdjensqzboumvsvydca3.streamlit.app/"),
    ("esgdigital.streamlit.app", 
     "https://esgdigital.streamlit.app/"),
    ("app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app", 
     "https://app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app/"),
    ("20072023digital.streamlit.app", 
     "https://20072023digital.streamlit.app/"),
    ("19992023digital.streamlit.app", 
     "https://19992023digital.streamlit.app/"),
    ("1999-2023companydeindex-tgax4uws6a7.streamlit.app", 
     "https://1999-2023companydeindex-tgax4uws6a7.streamlit.app/"),
    ("47.98.202.43 (SmartBI)", 
     "http://47.98.202.43/smartbi/vision/share.jsp?resid=100ef521ecf6c5860d5917a961a6e0b0"),
]

# ---------- 二维码生成函数 ----------
def generate_qr(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0b0f1a", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

# ---------- 卡片网格 ----------
cols_per_row = 3
for i in range(0, len(links), cols_per_row):
    row = links[i:i+cols_per_row]
    cols = st.columns(cols_per_row, gap="medium")
    for col, (name, url) in zip(cols, row):
        with col:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">{name}</div>
            """, unsafe_allow_html=True)
            
            # 二维码
            qr_bytes = generate_qr(url)
            st.image(qr_bytes, width=130, use_column_width="never", output_format="PNG")
            
            # 访问按钮（使用 link_button 确保跳转）
            st.link_button("🚀 打开平台", url, use_container_width=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

# ---------- 页脚 ----------
st.markdown("""
<div class="footer">
    <span>✦ 数据驱动未来 · 聚合所有核心应用 ✦</span><br>
    <span style="font-size:0.75rem; opacity:0.6;">版本 2.0 · 自动更新于 2026</span>
</div>
""", unsafe_allow_html=True)