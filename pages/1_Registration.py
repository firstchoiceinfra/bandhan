import streamlit as st
import datetime
import base64

# =====================================================================
# 1. PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Register | Bandhan.com",
    page_icon="✨",
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
    /* Registration Page specific background */
    .stApp { background-color: #FDFDFD !important; font-family: 'Helvetica Neue', sans-serif; }
    
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
    
    /* Registration Content Styles */
    .premium-header {
        color: #0F2027; font-family: 'Trebuchet MS', sans-serif;
        font-size: 2.5rem; font-weight: 800; margin-bottom: 0px;
    }
    .highlight-gold { color: #D4AF37; }
    .sub-text { font-size: 1.1rem; color: #666666; margin-bottom: 30px; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; background-color: transparent;
        border-radius: 4px 4px 0px 0px; padding-top: 10px;
        font-weight: bold; font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 6. PAGE CONTENT (Registration Form)
# =====================================================================
st.markdown("<h1 class='premium-header'>Create Your <span class='highlight-gold'>Premium Profile</span></h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Experience the world's most advanced AI-powered matrimonial and wedding ecosystem.</p>", unsafe_allow_html=True)
st.markdown("---")

# Dynamic Tabs
tab1, tab2, tab3 = st.tabs(["👤 1. Personal Details", "🎯 2. Match Preferences", "🛍️ 3. Wedding Ecosystem"])

# --- TAB 1: Personal Details ---
with tab1:
    st.markdown("### **Basic Information**")
    col1, col2 = st.columns(2)
    
    with col1:
        first_name = st.text_input("First Name")
        email = st.text_input("Email Address")
        gender = st.selectbox("Gender", ["Select...", "Male", "Female"])
        
    with col2:
        last_name = st.text_input("Last Name")
        phone = st.text_input("Phone Number")
        dob = st.date_input("Date of Birth", min_value=datetime.date(1970, 1, 1), max_value=datetime.date(2008, 1, 1))

    st.markdown("### **Background & Profession**")
    col3, col4 = st.columns(2)
    with col3:
        religion = st.selectbox("Religion", ["Select...", "Hindu", "Muslim", "Sikh", "Christian", "Jain", "Other"])
        education = st.selectbox("Highest Education", ["Select...", "Bachelors", "Masters", "Doctorate", "Other"])
    with col4:
        income = st.selectbox("Annual Income", ["Select...", "Below $50k", "$50k - $100k", "Above $100k"])

# --- TAB 2: Match Preferences ---
with tab2:
    st.markdown("### **What are you looking for?**")
    ai_match = st.toggle("🤖 Enable AI Smart Match (Recommended)", value=True)
    
    pref_col1, pref_col2 = st.columns(2)
    with pref_col1:
        age_range = st.slider("Preferred Age Range", 21, 60, (25, 30))
    with pref_col2:
        min_height = st.slider("Minimum Height (in cm)", 140, 210, 150)

# --- TAB 3: Wedding Ecosystem ---
with tab3:
    st.markdown("### **Plan Your Dream Wedding**")
    services = st.multiselect(
        "Which ecosystem services are you looking for?",
        ["Luxury Venue", "Designer Bridal Wear", "Premium Catering", "Vintage Cars", "Honeymoon Packages"]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Submit Button
    submit = st.button("Complete Registration & Enter Ecosystem", type="primary", use_container_width=True)
    
    if submit:
        # Check if first name is entered before submitting
        if first_name == "":
            st.error("Please enter your First Name in Tab 1.")
        else:
            st.success(f"🎉 Registration Successful, {first_name}! Welcome to the Bandhan Premium Ecosystem.")
            st.balloons()
