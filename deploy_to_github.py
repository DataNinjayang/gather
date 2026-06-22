import streamlit as st
import qrcode
from PIL import Image
import io

# ===================== 全局页面配置 =====================
st.set_page_config(
    page_title="数字化转型全域导航中台",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===================== 自定义科技风CSS =====================
tech_css = """
<style>
/* 全局背景 深蓝科技渐变 */
.main {
    background: linear-gradient(135deg, #020617 0%, #0c1942 50%, #050d2b 100%);
    background-attachment: fixed;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1600px;
}

/* 标题发光效果 */
h1, h2, h3 {
    color: #00e5ff;
    font-weight: 700;
    text-shadow: 0 0 10px rgba(0, 229, 255, 0.6),
                 0 0 20px rgba(0, 170, 255, 0.4);
}

/* 顶部Banner装饰线 */
.tech-divider {
    height: 2px;
    background: linear-gradient(90deg, 
        transparent 0%, 
        #00e5ff 20%, 
        #0088ff 50%, 
        #00e5ff 80%, 
        transparent 100%);
    margin: 1.5rem 0;
    box-shadow: 0 0 10px rgba(0, 229, 255, 0.6);
}

/* 卡片容器 玻璃态+发光边框 */
.tech-card {
    background: linear-gradient(145deg, rgba(15, 35, 80, 0.85), rgba(8, 20, 50, 0.9));
    border: 1px solid rgba(0, 180, 255, 0.4);
    border-radius: 16px;
    padding: 0;
    margin-bottom: 1.5rem;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0, 100, 200, 0.2);
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}
.tech-card:hover {
    transform: translateY(-8px);
    border-color: #00e5ff;
    box-shadow: 0 10px 40px rgba(0, 200, 255, 0.35),
                0 0 25px rgba(0, 229, 255, 0.25);
}

/* 卡片头图 */
.card-img {
    width: 100%;
    height: 160px;
    object-fit: cover;
    border-bottom: 1px solid rgba(0, 180, 255, 0.3);
}

/* 卡片内容区 */
.card-body {
    padding: 18px 20px;
}
.card-title {
    color: #e6f7ff;
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 6px;
}
.card-desc {
    color: #94c7ff;
    font-size: 13px;
    margin-bottom: 12px;
    line-height: 1.5;
}
.card-url {
    background: rgba(0, 20, 50, 0.6);
    padding: 8px 10px;
    border-radius: 6px;
    font-family: monospace;
    font-size: 11px;
    color: #5fd0ff;
    word-break: break-all;
    margin-bottom: 14px;
}

/* 二维码+按钮底部区 */
.card-footer {
    display: flex;
    align-items: center;
    gap: 16px;
}
.qr-wrap {
    background: #ffffff;
    padding: 6px;
    border-radius: 8px;
    flex-shrink: 0;
}

/* 按钮样式重写 */
.stLinkButton > a {
    width: 100% !important;
    background: linear-gradient(90deg, #0077ff, #00ccff) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    text-align: center !important;
    box-shadow: 0 0 12px rgba(0, 150, 255, 0.5) !important;
    transition: all 0.2s !important;
}
.stLinkButton > a:hover {
    box-shadow: 0 0 20px rgba(0, 229, 255, 0.8) !important;
    transform: scale(1.03) !important;
}

/* 页脚 */
.footer-text {
    text-align: center;
    color: #6aa8dd;
    font-size: 13px;
    margin-top: 2rem;
}
</style>
"""
st.markdown(tech_css, unsafe_allow_html=True)

# ===================== 二维码生成函数 =====================
def make_qr_image(url):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=6,
        border=2
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0a2463", back_color="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return Image.open(buf)

# ===================== 链接数据（11个精准对应） =====================
nav_items = [
    {
        "title": "智能预测分析平台",
        "url": "https://newprediction-mg4o5rgtrygzhu2vrsznth.streamlit.app/",
        "desc": "基于时序算法的智能预测模型可视化系统",
        "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80"
    },
    {
        "title": "数字经济可视化平台",
        "url": "https://digital-encomy.streamlit.app/",
        "desc": "数字经济产业数据多维分析看板",
        "img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&q=80"
    },
    {
        "title": "数字经济主站系统",
        "url": "https://digital-encomy-main.streamlit.app/",
        "desc": "数字经济项目核心主入口站点",
        "img": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&q=80"
    },
    {
        "title": "大数据作业实训平台",
        "url": "https://xuejiededashujuzuoye.streamlit.app/",
        "desc": "学生大数据课程作业实训演示系统",
        "img": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&q=80"
    },
    {
        "title": "海量大数据处理平台",
        "url": "https://big-data-hmjdjensqzboumvsvydca3.streamlit.app/",
        "desc": "超大规模数据集离线计算与可视化平台",
        "img": "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=800&q=80"
    },
    {
        "title": "ESG数字化评价系统",
        "url": "https://esgdigital.streamlit.app/",
        "desc": "企业环境社会治理数字化评分体系",
        "img": "https://images.unsplash.com/photo-1532619675605-1ede6c2ed2b0?w=800&q=80"
    },
    {
        "title": "业务应用一号系统",
        "url": "https://app-app1-sp9zaesfztlkn5htxxpdqi.streamlit.app/",
        "desc": "核心业务线专属应用门户系统",
        "img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&q=80"
    },
    {
        "title": "2007-2023数字化时序分析平台",
        "url": "https://20072023digital.streamlit.app/",
        "desc": "2007-2023年度数字化发展时序数据看板",
        "img": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800&q=80"
    },
    {
        "title": "1999-2023数字化发展看板",
        "url": "https://19992023digital.streamlit.app/",
        "desc": "1999-2023全周期数字化进程可视化",
        "img": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&q=80"
    },
    {
        "title": "企业数字化指数查询系统",
        "url": "https://1999-2023companydeindex-tgax4uws6a7.streamlit.app/",
        "desc": "上市公司数字化转型指数检索后台",
        "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80"
    },
    {
        "title": "数字化转型可视化大屏",
        "url": "http://47.98.202.43/smartbi/vision/share.jsp?resid=100ef521ecf6c5860d5917a961a6e0b0",
        "desc": "SmartBI上市公司数字化转型综合报表平台",
        "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80"
    }
]

# ===================== 页面头部 =====================
st.markdown("""
# 🌐 数字化转型全域导航中台
### Streamlit 应用集群 · SmartBI 可视化报表 · 统一入口门户
""")
st.markdown('<div class="tech-divider"></div>', unsafe_allow_html=True)

# ===================== 三列卡片布局 =====================
col1, col2, col3 = st.columns(3, gap="large")

for idx, item in enumerate(nav_items):
    # 分配到三列
    if idx % 3 == 0:
        col = col1
    elif idx % 3 == 1:
        col = col2
    else:
        col = col3
    
    with col:
        # 生成二维码
        qr_img = make_qr_image(item["url"])
        
        # 卡片HTML结构
        st.markdown(f'''
        <div class="tech-card">
            <img src="{item["img"]}" class="card-img" alt="配图">
            <div class="card-body">
                <div class="card-title">🔹 {item["title"]}</div>
                <div class="card-desc">{item["desc"]}</div>
                <div class="card-url">{item["url"]}</div>
                <div class="card-footer">
        ''', unsafe_allow_html=True)
        
        # 左侧二维码
        qr_col, btn_col = st.columns([1, 1.4])
        with qr_col:
            st.image(qr_img, width=90)
        with btn_col:
            st.link_button("🚀 立即访问", url=item["url"], use_container_width=True)
        
        st.markdown('''
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

# ===================== 页脚 =====================
st.markdown('<div class="tech-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="footer-text">数字化转型导航中台 · 科技可视化门户 · 一键跳转 · 扫码直达</div>', unsafe_allow_html=True)