import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Royal Budget Planner | Bandhan", page_icon="💰", layout="wide")

# 2. Premium CSS for the Page
st.markdown("""
    <style>
    .stApp { background-color: #FAFAFA; }
    
    /* Title Container with Dark Royal Gradient and Stickers */
    .premium-title-container {
        position: relative;
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        padding: 40px 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        border: 2px solid #D4AF37;
        margin-bottom: 30px;
    }
    
    /* Golden Gradient Text for Heading */
    .premium-title {
        font-family: 'Georgia', serif;
        font-size: 3.5rem;
        font-weight: 900;
        margin: 0;
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    /* Stickers */
    .sticker-left {
        position: absolute; top: -25px; left: -20px; width: 90px; transform: rotate(-15deg);
        filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.3));
    }
    .sticker-right {
        position: absolute; bottom: -25px; right: -20px; width: 90px; transform: rotate(15deg);
        filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.3));
    }
    
    /* Grand Total Box */
    .total-box { 
        background: linear-gradient(135deg, #D4AF37 0%, #AA771C 100%); 
        color: white; padding: 20px; border-radius: 12px; text-align: center; 
        font-size: 2.2rem; font-weight: bold; box-shadow: 0 10px 20px rgba(212, 175, 55, 0.3); 
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# 3. The Attractive Header Section with Stickers
st.markdown("""
    <div class="premium-title-container">
        <!-- Diamond/Ring Sticker on Top Left -->
        <img src="https://cdn-icons-png.flaticon.com/512/3655/3655645.png" class="sticker-left">
        
        <h1 class="premium-title">AI Wedding Budget</h1>
        <p style="color:#FBF5B7; font-size:1.2rem; margin-top:10px; font-style:italic;">Plan Your Dream Royal Wedding Flawlessly</p>
        
        <!-- Wedding Bell Sticker on Bottom Right -->
        <img src="https://cdn-icons-png.flaticon.com/512/7580/7580327.png" class="sticker-right">
    </div>
""", unsafe_allow_html=True)

# 4. Budget Input Section
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown("### 🎯 Step 1: Set Total Budget")
    total_budget = st.number_input("Enter Amount (in INR ₹)", min_value=100000, max_value=50000000, value=2500000, step=50000)
    
    st.markdown("### 👥 Step 2: Guest Count")
    guests = st.slider("Estimated Number of Guests", 50, 2000, 500)
    
    st.button("🔄 Recalculate AI Plan", type="primary", use_container_width=True)

with col2:
    st.markdown(f"<div class='total-box'>Grand Total: ₹ {total_budget:,.0f}</div><br>", unsafe_allow_html=True)
    
    # AI Logic for Budget Breakdown
    venue_cat = int(total_budget * 0.40)
    jewelry = int(total_budget * 0.25)
    apparel = int(total_budget * 0.15)
    photo_misc = int(total_budget * 0.20)
    
    st.markdown("### 📊 Recommended Breakdown")
    
    # Custom Function to Create Premium Image Cards
    def create_budget_card(title, amount, percentage, img_url, color):
        return f"""
        <div style="display:flex; background:white; border-radius:15px; margin-bottom:15px; box-shadow:0 8px 20px rgba(0,0,0,0.06); overflow:hidden; border:1px solid #EAEAEA; border-left:6px solid {color}; transition: transform 0.3s;">
            <img src="{img_url}" style="width:140px; object-fit:cover;">
            <div style="padding:15px; width:100%; display:flex; flex-direction:column; justify-content:center;">
                <h4 style="margin:0; color:#1A365D; font-size:1.1rem;">{title} ({percentage}%)</h4>
                <h2 style="margin:5px 0; color:#27AE60; font-weight:800;">₹ {amount:,.0f}</h2>
                <div style="background:#F0F0F0; border-radius:10px; height:8px; width:100%; margin-top:5px;">
                    <div style="background:{color}; width:{percentage}%; height:100%; border-radius:10px;"></div>
                </div>
            </div>
        </div>
        """

    # 1. Venue & Catering Card
    st.markdown(create_budget_card(
        "🏰 Venue & Premium Catering", venue_cat, 40, 
        "https://images.unsplash.com/photo-1519225421980-715cb0215aed?auto=format&fit=crop&w=400&q=80", 
        "#D4AF37"
    ), unsafe_allow_html=True)
    
    # 2. Jewelry Card
    st.markdown(create_budget_card(
        "💍 Wedding Jewelry & Ornaments", jewelry, 25, 
        "https://images.unsplash.com/photo-1599643477874-5c866f5c88c7?auto=format&fit=crop&w=400&q=80", 
        "#8E44AD"
    ), unsafe_allow_html=True)
    
    # 3. Designer Apparel Card
    st.markdown(create_budget_card(
        "👗 Designer Apparel & Styling", apparel, 15, 
        "https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=400&q=80", 
        "#E74C3C"
    ), unsafe_allow_html=True)
    
    # 4. Photography & Music Card
    st.markdown(create_budget_card(
        "📸 Photography, Music & Misc", photo_misc, 20, 
        "https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=400&q=80", 
        "#2980B9"
    ), unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)
st.info("💡 **AI Tip:** Booking your venue 6 months in advance can save you up to 15% on catering costs. Check our 'Wedding Ecosystem' tab for exclusive deals.")
