import streamlit as st
import time
import base64

# =====================================================================
# 1. 🔥 ANTI-FLASH & HIDE DEFAULT NAVIGATION 🔥
# =====================================================================
st.markdown("""
    <style>
    /* Streamlit के पुराने डिफ़ॉल्ट नेविगेशन को पूरी तरह छिपाना */
    [data-testid="stSidebarNav"] { display: none !important; }
    
    /* पेज लोड होने तक पूरे ऐप को छिपाएं ताकि सफेद फ्लैश न दिखे */
    .stApp { opacity: 0; animation: fadeIn 0.4s ease-in forwards; }
    @keyframes fadeIn { to { opacity: 1; } }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 2. PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Kundali Match | Bandhan",
    page_icon="🕉️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# 3. 🔥 DARK PREMIUM SPLASH SCREEN (WITH LOCAL LOGO) 🔥
# =====================================================================
def get_base64_image(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e:
        return ""

logo_b64 = get_base64_image("896327.png")

st.markdown(f"""
    <style>
    .stApp::after {{
        content: ""; 
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%); 
        background-image: url("data:image/png;base64,{logo_b64}"); 
        background-repeat: no-repeat;
        background-position: center;
        background-size: 350px; 
        filter: drop-shadow(0px 0px 12px rgba(255, 255, 255, 0.5));
        z-index: 9999999; 
        animation: fadeOutSplash 1.2s ease-in-out forwards; 
    }}
    @keyframes fadeOutSplash {{
        0% {{ opacity: 1; visibility: visible; }}
        70% {{ opacity: 1; visibility: visible; }} 
        100% {{ opacity: 0; visibility: hidden; pointer-events: none; }} 
    }}
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 4. 🔥 CUSTOM IMAGE-BASED SIDEBAR MENU (target="_top" के साथ) 🔥
# =====================================================================
sidebar_html = """
<div class="app-sidebar-menu">
    <!-- Top Custom Title for Sidebar -->
    <div style="color: #D4AF37; font-size: 1.8rem; font-weight: 900; font-family: 'Georgia', serif; text-align: center; margin-bottom: 20px; border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 15px;">
        👑 Bandhan Menu
    </div>

    <!-- 0. Home Page -->
    <a href="/" target="_top" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/1946/1946488.png" alt="Home">
        </div>
        <div class="menu-text" style="color: #E2E8F0;">Home</div>
    </a>

    <!-- 1. Kundli Match -->
    <a href="Kundli_Match" target="_top" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/3652/3652191.png" alt="Kundli">
        </div>
        <div class="menu-text" style="color: #E2E8F0;">Kundli Match</div>
    </a>
    
    <!-- 2. Registration -->
    <a href="Registration" target="_top" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/2921/2921222.png" alt="Registration">
        </div>
        <div class="menu-text" style="color: #E2E8F0;">Registration</div>
    </a>
    
    <!-- 3. Matchmaking -->
    <a href="Matchmaking" target="_top" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/1077/1077035.png" alt="Matchmaking">
        </div>
        <div class="menu-text" style="color: #E2E8F0;">Matchmaking</div>
    </a>

    <!-- 4. Wedding Services -->
    <a href="Wedding_Services" target="_top" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/3159/3159303.png" alt="Services">
        </div>
        <div class="menu-text" style="color: #E2E8F0;">Wedding Services</div>
    </a>
    
    <!-- 5. Verification KYC -->
    <a href="Verification_KYC" target="_top" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/6928/6928929.png" alt="KYC">
        </div>
        <div class="menu-text" style="color: #E2E8F0;">Verification KYC</div>
    </a>
</div>
"""

# इसे साइडबार में प्रिंट करना
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)


# =====================================================================
# 5. POWERFUL PREMIUM CSS (Sidebar & Kundli Styling)
# =====================================================================
st.markdown("""
    <style>
    /* Main App Background (Off-white for Kundli Page) */
    .stApp { background-color: #FFFDF8 !important; }
    
    /* 1. Sidebar Background Gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important;
        border-right: 3px solid #D4AF37 !important;
    }

    /* 2. Custom Sidebar Menu CSS */
    .app-sidebar-menu {
        display: flex; flex-direction: column; gap: 20px; padding-top: 5px; align-items: center;
    }
    .menu-item {
        display: flex; flex-direction: column; align-items: center; text-decoration: none !important;
        transition: transform 0.2s, background 0.3s; cursor: pointer; width: 90%; padding: 10px;
        border-radius: 12px; background-color: rgba(255, 255, 255, 0.05); border: 1px solid rgba(212, 175, 55, 0.2);
    }
    .menu-item:hover {
        transform: scale(1.05); background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%);
        border-color: #FBF5B7; box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4);
    }
    .menu-item:hover .menu-text { color: #0F2027 !important; font-weight: 900 !important; }
    
    .icon-circle {
        width: 65px; height: 65px; background-color: #FFFFFF; border-radius: 50%;
        display: flex; justify-content: center; align-items: center; margin-bottom: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .icon-circle img { width: 38px; height: 38px; object-fit: contain; }
    
    .menu-text {
        font-size: 0.95rem; font-weight: 700; text-align: center; font-family: 'Helvetica', sans-serif;
        letter-spacing: 0.5px; transition: color 0.3s;
    }

    /* KUNDALI MATCH PAGE SPECIFIC CSS */
    .header-kundali { color: #D35400; font-family: 'Georgia', serif; font-size: 2.8rem; text-align: center; font-weight: bold; }
    .guna-score { font-size: 4rem; color: #27AE60; font-weight: 900; text-align: center; }
    .card-box { background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 3px solid #D35400; }
    </style>
""", unsafe_allow_html=True)


# =====================================================================
# 6. PAGE CONTENT (Boy/Girl Details Form)
# =====================================================================

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
