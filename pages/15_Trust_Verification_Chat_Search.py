import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Trust & Messages | Bandhan",
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
    </style>
""", unsafe_allow_html=True)

# Main Header
st.markdown("""
<div class="tool-header">
    <h1 style="margin:0; font-family:'Georgia', serif;">🛡️ Trust Verification & Secure Messaging</h1>
    <p style="font-size:1.1rem; margin-top:10px; color:#E3F2FD;">Ensure 100% authenticity with KYC and chat securely with verified matches.</p>
</div>
""", unsafe_allow_html=True)

# 3. Top-level Tabs to Switch between KYC and Chat System
tab1, tab2 = st.tabs([
    "🛡️ ID Verification & Trust Badge (KYC)", 
    "💬 Secure In-App Live Messages"
])

# --- TAB 1: ID Verification & Trust Badge ---
with tab1:
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h3>🆔 Get Your Profile 'Verified Trust Badge'</h3>", unsafe_allow_html=True)
    st.write("Verified profiles get 5x more responses and build instant trust with families.")
    
    with st.form("kyc_form"):
        id_type = st.selectbox("Select Government ID Type", ["Aadhaar Card", "PAN Card", "Passport", "Driving License"])
        id_number = st.text_input("Enter ID Number")
        uploaded_file = st.file_uploader("Upload Clear Photo/Scan of ID (JPG/PNG/PDF)", type=["jpg", "png", "pdf"])
        
        submit_kyc = st.form_submit_button("📤 Submit for Verification", type="primary")
        if submit_kyc:
            if id_number:
                with st.spinner("Verifying documents with government registry..."):
                    time.sleep(2)
                st.balloons()
                st.success("✅ Document submitted successfully! Your profile will display the 'Verified Trust Badge' within 2 hours.")
            else:
                st.warning("Please enter your ID number.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 2: Secure In-App Live Messages (Your Custom Code Integrated) ---
with tab2:
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    
    # Using columns or sub-layout to simulate sidebar chat navigation inside the tab
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

        # Session State for Dynamic Chat History
        chat_key = f"chat_{contact_name}"

        if chat_key not in st.session_state:
            if "Support" in contact_name:
                st.session_state[chat_key] = [{"role": "assistant", "content": "Hello! Welcome to Bandhan Premium Support. How can I assist you with your wedding planning today?"}]
            else:
                st.session_state[chat_key] = [{"role": "assistant", "content": f"Hi there! I saw we have a high AI compatibility score. How are you doing?"}]

        # Display Chat History Container
        for message in st.session_state[chat_key]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat Input Field
        if prompt := st.chat_input(f"Message {contact_name}..."):
            st.session_state[chat_key].append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
                
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                message_placeholder.markdown("*(typing...)*")
                time.sleep(1.2) # Artificial delay for realism
                
                if "Support" in contact_name:
                    reply = "Thank you for reaching out. A premium relationship manager will call you shortly."
                else:
                    reply = "That sounds wonderful! I would love to know more about your interests. Shall we connect on a quick call this weekend?"
                    
                message_placeholder.markdown(reply)
                
            st.session_state[chat_key].append({"role": "assistant", "content": reply})

    st.markdown("</div>", unsafe_allow_html=True)
