import streamlit as st

# Page Config
st.set_page_config(page_title="Wedding Finance | Bandhan", page_icon="💳", layout="wide")

# CSS
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    .finance-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 30px; border-radius: 15px; color: white; text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1); margin-bottom: 30px; border-bottom: 5px solid #D4AF37;
    }
    .emi-box {
        background: white; padding: 25px; border-radius: 12px;
        text-align: center; border-top: 5px solid #27AE60;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    .emi-amount { font-size: 2.8rem; color: #27AE60; font-weight: 900; }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="finance-header">
    <h1 style="margin:0; font-family:'Georgia', serif;">💳 Instant Wedding Finance</h1>
    <p style="font-size:1.2rem; margin-top:10px; color:#E3F2FD;">Get up to ₹50 Lakhs with zero processing fee and lowest interest rates from our Partner Banks.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 🧮 EMI Calculator")
    loan_amount = st.slider("Select Loan Amount (₹)", 100000, 5000000, 1000000, step=50000)
    tenure = st.selectbox("Select Tenure (Years)", [1, 2, 3, 4, 5])
    interest_rate = 10.5 # Fixed simulation rate
    
    # Mathematical Logic for EMI
    monthly_rate = interest_rate / (12 * 100)
    months = tenure * 12
    emi = (loan_amount * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    
    st.info("✨ Interest Rate: 10.5% p.a. (Exclusive Bandhan Premium Partner Rate)")
    
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="emi-box">
        <h3 style="color:#1e3c72; margin:0;">Estimated Monthly EMI</h3>
        <div class="emi-amount">₹ {emi:,.0f}</div>
        <p style="color:gray;">For {months} months</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 Apply for Instant Pre-Approval", type="primary", use_container_width=True):
        st.balloons()
        st.success("✅ Application Submitted Successfully! Our partner bank (HDFC/ICICI) will contact you within 24 hours.")
