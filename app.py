import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Bandhan | Premium Matrimony & Ecosystem",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="expanded"
)
import streamlit as st

# --- NEW PREMIUM SIDEBAR CSS (Left Icon, Right Text) ---
if 'unread_msgs' not in st.session_state:
    st.session_state.unread_msgs = 2 

badge_css = ""
if st.session_state.unread_msgs > 0:
    badge_css = f"""
    [data-testid="stSidebarNav"] a[href*="Chat_Alerts"]::after,
    [data-testid="stSidebarNav"] a[href*="chat_alerts"]::after {{
        content: "{st.session_state.unread_msgs}";
        background-color: #FF2A2A !important; color: white !important;
        font-size: 0.85rem !important; font-weight: 900 !important;
        border-radius: 50% !important; min-width: 22px; height: 22px;
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
    /* 1. Sidebar Background (Dark Royal Blue) */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important;
        border-right: 3px solid #D4AF37 !important;
    }}
    
    /* 2. Top Custom Title for Sidebar */
    [data-testid="stSidebarNav"]::before {{
        content: "👑 Bandhan Menu";
        color: #D4AF37; font-size: 1.8rem; font-weight: 900;
        font-family: 'Georgia', serif; text-align: center; display: block;
        margin-bottom: 25px; padding-top: 20px;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 15px;
    }}

    /* 3. Main Menu Item Styling (HORIZONTAL LAYOUT) */
    [data-testid="stSidebarNav"] a {{
        display: flex !important;
        flex-direction: row !important; /* Left to Right */
        align-items: center !important; /* Vertically center */
        justify-content: flex-start !important; /* Align to Left */
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
        margin: 10px 15px !important;
        padding: 10px 15px !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        transition: all 0.3s ease-in-out !important;
        position: relative;
        text-decoration: none !important;
    }}

    /* 4. ICON CIRCLE STYLING (Left Side) */
    [data-testid="stSidebarNav"] a span:first-child {{
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 42px !important;
        height: 42px !important;
        min-width: 42px !important; /* Prevent squeezing */
        background-color: #FFFFFF !important; /* White circle background */
        border-radius: 50% !important; /* Perfect circle */
        font-size: 20px !important; /* Emoji size */
        margin-right: 15px !important; /* Gap between circle and text */
        box-shadow: 0 4px 6px rgba(0,0,0,0.2) !important;
    }}

    /* 5. TEXT STYLING (Right Side) */
    [data-testid="stSidebarNav"] a span:last-child {{
        color: #E2E8F0 !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        font-family: 'Helvetica', sans-serif !important;
        text-align: left !important;
        white-space: normal !important; /* Allow text to wrap if it's long */
        line-height: 1.2 !important;
    }}

    /* 6. Hover Effects */
    [data-testid="stSidebarNav"] a:hover {{
        background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%) !important;
        transform: translateX(8px) !important;
        border-color: #FBF5B7 !important;
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4) !important;
    }}
    
    [data-testid="stSidebarNav"] a:hover span:last-child {{
        color: #0F2027 !important;
        font-weight: 800 !important;
    }}

    /* 7. Active Page Styling */
    [data-testid="stSidebarNav"] a[aria-current="page"] {{
        background: linear-gradient(135deg, #D4AF37 0%, #AA771C 100%) !important;
        box-shadow: 0 5px 20px rgba(212, 175, 55, 0.6) !important;
        border: 2px solid #FBF5B7 !important;
    }}
    
    [data-testid="stSidebarNav"] a[aria-current="page"] span:last-child {{
        color: #0F2027 !important;
        font-weight: 900 !important;
    }}
    
    {badge_css}
    </style>
""", unsafe_allow_html=True)
import streamlit as st

# --- NEW PREMIUM SIDEBAR CSS (Left Icon, Right Text) ---
if 'unread_msgs' not in st.session_state:
    st.session_state.unread_msgs = 2 

