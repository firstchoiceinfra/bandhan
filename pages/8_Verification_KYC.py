import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Trust, KYC & Chat | Bandhan",
    page_icon="🛡️",
    layout="wide"
)

# 2. Premium CSS Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #F8F9FA;
    }
    .tool-header {
        background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%);
        padding: 30px; border-radius: 15px; color: white; text-align: center;
        border-bottom: 5px solid #D4AF37; margin-bottom: 25px;
    }
    .section-card {
        background: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.06); border: 1px solid #EAEAEA;
        margin-bottom: 25px;
    }
    .status-dot {
        height: 12px; width: 12px; background-color: #27AE60;
        border-radius: 50%; display: inline-block; margin-right: 8px;
    }
    .alert-card {
        background: white; padding: 20px; border-radius: 12px; margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 6px solid #D4AF37;
        border-top: 1px solid #EAEAEA; border-right: 1px solid #EAEAEA; border-bottom: 1px solid #EAEAEA;
    }
    .whatsapp-box {
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white; padding: 20px; border-radius: 12px; margin-top: 25px;
        box-shadow: 0 5px 15px rgba(37, 211, 102, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Main Header
st.markdown("""
<div class="tool-header">
    <h1 style="margin:0; font-family:'Georgia', serif;">🛡️ Trust & KYC Verification, Live Chat & Alerts</h1>
    <p style="font-size:1.1rem; margin-top:10px; color:#E3F2FD;">Complete your KYC verification, chat securely, and manage instant WhatsApp match alerts.</p>
</div>
""", unsafe_allow_html=True)

# 3. Top-level Tabs for Unified KYC & Trust, Chat, and Match Alerts
tab1, tab2, tab3 = st.tabs([
    "🛡️ Trust & KYC Verification", 
    "💬 Secure In-App Live Messages",
    "🔔 Real-Time Match & WhatsApp Alerts"
])

# --- TAB 1: Unified Trust & KYC Verification ---
with tab1:
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h3>🆔 Profile Verification & Trust Badge (KYC)</h3>", unsafe_allow_html=True)
    st.write("Submit your government ID to complete your KYC and get the official 'Verified Trust Badge' on your profile to build instant trust.")
    
    with st.form("kyc_verification_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            id_type = st.selectbox("Select Government ID Type", ["Aadhaar Card", "PAN Card", "Passport", "Driving License"])
            full_name = st.text_input("Full Name as per ID Document")
        with col_b:
            id_number = st.text_input("Enter ID Number")
            dob = st.date_input("Date of Birth")
            
        uploaded_file = st.file_uploader("Upload Clear Scanned Copy / Photo of ID (JPG/PNG/PDF)", type=["jpg", "png", "pdf"])
        
        submit_verify = st.form_submit_button("📤 Submit KYC for Verification", type="primary")
        if submit_verify:
            if id_number and full_name:
                with st.spinner("Encrypting and verifying details with government registry..."):
                    time.sleep(2.5)
                st.balloons()
                st.success(f"✅ KYC Verified Successfully for {full_name}! Your 'Verified Trust Badge' is now active on your profile.")
            else:
                st.warning("Please fill in your Full Name and ID Number to proceed.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 2: Secure In-App Live Messages ---
with tab2:
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    
    chat_col1, chat_col2 = st.columns([1, 3], gap="medium")
    
    with chat_col1:
        st.markdown("### 💬 Conversations")
        st.markdown("---")
        contact = st.radio(
            "Select a Match to chat with:",
            ["Priya Sharma (98% Match)", "Aisha Khan (94% Match)", "Bandhan Premium Support"]
        )
        contact_name = contact.split(" (")[0]

    with chat_col2:
        st.markdown(f"<h2 style='color:#1A365D; margin-top:0;'>{contact_name}</h2>", unsafe_allow_html=True)
        st.markdown("<div><span class='status-dot'></span><span style='color:gray;'>Online Now & Verified</span></div>", unsafe_allow_html=True)
        st.markdown("---")

        chat_key = f"chat_{contact_name}"

        if chat_key not in st.session_state:
            if "Support" in contact_name:
                st.session_state[chat_key] = [{"role": "assistant", "content": "Hello! Welcome to Bandhan Premium Support. How can I assist you with your wedding planning today?"}]
            else:
                st.session_state[chat_key] = [{"role": "assistant", "content": f"Hi there! I saw we have a high AI compatibility score. How are you doing?"}]

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
                
                if "Support" in contact_name:
                    reply = "Thank you for reaching out. A premium relationship manager will call you shortly."
                else:
                    reply = "That sounds wonderful! I would love to know more about your interests. Shall we connect on a quick call this weekend?"
                    
                message_placeholder.markdown(reply)
                
            st.session_state[chat_key].append({"role": "assistant", "content": reply})

    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: Real-Time Match & WhatsApp Alerts ---
with tab3:
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h3>🔔 Your Daily & Instant Match Alerts</h3>", unsafe_allow_html=True)
    st.write("Smart AI-based alerts generated according to your partner preferences and kundli compatibility.")
    
    st.markdown("""
    <div class="alert-card">
        <h4 style="color:#1A365D; margin-top:0;">✨ New High Compatibility Match Found!</h4>
        <p><b>Profile:</b> Ritu Deshmukh (24 yrs, Nagpur) | <b>Match Score:</b> 96%</p>
        <p style="color:gray; font-size:0.9rem;">🕒 Alert received 10 minutes ago • Shared similar career & lifestyle goals.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="alert-card" style="border-left-color: #27AE60;">
        <h4 style="color:#1A365D; margin-top:0;">🛡️ Profile View Alert</h4>
        <p><b>Sneha Patil (Pune)</b> viewed your verified profile and sent an interest request.</p>
        <p style="color:gray; font-size:0.9rem;">🕒 Alert received 2 hours ago • Kundli Match: Excellent (32/36 Gunas)</p>
    </div>
    """, unsafe_allow_html=True)

    # Integrated WhatsApp Alert Configuration Box
    st.markdown("""
    <div class="whatsapp-box">
        <h3 style="margin-top:0; color:white;">🟢 Get Instant Match Alerts on WhatsApp</h3>
        <p>Never miss a connection! Receive direct match recommendations and interest alerts straight to your WhatsApp.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("whatsapp_alert_form"):
        wa_number = st.text_input("Enter Your WhatsApp Mobile Number (+91)")
        wa_frequency = st.selectbox("Alert Frequency", ["Instant (Real-time)", "Daily Summary Digest", "Weekly Highlights"])
        
        enable_wa = st.form_submit_button("📲 Enable WhatsApp Match Alerts", type="primary")
        if enable_wa:
            if wa_number:
                st.balloons()
                st.success(f"✅ Success! WhatsApp alerts have been successfully activated for {wa_number}. You will now receive instant match updates.")
            else:
                st.warning("Please enter a valid WhatsApp mobile number.")

    st.markdown("</div>", unsafe_allow_html=True)
