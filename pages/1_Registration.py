import streamlit as st
import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="Register | Bandhan.com",
    page_icon="✨",
    layout="wide"
)

# 2. Premium Custom CSS (For English UI & Dynamic Look)
st.markdown("""
    <style>
    /* Global Styling */
    .stApp {
        background-color: #FDFDFD;
    }
    
    /* Premium Headers */
    .premium-header {
        color: #0F2027;
        font-family: 'Trebuchet MS', sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .highlight-gold {
        color: #D4AF37; /* Premium Gold */
    }
    
    /* Subtitles */
    .sub-text {
        font-size: 1.1rem;
        color: #666666;
        margin-bottom: 30px;
    }
    
    /* Tab Styling Customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: bold;
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Page Header
st.markdown("<h1 class='premium-header'>Create Your <span class='highlight-gold'>Premium Profile</span></h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Experience the world's most advanced AI-powered matrimonial and wedding ecosystem. Please provide your details below.</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. Dynamic Tabs for Advanced Form Layout
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
        education = st.selectbox("Highest Education", ["Select...", "Bachelors", "Masters", "Doctorate", "Diploma", "Other"])
    with col4:
        mother_tongue = st.selectbox("Mother Tongue", ["Select...", "Hindi", "English", "Marathi", "Gujarati", "Punjabi", "Other"])
        income = st.selectbox("Annual Income", ["Select...", "Below $50k", "$50k - $100k", "$100k - $250k", "Above $250k", "Prefer not to say"])

    st.file_uploader("Upload Profile Picture (AI Face Verification enabled)", type=['jpg', 'png', 'jpeg'])

# --- TAB 2: Match Preferences ---
with tab2:
    st.markdown("### **What are you looking for?**")
    
    st.markdown("Enable **AI Smart Match** to let our algorithm find the best profile based on your behavioral traits.")
    ai_match = st.toggle("🤖 Enable AI Smart Match (Recommended)", value=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    pref_col1, pref_col2 = st.columns(2)
    
    with pref_col1:
        age_range = st.slider("Preferred Age Range", 21, 60, (25, 30))
        pref_religion = st.multiselect("Preferred Religion", ["Hindu", "Muslim", "Sikh", "Christian", "Jain", "Doesn't Matter"])
    
    with pref_col2:
        min_height = st.slider("Minimum Height (in cm)", 140, 210, 150)
        pref_location = st.text_input("Preferred City / Country")

# --- TAB 3: Wedding Ecosystem (Advanced Feature) ---
with tab3:
    st.markdown("### **Plan Your Dream Wedding**")
    st.markdown("Select the services you need. Our ecosystem vendors will provide customized, premium quotes.")
    
    services = st.multiselect(
        "Which ecosystem services are you looking for?",
        ["Luxury Venue / Banquet", "Designer Bridal Wear", "Premium Catering", "Vintage Cars / Supercars", "Photography & Cinematography", "Honeymoon Packages", "Wedding Planners"]
    )
    
    budget = st.select_slider(
        "Estimated Wedding Budget",
        options=["Standard", "Premium", "Luxury", "Ultra-Luxury (Destination)"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Submit Button
    submit = st.button("Complete Registration & Enter Ecosystem", type="primary", use_container_width=True)
    
    if submit:
        st.success("🎉 Registration Successful! Welcome to the Bandhan Premium Ecosystem.")
        st.balloons()