badge_css = ""
if st.session_state.unread_msgs > 0:
    badge_css = f"""
    [data-testid="stSidebarNav"] a[href*="Chat_Alerts"]::after,
    [data-testid="stSidebarNav"] a[href*="chat_alerts"]::after {{
        content: "{st.session_state.unread_msgs}";
        background-color: #FF2A2A !important; color: white !important;
        font-size: 0.85rem !important; font-weight: 900 !important;
        border-radius: 50% !important; min-width: 22px; height: 22px;
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
    /* 1. Sidebar Background (Dark Royal Blue) */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important;
        border-right: 3px solid #D4AF37 !important;
    }}
    
    /* 2. Top Custom Title for Sidebar */
    [data-testid="stSidebarNav"]::before {{
        content: "👑 Bandhan Menu";
        color: #D4AF37; font-size: 1.8rem; font-weight: 900;
        font-family: 'Georgia', serif; text-align: center; display: block;
        margin-bottom: 25px; padding-top: 20px;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 15px;
    }}

    /* 3. Main Menu Item Styling (HORIZONTAL LAYOUT) */
    [data-testid="stSidebarNav"] a {{
        display: flex !important;
        flex-direction: row !important; /* Left to Right */
        align-items: center !important; /* Vertically center */
        justify-content: flex-start !important; /* Align to Left */
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
        margin: 10px 15px !important;
        padding: 10px 15px !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        transition: all 0.3s ease-in-out !important;
        position: relative;
        text-decoration: none !important;
    }}

    /* 4. ICON CIRCLE STYLING (Left Side) */
    [data-testid="stSidebarNav"] a span:first-child {{
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 42px !important;
        height: 42px !important;
        min-width: 42px !important; /* Prevent squeezing */
        background-color: #FFFFFF !important; /* White circle background */
        border-radius: 50% !important; /* Perfect circle */
        font-size: 20px !important; /* Emoji size */
        margin-right: 15px !important; /* Gap between circle and text */
        box-shadow: 0 4px 6px rgba(0,0,0,0.2) !important;
    }}

    /* 5. TEXT STYLING (Right Side) */
    [data-testid="stSidebarNav"] a span:last-child {{
        color: #E2E8F0 !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        font-family: 'Helvetica', sans-serif !important;
        text-align: left !important;
        white-space: normal !important; /* Allow text to wrap if it's long */
        line-height: 1.2 !important;
    }}

    /* 6. Hover Effects */
    [data-testid="stSidebarNav"] a:hover {{
        background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%) !important;
        transform: translateX(8px) !important;
        border-color: #FBF5B7 !important;
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4) !important;
    }}
    
    [data-testid="stSidebarNav"] a:hover span:last-child {{
        color: #0F2027 !important;
        font-weight: 800 !important;
    }}

    /* 7. Active Page Styling */
    [data-testid="stSidebarNav"] a[aria-current="page"] {{
        background: linear-gradient(135deg, #D4AF37 0%, #AA771C 100%) !important;
        box-shadow: 0 5px 20px rgba(212, 175, 55, 0.6) !important;
        border: 2px solid #FBF5B7 !important;
    }}
    
    [data-testid="stSidebarNav"] a[aria-current="page"] span:last-child {{
        color: #0F2027 !important;
        font-weight: 900 !important;
    }}
    
    {badge_css}
    </style>
""", unsafe_allow_html=True)import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Bandhan App", layout="wide")

# =====================================================================
# 2. 🔥 CUSTOM IMAGE-BASED SIDEBAR MENU (Like the Photo) 🔥
# =====================================================================

