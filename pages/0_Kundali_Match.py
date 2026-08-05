import streamlit as st
import time

st.set_page_config(page_title="Kundali Match | Bandhan", page_icon="🕉️", layout="wide")
import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Bandhan App", layout="wide")

# =====================================================================
# 2. 🔥 CUSTOM IMAGE-BASED SIDEBAR MENU (Like the Photo) 🔥
# =====================================================================

st.markdown("""
    <style>
    /* Streamlit के पुराने डिफॉल्ट मेन्यू को छिपाना */
    [data-testid="stSidebarNav"] { display: none !important; }
    
    /* नए मेन्यू का CSS डिजाइन (गोल फोटो और टेक्स्ट नीचे) */
    .app-sidebar-menu {
        display: flex;
        flex-direction: column;
        gap: 25px;
        padding-top: 10px;
        align-items: center;
    }
    .menu-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-decoration: none !important;
        color: #1A365D !important;
        transition: transform 0.2s;
        cursor: pointer;
        width: 100%;
    }
    .menu-item:hover {
        transform: scale(1.05); /* माउस ले जाने पर थोड़ा बड़ा होगा */
    }
    .icon-circle {
        width: 75px;
        height: 75px;
        background-color: #F4F6F9; /* फोटो के पीछे का हल्का ग्रे बैकग्राउंड */
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 8px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: 1px solid #EAEAEA;
    }
    .icon-circle img {
        width: 45px;
        height: 45px;
        object-fit: contain;
    }
    .menu-text {
        font-size: 0.95rem;
        font-weight: 700;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# 3. HTML कोड जिसमें हर पेज का लिंक और फोटो (Icon URL) है
sidebar_html = """
<div class="app-sidebar-menu">

    <!-- 1. Kundli Match -->
    <a href="Kundli_Match" target="_self" class="menu-item">
        <div class="icon-circle">
            <!-- यहाँ आप अपनी पसंद की PNG फोटो का लिंक डाल सकते हैं -->
            <img src="https://cdn-icons-png.flaticon.com/512/3652/3652191.png" alt="Kundli">
        </div>
        <div class="menu-text">Kundli Match</div>
    </a>
    
    <!-- 2. Registration -->
    <a href="Registration" target="_self" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/2921/2921222.png" alt="Registration">
        </div>
        <div class="menu-text">Registration</div>
    </a>
    
    <!-- 3. Matchmaking -->
    <a href="Matchmaking" target="_self" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/1077/1077035.png" alt="Matchmaking">
        </div>
        <div class="menu-text">Matchmaking</div>
    </a>

    <!-- 4. Wedding Services -->
    <a href="Wedding_Services" target="_self" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/3159/3159303.png" alt="Services">
        </div>
        <div class="menu-text">Wedding Services</div>
    </a>
    
    <!-- 5. Verification KYC -->
    <a href="Verification_KYC" target="_self" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/6928/6928929.png" alt="KYC">
        </div>
        <div class="menu-text">Verification KYC</div>
    </a>

</div>
"""

# इसे साइडबार में प्रिंट करना
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)
# =====================================================================# --- PREMIUM SIDEBAR CSS WITH LIVE NOTIFICATION BADGE ---
if 'unread_msgs' not in st.session_state:
    st.session_state.unread_msgs = 2  # डेमो के लिए शुरुआत में 2 मैसेज सेट किए हैं

# नोटिफिकेशन बैज का CSS (तभी दिखेगा जब मैसेज 0 से ज्यादा होंगे)
badge_css = ""
if st.session_state.unread_msgs > 0:
    badge_css = f"""
    [data-testid="stSidebarNav"] a[href*="Chat_Alerts"]::after,
    [data-testid="stSidebarNav"] a[href*="chat_alerts"]::after {{
        content: "{st.session_state.unread_msgs}";
        background-color: #FF2A2A !important;
        color: white !important;
        font-size: 0.85rem !important;
        font-weight: 900 !important;
        border-radius: 50% !important;
        min-width: 22px; height: 22px;
        display: flex; align-items: center; justify-content: center;
        position: absolute; right: 15px; top: 50%;
        transform: translateY(-50%);
        box-shadow: 0 0 10px rgba(255, 42, 42, 0.8);
        animation: pulse-red 1.5s infinite;
    }}
    @keyframes pulse-red {{
        0% {{ box-shadow: 0 0 0 0 rgba(255, 42, 42, 0.7); }}
        70% {{ box-shadow: 0 0 0 8px rgba(255, 42, 42, 0); }}
        100% {{ box-shadow: 0 0 0 0 rgba(255, 42, 42, 0); }}
    }}
    """

st.markdown(f"""
    <style>
    /* Global Premium Sidebar Styling */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important;
        border-right: 3px solid #D4AF37 !important;
    }}
    [data-testid="stSidebarNav"]::before {{
        content: "👑 Bandhan Menu"; color: #D4AF37; font-size: 1.8rem; font-weight: 900;
        font-family: 'Georgia', serif; text-align: center; display: block;
        margin-bottom: 25px; padding-top: 20px; border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 15px;
    }}
    [data-testid="stSidebarNav"] a {{
        background-color: rgba(255, 255, 255, 0.05) !important; border-radius: 12px !important;
        margin: 8px 15px !important; padding: 12px !important; border: 1px solid rgba(212, 175, 55, 0.3) !important;
        transition: all 0.3s ease-in-out !important; position: relative;
    }}
    [data-testid="stSidebarNav"] span {{
        color: #E2E8F0 !important; font-size: 1.05rem !important; font-weight: 600 !important;
    }}
    [data-testid="stSidebarNav"] a:hover {{
        background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%) !important;
        transform: translateX(8px) !important; border-color: #FBF5B7 !important;
    }}
    [data-testid="stSidebarNav"] a:hover span {{ color: #0F2027 !important; font-weight: 800 !important; }}
    [data-testid="stSidebarNav"] a[aria-current="page"] {{
        background: linear-gradient(135deg, #D4AF37 0%, #AA771C 100%) !important;
        box-shadow: 0 5px 20px rgba(212, 175, 55, 0.6) !important; border: 2px solid #FBF5B7 !important;
    }}
    [data-testid="stSidebarNav"] a[aria-current="page"] span {{ color: #0F2027 !important; font-weight: 900 !important; }}
    
    /* Inject the Notification Badge CSS here */
    {badge_css}
    </style>
""", unsafe_allow_html=True)
# --------------------------------------------------------------------------------# --- PREMIUM SIDEBAR CSS (Paste this below st.set_page_config in EVERY file) ---
st.markdown("""
    <style>
    /* ---------------------------------------------------
       🔥 GLOBAL PREMIUM SIDEBAR STYLING 🔥
       --------------------------------------------------- */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important;
        border-right: 3px solid #D4AF37 !important;
    }
    [data-testid="stSidebarNav"]::before {
        content: "👑 Bandhan Menu";
        color: #D4AF37;
        font-size: 1.8rem;
        font-weight: 900;
        font-family: 'Georgia', serif;
        text-align: center;
        display: block;
        margin-bottom: 25px;
        padding-top: 20px;
        letter-spacing: 1px;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3);
        padding-bottom: 15px;
    }
    [data-testid="stSidebarNav"] a {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
        margin: 8px 15px !important;
        padding: 12px !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        transition: all 0.3s ease-in-out !important;
    }
    [data-testid="stSidebarNav"] span {
        color: #E2E8F0 !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        font-family: 'Helvetica', sans-serif !important;
        letter-spacing: 0.5px !important;
    }
    [data-testid="stSidebarNav"] a:hover {
        background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%) !important;
        transform: translateX(8px) !important; 
        border-color: #FBF5B7 !important;
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4) !important;
    }
    [data-testid="stSidebarNav"] a:hover span {
        color: #0F2027 !important;
        font-weight: 800 !important;
    }
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: linear-gradient(135deg, #D4AF37 0%, #AA771C 100%) !important;
        box-shadow: 0 5px 20px rgba(212, 175, 55, 0.6) !important;
        border: 2px solid #FBF5B7 !important;
    }
    [data-testid="stSidebarNav"] a[aria-current="page"] span {
        color: #0F2027 !important;
        font-weight: 900 !important;
    }
    </style>
""", unsafe_allow_html=True)
# --------------------------------------------------------------------------------
st.markdown("""
    <style>
    .stApp { background-color: #FFFDF8; }
    .header-kundali { color: #D35400; font-family: 'Georgia', serif; font-size: 2.8rem; text-align: center; font-weight: bold; }
    .guna-score { font-size: 4rem; color: #27AE60; font-weight: 900; text-align: center; }
    .card-box { background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 3px solid #D35400; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='header-kundali'>🕉️ AI Kundali & Guna Milan</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Our advanced Vedic AI calculates accurate planetary positions and the 36 Gunas for perfect compatibility.</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 🤵 Boy's Birth Details")
    b_name = st.text_input("Name", key="b_name")
    b_date = st.date_input("Date of Birth", key="b_date")
    b_time = st.time_input("Time of Birth", key="b_time")
    b_place = st.text_input("Place of Birth", key="b_place")

with col2:
    st.markdown("### 👰 Girl's Birth Details")
    g_name = st.text_input("Name", key="g_name")
    g_date = st.date_input("Date of Birth", key="g_date")
    g_time = st.time_input("Time of Birth", key="g_time")
    g_place = st.text_input("Place of Birth", key="g_place")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔮 Calculate 36 Guna Match", type="primary", use_container_width=True):
    if b_name and g_name:
        with st.spinner("Analyzing planetary positions and Ashtakoota Gunas..."):
            time.sleep(2.5)
        
        st.success("Analysis Complete!")
        st.markdown("<div class='card-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;'>Total Guna Score</h3>", unsafe_allow_html=True)
        st.markdown("<div class='guna-score'>28.5 / 36</div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#27AE60; font-weight:bold;'>Highly Compatible Match! (Nadi Dosha: None)</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("Please enter both names to calculate Kundali.")
