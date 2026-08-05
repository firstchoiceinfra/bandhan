import streamlit as st

# Page Config
st.set_page_config(page_title="Instant Wedding Finance | Bandhan", page_icon="💳", layout="wide")
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
# Premium CSS & Styling
st.markdown("""
    <style>
    .stApp { background-color: #F4F6F9; }
    
    /* Header Container with Credit Card & Money Background Vibe */
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
    
    .header-flex {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        flex-wrap: wrap;
    }
    
    .card-img-left {
        width: 80px;
        filter: drop-shadow(2px 4px 8px rgba(0,0,0,0.5));
    }
    
    .finance-title {
        font-family: 'Georgia', serif;
        font-size: 3rem;
        font-weight: 900;
        margin: 0;
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .money-img-right {
        width: 75px;
        filter: drop-shadow(2px 4px 8px rgba(0,0,0,0.5));
    }

    /* Main Calculator Container Background */
    .calc-container {
        background: white;
        padding: 35px;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.08);
        border: 1px solid #EAEAEA;
    }

    /* Section Headings with Background Cards */
    .section-box-header {
        background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%);
        color: #FBF5B7;
        padding: 14px 20px;
        border-radius: 12px;
        font-size: 1.25rem;
        font-weight: 800;
        margin-bottom: 15px;
        border-left: 5px solid #D4AF37;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Premium Value Highlight Boxes (For Loan Amount, Tenure, & Interest Rate) */
    .premium-value-box {
        background: linear-gradient(135deg, #F8F9FA 0%, #E9ECEF 100%);
        border: 2px solid #CBD5E1;
        padding: 12px 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.4rem;
        font-weight: 900;
        color: #D97706; /* Rich Premium Amber/Gold tone */
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
        margin-top: 10px;
        margin-bottom: 25px;
        letter-spacing: 0.5px;
    }

    /* Estimated Monthly EMI Premium Box */
    .emi-box {
        background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%);
        color: white;
        padding: 35px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 15px 30px rgba(26, 54, 93, 0.25);
        border: 2px solid #D4AF37;
    }
    
    .emi-amount {
        font-size: 3.2rem;
        color: #27AE60;
        font-weight: 900;
        margin: 15px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* Animated & Cinematic Compact Button */
    .stButton > button {
        background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%) !important;
        color: white !important;
        font-size: 1.15rem !important;
        font-weight: 800 !important;
        padding: 12px 30px !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 10px 25px rgba(255, 65, 108, 0.45) !important;
        transition: all 0.4s ease !important;
        display: block !important;
        margin: 0 auto !important;
        animation: pulse-animation 2s infinite;
    }
    
    @keyframes pulse-animation {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 65, 108, 0.5); }
        70% { transform: scale(1.03); box-shadow: 0 0 0 12px rgba(255, 65, 108, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 65, 108, 0); }
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.04);
        background: linear-gradient(135deg, #FF4B2B 0%, #FF416C 100%) !important;
        box-shadow: 0 15px 30px rgba(255, 65, 108, 0.7) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section with Credit Card & Money Images
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

# Layout Grid
col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown("<div class='calc-container'>", unsafe_allow_html=True)
    
    # Advanced EMI Calculator Header with Background
    st.markdown("<div class='section-box-header'>🧮 Advanced EMI Calculator</div>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 10px 0 20px 0;'>", unsafe_allow_html=True)
    
    # 1. Select Loan Amount Box & Slider
    st.markdown("<div class='section-box-header' style='font-size: 1.1rem;'>💳 Select Loan Amount (₹)</div>", unsafe_allow_html=True)
    loan_amount = st.slider("", min_value=100000, max_value=5000000, value=1500000, step=50000, label_visibility="collapsed")
    st.markdown(f"<div class='premium-value-box'>₹ {loan_amount:,.0f}</div>", unsafe_allow_html=True)
    
    # 2. Select Tenure Box & Slider
    st.markdown("<div class='section-box-header' style='font-size: 1.1rem;'>⏳ Select Tenure (Years)</div>", unsafe_allow_html=True)
    tenure = st.slider("", min_value=1, max_value=10, value=5, step=1, label_visibility="collapsed")
    st.markdown(f"<div class='premium-value-box'>{tenure} Years ({tenure * 12} Months)</div>", unsafe_allow_html=True)
    
    # 3. Rate of Interest Box & Input
    st.markdown("<div class='section-box-header' style='font-size: 1.1rem;'>📊 Rate of Interest (% p.a.)</div>", unsafe_allow_html=True)
    interest_rate = st.number_input("", min_value=5.0, max_value=25.0, value=10.5, step=0.5, label_visibility="collapsed")
    st.markdown(f"<div class='premium-value-box'>{interest_rate}% p.a.</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Mathematical Logic for EMI calculation
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
    
    # Cinematic Animated Button for Instant Pre-Approval
    if st.button("Apply for Instant Pre-Approval"):
        st.balloons()
        st.success("✅ Application Submitted Successfully! Our partner bank executive will contact you within 24 hours.")
