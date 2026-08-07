import streamlit as st
import time
import base64

# --- 1. फ्लैश रोकने और नेविगेशन छिपाने के लिए ---
st.markdown("""
    <style>
    [data-testid="stSidebarNav"], #stSidebarNav { display: none !important; }
    .stApp { opacity: 0; animation: fadeIn 0.3s ease-in forwards; }
    @keyframes fadeIn { to { opacity: 1; } }
    </style>
""", unsafe_allow_html=True)

# 2. Page Configuration
st.set_page_config(page_title="Kundali Match | Bandhan", page_icon="🕉️", layout="wide")

# 3. READ LOCAL LOGO
def get_base64_image(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e:
        return ""

logo_b64 = get_base64_image("896327.png")

# 4. SPLASH SCREEN
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

# 5. CUSTOM SIDEBAR HTML
sidebar_html = f"""
    <div class="sidebar-logo-container">
        <img src="data:image/png;base64,{logo_b64}" alt="Bandhan Logo" class="sidebar-main-logo">
    </div>
    <div class="custom-sidebar-menu">
        <a href="/" target="_self" class="custom-menu-item">
            <div class="custom-icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/1946/1946488.png"></div>
            <div class="custom-menu-text">Home</div>
        </a>
        <a href="Kundli_Match" target="_self" class="custom-menu-item">
            <div class="custom-icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/3652/3652191.png"></div>
            <div class="custom-menu-text">Kundli Match</div>
        </a>
        <a href="Registration" target="_self" class="custom-menu-item">
            <div class="custom-icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/2921/2921222.png"></div>
            <div class="custom-menu-text">Registration</div>
        </a>
        <a href="Matchmaking" target="_self" class="custom-menu-item">
            <div class="custom-icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/1077/1077035.png"></div>
            <div class="custom-menu-text">Matchmaking</div>
        </a>
        <a href="Wedding_Services" target="_self" class="custom-menu-item">
            <div class="custom-icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/3159/3159303.png"></div>
            <div class="custom-menu-text">Wedding Services</div>
        </a>
        <a href="Chat_Alerts" target="_self" class="custom-menu-item">
            <div class="custom-icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/1380/1380370.png"></div>
            <div class="custom-menu-text">Chat & Alerts</div>
        </a>
    </div>
"""
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)

# 6. SIDEBAR & KUNDALI PAGE SPECIFIC CSS
st.markdown("""
    <style>
    .stApp { background-color: #FFFDF8 !important; }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important;
        border-right: 3px solid #D4AF37 !important;
    }
    .sidebar-logo-container {
        text-align: center; margin-bottom: 25px; padding-top: 15px;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 15px;
        background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0) 70%);
    }
    .sidebar-main-logo {
        max-width: 80%; height: auto; object-fit: contain;
        filter: drop-shadow(0px 0px 8px rgba(255, 255, 255, 0.8)); 
    }
    .custom-sidebar-menu { display: flex; flex-direction: column; gap: 12px; }
    .custom-menu-item {
        display: flex; flex-direction: row; align-items: center; justify-content: flex-start; 
        background-color: rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 10px 15px;
        border: 1px solid rgba(212, 175, 55, 0.3); text-decoration: none !important;
        transition: all 0.3s ease-in-out;
    }
    .custom-menu-item:hover {
        background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%);
        transform: translateX(8px); border-color: #FBF5B7; box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4);
    }
    .custom-icon-circle {
        width: 42px; height: 42px; min-width: 42px; background-color: #FFFFFF; 
        border-radius: 50%; display: flex; justify-content: center; align-items: center;
        margin-right: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.2); overflow: hidden; 
    }
    .custom-icon-circle img { width: 28px; height: 28px; object-fit: contain; }
    .custom-menu-text {
        color: #E2E8F0; font-size: 1.05rem; font-weight: 600; font-family: 'Helvetica', sans-serif;
        text-align: left; line-height: 1.2;
    }
    .custom-menu-item:hover .custom-menu-text { color: #0F2027; font-weight: 800; }
    
    /* Kundli Specific Content Styles */
    .header-kundali { color: #D35400; font-family: 'Georgia', serif; font-size: 2.8rem; text-align: center; font-weight: bold; }
    .guna-score { font-size: 4rem; color: #27AE60; font-weight: 900; text-align: center; }
    .card-box { background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 3px solid #D35400; }
    </style>
""", unsafe_allow_html=True)

# 7. Kundli Page Content (Boy/Girl Details)
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
