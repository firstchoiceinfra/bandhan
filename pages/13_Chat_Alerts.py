import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Chat & Alerts | Bandhan", page_icon="💬", layout="wide")
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
# --------------------------------------------------------------------------------
# जब यूजर इस पेज पर आता है, तो सारे मैसेज "पढ़ लिए गए" (Read) मानकर लाल अलर्ट 0 कर दें
if 'unread_msgs' not in st.session_state:
    st.session_state.unread_msgs = 0
else:
    st.session_state.unread_msgs = 0 # Mark as read

# --- PREMIUM SIDEBAR CSS (Paste this below st.set_page_config in EVERY file) ---
# नोटिफिकेशन बैज का CSS 
badge_css = ""
if st.session_state.unread_msgs > 0:
    badge_css = f"""
    [data-testid="stSidebarNav"] a[href*="Chat_Alerts"]::after,
    [data-testid="stSidebarNav"] a[href*="chat_alerts"]::after {{
        content: "{st.session_state.unread_msgs}"; background-color: #FF2A2A !important;
        color: white !important; font-size: 0.85rem !important; font-weight: 900 !important;
        border-radius: 50% !important; min-width: 22px; height: 22px; display: flex; align-items: center; justify-content: center;
        position: absolute; right: 15px; top: 50%; transform: translateY(-50%);
        box-shadow: 0 0 10px rgba(255, 42, 42, 0.8); animation: pulse-red 1.5s infinite;
    }}
    @keyframes pulse-red {{
        0% {{ box-shadow: 0 0 0 0 rgba(255, 42, 42, 0.7); }}
        70% {{ box-shadow: 0 0 0 8px rgba(255, 42, 42, 0); }}
        100% {{ box-shadow: 0 0 0 0 rgba(255, 42, 42, 0); }}
    }}
    """

st.markdown(f"""
    <style>
    [data-testid="stSidebar"] {{ background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important; border-right: 3px solid #D4AF37 !important; }}
    [data-testid="stSidebarNav"]::before {{ content: "👑 Bandhan Menu"; color: #D4AF37; font-size: 1.8rem; font-weight: 900; font-family: 'Georgia', serif; text-align: center; display: block; margin-bottom: 25px; padding-top: 20px; border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 15px; }}
    [data-testid="stSidebarNav"] a {{ background-color: rgba(255, 255, 255, 0.05) !important; border-radius: 12px !important; margin: 8px 15px !important; padding: 12px !important; border: 1px solid rgba(212, 175, 55, 0.3) !important; transition: all 0.3s ease-in-out !important; position: relative; }}
    [data-testid="stSidebarNav"] span {{ color: #E2E8F0 !important; font-size: 1.05rem !important; font-weight: 600 !important; }}
    [data-testid="stSidebarNav"] a:hover {{ background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%) !important; transform: translateX(8px) !important; border-color: #FBF5B7 !important; }}
    [data-testid="stSidebarNav"] a:hover span {{ color: #0F2027 !important; font-weight: 800 !important; }}
    [data-testid="stSidebarNav"] a[aria-current="page"] {{ background: linear-gradient(135deg, #D4AF37 0%, #AA771C 100%) !important; box-shadow: 0 5px 20px rgba(212, 175, 55, 0.6) !important; border: 2px solid #FBF5B7 !important; }}
    [data-testid="stSidebarNav"] a[aria-current="page"] span {{ color: #0F2027 !important; font-weight: 900 !important; }}
    {badge_css}
    </style>
""", unsafe_allow_html=True)
# --------------------------------------------------------------------------------

# 2. Page CSS Styling
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    .tool-header { background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%); padding: 30px; border-radius: 15px; color: white; text-align: center; border-bottom: 5px solid #D4AF37; margin-bottom: 25px; }
    .section-card { background: white; padding: 25px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.06); border: 1px solid #EAEAEA; margin-bottom: 25px; }
    .status-dot { height: 12px; width: 12px; background-color: #27AE60; border-radius: 50%; display: inline-block; margin-right: 8px; }
    </style>
""", unsafe_allow_html=True)

# 3. Main Header & Developer Test Button
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
        st.toast("नया मैसेज आया है! साइडबार में लाल अलर्ट चेक करें। किसी और पेज पर जाएँ।")

# 4. Tabs for Chat and Match Alerts
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
