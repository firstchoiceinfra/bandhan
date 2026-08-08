import streamlit as st
import time
import base64

# =====================================================================
# 1. PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="AI Matchmaking | Bandhan",
    page_icon="🧬",
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
    .stApp { background-color: #FAFAFA !important; font-family: 'Helvetica Neue', sans-serif; }
    
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
    
    /* Matchmaking Specific Styles */
    .header-text { color: #0F2027; font-family: 'Trebuchet MS', sans-serif; font-weight: 800; font-size: 2.2rem; }
    .gold-text { color: #D4AF37; }
    .profile-card { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 3px solid #1A365D; margin-bottom: 20px; }
    .match-score { color: #27AE60; font-weight: bold; font-size: 1.2rem; margin-bottom: 5px; }
    .profile-name { font-size: 1.5rem; font-weight: bold; color: #1A365D; margin-bottom: 5px; }
    .profile-details { color: #666666; font-size: 0.95rem; line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 6. PAGE CONTENT (Matchmaking)
# =====================================================================
st.markdown("<h1 class='header-text'>Bandhan <span class='gold-text'>AI Matchmaking</span> 🧬</h1>", unsafe_allow_html=True)
st.markdown("Our proprietary AI algorithm analyzes 50+ data points to find your perfect match.")
st.markdown("---")

# Sidebar for Manual Filters
st.sidebar.header("🎯 Refine Search")
age_filter = st.sidebar.slider("Age Range", 21, 60, (24, 32))
religion_filter = st.sidebar.multiselect("Religion", ["Hindu", "Muslim", "Sikh", "Christian", "Jain"], default=["Hindu"])
income_filter = st.sidebar.selectbox("Minimum Income", ["Any", "$50k+", "$100k+", "$200k+"])
st.sidebar.button("Apply Filters", type="primary", use_container_width=True)

# The AI Matching Simulation
if 'ai_run' not in st.session_state:
    st.session_state.ai_run = False

col1, col2 = st.columns([1, 4])
with col1:
    run_ai = st.button("🚀 Run AI Smart Search", type="primary", use_container_width=True)

if run_ai:
    with st.spinner('AI is analyzing behavioral traits and preferences...'):
        time.sleep(2) # AI के सोचने का एनिमेशन (2 सेकंड)
        st.session_state.ai_run = True

# Displaying Matches
if st.session_state.ai_run:
    st.success("✅ AI Analysis Complete. Here are your highly-compatible matches.")
    
    # Mock Data for Profiles
    profiles = [
        {
            "name": "Priya Sharma", "age": 27, "profession": "Software Engineer", 
            "location": "Mumbai, India", "match": "98%", "img": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "Aisha Khan", "age": 26, "profession": "Architect", 
            "location": "Dubai, UAE", "match": "94%", "img": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "Neha Patel", "age": 28, "profession": "Investment Banker", 
            "location": "London, UK", "match": "91%", "img": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80"
        }
    ]
    
    # Create rows of profiles
    p_col1, p_col2, p_col3 = st.columns(3)
    cols = [p_col1, p_col2, p_col3]
    
    for i, profile in enumerate(profiles):
        with cols[i]:
            st.image(profile["img"], use_container_width=True)
            st.markdown(f"""
                <div class="profile-card">
                    <div class="match-score">⭐ {profile['match']} AI Match</div>
                    <div class="profile-name">{profile['name']}, {profile['age']}</div>
                    <div class="profile-details">
                        💼 <b>Profession:</b> {profile['profession']}<br>
                        📍 <b>Location:</b> {profile['location']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Action Buttons
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.button("Send Request", key=f"req_{i}", type="primary", use_container_width=True)
            with btn_col2:
                st.button("View Profile", key=f"view_{i}", use_container_width=True)
else:
    st.info("👈 Click on 'Run AI Smart Search' to let our algorithm find your perfect matches, or use the sidebar filters for manual searching.")
