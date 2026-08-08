import streamlit as st
import pandas as pd
import numpy as np
import base64

# =====================================================================
# 1. PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Admin Dashboard | Bandhan",
    page_icon="📊",
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
    .stApp { background-color: #F4F6F9 !important; font-family: 'Helvetica Neue', sans-serif; }
    
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
    
    /* Admin Dashboard Specific Styles */
    .admin-header { color: #1A365D; font-family: 'Helvetica Neue', sans-serif; font-weight: 900; font-size: 2.5rem; margin-bottom: 0px; }
    .metric-card { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-top: 4px solid #D4AF37; }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 6. PAGE CONTENT (Admin Dashboard)
# =====================================================================
st.markdown("<h1 class='admin-header'>📊 Admin Control Center</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #666;'>Real-time overview of platform activity, user registrations, and ecosystem revenue.</p>", unsafe_allow_html=True)
st.markdown("---")

# Key Metrics (Top Row)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="👥 Total Users", value="12,543", delta="+324 this week")
with col2:
    st.metric(label="💎 Premium Members", value="3,210", delta="+85 this week")
with col3:
    st.metric(label="🛍️ Active Vendors", value="450", delta="+12 this week")
with col4:
    st.metric(label="💰 Ecosystem Revenue", value="$45,230", delta="+$4,500 this week")

st.markdown("<br><br>", unsafe_allow_html=True)

# Charts Section (Data Visualization)
chart_col1, chart_col2 = st.columns(2, gap="large")

with chart_col1:
    st.markdown("### 📈 User Growth (Last 7 Days)")
    # Mock data for line chart
    chart_data = pd.DataFrame(
        np.random.randint(150, 300, size=(7, 1)), 
        columns=["New Registrations"],
        index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    )
    st.line_chart(chart_data)

with chart_col2:
    st.markdown("### 🛍️ Top Ecosystem Bookings")
    # Mock data for bar chart
    services_data = pd.DataFrame({
        "Bookings": [120, 95, 150, 80]
    }, index=["Venues", "Luxury Rides", "Apparel", "Honeymoons"])
    st.bar_chart(services_data)

st.markdown("---")

# Recent Registrations Table
st.markdown("### 📋 Recent User Registrations")

# Mock Database Table
recent_users = pd.DataFrame({
    "User ID": ["#BND-1042", "#BND-1043", "#BND-1044", "#BND-1045", "#BND-1046"],
    "Name": ["Aarav Patel", "Priya Sharma", "Rohan Desai", "Neha Singh", "Vikram Rao"],
    "Age": [28, 26, 30, 27, 29],
    "Location": ["Mumbai, IN", "Delhi, IN", "London, UK", "Dubai, UAE", "New York, USA"],
    "Plan": ["Premium", "Free", "Free", "Premium", "Premium"],
    "Status": ["Verified ✅", "Pending ⏳", "Verified ✅", "Verified ✅", "Pending ⏳"]
})

# Displaying table with Streamlit's native dataframe UI
st.dataframe(recent_users, use_container_width=True, hide_index=True)

st.markdown("<br>", unsafe_allow_html=True)
st.button("📥 Download Full Report (CSV)", type="primary")
