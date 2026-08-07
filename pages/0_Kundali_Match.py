import streamlit as st
import time
import base64

# --- फ्लैश रोकने का पावरफुल तरीका ---
st.markdown("""
    <style>
    [data-testid="stSidebarNav"], #stSidebarNav { display: none !important; }
    .stApp { opacity: 0; animation: fadeIn 0.3s ease-in forwards; }
    @keyframes fadeIn { to { opacity: 1; } }
    </style>
""", unsafe_allow_html=True)

# 1. Page Configuration
st.set_page_config(page_title="Kundali Match | Bandhan", page_icon="🕉️", layout="wide")

# 2. READ LOCAL LOGO
def get_base64_image(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e: return ""

logo_b64 = get_base64_image("896327.png")

# 3. SPLASH SCREEN
st.markdown(f"""
    <style>
    .stApp::after {{
        content: ""; 
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%); 
        background-image: url("data:image/png;base64,{logo_b64}"); 
        background-repeat: no-repeat;
        background-position: center;
        background-size: 350px; 
        filter: drop-shadow(0px 0px 12px rgba(255, 255, 255, 0.5));
        z-index: 9999999; animation: fadeOutSplash 1.2s ease-in-out forwards; 
    }}
    @keyframes fadeOutSplash {{ 100% {{ opacity: 0; visibility: hidden; pointer-events: none; }} }}
    </style>
""", unsafe_allow_html=True)

# 4. SIDEBAR & CSS (Same as app.py)
# ... (यहाँ app.py वाला sidebar_html और style वाला हिस्सा पेस्ट करें)
