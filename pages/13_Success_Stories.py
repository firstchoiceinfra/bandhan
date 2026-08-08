import streamlit as st
import time
import base64

# =====================================================================
# 1. PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Success Stories | Bandhan",
    page_icon="💖",
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
    .stApp { background-color: #F8F9FA !important; font-family: 'Helvetica Neue', sans-serif; }
    
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
    
    /* Success Stories Specific Styles */
    .stories-header {
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        padding: 40px; border-radius: 20px; color: white; text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2); border: 2px solid #D4AF37; margin-bottom: 30px;
    }
    .stories-title {
        font-family: 'Georgia', serif; font-size: 3rem; font-weight: 900; margin: 0;
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .story-card {
        background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border: 1px solid #EAEAEA; border-top: 6px solid #D4AF37; margin-bottom: 25px; transition: transform 0.3s ease;
    }
    .story-card:hover { transform: translateY(-5px); box-shadow: 0 15px 30px rgba(212, 175, 55, 0.25); }
    .couple-name { color: #1A365D; font-family: 'Georgia', serif; font-size: 1.5rem; font-weight: bold; margin-bottom: 5px; }
    .story-date { color: #718096; font-size: 0.9rem; margin-bottom: 15px; }
    .story-quote { color: #334155; font-size: 1rem; line-height: 1.6; font-style: italic; }
    .share-box {
        background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%); color: white;
        padding: 30px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 6. PAGE CONTENT
# =====================================================================
st.markdown("""
<div class="stories-header">
    <h1 class="stories-title">Bandhan Success Stories</h1>
    <p style="font-size:1.2rem; margin-top:15px; color:#FBF5B7; font-style:italic;">Real couples, real connections, and happily ever afters made possible through Bandhan.</p>
</div>
""", unsafe_allow_html=True)

# Success Stories Grid Layout
col1, col2 = st.columns(2, gap="large")

with col1:
    # Story 1
    st.markdown("""
    <div class="story-card">
        <img src="https://images.unsplash.com/photo-1583939003579-730e3918a45a?auto=format&fit=crop&w=600&q=80" style="width:100%; border-radius:10px; margin-bottom:15px; height:220px; object-fit:cover;">
        <div class="couple-name">Rahul & Priya Sharma</div>
        <div class="story-date">📅 Married on: 14th February 2026 | Nagpur</div>
        <div class="story-quote">"We found each other through Bandhan's secure matching and privacy features. The platform made it so easy to connect with families, check kundlis, and plan our dream wedding seamlessly. Thank you Bandhan for giving us our happily ever after!"</div>
    </div>
    """, unsafe_allow_html=True)

    # Story 2
    st.markdown("""
    <div class="story-card">
        <img src="https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80" style="width:100%; border-radius:10px; margin-bottom:15px; height:220px; object-fit:cover;">
        <div class="couple-name">Amit & Neha Verma</div>
        <div class="story-date">📅 Married on: 28th November 2025 | Pune</div>
        <div class="story-quote">"The verified profiles and secure in-app calling gave us immense confidence. We used the Bandhan Budget Calculator and Wedding Services planner to execute everything without any stress. Highly recommended!"</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Story 3
    st.markdown("""
    <div class="story-card">
        <img src="https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=600&q=80" style="width:100%; border-radius:10px; margin-bottom:15px; height:220px; object-fit:cover;">
        <div class="couple-name">Vikram & Pooja Patil</div>
        <div class="story-date">📅 Married on: 10th January 2026 | Mumbai</div>
        <div class="story-quote">"Finding a life partner who shares the same values and goals was effortless here. The matchmaking algorithm is top-notch. Our families met and everything clicked instantly. Eternally grateful to Bandhan!"</div>
    </div>
    """, unsafe_allow_html=True)

    # Story 4
    st.markdown("""
    <div class="story-card">
        <img src="https://images.unsplash.com/photo-1519225421980-715cb0215aed?auto=format&fit=crop&w=600&q=80" style="width:100%; border-radius:10px; margin-bottom:15px; height:220px; object-fit:cover;">
        <div class="couple-name">Rohan & Ananya Gupta</div>
        <div class="story-date">📅 Married on: 5th May 2025 | Bangalore</div>
        <div class="story-quote">"From our first secure call to booking our wedding venue through Bandhan's ecosystem, the journey was magical. Best matchmaking and planning platform ever!"</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Share Your Story Form Section
st.markdown("""
<div class="share-box">
    <h2 style="color:#D4AF37; margin-top:0; font-family:'Georgia', serif;">💖 Share Your Success Story</h2>
    <p style="color:#E2E8F0;">Did you find your soulmate through Bandhan? Share your journey with us and inspire thousands of others!</p>
</div>
""", unsafe_allow_html=True)

with st.form("success_story_form"):
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        groom_name = st.text_input("Groom's Name")
        bride_name = st.text_input("Bride's Name")
        marriage_date = st.date_input("Date of Marriage")
    with s_col2:
        contact_email = st.text_input("Email / Mobile Number")
        city_name = st.text_input("Wedding City")
    
    story_text = st.text_area("Your Love & Success Story", placeholder="Write about how you met on Bandhan and your wedding experience...")
    
    submitted = st.form_submit_button("📤 Submit Your Success Story", type="primary")
    if submitted:
        if groom_name and bride_name and story_text:
            st.balloons()
            st.success("🎉 Thank you for sharing your story! Our team will verify and publish it on the Bandhan portal soon.")
        else:
            st.warning("Please fill in the essential details (Names and Story) before submitting.")
