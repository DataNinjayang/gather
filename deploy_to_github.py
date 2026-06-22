import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image
import base64

st.set_page_config(page_title="数字枢纽", page_icon="🌐", layout="wide")

st.markdown("""
<style>
.stApp {
    background: radial-gradient(ellipse at center, #0b0f1a 0%, #020408 100%);
    color: #e0e8ff;
}
h1, h2, h3 {
    font-family: 'Segoe UI', sans-serif;
    font-weight: 700;
    letter-spacing: 1px;
}
.main-title {
    text-align: center;
    font-size: 3.8rem;
    background: linear-gradient(135deg, #00f2fe, #4facfe);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 30px rgba(79, 172, 254, 0.3);
    margin-bottom: 0.2rem;
}
.sub-title {
    text-align: center;
    color: #8899bb;
    font-size: 1.1rem;
    letter-spacing: 6px;
    margin-top: -0.5rem;
    margin-bottom: 2rem;
}
.card {
    background: rgba(255, 255, 255, 0.04);
    backdrop-filter: blur(6px);
    border-radius: 24px;
    padding: 20px 16px 16px;
    border: 1px solid rgba(79, 172, 254, 0.15);
    box-shadow: 0 8px 32px rgba(0,0,0,0.5);
    transition: all 0.3s ease;
    text-align: center;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
}
.card:hover {
    transform: translateY(-6px);
    border-color: #4facfe;
    box-shadow: 0 12px 48px rgba(79, 172, 254, 0.25);
}
.card-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #b8ccff;
    margin-bottom: 12px;
    word-break: break-word;
}
.stLinkButton button {
    width: 100%;
    background: linear-gradient(135deg, #4facfe, #00f2fe);
    color: #0b0f1a;
    font-weight: 700;
    border: none;
    border-radius: 40px;
    padding: 0.5rem 0;
    transition: all 0.2s;
    box-shadow: 0 4px 16px rgba(79, 172, 254, 0.3);
}
.stLinkButton button:hover {
    transform: scale(1.02);
    box-shadow: 0 6px 24px rgba(79, 172, 254, 0.6);
}
.qr-img {
    margin-top: 10px;
    border-radius: 12px;
    background: white;
    padding: 4px;
}
.footer {
    text-align: center;
    color: #445577;
    font-size: 0.85rem;
    margin-top: 3rem;
    border-top: 1px solid #1a253a;
    padding-top: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

banner_url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&h=300&fit=crop"
st.image(banner_url, use_column_width=True)

st.markdown('<div class="main-title">✦ 数字枢纽 ✦</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">DATA · AI · ESG · 未来</div>', unsafe_allow_html=True)

links = [
    ("🔮 预测平台", "https://newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app/"),
    ("📊 数字经济 I", "https://digital-encomy.streamlit.app/"),
    ("📈 数字经济 II", "https://digital-encomy-main.streamlit.app/"),
    ("📚 大数据作业", "https://xuejiededashujuzuoye.streamlit.app/"),
    ("🧠 大数据分析", "https://big-data-hmjdjensqzboumvsvydca3.streamlit.app/"),
    ("🌿 ESG 数字", "https://esgdigital.streamlit.app/"),
    ("📱 App 1", "https://app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app/"),
    ("📆 2007-2023", "https://20072023digital.streamlit.app/"),
    ("📆 1999-2023", "https://19992023digital.streamlit.app/"),
    ("🏢 公司指数", "https://1999-2023companydeindex-tgax4uws6a7.streamlit.app/"),
    ("📊 SmartBI", "http://47.98.202.43/smartbi/vision/share.jsp?resid=100ef521ecf6c5860d5917a961a6e0b0"),
]

def generate_qr(url):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=4, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0b0f1a", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

cols_per_row = 3
for i in range(0, len(links), cols_per_row):
    row = links[i:i+cols_per_row]
    cols = st.columns(cols_per_row)
    for col, (name, url) in zip(cols, row):
        with col:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">{name}</div>
            """, unsafe_allow_html=True)
            st.link_button(f"🚀 访问", url, use_container_width=True)
            qr_bytes = generate_qr(url)
            st.image(qr_bytes, width=120, caption="扫码直达", output_format="PNG")
            st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="footer">⚡ 数字枢纽 · 聚合所有关键平台 &nbsp;|&nbsp; 2026</div>', unsafe_allow_html=True)
