import streamlit as st

# Page Config
st.set_page_config(page_title="Instant Wedding Finance | Bandhan", page_icon="💳", layout="wide")

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

    /* Broad & Bold Form Labels Styling */
    .custom-label {
        font-size: 1.3rem;
        font-weight: 800;
        color: #1A365D;
        margin-bottom: 5px;
        display: block;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* EMI Calculator Card Background */
    .calc-container {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.06);
        border: 1px solid #EAEAEA;
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

    /* Cinematic Compact Button Customization */
    .stButton > button {
        background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%) !important;
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: 800 !important;
        padding: 10px 25px !important;
        border-radius: 50px !important;
        border: none !important;
        box-shadow: 0 8px 20px rgba(255, 65, 108, 0.4) !important;
        transition: all 0.3s ease !important;
        display: block !important;
        margin: 0 auto !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 12px 25px rgba(255, 65, 108, 0.6) !important;
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
    st.markdown("<h2 style='color:#1A365D; margin-top:0;'>🧮 Advanced EMI Calculator</h2><hr>", unsafe_allow_html=True)
    
    # 1. Broad Loan Amount Input
    st.markdown("<span class='custom-label'>💳 Select Loan Amount (₹)</span>", unsafe_allow_html=True)
    loan_amount = st.slider("", min_value=100000, max_value=5000000, value=1500000, step=50000, label_visibility="collapsed")
    st.markdown(f"<p style='color:gray; font-weight:bold;'>Selected Amount: ₹ {loan_amount:,.0f}</p><br>", unsafe_allow_html=True)
    
    # 2. Broad Tenure Input (Up to 10 Years)
    st.markdown("<span class='custom-label'>⏳ Select Tenure (Years)</span>", unsafe_allow_html=True)
    tenure = st.slider("", min_value=1, max_value=10, value=5, step=1, label_visibility="collapsed")
    st.markdown(f"<p style='color:gray; font-weight:bold;'>Selected Tenure: {tenure} Years ({tenure * 12} Months)</p><br>", unsafe_allow_html=True)
    
    # 3. Custom Interest Rate Option
    st.markdown("<span class='custom-label'>📊 Rate of Interest (% p.a.)</span>", unsafe_allow_html=True)
    interest_rate = st.number_input("", min_value=5.0, max_value=25.0, value=10.5, step=0.5, label_visibility="collapsed")
    
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
    
    # Cinematic Compact Button for Instant Pre-Approval
    if st.button("Apply for Instant Pre-Approval"):
        st.balloons()
        st.success("✅ Application Submitted Successfully! Our partner bank executive will contact you within 24 hours.")
