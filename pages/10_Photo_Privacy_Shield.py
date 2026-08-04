import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Privacy Shield | Bandhan", page_icon="🔒", layout="wide")

# 2. Custom CSS
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    .shield-header { color: #2C3E50; font-family: 'Helvetica', sans-serif; font-size: 2.5rem; font-weight: 800; }
    .security-card { background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #EAEAEA; margin-bottom: 20px; }
    .premium-badge { background-color: #D4AF37; color: white; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='shield-header'>🔒 Advanced Privacy Shield</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:gray;'>Control who sees your photos, contact details, and secure your profile from unauthorized screenshots.</p><hr>", unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown("<div class='security-card'>", unsafe_allow_html=True)
    st.markdown("### 📸 Photo Visibility Settings")
    photo_setting = st.radio(
        "Who can see your profile photos?",
        ["Everyone (Recommended)", "Only Premium Members", "Only Members I Accept (Blur for others)"]
    )
    if photo_setting == "Only Members I Accept (Blur for others)":
        st.warning("Your photos will appear blurred to all users until you accept their request.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='security-card'>", unsafe_allow_html=True)
    st.markdown("### 🛡️ Anti-Screenshot Protection <span class='premium-badge'>PLATINUM FEATURE</span>", unsafe_allow_html=True)
    st.markdown("Prevent users from taking screenshots or screen recordings of your profile.")
    screenshot_block = st.toggle("Block Screenshots (Requires Platinum Plan)")
    
    if screenshot_block:
        st.success("Screenshot protection is actively monitoring your profile.")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='security-card'>", unsafe_allow_html=True)
    st.markdown("### 📞 Contact Info Privacy")
    st.markdown("Control who can see your mobile number and email.")
    contact_setting = st.selectbox(
        "Phone Number Visibility",
        ["Hide Completely", "Show to Accepted Matches", "Show to Premium Members"]
    )
    
    st.markdown("### 🕵️ Incognito Mode")
    incognito = st.toggle("Browse profiles silently (They won't know you visited)")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
if st.button("💾 Save Privacy Settings", type="primary"):
    with st.spinner("Encrypting your preferences..."):
        time.sleep(1.5)
    st.success("✅ Your privacy settings have been updated and secured.")
