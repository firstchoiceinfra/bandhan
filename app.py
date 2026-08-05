import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Bandhan | Premium Matrimony",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# 2. 🔥 CUSTOM IMAGE-BASED SIDEBAR MENU (Real Photos + Text) 🔥
# =====================================================================

st.markdown("""
    <style>
    /* Main App Background */
    .stApp {
        background-color: #FAFAFA;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* 1. Hide Streamlit's Default Menu Completely */
    [data-testid="stSidebarNav"] { 
        display: none !important; 
    }
    
    /* 2. Sidebar Background (Dark Royal Blue) */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important;
        border-right: 3px solid #D4AF37 !important;
    }

    /* 3. Top Custom Title for Sidebar */
    .sidebar-title {
        color: #D4AF37; font-size: 1.8rem; font-weight: 900;
        font-family: 'Georgia', serif; text-align: center; display: block;
        margin-bottom: 25px; padding-top: 20px;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 15px;
    }

    /* 4. Custom Menu Container */
    .custom-sidebar-menu {
        display: flex;
        flex-direction: column;
        gap: 12px;
        padding: 0 10px;
    }

    /* 5. Menu Item Styling (HORIZONTAL LAYOUT) */
    .custom-menu-item {
        display: flex;
        flex-direction: row; /* Left to Right */
        align-items: center; /* Vertically center */
        justify-content: flex-start; 
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 10px 15px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        text-decoration: none !important;
        transition: all 0.3s ease-in-out;
    }

    /* 6. Hover Effects */
    .custom-menu-item:hover {
        background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%);
        transform: translateX(8px);
        border-color: #FBF5B7;
        box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4);
    }

    /* 7. ICON CIRCLE STYLING (Left Side for Real Images) */
    .custom-icon-circle {
        width: 42px;
        height: 42px;
        min-width: 42px;
        background-color: #FFFFFF; /* White circle background */
        border-radius: 50%; /* Perfect circle */
        display: flex;
        justify-content: center;
        align-items: center;
        margin-right: 15px; /* Gap between circle and text */
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        overflow: hidden; /* Keeps image inside the circle */
    }

    /* 8. Image inside the circle */
    .custom-icon-circle img {
        width: 28px; /* Size of the image inside circle */
        height: 28px;
        object-fit: contain;
    }

    /* 9. TEXT STYLING (Right Side) */
    .custom-menu-text {
        color: #E2E8F0;
        font-size: 1.05rem;
        font-weight: 600;
        font-family: 'Helvetica', sans-serif;
        text-align: left;
        line-height: 1.2;
    }

    .custom-menu-item:hover .custom-menu-text {
        color: #0F2027;
        font-weight: 800;
    }
    </style>
""", unsafe_allow_html=True)

# 3. HTML Code for the Sidebar with Real Images
sidebar_html = """
<div class="sidebar-title">👑 Bandhan Menu</div>
<div class="custom-sidebar-menu">

    <!-- 1. Home / App -->
    <a href="/" target="_self" class="custom-menu-item">
        <div class="custom-icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/1946/1946488.png" alt="Home">
        </div>
        <div class="custom-menu-text">Home</div>
    </a>

    <!-- 2. Kundli Match -->
    <a href="Kundli_Match" target="_self" class="custom-menu-item">
        <div class="custom-icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/3652/3652191.png" alt="Kundli">
        </div>
        <div class="custom-menu-text">Kundli Match</div>
    </a>
    
    <!-- 3. Registration -->
    <a href="Registration" target="_self" class="custom-menu-item">
        <div class="custom-icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/2921/2921222.png" alt="Registration">
        </div>
        <div class="custom-menu-text">Registration</div>
    </a>
    
    <!-- 4. Matchmaking -->
    <a href="Matchmaking" target="_self" class="custom-menu-item">
        <div class="custom-icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/1077/1077035.png" alt="Matchmaking">
        </div>
        <div class="custom-menu-text">Matchmaking</div>
    </a>

    <!-- 5. Wedding Services -->
    <a href="Wedding_Services" target="_self" class="custom-menu-item">
        <div class="custom-icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/3159/3159303.png" alt="Services">
        </div>
        <div class="custom-menu-text">Wedding Services</div>
    </a>
    
    <!-- 6. Chat & Alerts -->
    <a href="Chat_Alerts" target="_self" class="custom-menu-item">
        <div class="custom-icon-circle">
            <img src="https://cdn-icons-png.flaticon.com/512/1380/1380370.png" alt="Chat">
        </div>
        <div class="custom-menu-text">Chat & Alerts</div>
    </a>

</div>
"""

# प्रिंटिंग साइडबार
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)
# =====================================================================

# 4. Main Page Content (Hero Section)
st.markdown("<br><br>", unsafe_allow_html=True)
st.title("Bandhan.com 💍")
st.write("Welcome to the world's first AI-powered matrimonial platform.")
