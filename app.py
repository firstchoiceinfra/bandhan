import streamlit as st
import base64

# 1. Page Configuration
st.set_page_config(
    page_title="Bandhan | Premium Matrimony & Ecosystem",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. READ LOCAL LOGO (896327.png) AUTOMATICALLY
def get_base64_image(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e:
        return ""

logo_b64 = get_base64_image("896327.png")

# 3. SPLASH SCREEN (NOW DARK & MATCHING WITH SIDEBAR)
st.markdown(f"""
    <style>
    .stApp::after {{
        content: ""; 
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        /* साइडबार की तरह डार्क ब्लू ग्रेडिएंट बैकग्राउंड */
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%); 
        background-image: url("data:image/png;base64,{logo_b64}"); 
        background-repeat: no-repeat;
        background-position: center;
        background-size: 350px; 
        /* लोगो को डार्क स्क्रीन पर चमकाने के लिए चमक (Glow) */
        filter: drop-shadow(0px 0px 12px rgba(255, 255, 255, 0.5));
        z-index: 999999; 
        animation: fadeOutSplash 1.2s ease-in-out forwards; 
    }}

    @keyframes fadeOutSplash {{
        0% {{ opacity: 1; visibility: visible; }}
        65% {{ opacity: 1; visibility: visible; }} 
        100% {{ opacity: 0; visibility: hidden; }} 
    }}
    </style>
""", unsafe_allow_html=True)


# 4. CUSTOM SIDEBAR HTML (Real Logo & Menu Links)
sidebar_html = f"""
    <div class="sidebar-logo-container">
        <img src="data:image/png;base64,{logo_b64}" alt="Bandhan Logo" class="sidebar-main-logo">
    </div>
    <div class="custom-sidebar-menu">
        <a href="/" target="_self" class="custom-menu-item">
            <div class="custom-icon-circle">
                <img src="https://cdn-icons-png.flaticon.com/512/1946/1946488.png" alt="Home">
            </div>
            <div class="custom-menu-text">Home</div>
        </a>
        <a href="Kundli_Match" target="_self" class="custom-menu-item">
            <div class="custom-icon-circle">
                <img src="https://cdn-icons-png.flaticon.com/512/3652/3652191.png" alt="Kundli">
            </div>
            <div class="custom-menu-text">Kundli Match</div>
        </a>
        <a href="Registration" target="_self" class="custom-menu-item">
            <div class="custom-icon-circle">
                <img src="https://cdn-icons-png.flaticon.com/512/2921/2921222.png" alt="Registration">
            </div>
            <div class="custom-menu-text">Registration</div>
        </a>
        <a href="Matchmaking" target="_self" class="custom-menu-item">
            <div class="custom-icon-circle">
                <img src="https://cdn-icons-png.flaticon.com/512/1077/1077035.png" alt="Matchmaking">
            </div>
            <div class="custom-menu-text">Matchmaking</div>
        </a>
        <a href="Wedding_Services" target="_self" class="custom-menu-item">
            <div class="custom-icon-circle">
                <img src="https://cdn-icons-png.flaticon.com/512/3159/3159303.png" alt="Services">
            </div>
            <div class="custom-menu-text">Wedding Services</div>
        </a>
        <a href="Chat_Alerts" target="_self" class="custom-menu-item">
            <div class="custom-icon-circle">
                <img src="https://cdn-icons-png.flaticon.com/512/1380/1380370.png" alt="Chat">
            </div>
            <div class="custom-menu-text">Chat & Alerts</div>
        </a>
    </div>
"""
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)


# 5. POWERFUL PREMIUM CSS (Sidebar Customization)
st.markdown("""
    <style>
    /* HIDE DEFAULT STREAMLIT MENU */
    [data-testid="stSidebarNav"] { display: none !important; }

    /* Main App Background and Font */
    .stApp { background-color: #FAFAFA; font-family: 'Helvetica Neue', sans-serif; }
    
    /* Sidebar Background Gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important;
        border-right: 3px solid #D4AF37 !important;
    }

    /* CUSTOM MENU LOGO STYLING */
    .sidebar-logo-container {
        text-align: center; 
        margin-bottom: 25px; 
        padding-top: 15px;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3); 
        padding-bottom: 15px;
        background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0) 70%);
    }
    
    .sidebar-main-logo {
        max-width: 80%; 
        height: auto;
        object-fit: contain;
        filter: drop-shadow(0px 0px 8px rgba(255, 255, 255, 0.8)); 
    }

    .custom-sidebar-menu { display: flex; flex-direction: column; gap: 12px; }

    .custom-menu-item {
        display: flex; flex-direction: row; align-items: center; justify-content: flex-start; 
        background-color: rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 10px 15px;
        border: 1px solid rgba(212, 175, 55, 0.3); text-decoration: none !important;
        transition: all 0.3s ease-in-out;
    }

    .custom-menu-item:hover {
        background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%);
        transform: translateX(8px); border-color: #FBF5B7; box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4);
    }

    .custom-icon-circle {
        width: 42px; height: 42px; min-width: 42px; background-color: #FFFFFF; 
        border-radius: 50%; display: flex; justify-content: center; align-items: center;
        margin-right: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.2); overflow: hidden; 
    }

    .custom-icon-circle img { width: 28px; height: 28px; object-fit: contain; }

    .custom-menu-text {
        color: #E2E8F0; font-size: 1.05rem; font-weight: 600; font-family: 'Helvetica', sans-serif;
        text-align: left; line-height: 1.2;
    }

    .custom-menu-item:hover .custom-menu-text { color: #0F2027; font-weight: 800; }

    /* PAGE CONTENT STYLING */
    h1 { color: #0F2027; font-weight: 700; letter-spacing: 1px; }
    
    .feature-box {
        background-color: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); text-align: center;
        border-bottom: 4px solid #D4AF37; transition: transform 0.3s ease;
    }
    .feature-box:hover { transform: translateY(-5px); }
    .tagline { font-size: 1.5rem; color: #555555; font-weight: 300; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)


# 6. Hero Section (Top Header & Image)
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


# 7. Features Section (Ecosystem & AI)
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


# 8. Footer Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; color: #888888; padding: 20px;'>
        <p>Bandhan.com © 2026 | Matrimony • Planning • Vendors • Honeymoon</p>
    </div>
""", unsafe_allow_html=True)
