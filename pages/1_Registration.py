import streamlit as st
import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="Register | Bandhan.com",
    page_icon="✨",
    layout="wide"
)
# --- PREMIUM SIDEBAR CSS (Paste this below st.set_page_config in EVERY file) ---
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
# 2. Premium Custom CSS
st.markdown("""
    <style>
    .stApp { background-color: #FDFDFD; }
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

# 3. Page Header
st.markdown("<h1 class='premium-header'>Create Your <span class='highlight-gold'>Premium Profile</span></h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Experience the world's most advanced AI-powered matrimonial and wedding ecosystem.</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. Dynamic Tabs
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
