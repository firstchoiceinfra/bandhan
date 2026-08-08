import streamlit as st
import time
import base64

# =====================================================================
# 1. PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Instant Wedding Finance | Bandhan",
    page_icon="💳",
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
    .stApp { background-color: #F4F6F9 !important; font-family: 'Helvetica Neue', sans-serif; }
    
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
    
    /* Instant Wedding Finance Specific Styles */
    .finance-header {
        position: relative;
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        padding: 40px 30px;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        border: 2px solid #D4AF37;
        margin-bottom: 30px;
        overflow: hidden;
    }
    .header-flex { display: flex; justify-content: center; align-items: center; gap: 20px; flex-wrap: wrap; }
    .card-img-left { width: 80px; filter: drop-shadow(2px 4px 8px rgba(0,0,0,0.5)); }
    .finance-title {
        font-family: 'Georgia', serif; font-size: 3rem; font-weight: 900; margin: 0;
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .money-img-right { width: 75px; filter: drop-shadow(2px 4px 8px rgba(0,0,0,0.5)); }
    .calc-container { background: white; padding: 35px; border-radius: 20px; box-shadow: 0 15px 35px rgba(0,0,0,0.08); border: 1px solid #EAEAEA; }
    .section-box-header {
        background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%); color: #FBF5B7;
        padding: 14px 20px; border-radius: 12px; font-size: 1.25rem; font-weight: 800; margin-bottom: 15px;
        border-left: 5px solid #D4AF37; box-shadow: 0 5px 15px rgba(0,0,0,0.1); display: flex; align-items: center; gap: 10px;
    }
    .premium-value-box {
        background: linear-gradient(135deg, #F8F9FA 0%, #E9ECEF 100%); border: 2px solid #CBD5E1;
        padding: 12px 20px; border-radius: 10px; text-align: center; font-size: 1.4rem; font-weight: 900;
        color: #D97706; box-shadow: inset 0 2px 4px rgba(0,0,0,0.05); margin-top: 10px; margin-bottom: 25px; letter-spacing: 0.5px;
    }
    .emi-box {
        background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%); color: white; padding: 35px;
        border-radius: 20px; text-align: center; box-shadow: 0 15px 30px rgba(26, 54, 93, 0.25); border: 2px solid #D4AF37;
    }
    .emi-amount { font-size: 3.2rem; color: #27AE60; font-weight: 900; margin: 15px 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
    
    .stButton > button {
        background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%) !important; color: white !important;
        font-size: 1.15rem !important; font-weight: 800 !important; padding: 12px 30px !important;
        border-radius: 50px !important; border: none !important; box-shadow: 0 10px 25px rgba(255, 65, 108, 0.45) !important;
        transition: all 0.4s ease !important; display: block !important; margin: 0 auto !important;
        animation: pulse-animation 2s infinite;
    }
    @keyframes pulse-animation {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 65, 108, 0.5); }
        70% { transform: scale(1.03); box-shadow: 0 0 0 12px rgba(255, 65, 108, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 65, 108, 0); }
    }
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.04); background: linear-gradient(135deg, #FF4B2B 0%, #FF416C 100%) !important;
        box-shadow: 0 15px 30px rgba(255, 65, 108, 0.7) !important;
    }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 6. PAGE CONTENT
# =====================================================================
st.markdown("""
<div class="finance-header">
    <div class="header-flex">
        <img src="https://cdn-icons-png.flaticon.com/512/6963/6963703.png" class="card-img-left" title="Instant Credit Card">
        <h1 class="finance-title">Instant Wedding Finance</h1>
        <img src="https://cdn-icons-png.flaticon.com/512/2489/2489756.png" class="money-img-right" title="Wedding Money">
    </div>
    <p style="font-size:1.2rem; margin-top:15px; color:#FBF5B7; font-style:italic;">Get up to ₹50 Lakhs with zero processing fee and flexible EMI options.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown("<div class='calc-container'>", unsafe_allow_html=True)
    st.markdown("<div class='section-box-header'>🧮 Advanced EMI Calculator</div>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 10px 0 20px 0;'>", unsafe_allow_html=True)
    
    st.markdown("<div class='section-box-header' style='font-size: 1.1rem;'>💳 Select Loan Amount (₹)</div>", unsafe_allow_html=True)
    loan_amount = st.slider("", min_value=100000, max_value=5000000, value=1500000, step=50000, label_visibility="collapsed")
    st.markdown(f"<div class='premium-value-box'>₹ {loan_amount:,.0f}</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='section-box-header' style='font-size: 1.1rem;'>⏳ Select Tenure (Years)</div>", unsafe_allow_html=True)
    tenure = st.slider("", min_value=1, max_value=10, value=5, step=1, label_visibility="collapsed")
    st.markdown(f"<div class='premium-value-box'>{tenure} Years ({tenure * 12} Months)</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='section-box-header' style='font-size: 1.1rem;'>📊 Rate of Interest (% p.a.)</div>", unsafe_allow_html=True)
    interest_rate = st.number_input("", min_value=5.0, max_value=25.0, value=10.5, step=0.5, label_visibility="collapsed")
    st.markdown(f"<div class='premium-value-box'>{interest_rate}% p.a.</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    monthly_rate = interest_rate / (12 * 100)
    months = tenure * 12
    emi = (loan_amount * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="emi-box">
        <h3 style="color:#D4AF37; margin:0; font-size:1.5rem; text-transform:uppercase; letter-spacing:1px;">Estimated Monthly EMI</h3>
        <div class="emi-amount">₹ {emi:,.0f}</div>
        <p style="color:#E2E8F0; font-size:1rem; margin:0;">Total Tenure: <b>{months} Months</b> @ <b>{interest_rate}% Interest</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.button("Apply for Instant Pre-Approval"):
        st.balloons()
        st.success("✅ Application Submitted Successfully! Our partner bank executive will contact you within 24 hours.")