st.markdown("""
    <style>
    /* Streamlit के पुराने डिफॉल्ट मेन्यू को छिपाना */
    [data-testid="stSidebarNav"] { display: none !important; }
    
    /* नए मेन्यू का CSS डिजाइन (गोल फोटो और टेक्स्ट नीचे) */
    .app-sidebar-menu {
        display: flex;
        flex-direction: column;
        gap: 25px;
        padding-top: 10px;
        align-items: center;
    }
    .menu-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-decoration: none !important;
        color: #1A365D !important;
        transition: transform 0.2s;
        cursor: pointer;
        width: 100%;
    }
    .menu-item:hover {
        transform: scale(1.05); /* माउस ले जाने पर थोड़ा बड़ा होगा */
    }
    .icon-circle {
        width: 75px;
        height: 75px;
        background-color: #F4F6F9; /* फोटो के पीछे का हल्का ग्रे बैकग्राउंड */
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 8px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: 1px solid #EAEAEA;
    }
    .icon-circle img {
        width: 45px;
        height: 45px;
        object-fit: contain;
    }
    .menu-text {
        font-size: 0.95rem;
        font-weight: 700;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# 3. HTML कोड जिसमें हर पेज का लिंक और फोटो (Icon URL) है
sidebar_html = """
<div class="app-sidebar-menu">

    <!-- 1. Kundli Match -->
    <a href="Kundli_Match" target="_self" class="menu-item">
        <div class="icon-circle">
            <!-- यहाँ आप अपनी पसंद की PNG फोटो का लिंक डाल सकते हैं -->
            <img src="https://cdn-icons-png.flaticon.com/512/3652/3652191.png" alt="Kundli">
        </div>
        <div class="menu-text">Kundli Match</div>
    </a>
    
    <!-- 2. Registration -->
    <a href="Registration" target="_self" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/2921/2921222.png" alt="Registration">
        </div>
        <div class="menu-text">Registration</div>
    </a>
    
    <!-- 3. Matchmaking -->
    <a href="Matchmaking" target="_self" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/1077/1077035.png" alt="Matchmaking">
        </div>
        <div class="menu-text">Matchmaking</div>
    </a>

    <!-- 4. Wedding Services -->
    <a href="Wedding_Services" target="_self" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/3159/3159303.png" alt="Services">
        </div>
        <div class="menu-text">Wedding Services</div>
    </a>
    
    <!-- 5. Verification KYC -->
    <a href="Verification_KYC" target="_self" class="menu-item">
        <div class="icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/6928/6928929.png" alt="KYC">
        </div>
        <div class="menu-text">Verification KYC</div>
    </a>

</div>
"""

# इसे साइडबार में प्रिंट करना
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)
# =====================================================================
# 2. POWERFUL PREMIUM CSS (Forceful override for Sidebar)
st.markdown("""
    <style>
    /* Main Background and Font */
    .stApp {
        background-color: #FAFAFA;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* ---------------------------------------------------
       🔥 EXTREME SIDEBAR STYLING (OVERRIDES DEFAULT) 🔥
       --------------------------------------------------- */
       
    /* 1. Sidebar Background Gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important;
        border-right: 3px solid #D4AF37 !important;
    }

    /* 2. Top Custom Title for Sidebar */
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

    /* 3. Style Every Page Link like a Premium Button */
    [data-testid="stSidebarNav"] a {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
        margin: 8px 15px !important;
        padding: 12px !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        transition: all 0.3s ease-in-out !important;
    }
    
    /* Text Color inside Links */
    [data-testid="stSidebarNav"] span {
        color: #E2E8F0 !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        font-family: 'Helvetica', sans-serif !important;
        letter-spacing: 0.5px !important;
    }

    /* 4. Hover Effect - When mouse goes over the button */
    [data-testid="stSidebarNav"] a:hover {
        background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%) !important;
        transform: translateX(8px) !important; /* Button moves slightly right */
        border-color: #FBF5B7 !important;
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4) !important;
    }
    
    /* Change text color on hover */
    [data-testid="stSidebarNav"] a:hover span {
        color: #0F2027 !important;
        font-weight: 800 !important;
    }

    /* 5. Active/Selected Page Styling (Currently open page) */
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: linear-gradient(135deg, #D4AF37 0%, #AA771C 100%) !important;
        box-shadow: 0 5px 20px rgba(212, 175, 55, 0.6) !important;
        border: 2px solid #FBF5B7 !important;
    }
    
    /* Active Page Text */
    [data-testid="stSidebarNav"] a[aria-current="page"] span {
        color: #0F2027 !important;
        font-weight: 900 !important;
    }
    /* --------------------------------------------------- */

    /* Heading Style */
    h1 {
        color: #0F2027;
        font-weight: 700;
        letter-spacing: 1px;
    }
    
    /* Premium Cards */
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

# 3. Hero Section (Top Header & Image)
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

# 4. Features Section (Ecosystem & AI)
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

# 5. Footer Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; color: #888888; padding: 20px;'>
        <p>Bandhan.com © 2026 | Matrimony • Planning • Vendors • Honeymoon</p>
    </div>
""", unsafe_allow_html=True)
