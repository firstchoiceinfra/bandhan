import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Premium Plans | Bandhan",
    page_icon="💎",
    layout="wide"
)

# 2. Premium Pricing CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #FAFAFA;
    }
    .pricing-header {
        color: #0F2027;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 900;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 5px;
    }
    
    /* Pricing Card Standard */
    .pricing-card {
        background: white;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #EAEAEA;
        transition: transform 0.3s;
    }
    .pricing-card:hover {
        transform: translateY(-10px);
    }
    
    /* Highlighted Premium Card */
    .premium-card {
        background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%);
        color: white;
        border-radius: 15px;
        padding: 35px 30px;
        box-shadow: 0 15px 35px rgba(26, 54, 93, 0.3);
        text-align: center;
        transform: scale(1.05);
        border: 2px solid #D4AF37;
    }
    
    .price-text {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 15px 0px;
    }
    .gold-text { color: #D4AF37; }
    
    .feature-list {
        text-align: left;
        line-height: 2;
        margin-bottom: 25px;
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header
st.markdown("<h1 class='pricing-header'>Upgrade to <span class='gold-text'>Bandhan Premium</span> 💎</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:1.2rem; color:gray;'>Unlock the full power of our AI Matchmaking and Wedding Ecosystem.</p><br>", unsafe_allow_html=True)

# 4. Pricing Cards (3 Columns)
col1, col2, col3 = st.columns([1, 1.1, 1], gap="medium")

# --- Basic Plan ---
with col1:
    st.markdown("""
        <div class="pricing-card">
            <h2 style='color:#1A365D;'>Gold Plan</h2>
            <p style='color:gray;'>Perfect for getting started</p>
            <div class="price-text">$29 <span style='font-size:1rem; color:gray;'>/ month</span></div>
            <div class="feature-list">
                ✅ Create Basic Profile<br>
                ✅ View Up To 50 Profiles/Day<br>
                ✅ Standard Search Filters<br>
                ❌ No AI Matchmaking<br>
                ❌ No Ecosystem Access
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Select Gold", key="gold_btn", use_container_width=True):
        st.info("Redirecting to Gold Checkout...")

# --- Premium Plan (Highlighted) ---
with col2:
    st.markdown("""
        <div class="premium-card">
            <h2 style='color:#D4AF37;'>Platinum Plan 👑</h2>
            <p style='color:#EAEAEA;'>Most Popular Choice</p>
            <div class="price-text" style='color:white;'>$79 <span style='font-size:1rem; color:#EAEAEA;'>/ month</span></div>
            <div class="feature-list">
                ⭐ <b>Unlimited Profile Views</b><br>
                ⭐ <b>Advanced AI Matchmaking</b><br>
                ⭐ Direct Messaging & Chat<br>
                ⭐ Access to Wedding Ecosystem<br>
                ⭐ Priority Customer Support
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Upgrade to Platinum", key="plat_btn", type="primary", use_container_width=True):
        with st.spinner("Processing secure payment..."):
            time.sleep(2)
        st.balloons()
        st.success("🎉 Payment Successful! Welcome to Bandhan Platinum.")

# --- Luxury Plan ---
with col3:
    st.markdown("""
        <div class="pricing-card">
            <h2 style='color:#1A365D;'>Imperial Plan</h2>
            <p style='color:gray;'>For the ultimate luxury experience</p>
            <div class="price-text">$199 <span style='font-size:1rem; color:gray;'>/ month</span></div>
            <div class="feature-list">
                💎 Everything in Platinum<br>
                💎 Dedicated Relationship Manager<br>
                💎 10% Discount on Ecosystem Bookings<br>
                💎 Premium Background Verification<br>
                💎 VIP Profile Highlighting
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Select Imperial", key="imp_btn", use_container_width=True):
        st.info("Redirecting to Imperial Checkout...")

st.markdown("<br><hr><p style='text-align:center; color:gray;'>Secure Checkout powered by Stripe. Cancel anytime.</p>", unsafe_allow_html=True)
