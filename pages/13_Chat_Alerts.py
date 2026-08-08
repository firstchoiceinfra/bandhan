import streamlit as st
import time
import base64

# =====================================================================
# 1. PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Chat & Alerts | Bandhan",
    page_icon="💬",
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
# 4. 🔥 UNREAD MESSAGES RESET LOGIC 🔥
# =====================================================================
# जब यूजर इस पेज पर आता है, तो सारे मैसेज "पढ़ लिए गए" (Read) मानकर लाल अलर्ट 0 कर दें
if 'unread_msgs' not in st.session_state:
    st.session_state.unread_msgs = 0
else:
    st.session_state.unread_msgs = 0 # Mark as read

# =====================================================================
# 5. 🔥 CUSTOM IMAGE-BASED SIDEBAR MENU (अब नए लोगो के साथ) 🔥
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
# 6. POWERFUL PREMIUM CSS
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
    
    /* Chat & Alerts Specific Styles */
    .tool-header { background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%); padding: 30px; border-radius: 15px; color: white; text-align: center; border-bottom: 5px solid #D4AF37; margin-bottom: 25px; }
    .section-card { background: white; padding: 25px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.06); border: 1px solid #EAEAEA; margin-bottom: 25px; }
    .status-dot { height: 12px; width: 12px; background-color: #27AE60; border-radius: 50%; display: inline-block; margin-right: 8px; }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 7. PAGE CONTENT (Chat Interface & Alerts)
# =====================================================================
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown("""
    <div class="tool-header">
        <h1 style="margin:0; font-family:'Georgia', serif;">💬 Chat & Alerts</h1>
        <p style="font-size:1.1rem; margin-top:10px; color:#E3F2FD;">Chat safely with your verified matches and receive instant WhatsApp & Match updates.</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    # यह बटन आपको सिस्टम टेस्ट करने के लिए है। असली ऐप में यह बैकएंड से कंट्रोल होगा।
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔔 Simulate New Message", type="primary", use_container_width=True):
        st.session_state.unread_msgs += 1
        st.toast("नया मैसेज आया है! किसी और पेज पर जाएँ तो साइडबार में लाल अलर्ट दिखेगा।")
        st.rerun()

# Tabs for Chat and Match Alerts
tab_chat, tab_alerts = st.tabs(["💬 Secure In-App Messages", "🔔 Match & WhatsApp Alerts"])

# --- TAB 1: Secure In-App Live Messages ---
with tab_chat:
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    chat_col1, chat_col2 = st.columns([1, 3], gap="medium")
    
    with chat_col1:
        st.markdown("### 💬 Conversations")
        st.markdown("---")
        contact = st.radio("Select a Match:", ["Priya Sharma (98% Match)", "Aisha Khan (94% Match)", "Bandhan Premium Support"])
        contact_name = contact.split(" (")[0]

    with chat_col2:
        st.markdown(f"<h2 style='color:#1A365D; margin-top:0;'>{contact_name}</h2>", unsafe_allow_html=True)
        st.markdown("<div><span class='status-dot'></span><span style='color:gray;'>Online Now & Verified</span></div>", unsafe_allow_html=True)
        st.markdown("---")

        chat_key = f"chat_{contact_name}"
        if chat_key not in st.session_state:
            if "Support" in contact_name:
                st.session_state[chat_key] = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]
            else:
                st.session_state[chat_key] = [{"role": "assistant", "content": f"Hi there! I saw we have a high AI compatibility score."}]

        for message in st.session_state[chat_key]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input(f"Message {contact_name}..."):
            st.session_state[chat_key].append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
                
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                message_placeholder.markdown("*(typing...)*")
                time.sleep(1.2)
                reply = "That sounds wonderful! Shall we connect on a quick call this weekend?" if "Support" not in contact_name else "A manager will call you shortly."
                message_placeholder.markdown(reply)
                
            st.session_state[chat_key].append({"role": "assistant", "content": reply})
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 2: Alerts ---
with tab_alerts:
    st.markdown("<div class='section-card'><h3>🔔 Notifications</h3><p>Your alerts will appear here.</p></div>", unsafe_allow_html=True)
