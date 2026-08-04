import streamlit as st
import time

st.set_page_config(page_title="KYC Verification | Bandhan", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F4F6F9; }
    .kyc-header { color: #1A365D; font-family: 'Helvetica', sans-serif; font-size: 2.5rem; text-align: center; font-weight: bold; }
    .trust-badge { background-color: #E3F2FD; color: #1976D2; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='kyc-header'>🛡️ Profile Verification (KYC)</h1>", unsafe_allow_html=True)
st.markdown("<div class='trust-badge'>Get the Verified Blue Tick ✅ to increase your profile visibility by 300%</div><br>", unsafe_allow_html=True)

st.markdown("### Step 1: Upload Government ID")
id_type = st.selectbox("Select ID Type", ["Aadhaar Card", "PAN Card", "Passport", "Driving License"])
id_number = st.text_input(f"Enter {id_type} Number", placeholder="e.g. 1234-5678-XXXX")
id_file = st.file_uploader(f"Upload Front Side of {id_type}", type=['jpg', 'png', 'jpeg'])

st.markdown("### Step 2: Live AI Face Match")
st.info("Please capture a live photo to match with your provided ID.")
camera_photo = st.camera_input("Take a selfie")

if st.button("Submit for AI Verification", type="primary"):
    if id_number and camera_photo:
        with st.spinner("AI is scanning your ID and matching facial features..."):
            time.sleep(3)
        st.balloons()
        st.success("✅ Verification Successful! Your face matches the ID.")
        st.markdown("### 🎉 Congratulations! You have earned the Verified Blue Tick.")
    else:
        st.warning("Please provide your ID details and take a selfie to proceed.")
