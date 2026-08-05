import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Success Stories | Bandhan",
    page_icon="💖",
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
    .stories-header {
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        padding: 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        border: 2px solid #D4AF37;
        margin-bottom: 30px;
    }
    .stories-title {
        font-family: 'Georgia', serif;
        font-size: 3rem;
        font-weight: 900;
        margin: 0;
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .story-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border: 1px solid #EAEAEA;
        border-top: 6px solid #D4AF37;
        margin-bottom: 25px;
        transition: transform 0.3s ease;
    }
    .story-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(212, 175, 55, 0.25);
    }
    .couple-name {
        color: #1A365D;
        font-family: 'Georgia', serif;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .story-date {
        color: #718096;
        font-size: 0.9rem;
        margin-bottom: 15px;
    }
    .story-quote {
        color: #334155;
        font-size: 1rem;
        line-height: 1.6;
        font-style: italic;
    }
    .share-box {
        background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Hero Header
st.markdown("""
<div class="stories-header">
    <h1 class="stories-title">Bandhan Success Stories</h1>
    <p style="font-size:1.2rem; margin-top:15px; color:#FBF5B7; font-style:italic;">Real couples, real connections, and happily ever afters made possible through Bandhan.</p>
</div>
""", unsafe_allow_html=True)

# 4. Success Stories Grid Layout
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

# 5. Share Your Story Form Section
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
