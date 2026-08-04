import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Wedding Ecosystem | Bandhan",
    page_icon="🛍️",
    layout="wide"
)

# 2. Advanced Dynamic CSS (Gradient & Hover Effects)
st.markdown("""
    <style>
    .stApp {
        background-color: #F8F9FA;
    }
    .main-header {
        background: -webkit-linear-gradient(45deg, #1A365D, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Trebuchet MS', sans-serif;
        font-weight: 900;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 0px;
    }
    .dynamic-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.08);
        transition: all 0.4s ease;
        border: 1px solid #EAEAEA;
    }
    .dynamic-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 15px 30px rgba(212, 175, 55, 0.2);
        border-color: #D4AF37;
    }
    .cart-box {
        background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    .price-tag {
        color: #27AE60; font-size: 1.4rem; font-weight: 800;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Session State for Dynamic Cart (वेडिंग प्लानर)
if 'wedding_cart' not in st.session_state:
    st.session_state.wedding_cart = []
if 'total_budget' not in st.session_state:
    st.session_state.total_budget = 0

# 4. Hero Section
st.markdown("<h1 class='main-header'>The Ultimate Wedding Ecosystem</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:1.2rem; color:gray;'>Design your dream wedding dynamically. Add services to your planner and track your estimated budget in real-time.</p>", unsafe_allow_html=True)
st.markdown("---")

# 5. Dynamic Tabs
tab1, tab2, tab3 = st.tabs(["🏰 Luxury Venues", "🏎️ Premium Rides", "📋 My Wedding Planner (Cart)"])

# --- TAB 1: Luxury Venues (With Booking Animation) ---
with tab1:
    v_col1, v_col2 = st.columns(2, gap="large")
    
    with v_col1:
        st.markdown("""<div class='dynamic-card'>""", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1519225421980-715cb0215aed?auto=format&fit=crop&w=800&q=80", use_container_width=True, border_radius=10)
        st.markdown("### The Royal Orchid Banquet\n⭐⭐⭐⭐⭐ (4.9/5)\n\n<span class='price-tag'>$5,000</span> / Day", unsafe_allow_html=True)
        
        if st.button("Check & Add to Planner", key="v1_btn", use_container_width=True):
            with st.spinner("Checking real-time availability..."):
                time.sleep(1.5)
            st.session_state.wedding_cart.append({"item": "Royal Orchid Banquet", "price": 5000})
            st.session_state.total_budget += 5000
            st.toast("✅ Venue added to your Wedding Planner!", icon="🏰")
        st.markdown("</div>", unsafe_allow_html=True)

    with v_col2:
        st.markdown("""<div class='dynamic-card'>""", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=800&q=80", use_container_width=True)
        st.markdown("### Heritage Palace Courtyard\n⭐⭐⭐⭐⭐ (5.0/5)\n\n<span class='price-tag'>$8,500</span> / Day", unsafe_allow_html=True)
        
        if st.button("Check & Add to Planner", key="v2_btn", use_container_width=True):
            with st.spinner("Checking real-time availability..."):
                time.sleep(1.5)
            st.session_state.wedding_cart.append({"item": "Heritage Palace Courtyard", "price": 8500})
            st.session_state.total_budget += 8500
            st.toast("✅ Venue added to your Wedding Planner!", icon="🏰")
        st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 2: Premium Rides (With Dynamic Price Slider) ---
with tab2:
    r_col1, r_col2 = st.columns(2, gap="large")
    
    with r_col1:
        st.markdown("""<div class='dynamic-card'>""", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1503376712356-6552988147d3?auto=format&fit=crop&w=800&q=80", use_container_width=True)
        st.markdown("### Mercedes-Maybach S-Class")
        st.markdown("Base Price: **$150 / Hour**")
        
        # Dynamic Slider
        hours_maybach = st.slider("Select Rental Duration (Hours)", min_value=2, max_value=12, value=4, key="slider_m")
        total_maybach_price = hours_maybach * 150
        
        # Real-time Metric
        st.metric(label="Estimated Cost", value=f"${total_maybach_price}")
        
        if st.button("Reserve Ride", key="r1_btn", type="primary", use_container_width=True):
            st.session_state.wedding_cart.append({"item": f"Maybach ({hours_maybach} Hrs)", "price": total_maybach_price})
            st.session_state.total_budget += total_maybach_price
            st.toast(f"✅ Maybach reserved for {hours_maybach} hours!", icon="🚗")
        st.markdown("</div>", unsafe_allow_html=True)

    with r_col2:
        st.markdown("""<div class='dynamic-card'>""", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1536531388554-7f123fcd1059?auto=format&fit=crop&w=800&q=80", use_container_width=True)
        st.markdown("### Vintage Rolls Royce")
        st.markdown("Base Price: **$250 / Hour**")
        
        hours_rolls = st.slider("Select Rental Duration (Hours)", min_value=2, max_value=12, value=4, key="slider_r")
        total_rolls_price = hours_rolls * 250
        
        st.metric(label="Estimated Cost", value=f"${total_rolls_price}")
        
        if st.button("Reserve Ride", key="r2_btn", type="primary", use_container_width=True):
            st.session_state.wedding_cart.append({"item": f"Rolls Royce ({hours_rolls} Hrs)", "price": total_rolls_price})
            st.session_state.total_budget += total_rolls_price
            st.toast(f"✅ Rolls Royce reserved for {hours_rolls} hours!", icon="🚗")
        st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: My Wedding Planner (Dynamic Cart & Checkout) ---
with tab3:
    st.markdown("<div class='cart-box'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:white; margin-top:0;'>📋 Your Customized Wedding Plan</h2>", unsafe_allow_html=True)
    
    if len(st.session_state.wedding_cart) == 0:
        st.warning("Your planner is currently empty. Please add venues or rides from the tabs above.")
    else:
        for i, item in enumerate(st.session_state.wedding_cart):
            st.markdown(f"**{i+1}. {item['item']}**  ..........  **${item['price']}**")
        
        st.markdown("---")
        st.markdown(f"<h3 style='color:#D4AF37;'>Grand Total: ${st.session_state.total_budget}</h3>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💳 Proceed to Secure Checkout", type="primary"):
            st.balloons()
            st.success("Redirecting to secure payment gateway... (Mock Checkout Complete!)")
            
        if st.button("🗑️ Clear Planner"):
            st.session_state.wedding_cart = []
            st.session_state.total_budget = 0
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)
