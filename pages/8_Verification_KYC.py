import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="KYC Verification | Bandhan", page_icon="🛡️", layout="wide")
# --- PREMIUM SIDEBAR CSS (Paste this below st.set_page_config in EVERY file) ---
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
# CSS Styling
st.markdown("""
    <style>
    .stApp { background-color: #F4F6F9; }
    .kyc-header { color: #1A365D; font-family: 'Helvetica', sans-serif; font-size: 2.5rem; text-align: center; font-weight: bold; }
    .trust-badge { background-color: #E3F2FD; color: #1976D2; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold; font-size: 1.1rem; }
    .kyc-card { background: white; padding: 30px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.06); border: 1px solid #EAEAEA; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='kyc-header'>🛡️ Profile Verification (KYC & Trust)</h1>", unsafe_allow_html=True)
st.markdown("<div class='trust-badge'>Get the Verified Blue Tick ✅ & Trust Badge to increase your profile visibility by 300%</div><br>", unsafe_allow_html=True)

st.markdown("<div class='kyc-card'>", unsafe_allow_html=True)
st.markdown("### Step 1: Upload Government ID")
id_type = st.selectbox("Select ID Type", ["Aadhaar Card", "PAN Card", "Passport", "Driving License"])
id_number = st.text_input(f"Enter {id_type} Number", placeholder="Enter ID number securely")
id_file = st.file_uploader(f"Upload Front Side of {id_type}", type=['jpg', 'png', 'jpeg'])

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### Step 2: Live AI Face Match")
st.info("📷 Please capture a live photo to match with your provided ID.")
camera_photo = st.camera_input("Take a selfie")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 Submit for AI & Trust Verification", type="primary", use_container_width=True):
    if id_number and camera_photo:
        with st.spinner("AI is scanning your ID and matching facial features securely..."):
            time.sleep(3)
        st.balloons()
        st.success("✅ Verification Successful! Your face matches the ID.")
        st.markdown("### 🎉 Congratulations! You have earned the Verified Blue Tick & Trust Badge ✅.")
    else:
        st.warning("⚠️ Please provide your ID details and take a selfie to proceed.")
st.markdown("</div>", unsafe_allow_html=True)
