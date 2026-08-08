import streamlit as st
import base64

# =====================================================================
# 1. 🔥 ANTI-FLASH & HIDE DEFAULT NAVIGATION (Must be at the very top) 🔥
# =====================================================================
st.markdown("""
    <style>
    /* Streamlit के पुराने डिफ़ॉल्ट नेविगेशन को पूरी तरह छिपाना */
    [data-testid="stSidebarNav"] { display: none !important; }
    
    /* पेज लोड होने तक पूरे ऐप को छिपाएं ताकि सफेद फ्लैश न दिखे */
    .stApp { opacity: 0; animation: fadeIn 0.4s ease-in forwards; }
    @keyframes fadeIn { to { opacity: 1; } }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 2. PAGE CONFIGURATION (सिर्फ एक बार इस्तेमाल होगा)
# =====================================================================
st.set_page_config(
    page_title="Bandhan | Premium Matrimony & Ecosystem",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# 3. 🔥 DARK PREMIUM SPLASH SCREEN (WITH LOCAL LOGO) 🔥
# =====================================================================
def get_base64_image(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e:
        return ""

logo_b64 = get_base64_image("896327.png")

st.markdown(f"""
    <style>
    .stApp::after {{
        content: ""; 
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%); 
        background-image: url("data:image/png;base64,{logo_b64}"); 
        background-repeat: no-repeat;
        background-position: center;
        background-size: 350px; 
        filter: drop-shadow(0px 0px 12px rgba(255, 255, 255, 0.5));
        z-index: 9999999; 
        animation: fadeOutSplash 1.2s ease-in-out forwards; 
    }}
    @keyframes fadeOutSplash {{
        0% {{ opacity: 1; visibility: visible; }}
        70% {{ opacity: 1; visibility: visible; }} 
        100% {{ opacity: 0; visibility: hidden; pointer-events: none; }} 
    }}
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 4. 🔥 CUSTOM IMAGE-BASED SIDEBAR MENU (आपका ओरिजिनल HTML) 🔥
# =====================================================================

# Unread Messages Badge Logic (Your original logic)
if 'unread_msgs' not in st.session_state:
    st.session_state.unread_msgs = 2 

sidebar_html = """
<div class="app-sidebar-menu">
    <!-- Top Custom Title for Sidebar -->
    <div style="color: #D4AF37; font-size: 1.8rem; font-weight: 900; font-family: 'Georgia', serif; text-align: center; margin-bottom: 20px; border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 15px;">
        👑 Bandhan Menu
    </div>

    <!-- 1. Kundli Match -->
    <a href="Kundli_Match" target="_self" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/3652/3652191.png" alt="Kundli">
        </div>
        <div class="menu-text" style="color: #E2E8F0;">Kundli Match</div>
    </a>
    
    <!-- 2. Registration -->
    <a href="Registration" target="_self" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/2921/2921222.png" alt="Registration">
        </div>
        <div class="menu-text" style="color: #E2E8F0;">Registration</div>
    </a>
    
    <!-- 3. Matchmaking -->
    <a href="Matchmaking" target="_self" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/1077/1077035.png" alt="Matchmaking">
        </div>
        <div class="menu-text" style="color: #E2E8F0;">Matchmaking</div>
    </a>

    <!-- 4. Wedding Services -->
    <a href="Wedding_Services" target="_self" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/3159/3159303.png" alt="Services">
        </div>
        <div class="menu-text" style="color: #E2E8F0;">Wedding Services</div>
    </a>
    
    <!-- 5. Verification KYC -->
    <a href="Verification_KYC" target="_self" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/6928/6928929.png" alt="KYC">
        </div>
        <div class="menu-text" style="color: #E2E8F0;">Verification KYC</div>
    </a>
</div>
"""

# इसे साइडबार में प्रिंट करना
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)


