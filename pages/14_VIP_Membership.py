import streamlit as st
import time
import base64

# =====================================================================
# 1. PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="VIP Membership & Plans | Bandhan",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# 2. READ LOCAL LOGO (नया लोगो)
# =====================================================================
def get_base64_image(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e:
        return ""

main_logo_b64 = get_base64_image("896430.png")

# =====================================================================
# 3. 🔥 ANTI-FLASH & NEW LOGO SPLASH SCREEN 🔥
# =====================================================================
st.markdown(f"""
    <style>
    [data-testid="stSidebarNav"] {{ display: none !important; }}
    
    .stApp::before {{
        content: ""; 
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background-color: #0F2027; 
        background-image: url("data:image/png;base64,{main_logo_b64}"); 
        background-repeat: no-repeat; background-position: center; background-size: 350px; 
        z-index: 9999999; animation: fadeOutSplash 0.8s ease-in-out forwards; 
    }}
    @keyframes fadeOutSplash {{
        0% {{ opacity: 1; visibility: visible; }}
        60% {{ opacity: 1; visibility: visible; }} 
        100% {{ opacity: 0; visibility: hidden; pointer-events: none; }} 
    }}
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 4. 🔥 CUSTOM IMAGE-BASED SIDEBAR MENU (अब नए लोगो के साथ) 🔥
# =====================================================================
sidebar_html = f"""
<div class="app-sidebar-menu">
    <div style="text-align: center; margin-bottom: 20px; border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 15px;">
        <img src="data:image/png;base64,{main_logo_b64}" style="max-width: 85%; height: auto; filter: drop-shadow(0px 4px 6px rgba(0,0,0,0.5));">
    </div>
    
    <a href="/" target="_top" class="menu-item"><div class="icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/1946/1946488.png" alt="Home"></div><div class="menu-text" style="color: #E2E8F0;">Home</div></a>
    <a href="Kundli_Match" target="_top" class="menu-item"><div class="icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/3652/3652191.png" alt="Kundli"></div><div class="menu-text" style="color: #E2E8F0;">Kundli Match</div></a>
    <a href="Registration" target="_top" class="menu-item"><div class="icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/2921/2921222.png" alt="Registration"></div><div class="menu-text" style="color: #E2E8F0;">Registration</div></a>
    <a href="Matchmaking" target="_top" class="menu-item"><div class="icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/1077/1077035.png" alt="Matchmaking"></div><div class="menu-text" style="color: #E2E8F0;">Matchmaking</div></a>
    <a href="Wedding_Services" target="_top" class="menu-item"><div class="icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/3159/3159303.png" alt="Services"></div><div class="menu-text" style="color: #E2E8F0;">Wedding Services</div></a>
    <a href="Verification_KYC" target="_top" class="menu-item"><div class="icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/6928/6928929.png" alt="KYC"></div><div class="menu-text" style="color: #E2E8F0;">Verification KYC</div></a>
</div>
"""
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)

# =====================================================================
# 5. POWERFUL PREMIUM CSS
# =====================================================================
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA !important; font-family: 'Helvetica Neue', sans-serif; }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important;
        border-right: 3px solid #D4AF37 !important;
    }
    .app-sidebar-menu { display: flex; flex-direction: column; gap: 20px; padding-top: 5px; align-items: center; }
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
    .menu-text { font-size: 0.95rem; font-weight: 700; text-align: center; font-family: 'Helvetica', sans-serif; letter-spacing: 0.5px; transition: color 0.3s; }
    
    /* VIP Plans Specific Styles */
    .vip-header {
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        padding: 40px; border-radius: 20px; color: white; text-align: center;
        border: 2px solid #D4AF37; box-shadow: 0 15px 35px rgba(0,0,0,0.2); margin-bottom: 30px;
    }
    .vip-title {
        font-family: 'Georgia', serif; font-size: 3rem; font-weight: 900; margin: 0;
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .plan-card {
        background: white; border-radius: 15px; padding: 30px; text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08); border: 1px solid #EAEAEA;
        border-top: 6px solid #D4AF37; transition: transform 0.3s ease; margin-bottom: 20px;
    }
    .plan-card:hover { transform: translateY(-8px); box-shadow: 0 15px 30px rgba(212, 175, 55, 0.25); }
    .price-tag { font-size: 2.5rem; color: #27AE60; font-weight: 900; margin: 15px 0; }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 6. PAGE CONTENT (Membership Plans)
# =====================================================================
st.markdown("""
<div class="vip-header">
    <h1 class="vip-title">Bandhan VIP & Premium Memberships</h1>
    <p style="font-size:1.2rem; margin-top:15px; color:#FBF5B7; font-style:italic;">Upgrade your account to unlock direct phone numbers, unlimited secure chats, verified badges, and priority matching.</p>
</div>
""", unsafe_allow_html=True)

# Three-Column Membership Plans Layout
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="plan-card">
        <h3>🥉 Silver VIP</h3>
        <p style="color:gray;">Essential features for quick matching</p>
        <div class="price-tag">₹ 2,999</div>
        <p style="font-size:0.9rem; color:#555;">Valid for 3 Months</p>
        <hr>
        <p style="text-align:left;">
        ✅ View 50 Verified Phone Numbers<br>
        ✅ Send 100 Direct Messages<br>
        ✅ Basic Profile Trust Badge<br>
        ❌ Dedicated Relationship Manager
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Choose Silver Plan", key="p1", use_container_width=True):
        st.success("🎉 Silver VIP Selected! Redirecting to secure payment gateway...")

with col2:
    st.markdown("""
    <div class="plan-card" style="border-top: 6px solid #1A365D;">
        <h3>🥇 Gold VIP (Most Popular)</h3>
        <p style="color:gray;">Best value for serious matchmaking</p>
        <div class="price-tag">₹ 5,999</div>
        <p style="font-size:0.9rem; color:#555;">Valid for 6 Months</p>
        <hr>
        <p style="text-align:left;">
        ✅ Unlimited Phone Numbers & Calls<br>
        ✅ Unlimited Direct Live Chat<br>
        ✅ Gold Verified Trust Badge<br>
        ✅ Profile Highlight in Search Results
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Choose Gold Plan", key="p2", type="primary", use_container_width=True):
        st.balloons()
        st.success("🎉 Gold VIP Selected! Premium benefits unlocked successfully.")

with col3:
    st.markdown("""
    <div class="plan-card" style="border-top: 6px solid #E74C3C;">
        <h3>💎 Diamond Elite</h3>
        <p style="color:gray;">Personalized matchmaking & luxury service</p>
        <div class="price-tag">₹ 11,999</div>
        <p style="font-size:0.9rem; color:#555;">Valid for 1 Year</p>
        <hr>
        <p style="text-align:left;">
        ✅ Dedicated Relationship Manager<br>
        ✅ Hand-picked Verified Matches<br>
        ✅ Complete Privacy Shield<br>
        ✅ Wedding Planning Assistance
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Choose Diamond Plan", key="p3", use_container_width=True):
        st.success("🎉 Diamond Elite Selected! Our senior relationship manager will contact you shortly.")
