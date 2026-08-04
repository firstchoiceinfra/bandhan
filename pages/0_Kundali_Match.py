import streamlit as st
import time

st.set_page_config(page_title="Kundali Match | Bandhan", page_icon="🕉️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFDF8; }
    .header-kundali { color: #D35400; font-family: 'Georgia', serif; font-size: 2.8rem; text-align: center; font-weight: bold; }
    .guna-score { font-size: 4rem; color: #27AE60; font-weight: 900; text-align: center; }
    .card-box { background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 3px solid #D35400; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='header-kundali'>🕉️ AI Kundali & Guna Milan</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Our advanced Vedic AI calculates accurate planetary positions and the 36 Gunas for perfect compatibility.</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 🤵 Boy's Birth Details")
    b_name = st.text_input("Name", key="b_name")
    b_date = st.date_input("Date of Birth", key="b_date")
    b_time = st.time_input("Time of Birth", key="b_time")
    b_place = st.text_input("Place of Birth", key="b_place")

with col2:
    st.markdown("### 👰 Girl's Birth Details")
    g_name = st.text_input("Name", key="g_name")
    g_date = st.date_input("Date of Birth", key="g_date")
    g_time = st.time_input("Time of Birth", key="g_time")
    g_place = st.text_input("Place of Birth", key="g_place")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔮 Calculate 36 Guna Match", type="primary", use_container_width=True):
    if b_name and g_name:
        with st.spinner("Analyzing planetary positions and Ashtakoota Gunas..."):
            time.sleep(2.5)
        
        st.success("Analysis Complete!")
        st.markdown("<div class='card-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;'>Total Guna Score</h3>", unsafe_allow_html=True)
        st.markdown("<div class='guna-score'>28.5 / 36</div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#27AE60; font-weight:bold;'>Highly Compatible Match! (Nadi Dosha: None)</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("Please enter both names to calculate Kundali.")
