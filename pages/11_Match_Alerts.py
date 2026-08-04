import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="WhatsApp Alerts | Bandhan", page_icon="💬", layout="wide")

# 2. Premium WhatsApp Theme CSS
st.markdown("""
    <style>
    .stApp { background-color: #F0FDF4; } /* Light Green Background */
    
    .wa-header { 
        color: #075E54; /* WhatsApp Dark Green */
        font-family: 'Helvetica Neue', sans-serif; 
        font-size: 3rem; 
        font-weight: 900; 
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .alert-card { 
        background: white; 
        padding: 35px; 
        border-radius: 20px; 
        box-shadow: 0 15px 30px rgba(37, 211, 102, 0.15); 
        border-top: 6px solid #25D366; /* WhatsApp Light Green */
    }
    
    .feature-list {
        font-size: 1.1rem;
        color: #4A4A4A;
        line-height: 1.8;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("<h1 class='wa-header'>💬 Instant WhatsApp Alerts</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555; font-size:1.2rem;'>Never miss a perfect match. Get instant notifications and profiles directly on your WhatsApp.</p><hr>", unsafe_allow_html=True)

# 4. Main Content Layout
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("<br>", unsafe_allow_html=True)
    # 3D illustration of phone/messaging
    st.image("https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=600&q=80", use_container_width=True, caption="Powered by WhatsApp API")
    
    st.markdown("""
        ### Why enable WhatsApp Alerts?
        <div class="feature-list">
            ✅ <b>Be the first to know:</b> Get notified the moment an AI match is found.<br>
            ✅ <b>Quick Actions:</b> Accept or Reject requests directly from the chat.<br>
            ✅ <b>Secure & Private:</b> Your number remains hidden from other users.
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<div class='alert-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#075E54;'>🔔 Setup Your Match Alerts</h3>", unsafe_allow_html=True)
    
    # User Inputs
    mobile_number = st.text_input("WhatsApp Mobile Number", placeholder="+91 9876543210")
    
    alert_frequency = st.radio(
        "How often do you want to receive match alerts?",
        [
            "🚀 Instant (As soon as a 90%+ match is found)", 
            "📅 Daily Summary (Every morning at 9 AM)", 
            "🗓️ Weekly Digest (Every Sunday)"
        ]
    )
    
    st.markdown("### ⚙️ Alert Preferences")
    show_photos = st.checkbox("Show Profile Photos in WhatsApp messages", value=True)
    show_buttons = st.checkbox("Include direct 'Accept/Reject' buttons", value=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Activation Button
    if st.button("Activate WhatsApp Alerts 📲", type="primary", use_container_width=True):
        if mobile_number and len(mobile_number) >= 10:
            with st.spinner("Securely connecting to Bandhan WhatsApp API..."):
                time.sleep(2)
            st.success(f"✅ Alerts successfully activated for {mobile_number}! You will receive a welcome message shortly.")
            st.balloons()
        else:
            st.error("⚠️ Please enter a valid 10-digit mobile number.")
            
    st.markdown("</div>", unsafe_allow_html=True)
