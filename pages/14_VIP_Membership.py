import streamlit as st
import time

# Page Config
st.set_page_config(page_title="VIP Membership | Bandhan", page_icon="👑", layout="wide")

# CSS Styling
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    .vip-header {
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        padding: 40px; border-radius: 20px; color: white; text-align: center;
        border: 2px solid #D4AF37; box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        margin-bottom: 30px;
    }
    .vip-title {
        font-family: 'Georgia', serif; font-size: 3rem; font-weight: 900; margin: 0;
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .plan-card {
        background: white; border-radius: 15px; padding: 30px; text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08); border: 1px solid #EAEAEA;
        border-top: 6px solid #D4AF37; transition: transform 0.3s ease;
    }
    .plan-card:hover { transform: translateY(-8px); box-shadow: 0 15px 30px rgba(212, 175, 55, 0.25); }
    .price-tag { font-size: 2.5rem; color: #27AE60; font-weight: 900; margin: 15px 0; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="vip-header">
    <h1 class="vip-title">Bandhan VIP Memberships</h1>
    <p style="font-size:1.2rem; margin-top:15px; color:#FBF5B7; font-style:italic;">Upgrade to VIP to unlock direct phone numbers, unlimited chats, and profile booster.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="plan-card">
        <h3>🥉 Silver VIP</h3>
        <p style="color:gray;">Essential features for quick matching</p>
        <div class="price-tag">₹ 2,999</div>
        <p style="font-size:0.9rem; color:#555;">Valid for 3 Months</p>
        <hr>
        <p style="text-align:left;">✅ View 50 Verified Phone Numbers<br>✅ Send 100 Direct Messages<br>✅ Basic Profile Badge<br>❌ Dedicated Relationship Manager</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Choose Silver Plan", key="p1", use_container_width=True):
        st.success("🎉 Silver VIP Selected! Redirecting to secure payment...")

with col2:
    st.markdown("""
    <div class="plan-card" style="border-top: 6px solid #1A365D;">
        <h3>🥇 Gold VIP (Most Popular)</h3>
        <p style="color:gray;">Best value for serious matchmaking</p>
        <div class="price-tag">₹ 5,999</div>
        <p style="font-size:0.9rem; color:#555;">Valid for 6 Months</p>
        <hr>
        <p style="text-align:left;">✅ Unlimited Phone Numbers<br>✅ Unlimited Direct Chat & Calls<br>✅ Gold Verified Trust Badge<br>✅ Profile Highlight in Search</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Choose Gold Plan", key="p2", type="primary", use_container_width=True):
        st.balloons()
        st.success("🎉 Gold VIP Selected! Premium benefits unlocked.")

with col3:
    st.markdown("""
    <div class="plan-card" style="border-top: 6px solid #E74C3C;">
        <h3>💎 Diamond Elite</h3>
        <p style="color:gray;">Personalized matchmaking & luxury service</p>
        <div class="price-tag">₹ 11,999</div>
        <p style="font-size:0.9rem; color:#555;">Valid for 1 Year</p>
        <hr>
        <p style="text-align:left;">✅ Dedicated Relationship Manager<br>✅ Hand-picked Verified Matches<br>✅ Complete Privacy Shield<br>✅ Wedding Planning Assistance</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Choose Diamond Plan", key="p3", use_container_width=True):
        st.success("🎉 Diamond Elite Selected! Our manager will contact you.")
