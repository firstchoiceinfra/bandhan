import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="VIP Membership & Plans | Bandhan",
    page_icon="👑",
    layout="wide"
)
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
# 2. Premium CSS Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #F8F9FA;
    }
    .vip-header {
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        padding: 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
        border: 2px solid #D4AF37;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        margin-bottom: 30px;
    }
    .vip-title {
        font-family: 'Georgia', serif;
        font-size: 3rem;
        font-weight: 900;
        margin: 0;
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .plan-card {
        background: white;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border: 1px solid #EAEAEA;
        border-top: 6px solid #D4AF37;
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    .plan-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(212, 175, 55, 0.25);
    }
    .price-tag {
        font-size: 2.5rem;
        color: #27AE60;
        font-weight: 900;
        margin: 15px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Hero Header
st.markdown("""
<div class="vip-header">
    <h1 class="vip-title">Bandhan VIP & Premium Memberships</h1>
    <p style="font-size:1.2rem; margin-top:15px; color:#FBF5B7; font-style:italic;">Upgrade your account to unlock direct phone numbers, unlimited secure chats, verified badges, and priority matching.</p>
</div>
""", unsafe_allow_html=True)

# 4. Three-Column Membership Plans Layout
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="plan-card">
        <h3>🥉 Silver VIP</h3>
        <p style="color:gray;">Essential features for quick matching</p>
        <div class="price-tag">₹ 2,999</div>
        <p style="font-size:0.9rem; color:#555;">Valid for 3 Months</p>
        <hr>
        <p style="text-align:left;">
        ✅ View 50 Verified Phone Numbers<br>
        ✅ Send 100 Direct Messages<br>
        ✅ Basic Profile Trust Badge<br>
        ❌ Dedicated Relationship Manager
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Choose Silver Plan", key="p1", use_container_width=True):
        st.success("🎉 Silver VIP Selected! Redirecting to secure payment gateway...")

with col2:
    st.markdown("""
    <div class="plan-card" style="border-top: 6px solid #1A365D;">
        <h3>🥇 Gold VIP (Most Popular)</h3>
        <p style="color:gray;">Best value for serious matchmaking</p>
        <div class="price-tag">₹ 5,999</div>
        <p style="font-size:0.9rem; color:#555;">Valid for 6 Months</p>
        <hr>
        <p style="text-align:left;">
        ✅ Unlimited Phone Numbers & Calls<br>
        ✅ Unlimited Direct Live Chat<br>
        ✅ Gold Verified Trust Badge<br>
        ✅ Profile Highlight in Search Results
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Choose Gold Plan", key="p2", type="primary", use_container_width=True):
        st.balloons()
        st.success("🎉 Gold VIP Selected! Premium benefits unlocked successfully.")

with col3:
    st.markdown("""
    <div class="plan-card" style="border-top: 6px solid #E74C3C;">
        <h3>💎 Diamond Elite</h3>
        <p style="color:gray;">Personalized matchmaking & luxury service</p>
        <div class="price-tag">₹ 11,999</div>
        <p style="font-size:0.9rem; color:#555;">Valid for 1 Year</p>
        <hr>
        <p style="text-align:left;">
        ✅ Dedicated Relationship Manager<br>
        ✅ Hand-picked Verified Matches<br>
        ✅ Complete Privacy Shield<br>
        ✅ Wedding Planning Assistance
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Choose Diamond Plan", key="p3", use_container_width=True):
        st.success("🎉 Diamond Elite Selected! Our senior relationship manager will contact you shortly.")
