import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Budget Calculator | Bandhan", page_icon="💰", layout="wide")

# 2. Premium CSS
st.markdown("""
    <style>
    .stApp { background-color: #FAFAFA; }
    .budget-header { color: #1A365D; font-family: 'Helvetica', sans-serif; font-size: 2.5rem; font-weight: 800; }
    .total-box { background: linear-gradient(135deg, #27AE60 0%, #1E8449 100%); color: white; padding: 20px; border-radius: 12px; text-align: center; font-size: 2rem; font-weight: bold; box-shadow: 0 5px 15px rgba(39,174,96,0.3); }
    .category-box { background: white; padding: 15px; border-radius: 8px; border-left: 5px solid #D4AF37; margin-bottom: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='budget-header'>💰 AI Wedding Budget Planner</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:gray;'>Enter your total budget, and our AI will suggest the perfect financial breakdown for your dream wedding.</p><hr>", unsafe_allow_html=True)

# 3. Budget Input Section
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown("### Step 1: Set Total Budget")
    total_budget = st.number_input("Enter Amount (in USD $)", min_value=1000, max_value=1000000, value=25000, step=1000)
    
    st.markdown("### Step 2: Guest Count")
    guests = st.slider("Estimated Number of Guests", 50, 1000, 250)
    
    st.button("🔄 Recalculate AI Plan", type="primary", use_container_width=True)

with col2:
    st.markdown(f"<div class='total-box'>Grand Total: ${total_budget:,}</div><br>", unsafe_allow_html=True)
    
    # AI Logic for Budget Breakdown
    venue_cat = int(total_budget * 0.40)
    jewelry = int(total_budget * 0.25)
    apparel = int(total_budget * 0.15)
    photo_video = int(total_budget * 0.10)
    misc = int(total_budget * 0.10)
    
    st.markdown("### 📊 Recommended Breakdown")
    
    # Progress bars and metrics
    st.markdown(f"<div class='category-box'><b>🏰 Venue & Catering (40%):</b> ${venue_cat:,}</div>", unsafe_allow_html=True)
    st.progress(40)
    
    st.markdown(f"<div class='category-box'><b>💍 Jewelry & Accessories (25%):</b> ${jewelry:,}</div>", unsafe_allow_html=True)
    st.progress(25)
    
    st.markdown(f"<div class='category-box'><b>👗 Designer Apparel (15%):</b> ${apparel:,}</div>", unsafe_allow_html=True)
    st.progress(15)
    
    st.markdown(f"<div class='category-box'><b>📸 Photography & Misc (20%):</b> ${(photo_video + misc):,}</div>", unsafe_allow_html=True)
    st.progress(20)

st.markdown("<br><hr>", unsafe_allow_html=True)
st.info("💡 **AI Tip:** Booking your venue 6 months in advance can save you up to 15% on catering costs. Check our 'Wedding Ecosystem' tab for exclusive deals.")
