import streamlit as st
import time

# Page Config
st.set_page_config(page_title="Search Partner | Bandhan", page_icon="🔍", layout="wide")
# --- PREMIUM SIDEBAR CSS WITH LIVE NOTIFICATION BADGE ---
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
# CSS Styling
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    .search-header {
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        padding: 35px; border-radius: 15px; color: white; text-align: center;
        border-bottom: 5px solid #D4AF37; margin-bottom: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    .search-title {
        font-family: 'Georgia', serif; font-size: 2.8rem; font-weight: 900; margin: 0;
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .filter-card {
        background: white; padding: 30px; border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.06); border: 1px solid #EAEAEA;
    }
    .profile-result-card {
        background: white; padding: 20px; border-radius: 12px; margin-top: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05); border-left: 6px solid #27AE60;
        border-top: 1px solid #EAEAEA; border-right: 1px solid #EAEAEA; border-bottom: 1px solid #EAEAEA;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="search-header">
    <h1 class="search-title">Search Partner</h1>
    <p style="font-size:1.1rem; margin-top:10px; color:#FBF5B7; font-style:italic;">Filter through thousands of verified profiles to find your perfect life partner.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='filter-card'>", unsafe_allow_html=True)
st.markdown("<h3>🎯 Set Your Partner Preferences</h3><br>", unsafe_allow_html=True)

f_col1, f_col2 = st.columns(2, gap="large")

with f_col1:
    age_range = st.slider("Select Age Range (Years)", 18, 60, (21, 28))
    religion = st.selectbox("Religion", ["Any", "Hindu", "Muslim", "Sikh", "Christian", "Jain", "Buddhist"])
    profession = st.selectbox("Profession / Occupation", ["Any", "Software Engineer", "Doctor", "Business Owner", "Chartered Accountant", "Civil Servant", "Banker", "Teacher"])
    education = st.selectbox("Minimum Education", ["Any", "B.Tech / B.E.", "MBA / PG", "MBBS / MD", "Post Graduate", "Graduate"])

with f_col2:
    city = st.selectbox("Preferred City / Location", ["Any", "Nagpur", "Mumbai", "Pune", "Bangalore", "Delhi", "Hyderabad", "Kolkata"])
    income = st.selectbox("Annual Income", ["Any", "₹ 5 Lakhs - ₹ 10 Lakhs", "₹ 10 Lakhs - ₹ 20 Lakhs", "₹ 20 Lakhs - ₹ 50 Lakhs", "₹ 50 Lakhs+"])
    manglik = st.selectbox("Kundli / Manglik Preference", ["Doesn't Matter", "Non-Manglik", "Manglik"])
    marital_status = st.selectbox("Marital Status", ["Any", "Unmarried", "Divorced", "Widowed"])

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Search Matching Profiles", type="primary", use_container_width=True):
    with st.spinner("Searching verified database based on your filters..."):
        time.sleep(1.5)
    st.success("✨ Found 42 verified profiles matching your exact preferences!")
    
    # Sample Results Display
    st.markdown("""
    <div class="profile-result-card">
        <h3 style="color:#1A365D; margin-top:0;">1. Ritu Deshmukh (24 yrs, Nagpur) ⭐ 96% Match</h3>
        <p><b>Profession:</b> Software Engineer | <b>Education:</b> B.Tech | <b>Income:</b> ₹ 12 Lakhs p.a. | <b>Religion:</b> Hindu (Non-Manglik)</p>
        <p style="color:gray; font-size:0.9rem;">Verified ID (Aadhaar) • Active 2 hours ago</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="profile-result-card" style="border-left-color: #1A365D;">
        <h3 style="color:#1A365D; margin-top:0;">2. Sneha Patil (26 yrs, Pune) ⭐ 92% Match</h3>
        <p><b>Profession:</b> Chartered Accountant | <b>Education:</b> CA / M.Com | <b>Income:</b> ₹ 15 Lakhs p.a. | <b>Religion:</b> Hindu</p>
        <p style="color:gray; font-size:0.9rem;">Verified ID (PAN Card) • Active Online Now</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
