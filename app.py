import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Bandhan | Premium Matrimony & Ecosystem",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="expanded"
)
import streamlit as st

# 1. सबसे पहली लाइन हमेशा page_config की होनी चाहिए
st.set_page_config(
    page_title="Bandhan | Premium Matrimony",
    page_icon="💍",
    layout="wide"
)

# =====================================================================
# 2. <--- यहाँ से आपको अपना वह नया प्रीमियम साइडबार वाला CSS कोड पेस्ट करना है --->
# =====================================================================
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
        position: absolute; right: 20px; top: 15px;
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
    /* Sidebar Background */
    [data-testid="stSidebar"] {{
        background-color: #FFFFFF !important; 
        border-right: 1px solid #EAEAEA !important;
    }}
    
    /* Hide the default Streamlit top header */
    [data-testid="stSidebarNav"]::before {{
        content: "Main Menu"; color: #333; font-size: 1.2rem; font-weight: 900;
        font-family: 'Helvetica', sans-serif; text-align: center; display: block;
        margin-bottom: 20px; padding-top: 20px; border-bottom: 1px solid #EAEAEA; padding-bottom: 15px;
    }}

    /* Container for the links */
    [data-testid="stSidebarNav"] ul {{
        display: flex; flex-direction: column; gap: 5px; padding-top: 10px;
    }}

    /* Main Menu Item Styling (Vertical Layout) */
    [data-testid="stSidebarNav"] a {{
        display: flex !important;
        flex-direction: column !important; 
        align-items: center !important;
        text-align: center !important;
        background-color: transparent !important;
        border: none !important;
        padding: 15px 5px !important;
        position: relative;
    }}

    /* ICON CIRCLE STYLING (Targeting the Emoji) */
    [data-testid="stSidebarNav"] a span:first-child {{
        font-size: 32px !important; 
        background-color: #F4F5F7 !important; 
        width: 65px !important;
        height: 65px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        border-radius: 50% !important; 
        margin-bottom: 8px !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.03) !important;
        transition: transform 0.2s ease;
    }}

    /* TEXT STYLING (Below the icon) */
    [data-testid="stSidebarNav"] a span:last-child {{
        font-size: 13px !important;
        color: #4A4A4A !important;
        font-weight: 600 !important;
        white-space: pre-wrap !important; 
        line-height: 1.2 !important;
        max-width: 90%;
    }}

    /* Hover Effects */
    [data-testid="stSidebarNav"] a:hover span:first-child {{
        transform: scale(1.1); 
        background-color: #E2E8F0 !important;
    }}

    /* Active Page Styling */
    [data-testid="stSidebarNav"] a[aria-current="page"] span:first-child {{
        background-color: #E3F2FD !important; 
        border: 2px solid #1976D2 !important;
    }}
    [data-testid="stSidebarNav"] a[aria-current="page"] span:last-child {{
        color: #1976D2 !important;
        font-weight: 800 !important;
    }}
    
    {badge_css}
    </style>
""", unsafe_allow_html=True)
# =====================================================================
# <--- यहाँ पर प्रीमियम साइडबार का कोड खत्म हो गया --->
# =====================================================================

# 3. इसके नीचे आपके उस पेज का बाकी का नॉर्मल कोड आएगा
# (जैसे Title, Buttons, Tabs, Images आदि)
st.title("Bandhan.com 💍")
st.write("बाकी का पूरा कोड यहाँ रहेगा...")
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
