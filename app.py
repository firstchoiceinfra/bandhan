import streamlit as st
import base64

# --- फ्लैश रोकने का सबसे पावरफुल तरीका (सबसे ऊपर) ---
st.markdown("""
    <style>
    [data-testid="stSidebarNav"], #stSidebarNav { display: none !important; }
    .stApp { opacity: 0; animation: fadeIn 0.3s ease-in forwards; }
    @keyframes fadeIn { to { opacity: 1; } }
    </style>
""", unsafe_allow_html=True)

# 1. Page Configuration
st.set_page_config(
    page_title="Bandhan | Premium Matrimony & Ecosystem",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. READ LOCAL LOGO (896327.png)
def get_base64_image(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e: return ""

logo_b64 = get_base64_image("896327.png")

# 3. SPLASH SCREEN (Dark & Premium)
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

# 4. SIDEBAR & CSS
sidebar_html = f"""
    <div class="sidebar-logo-container">
        <img src="data:image/png;base64,{logo_b64}" alt="Bandhan Logo" class="sidebar-main-logo">
    </div>
    <div class="custom-sidebar-menu">
        <a href="/" target="_self" class="custom-menu-item"><div class="custom-icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/1946/1946488.png"></div><div class="custom-menu-text">Home</div></a>
        <a href="Kundli_Match" target="_self" class="custom-menu-item"><div class="custom-icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/3652/3652191.png"></div><div class="custom-menu-text">Kundli Match</div></a>
        <a href="Registration" target="_self" class="custom-menu-item"><div class="custom-icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/2921/2921222.png"></div><div class="custom-menu-text">Registration</div></a>
        <a href="Matchmaking" target="_self" class="custom-menu-item"><div class="custom-icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/1077/1077035.png"></div><div class="custom-menu-text">Matchmaking</div></a>
        <a href="Wedding_Services" target="_self" class="custom-menu-item"><div class="custom-icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/3159/3159303.png"></div><div class="custom-menu-text">Wedding Services</div></a>
        <a href="Chat_Alerts" target="_self" class="custom-menu-item"><div class="custom-icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/1380/1380370.png"></div><div class="custom-menu-text">Chat & Alerts</div></a>
    </div>
"""
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)

st.markdown("""
    <style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important; border-right: 3px solid #D4AF37 !important; }
    .sidebar-logo-container { text-align: center; margin-bottom: 25px; padding: 15px; border-bottom: 1px solid rgba(212, 175, 55, 0.3); background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0) 70%); }
    .sidebar-main-logo { max-width: 80%; height: auto; filter: drop-shadow(0px 0px 8px rgba(255, 255, 255, 0.8)); }
    .custom-sidebar-menu { display: flex; flex-direction: column; gap: 12px; }
    .custom-menu-item { display: flex; align-items: center; background: rgba(255,255,255,0.05); border-radius: 12px; padding: 10px 15px; border: 1px solid rgba(212,175,55,0.3); text-decoration: none !important; }
    .custom-icon-circle { width: 42px; height: 42px; background: white; border-radius: 50%; display: flex; justify-content: center; align-items: center; margin-right: 15px; overflow: hidden; }
    .custom-icon-circle img { width: 28px; }
    .custom-menu-text { color: #E2E8F0; font-weight: 600; }
    .feature-box { background: white; padding: 25px; border-radius: 15px; border-bottom: 4px solid #D4AF37; }
    </style>
""", unsafe_allow_html=True)

# Content...
st.title("Bandhan.com 💍")
# ... (बाकी कंटेंट)
