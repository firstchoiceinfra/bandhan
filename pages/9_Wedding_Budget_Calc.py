import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Wedding Budget | Bandhan", page_icon="💰", layout="wide")

# 2. Premium CSS for the Page
st.markdown("""
    <style>
    /* Attractive Page Background */
    .stApp { 
        background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
    }
    
    /* Title Container with Dark Royal Gradient */
    .premium-title-container {
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        padding: 30px 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        border: 2px solid #D4AF37;
        margin-bottom: 30px;
    }
    
    /* Flexbox to keep stickers inside the frame next to text */
    .title-flex {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        flex-wrap: wrap;
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
    
    /* Colorful Inner Stickers */
    .inner-sticker {
        width: 75px;
        filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.4));
    }
    
    /* Step Headers Background Styling */
    .step-header {
        background: linear-gradient(135deg, #1A365D 0%, #0F2027 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 12px;
        font-size: 1.4rem;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 15px;
        border-left: 6px solid #D4AF37;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
    }
    
    .step-icon {
        width: 35px;
        height: 35px;
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

# 3. The Attractive Header Section (Stickers are now inside the frame)
st.markdown("""
<div class="premium-title-container">
<div class="title-flex">
<img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" class="inner-sticker">
<h1 class="premium-title">Wedding Budget</h1>
<img src="https://cdn-icons-png.flaticon.com/512/2953/2953363.png" class="inner-sticker">
</div>
<p style="color:#FBF5B7; font-size:1.2rem; margin-top:10px; font-style:italic;">Plan Your Dream Royal Wedding Flawlessly</p>
</div>
""", unsafe_allow_html=True)

# 4. Budget Input Section
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    # Step 1 with Background and Icon
    st.markdown("""
    <div class="step-header">
    <img src="https://cdn-icons-png.flaticon.com/512/5501/5501375.png" class="step-icon">
    Step 1: Set Total Budget
    </div>
    """, unsafe_allow_html=True)
    total_budget = st.number_input("Enter Amount (in INR ₹)", min_value=100000, max_value=50000000, value=2500000, step=50000)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Step 2 with Background and Icon
    st.markdown("""
    <div class="step-header">
    <img src="https://cdn-icons-png.flaticon.com/512/3126/3126647.png" class="step-icon">
    Step 2: Guest Count
    </div>
    """, unsafe_allow_html=True)
    guests = st.slider("Estimated Number of Guests", 50, 2000, 500)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("🔄 Recalculate Plan", type="primary", use_container_width=True)

with col2:
    st.markdown(f"<div class='total-box'>Grand Total: ₹ {total_budget:,.0f}</div><br>", unsafe_allow_html=True)
    
    # Logic for Budget Breakdown
    venue_cat = int(total_budget * 0.40)
    jewelry = int(total_budget * 0.25)
    apparel = int(total_budget * 0.15)
    photo_misc = int(total_budget * 0.20)
    
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
    
    # 2. Jewelry Card (Fixed Image URL)
    st.markdown(create_budget_card(
        "💍 Wedding Jewelry & Ornaments", jewelry, 25, 
        "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=400&q=80", 
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
