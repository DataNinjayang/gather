import streamlit as st
import qrcode
from PIL import Image
import io
import base64

# -------------------------- 全局页面配置 科技深色主题 --------------------------
st.set_page_config(
    page_title="全域链接导航中台 | 科技门户",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义CSS 科技风深色渐变、发光按钮、卡片悬浮动画
custom_css = """
<style>
* {
    font-family: "Microsoft YaHei", sans-serif;
}
.main {
    background: linear-gradient(145deg, #050a1f, #0f1c40, #04102b);
}
.block-container {
    padding: 2rem 4rem !important;
}
h1, h2, h3 {
    color: #00e5ff;
    text-shadow: 0 0 12px #00ccff80;
}
.link-card {
    background: linear-gradient(135deg, #0a1a3d, #102859);
    border: 1px solid #00a8ff60;
    border-radius: 16px;
    padding: 24px;
    margin: 12px 0;
    box-shadow: 0 0 20px #0088ff30;
    transition: all 0.3s ease;
}
.link-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 32px #00ccff60;
    border-color: #00e5ff;
}
.qrcode-box {
    background: #ffffff;
    border-radius: 12px;
    padding: 10px;
    text-align: center;
}
.stButton>button {
    background: linear-gradient(90deg, #0077ff, #00ccff);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    padding: 10px 22px;
    box-shadow: 0 0 10px #0099ff70;
}
.stButton>button:hover {
    box-shadow: 0 0 20px #00e5ff;
    transform: scale(1.03);
}
.divider-line {
    height: 2px;
    background: linear-gradient(90deg, transparent, #00ccff, transparent);
    margin: 30px 0;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# -------------------------- 链接数据源（标题精准对应域名） --------------------------
link_list = [
    {
        "title": "预测分析平台 newprediction",
        "url": "https://newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app/",
        "desc": "预测类数据模型可视化系统"
    },
    {
        "title": "数字商业平台 digital-encomy",
        "url": "https://digital-encomy.streamlit.app/",
        "desc": "数字化商业数据分析看板"
    },
    {
        "title": "数字商业主站 digital-encomy-main",
        "url": "https://digital-encomy-main.streamlit.app/",
        "desc": "数字商业项目主入口站点"
    },
    {
        "title": "学生大数据作业平台 xuejiededashujuzuoye",
        "url": "https://xuejiededashujuzuoye.streamlit.app/",
        "desc": "学生大数据实训作业系统"
    },
    {
        "title": "海量大数据平台 big-data-hmjdjensqzboumvsvydca",
        "url": "https://big-data-hmjdjensqzboumvsvydca3.streamlit.app/",
        "desc": "海量离线大数据计算可视化平台"
    },
    {
        "title": "ESG数字化看板 esgdigital",
        "url": "https://esgdigital.streamlit.app/",
        "desc": "企业ESG环境社会治理数字化系统"
    },
    {
        "title": "一号业务应用 app-app1-sp9zaesfztlkn5htxxpdqi",
        "url": "https://app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app/",
        "desc": "一号业务专属应用门户"
    },
    {
        "title": "2007-2023数字业务站 20072023digital",
        "url": "https://20072023digital.streamlit.app/",
        "desc": "2007-2023年度历史数字业务数据平台"
    },
    {
        "title": "1999-2023智慧介护平台 19992023digital",
        "url": "https://19992023digital.streamlit.app/",
        "desc": "日式智慧介护/福祉设施电商管理系统（配套介护海报素材）"
    },
    {
        "title": "企业索引后台 1999-2023companydeindex",
        "url": "https://1999-2023companydeindex-tgax4uws6a7.streamlit.app/",
        "desc": "企业档案索引管理后台系统"
    },
    {
        "title": "SmartBI可视化报表中台",
        "url": "http://47.98.202.43/smartbi/vision/share.jsp?resid=100ef521ecf6c5860d5917a961a6e0b0",
        "desc": "企业级SmartBI数据可视化共享看板"
    }
]

# -------------------------- 二维码生成工具函数 --------------------------
def generate_qrcode_img(target_url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=2
    )
    qr.add_data(target_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#001133", back_color="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf

# -------------------------- 页面头部 --------------------------
st.markdown("""
# 🌐 全域业务链接导航中台
### 科技一体化入口 | Streamlit & SmartBI 统一门户
<div class="divider-line"></div>
""", unsafe_allow_html=True)

# 两栏循环渲染所有链接卡片
col_count = 2
cols = st.columns(col_count, gap="large")
for idx, item in enumerate(link_list):
    current_col = cols[idx % col_count]
    with current_col:
        # 生成二维码图片流
        qr_buffer = generate_qrcode_img(item["url"])
        qr_img = Image.open(qr_buffer)

        st.markdown(f'<div class="link-card">', unsafe_allow_html=True)
        st.subheader(f"🔹 {item['title']}")
        st.caption(f"说明：{item['desc']}")
        st.code(item["url"], language="text")
        
        # 分栏：二维码 + 跳转按钮
        sub_col1, sub_col2 = st.columns([1, 1.2])
        with sub_col1:
            st.markdown('<div class="qrcode-box">', unsafe_allow_html=True)
            st.image(qr_img, caption="扫码直达", width=140)
            st.markdown('</div>', unsafe_allow_html=True)
        with sub_col2:
            st.link_button("🚀 立即访问站点", url=item["url"], use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# 页脚
st.markdown("""
<div class="divider-line"></div>
<p style="text-align:center; color:#88ccff; font-size:14px;">
导航中台 · 科技可视化门户系统 | 自动生成二维码 · 一键跳转 · 深色科技主题
</p>
""", unsafe_allow_html=True)