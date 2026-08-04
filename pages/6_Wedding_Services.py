import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Wedding Services | Bandhan",
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
    .step-box {
        background: white;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.06);
        border: 1px solid #EAEAEA;
        border-left: 6px solid #D4AF37;
        transition: transform 0.3s ease;
    }
    .step-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 25px rgba(212, 175, 55, 0.2);
    }
    .step-number {
        background: #1A365D;
        color: white;
        padding: 5px 12px;
        border-radius: 50px;
        font-weight: bold;
        font-size: 1rem;
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
st.markdown("<h1 class='main-header'>Complete Wedding Services & Management</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:1.2rem; color:gray;'>Step-by-step verified wedding services including transportation, DJ, invitations, and baraat. Track your grand total in real-time (₹).</p>", unsafe_allow_html=True)
st.markdown("---")

# 5. Dynamic Tabs for Services & Cart
tab1, tab2 = st.tabs(["📋 Step-by-Step Wedding Services Master List", "🛒 My Wedding Planner Cart"])

with tab1:
    st.markdown("### 🛠️ All-in-One Wedding Services Master Checklist")
    st.write("Browse through all essential wedding categories, view images, and add them directly to your custom planner.")
    st.markdown("<br>", unsafe_allow_html=True)

    # --- SERVICE 1: Professional Wedding Planner & Management Agency ---
    st.markdown("<div class='step-box'><span class='step-number'>Service 1</span><h2 style='display:inline; margin-left:10px; color:#1A365D;'>📋 Professional Wedding Planner & Management Agency</h2></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    with c2:
        st.markdown("### End-to-End Wedding Management & Coordination")
        st.write("Complete event execution, guest hospitality, and logistics handled by top-rated professional planners.")
        st.markdown("<span class='price-tag'>₹ 2,00,000 (Management Fee)</span>", unsafe_allow_html=True)
        if st.button("➕ Add Wedding Planner to Cart", key="btn_planner"):
            st.session_state.wedding_cart.append({"item": "Professional Wedding Planner Agency", "price": 200000})
            st.session_state.total_budget += 200000
            st.toast("✅ Added Wedding Planner Agency to Cart!", icon="📋")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SERVICE 2: Hall / Lawn (Venues) ---
    st.markdown("<div class='step-box'><span class='step-number'>Service 2</span><h2 style='display:inline; margin-left:10px; color:#1A365D;'>🏰 Banquet Hall, Lawn & Resort</h2></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1519225421980-715cb0215aed?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    with c2:
        st.markdown("### The Royal Orchid Banquet & Wedding Lawn")
        st.write("Spacious air-conditioned hall with green lawn, stage setup, power backup, and guest stay rooms.")
        st.markdown("<span class='price-tag'>₹ 1,50,000 / Day</span>", unsafe_allow_html=True)
        if st.button("➕ Add Hall/Lawn to Cart", key="btn_step1"):
            st.session_state.wedding_cart.append({"item": "Banquet Hall & Lawn", "price": 150000})
            st.session_state.total_budget += 150000
            st.toast("✅ Added Banquet Hall to Cart!", icon="🏰")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SERVICE 3: Apparel (कपड़े) ---
    st.markdown("<div class='step-box'><span class='step-number'>Service 3</span><h2 style='display:inline; margin-left:10px; color:#1A365D;'>👗 Designer Wedding Apparel (Outfits)</h2></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    with c2:
        st.markdown("### Royal Bridal Lehenga & Groom Sherwani Package")
        st.write("Exclusive designer wedding collection featuring traditional hand-embroidery and custom fitting.")
        st.markdown("<span class='price-tag'>₹ 75,000</span>", unsafe_allow_html=True)
        if st.button("➕ Add Apparel Package to Cart", key="btn_step2"):
            st.session_state.wedding_cart.append({"item": "Designer Wedding Apparel", "price": 75000})
            st.session_state.total_budget += 75000
            st.toast("✅ Added Apparel Package to Cart!", icon="👗")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SERVICE 4: Jewelry (गहने) ---
    st.markdown("<div class='step-box'><span class='step-number'>Service 4</span><h2 style='display:inline; margin-left:10px; color:#1A365D;'>💍 Wedding Jewelry & Ornaments</h2></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    with c2:
        st.markdown("### Certified Gold & Diamond Bridal Set")
        st.write("Certified Hallmark gold necklace set, maang tikka, earrings, and traditional wedding ornaments.")
        st.markdown("<span class='price-tag'>₹ 2,50,000 (Rental/Making Package)</span>", unsafe_allow_html=True)
        if st.button("➕ Add Jewelry Package to Cart", key="btn_step3"):
            st.session_state.wedding_cart.append({"item": "Wedding Jewelry Set", "price": 250000})
            st.session_state.total_budget += 250000
            st.toast("✅ Added Jewelry Package to Cart!", icon="💍")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SERVICE 5: Makeup Artist (मेकअप) ---
    st.markdown("<div class='step-box'><span class='step-number'>Service 5</span><h2 style='display:inline; margin-left:10px; color:#1A365D;'>💄 Professional Makeup Artist & Grooming</h2></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    with c2:
        st.markdown("### Celebrity Bridal & Groom Makeup Package")
        st.write("HD airbrush bridal makeup, hair styling, draping, and groom grooming session by professional artists.")
        st.markdown("<span class='price-tag'>₹ 35,000</span>", unsafe_allow_html=True)
        if st.button("➕ Add Makeup Service to Cart", key="btn_step4"):
            st.session_state.wedding_cart.append({"item": "Bridal & Groom Makeup Service", "price": 35000})
            st.session_state.total_budget += 35000
            st.toast("✅ Added Makeup Service to Cart!", icon="💄")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SERVICE 6: Photographer (फोटोग्राफर) ---
    st.markdown("<div class='step-box'><span class='step-number'>Service 6</span><h2 style='display:inline; margin-left:10px; color:#1A365D;'>📸 Cinematic Photography & Videography</h2></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    with c2:
        st.markdown("### 4K Cinematic Video, Drone & Candid Shoot")
        st.write("Complete candid photography, traditional video, drone shots, pre-wedding shoot, and photo album.")
        st.markdown("<span class='price-tag'>₹ 60,000</span>", unsafe_allow_html=True)
        if st.button("➕ Add Photography to Cart", key="btn_step5"):
            st.session_state.wedding_cart.append({"item": "Cinematic Photography Package", "price": 60000})
            st.session_state.total_budget += 60000
            st.toast("✅ Added Photography to Cart!", icon="📸")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SERVICE 7: Decoration (डेकोरेशन) ---
    st.markdown("<div class='step-box'><span class='step-number'>Service 7</span><h2 style='display:inline; margin-left:10px; color:#1A365D;'>🌺 Mandap, Stage & Floral Decoration</h2></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    with c2:
        st.markdown("### Royal Floral Mandap & Lighting Setup")
        st.write("Exotic fresh flower arrangements, grand entrance gate, ambient fairy lighting, and theme stage decoration.")
        st.markdown("<span class='price-tag'>₹ 80,000</span>", unsafe_allow_html=True)
        if st.button("➕ Add Decoration to Cart", key="btn_step6"):
            st.session_state.wedding_cart.append({"item": "Mandap & Stage Decoration", "price": 80000})
            st.session_state.total_budget += 80000
            st.toast("✅ Added Decoration to Cart!", icon="🌺")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SERVICE 8: Catering (कैटरिंग) ---
    st.markdown("<div class='step-box'><span class='step-number'>Service 8</span><h2 style='display:inline; margin-left:10px; color:#1A365D;'>🍽️ Premium Catering & Food Service</h2></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1555244162-803834f70033?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    with c2:
        st.markdown("### Deluxe Multi-Cuisine Menu (Per 300 Guests)")
        st.write("Welcome drinks, starters, North/South Indian main courses, live chaat counters, and exotic royal desserts.")
        st.markdown("<span class='price-tag'>₹ 1,20,000</span>", unsafe_allow_html=True)
        if st.button("➕ Add Catering to Cart", key="btn_step7"):
            st.session_state.wedding_cart.append({"item": "Catering Service (300 Guests)", "price": 120000})
            st.session_state.total_budget += 120000
            st.toast("✅ Added Catering to Cart!", icon="🍽️")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SERVICE 9: Music & Entertainment / DJ (संगीत और डीजे) ---
    st.markdown("<div class='step-box'><span class='step-number'>Service 9</span><h2 style='display:inline; margin-left:10px; color:#1A365D;'>🎵 Music, Entertainment & Live DJ</h2></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    with c2:
        st.markdown("### Professional DJ Setup, Sound & Dhol Group")
        st.write("High-power JBL sound system, intelligent dance floor lighting, professional live DJ, and traditional Punjabi dhol for sangeet & wedding.")
        st.markdown("<span class='price-tag'>₹ 25,000</span>", unsafe_allow_html=True)
        if st.button("➕ Add Music & DJ to Cart", key="btn_step9"):
            st.session_state.wedding_cart.append({"item": "Music, Entertainment & DJ Package", "price": 25000})
            st.session_state.total_budget += 25000
            st.toast("✅ Added Music & DJ to Cart!", icon="🎵")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SERVICE 10: Invitations & Cards (इनविटेशन कार्ड्स) ---
    st.markdown("<div class='step-box'><span class='step-number'>Service 10</span><h2 style='display:inline; margin-left:10px; color:#1A365D;'>💌 Wedding Invitations & Digital Cards</h2></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    with c2:
        st.markdown("### Premium Boxed Invitations & WhatsApp Video Invite")
        st.write("100 designer box invitation cards with dry fruits/sweets packing + Custom animated WhatsApp video invitation link.")
        st.markdown("<span class='price-tag'>₹ 18,000</span>", unsafe_allow_html=True)
        if st.button("➕ Add Invitations to Cart", key="btn_step10"):
            st.session_state.wedding_cart.append({"item": "Wedding Invitations & Video Package", "price": 18000})
            st.session_state.total_budget += 18000
            st.toast("✅ Added Invitations Package to Cart!", icon="💌")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SERVICE 11: Transportation (गाड़ियाँ और बसें) ---
    st.markdown("<div class='step-box'><span class='step-number'>Service 11</span><h2 style='display:inline; margin-left:10px; color:#1A365D;'>🚗 Guest & Couple Transportation Services</h2></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1503376712356-6552988147d3?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    with c2:
        st.markdown("### Luxury Bridal Car & Guest Buses (AC Tempo Traveller)")
        st.write("Decorated luxury bridal car (Mercedes/Audi), plus 2 AC buses & tempo travellers for guest pickup and drop services.")
        st.markdown("<span class='price-tag'>₹ 35,000</span>", unsafe_allow_html=True)
        if st.button("➕ Add Transportation to Cart", key="btn_step11"):
            st.session_state.wedding_cart.append({"item": "Transportation & Guest Fleet", "price": 35000})
            st.session_state.total_budget += 35000
            st.toast("✅ Added Transportation to Cart!", icon="🚗")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SERVICE 12: Baraat & Ghodi/Buggy (बरात, घोड़ी और बग्गी) ---
    st.markdown("<div class='step-box'><span class='step-number'>Service 12</span><h2 style='display:inline; margin-left:10px; color:#1A365D;'>🐎 Royal Baraat: Ghodi, Buggy & Band</h2></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    with c2:
        st.markdown("### Royal Decorated Ghodi, Buggy & Brass Band")
        st.write("Grand royal decorated Ghodi/Buggy for groom entry, traditional brass band team, lighting umbrella (Fanos), and fireworks.")
        st.markdown("<span class='price-tag'>₹ 22,000</span>", unsafe_allow_html=True)
        if st.button("➕ Add Baraat & Ghodi to Cart", key="btn_step12"):
            st.session_state.wedding_cart.append({"item": "Royal Baraat (Ghodi, Buggy & Band)", "price": 22000})
            st.session_state.total_budget += 22000
            st.toast("✅ Added Baraat & Ghodi to Cart!", icon="🐎")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SERVICE 13: Rituals & Pandit Ji (पंडित जी) ---
    st.markdown("<div class='step-box'><span class='step-number'>Service 13</span><h2 style='display:inline; margin-left:10px; color:#1A365D;'>🕉️ Vedic Priest & Ritual Services</h2></div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image("https://images.unsplash.com/photo-1607344645866-009c320c5ab8?auto=format&fit=crop&w=600&q=80", use_container_width=True)
    with c2:
        st.markdown("### Experienced Acharya & Complete Pooja Samagri")
        st.write("Experienced purohits for kundli matching, muhurat checking, engagement, and wedding phera rituals with complete samagri.")
        st.markdown("<span class='price-tag'>₹ 11,000</span>", unsafe_allow_html=True)
        if st.button("➕ Add Priest Services to Cart", key="btn_step13"):
            st.session_state.wedding_cart.append({"item": "Vedic Priest & Ritual Services", "price": 11000})
            st.session_state.total_budget += 11000
            st.toast("✅ Added Priest Services to Cart!", icon="🕉️")

# --- TAB 2: My Wedding Planner Cart ---
with tab2:
    st.markdown("<div class='cart-box'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:white; margin-top:0;'>🛒 Your Wedding Services Cart</h2>", unsafe_allow_html=True)
    
    if len(st.session_state.wedding_cart) == 0:
        st.warning("Your cart is currently empty. Please select services step-by-step from the previous tab.")
    else:
        for i, item in enumerate(st.session_state.wedding_cart):
            st.markdown(f"**{i+1}. {item['item']}**  ..........  **₹ {item['price']:,}**")
        
        st.markdown("---")
        st.markdown(f"<h3 style='color:#D4AF37;'>Grand Total Budget: ₹ {st.session_state.total_budget:,}</h3>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💳 Proceed to Secure Booking", type="primary"):
            st.balloons()
            st.success("Redirecting to secure payment gateway... (Booking Confirmed Successfully!)")
            
        if st.button("🗑️ Clear All Services"):
            st.session_state.wedding_cart = []
            st.session_state.total_budget = 0
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)
