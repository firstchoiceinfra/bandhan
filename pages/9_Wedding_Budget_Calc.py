import streamlit as st
import time
import base64

# =====================================================================
# 1. PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Wedding Budget | Bandhan",
    page_icon="💰",
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
    .stApp { background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%) !important; font-family: 'Helvetica Neue', sans-serif; }
    
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
    
    /* Budget Specific Styles */
    .premium-title-container { background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%); padding: 30px 20px; border-radius: 20px; text-align: center; box-shadow: 0 15px 35px rgba(0,0,0,0.2); border: 2px solid #D4AF37; margin-bottom: 30px; }
    .title-flex { display: flex; justify-content: center; align-items: center; gap: 20px; flex-wrap: wrap; }
    .premium-title { font-family: 'Georgia', serif; font-size: 3.5rem; font-weight: 900; margin: 0; background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: 2px; text-transform: uppercase; }
    .inner-sticker { width: 75px; filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.4)); }
    .step-header { background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%); color: white; padding: 12px 20px; border-radius: 12px; font-size: 1.4rem; font-weight: bold; display: flex; align-items: center; gap: 15px; margin-bottom: 15px; border-left: 6px solid #D4AF37; box-shadow: 0 6px 15px rgba(0,0,0,0.1); }
    .step-icon { width: 35px; height: 35px; }
    .total-box { background: linear-gradient(135deg, #D4AF37 0%, #AA771C 100%); color: white; padding: 20px; border-radius: 12px; text-align: center; font-size: 2.2rem; font-weight: bold; box-shadow: 0 10px 20px rgba(212, 175, 55, 0.3); text-shadow: 1px 1px 2px rgba(0,0,0,0.2); }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 6. PAGE CONTENT (Budget Calculator)
# =====================================================================

# The Attractive Header Section
st.markdown("""
<div class="premium-title-container">
<div class="title-flex">
<img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" class="inner-sticker">
<h1 class="premium-title">Wedding Budget</h1>
<img src="https://cdn-icons-png.flaticon.com/512/2953/2953363.png" class="inner-sticker">
</div>
<p style="color:#FBF5B7; font-size:1.2rem; margin-top:10px; font-style:italic;">Plan Your Dream Royal Wedding Flawlessly</p>
</div>
""", unsafe_allow_html=True)

# Budget Input Section
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    # Step 1
    st.markdown("""
    <div class="step-header">
    <img src="https://cdn-icons-png.flaticon.com/512/5501/5501375.png" class="step-icon">
    Step 1: Set Total Budget
    </div>
    """, unsafe_allow_html=True)
    total_budget = st.number_input("Enter Amount (in INR ₹)", min_value=100000, max_value=50000000, value=2500000, step=50000)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Step 2
    st.markdown("""
    <div class="step-header">
    <img src="https://cdn-icons-png.flaticon.com/512/3126/3126647.png" class="step-icon">
    Step 2: Guest Count
    </div>
    """, unsafe_allow_html=True)
    guests = st.slider("Estimated Number of Guests", 50, 2000, 500)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("🔄 Recalculate Plan", type="primary", use_container_width=True)

with col2:
    st.markdown(f"<div class='total-box'>Grand Total: ₹ {total_budget:,.0f}</div><br>", unsafe_allow_html=True)
    
    # Logic for Budget Breakdown
    venue_cat = int(total_budget * 0.40)
    jewelry = int(total_budget * 0.25)
    apparel = int(total_budget * 0.15)
    photo_misc = int(total_budget * 0.20)
    
    # Custom Function to Create Premium Image Cards
    def create_budget_card(title, amount, percentage, img_url, color):
        return f"""
        <div style="display:flex; background:white; border-radius:15px; margin-bottom:15px; box-shadow:0 8px 20px rgba(0,0,0,0.06); overflow:hidden; border:1px solid #EAEAEA; border-left:6px solid {color}; transition: transform 0.3s;">
            <img src="{img_url}" style="width:140px; object-fit:cover;">
            <div style="padding:15px; width:100%; display:flex; flex-direction:column; justify-content:center;">
                <h4 style="margin:0; color:#1A365D; font-size:1.1rem;">{title} ({percentage}%)</h4>
                <h2 style="margin:5px 0; color:#27AE60; font-weight:800;">₹ {amount:,.0f}</h2>
                <div style="background:#F0F0F0; border-radius:10px; height:8px; width:100%; margin-top:5px;">
                    <div style="background:{color}; width:{percentage}%; height:100%; border-radius:10px;"></div>
                </div>
            </div>
        </div>
        """

    # 1. Venue & Catering Card
    st.markdown(create_budget_card(
        "🏰 Venue & Premium Catering", venue_cat, 40, 
        "https://images.unsplash.com/photo-1519225421980-715cb0215aed?auto=format&fit=crop&w=400&q=80", 
        "#D4AF37"
    ), unsafe_allow_html=True)
    
    # 2. Jewelry Card (Fixed Image URL)
    st.markdown(create_budget_card(
        "💍 Wedding Jewelry & Ornaments", jewelry, 25, 
        "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=400&q=80", 
        "#8E44AD"
    ), unsafe_allow_html=True)
    
    # 3. Designer Apparel Card
    st.markdown(create_budget_card(
        "👗 Designer Apparel & Styling", apparel, 15, 
        "https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=400&q=80", 
        "#E74C3C"
    ), unsafe_allow_html=True)
    
    # 4. Photography & Music Card
    st.markdown(create_budget_card(
        "📸 Photography, Music & Misc", photo_misc, 20, 
        "https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=400&q=80", 
        "#2980B9"
    ), unsafe_allow_html=True)
