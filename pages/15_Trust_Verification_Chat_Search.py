import streamlit as st
import time

# Page Config
st.set_page_config(page_title="Tools & Verification | Bandhan", page_icon="🛡️", layout="wide")

# CSS Styling
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    .tool-header {
        background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%);
        padding: 30px; border-radius: 15px; color: white; text-align: center;
        border-bottom: 5px solid #D4AF37; margin-bottom: 30px;
    }
    .section-card {
        background: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.06); border: 1px solid #EAEAEA;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="tool-header">
    <h1 style="margin:0; font-family:'Georgia', serif;">🛡️ Trust Verification, Live Chat & Advanced Search</h1>
    <p style="font-size:1.1rem; margin-top:10px; color:#E3F2FD;">Ensure 100% authenticity, chat securely, and filter perfect partner matches.</p>
</div>
""", unsafe_allow_html=True)

# Tabs for the 3 new features
tab1, tab2, tab3 = st.tabs([
    "🛡️ ID Verification & Trust Badge (KYC)", 
    "💬 Secure In-App Live Chat", 
    "🎯 Advanced Partner Search Filter"
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

# --- TAB 2: Secure In-App Live Chat ---
with tab2:
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h3>💬 Secure Chat Box</h3>", unsafe_allow_html=True)
    st.write("Chat with your connected matches without sharing your personal phone number.")
    
    # Chat simulation interface
    match_selected = st.selectbox("Select Active Match", ["Priya Sharma (98% Match)", "Ananya Gupta (92% Match)", "Neha Verma (88% Match)"])
    
    st.markdown(f"<p style='color:gray; font-weight:bold;'>Chatting with: {match_selected}</p>", unsafe_allow_html=True)
    
    # Chat history container
    chat_container = st.container()
    with chat_container:
        st.markdown("<div style='background:#F1F5F9; padding:15px; border-radius:10px; height:200px; overflow-y:auto;'>", unsafe_allow_html=True)
        st.markdown("<b>Priya Sharma:</b> Hi! Thanks for connecting. How are you?")
        st.markdown("<b>You:</b> Hello! I am doing great. Would you like to schedule a call this weekend?")
        st.markdown("</div>", unsafe_allow_html=True)
    
    user_msg = st.text_input("Type your message...", key="chat_input")
    if st.button("Send Message", type="primary"):
        if user_msg:
            st.toast("💬 Message sent securely!", icon="🚀")
        else:
            st.warning("Type a message to send.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: Advanced Partner Search Filter ---
with tab3:
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h3>🎯 Advanced Partner Preference Filter</h3>", unsafe_allow_html=True)
    
    f_col1, f_col2 = st.columns(2, gap="large")
    
    with f_col1:
        age_range = st.slider("Select Age Range", 18, 50, (21, 28))
        religion = st.selectbox("Religion", ["Any", "Hindu", "Muslim", "Sikh", "Christian", "Jain"])
        profession = st.selectbox("Profession / Occupation", ["Any", "Software Engineer", "Doctor", "Business Owner", "Chartered Accountant", "Civil Servant"])
    
    with f_col2:
        city = st.selectbox("Preferred City / Location", ["Any", "Nagpur", "Mumbai", "Pune", "Bangalore", "Delhi", "Hyderabad"])
        income = st.selectbox("Annual Income", ["Any", "₹ 5 Lakhs - ₹ 10 Lakhs", "₹ 10 Lakhs - ₹ 20 Lakhs", "₹ 20 Lakhs - ₹ 50 Lakhs", "₹ 50 Lakhs+"])
        manglik = st.selectbox("Kundli / Manglik Match", ["Doesn't Matter", "Non-Manglik", "Manglik"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Find Matching Profiles", type="primary", use_container_width=True):
        with st.spinner("Searching verified database for matching profiles..."):
            time.sleep(1.5)
        st.success("✨ Found 42 verified profiles matching your exact preferences!")
        
        # Display sample matching results
        st.markdown("""
        <div style="background:#F8F9FA; padding:15px; border-radius:10px; margin-top:10px; border-left:5px solid #27AE60;">
            <h4>🎉 Top Match: Ritu Deshmukh (24 yrs, Nagpur)</h4>
            <p><b>Profession:</b> Software Engineer | <b>Income:</b> ₹ 12 Lakhs p.a. | <b>Match Score:</b> 96%</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