# =====================================================================
# 5. POWERFUL PREMIUM CSS (आपका ओरिजिनल CSS)
# =====================================================================
st.markdown("""
    <style>
    /* Main Background and Font */
    .stApp {
        background-color: #FAFAFA;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* 1. Sidebar Background Gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important;
        border-right: 3px solid #D4AF37 !important;
    }

    /* 2. Custom Sidebar Menu CSS */
    .app-sidebar-menu {
        display: flex;
        flex-direction: column;
        gap: 20px;
        padding-top: 5px;
        align-items: center;
    }
    .menu-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-decoration: none !important;
        transition: transform 0.2s, background 0.3s;
        cursor: pointer;
        width: 90%;
        padding: 10px;
        border-radius: 12px;
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(212, 175, 55, 0.2);
    }
    .menu-item:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%);
        border-color: #FBF5B7;
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4);
    }
    .menu-item:hover .menu-text {
        color: #0F2027 !important;
        font-weight: 900 !important;
    }
    .icon-circle {
        width: 65px;
        height: 65px;
        background-color: #FFFFFF; 
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .icon-circle img {
        width: 38px;
        height: 38px;
        object-fit: contain;
    }
    .menu-text {
        font-size: 0.95rem;
        font-weight: 700;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        letter-spacing: 0.5px;
        transition: color 0.3s;
    }

    /* 3. Heading Style */
    h1 {
        color: #0F2027;
        font-weight: 700;
        letter-spacing: 1px;
    }
    
    /* 4. Premium Cards */
    .feature-box {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        text-align: center;
        border-bottom: 4px solid #D4AF37;
        transition: transform 0.3s ease;
    }
    .feature-box:hover {
        transform: translateY(-5px);
    }
    .tagline {
        font-size: 1.5rem;
        color: #555555;
        font-weight: 300;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 6. APP CONTENT (आपका ओरिजिनल होम पेज)
# =====================================================================

# Hero Section (Top Header & Image)
col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title("Bandhan.com 💍")
    st.markdown("""
        <p class="tagline">
        <b>Traditional Roots, Modern Approach.</b><br>
        The world's first AI-powered matrimonial platform and complete wedding ecosystem. <br>
        From finding the perfect life partner to wedding venues and honeymoons—everything in one place.
        </p>
    """, unsafe_allow_html=True)
    
    st.button("Create Your Premium Profile (Free)", type="primary", use_container_width=True)

with col2:
    st.image(
        "https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=800&q=80", 
        caption="The Perfect Match Awaits", 
        use_container_width=True
    )

st.markdown("<hr style='border: 1px solid #EAEAEA;'>", unsafe_allow_html=True)

# Features Section (Ecosystem & AI)
st.markdown("<h2 style='text-align: center; color: #1A365D;'>The Bandhan Ecosystem</h2><br>", unsafe_allow_html=True)

f_col1, f_col2, f_col3 = st.columns(3, gap="medium")

with f_col1:
    st.image("https://images.unsplash.com/photo-1573164713988-8665fc963095?auto=format&fit=crop&w=500&q=80", use_container_width=True)
    st.markdown("""
        <div class="feature-box">
            <h3 style='color:#D4AF37;'>🤖 AI Matchmaking</h3>
            <p>Our smart AI technology analyzes your personality, preferences, and habits to suggest the most accurate and highly compatible matches.</p>
        </div>
    """, unsafe_allow_html=True)

with f_col2:
    st.image("https://images.unsplash.com/photo-1519225421980-715cb0215aed?auto=format&fit=crop&w=500&q=80", use_container_width=True)
    st.markdown("""
        <div class="feature-box">
            <h3 style='color:#D4AF37;'>🛍️ Complete Ecosystem</h3>
            <p>Designer bridal wear, luxury cars, banquet halls, and premium catering. Our verified vendors cover every single wedding need.</p>
        </div>
    """, unsafe_allow_html=True)

with f_col3:
    st.image("https://images.unsplash.com/photo-1520854221256-17451cc331bf?auto=format&fit=crop&w=500&q=80", use_container_width=True)
    st.markdown("""
        <div class="feature-box">
            <h3 style='color:#D4AF37;'>🔒 100% Secure</h3>
            <p>Strict Identity Verification. Your personal information and photos are completely secure, giving you full control over your privacy.</p>
        </div>
    """, unsafe_allow_html=True)

# Footer Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; color: #888888; padding: 20px;'>
        <p>Bandhan.com © 2026 | Matrimony • Planning • Vendors • Honeymoon</p>
    </div>
""", unsafe_allow_html=True)
