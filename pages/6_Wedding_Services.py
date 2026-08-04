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
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border: 1px solid #EAEAEA;
        border-left: 8px solid #D4AF37;
        transition: transform 0.3s ease;
    }
    .step-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(212, 175, 55, 0.25);
    }
    
    /* Royal Background for Service Number + Main Heading Combined */
    .service-main-title-box {
        background: linear-gradient(135deg, #0F2027 0%, #203A43 50%, #2C5364 100%);
        color: white;
        padding: 12px 18px;
        border-radius: 10px;
        margin-bottom: 12px;
        border-bottom: 3px solid #D4AF37;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .step-badge {
        background: #D4AF37;
        color: #0F2027;
        padding: 4px 12px;
        border-radius: 50px;
        font-weight: 900;
        font-size: 0.95rem;
        text-transform: uppercase;
    }

    /* Colorful Background for Sub-heading / Title */
    .service-sub-title-box {
        background: linear-gradient(135deg, #E2E8F0 0%, #CBD5E1 100%);
        border-left: 5px solid #2563EB;
        color: #1E3A8A;
        padding: 10px 15px;
        border-radius: 8px;
        margin-bottom: 10px;
        font-weight: 800;
        font-size: 1.1rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    /* Description Box */
    .service-desc-text {
        color: #334155;
        font-size: 0.95rem;
        line-height: 1.5;
        margin-bottom: 15px;
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
st.markdown("<p style='text-align:center; font-size:1.2rem; color:gray;'>Step-by-step verified wedding services with royal formatting. Track your grand total in real-time (₹).</p>", unsafe_allow_html=True)
st.markdown("---")

# 5. Dynamic Tabs for Services & Cart
tab1, tab2 = st.tabs(["📋 Step-by-Step Wedding Services Master List", "🛒 My Wedding Planner Cart"])

with tab1:
    st.markdown("### 🛠️ All-in-One Wedding Services Master Checklist")
    st.write("Browse through all essential wedding categories, view images, and add them directly to your custom planner.")
    st.markdown("<br>", unsafe_allow_html=True)

    # Helper function to render service cards cleanly with exact requested formatting
    def render_service_card(step_num, title, img_url, sub_title, desc, price_text, button_key, cart_item_name, price_val):
        st.markdown("<div class='step-box'>", unsafe_allow_html=True)
        
        # Combined Royal Background for Service Number + Main Title
        st.markdown(f"""
        <div class='service-main-title-box'>
            <span class='step-badge'>Service {step_num}</span>
            <h3 style='margin:0; color:#FBF5B7; font-family: Georgia, serif; font-size: 1.35rem;'>{title}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns([1, 2], gap="medium")
        with c1:
            st.image(img_url, use_container_width=True)
        with c2:
            # Colorful Background for Sub-heading / Title
            st.markdown(f"""
            <div class='service-sub-title-box'>
                {sub_title}
            </div>
            """, unsafe_allow_html=True)
            
            # Description text
            st.markdown(f"""
            <div class='service-desc-text'>
                {desc}
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"<span class='price-tag'>{price_text}</span>", unsafe_allow_html=True)
            
            if st.button(f"➕ Add to Cart", key=button_key, use_container_width=True):
                st.session_state.wedding_cart.append({"item": cart_item_name, "price": price_val})
                st.session_state.total_budget += price_val
                st.toast(f"✅ Added {cart_item_name} to Cart!", icon="🛒")
                
        st.markdown("</div>", unsafe_allow_html=True)

    # --- SERVICE 1 ---
    render_service_card(
        1, "Professional Wedding Planner & Management Agency",
        "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=600&q=80",
        "End-to-End Wedding Management & Coordination",
        "Complete event execution, guest hospitality, and logistics handled by top-rated professional planners.",
        "₹ 2,00,000 (Management Fee)", "btn_s1", "Professional Wedding Planner Agency", 200000
    )

    # --- SERVICE 2 ---
    render_service_card(
        2, "Banquet Hall, Lawn & Resort",
        "https://images.unsplash.com/photo-1519225421980-715cb0215aed?auto=format&fit=crop&w=600&q=80",
        "The Royal Orchid Banquet & Wedding Lawn",
        "Spacious air-conditioned hall with green lawn, stage setup, power backup, and guest stay rooms.",
        "₹ 1,50,000 / Day", "btn_s2", "Banquet Hall & Lawn", 150000
    )

    # --- SERVICE 3 ---
    render_service_card(
        3, "Designer Wedding Apparel (Outfits)",
        "https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=600&q=80",
        "Royal Bridal Lehenga & Groom Sherwani Package",
        "Exclusive designer wedding collection featuring traditional hand-embroidery and custom fitting.",
        "₹ 75,000", "btn_s3", "Designer Wedding Apparel", 75000
    )

    # --- SERVICE 4 ---
    render_service_card(
        4, "Wedding Jewelry & Ornaments",
        "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=600&q=80",
        "Certified Gold & Diamond Bridal Set",
        "Certified Hallmark gold necklace set, maang tikka, earrings, and traditional wedding ornaments.",
        "₹ 2,50,000 (Rental/Making Package)", "btn_s4", "Wedding Jewelry Set", 250000
    )

    # --- SERVICE 5 ---
    render_service_card(
        5, "Professional Makeup Artist & Grooming",
        "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?auto=format&fit=crop&w=600&q=80",
        "Celebrity Bridal & Groom Makeup Package",
        "HD airbrush bridal makeup, hair styling, draping, and groom grooming session by professional artists.",
        "₹ 35,000", "btn_s5", "Bridal & Groom Makeup Service", 35000
    )

    # --- SERVICE 6 ---
    render_service_card(
        6, "Cinematic Photography & Videography",
        "https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=600&q=80",
        "4K Cinematic Video, Drone & Candid Shoot",
        "Complete candid photography, traditional video, drone shots, pre-wedding shoot, and photo album.",
        "₹ 60,000", "btn_s6", "Cinematic Photography Package", 60000
    )

    # --- SERVICE 7 ---
    render_service_card(
        7, "Mandap, Stage & Floral Decoration",
        "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80",
        "Royal Floral Mandap & Lighting Setup",
        "Exotic fresh flower arrangements, grand entrance gate, ambient fairy lighting, and theme stage decoration.",
        "₹ 80,000", "btn_s7", "Mandap & Stage Decoration", 80000
    )

    # --- SERVICE 8 ---
    render_service_card(
        8, "Premium Catering & Food Service",
        "https://images.unsplash.com/photo-1555244162-803834f70033?auto=format&fit=crop&w=600&q=80",
        "Deluxe Multi-Cuisine Menu (Per 300 Guests)",
        "Welcome drinks, starters, North/South Indian main courses, live chaat counters, and exotic royal desserts.",
        "₹ 1,20,000", "btn_s8", "Catering Service (300 Guests)", 120000
    )

    # --- SERVICE 9 ---
    render_service_card(
        9, "Music, Entertainment & Live DJ",
        "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&w=600&q=80",
        "Professional DJ Setup, Sound & Dhol Group",
        "High-power JBL sound system, intelligent dance floor lighting, professional live DJ, and traditional Punjabi dhol.",
        "₹ 25,000", "btn_s9", "Music, Entertainment & DJ Package", 25000
    )

    # --- SERVICE 10 ---
    render_service_card(
        10, "Wedding Invitations & Digital Cards",
        "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=600&q=80",
        "Premium Boxed Invitations & WhatsApp Video Invite",
        "100 designer box invitation cards with dry fruits/sweets packing + Custom animated WhatsApp video invitation link.",
        "₹ 18,000", "btn_s10", "Wedding Invitations & Video Package", 18000
    )

    # --- SERVICE 11 (Fixed with proper Transportation Image) ---
    render_service_card(
        11, "Guest & Couple Transportation Services",
        "https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&w=600&q=80",
        "Luxury Bridal Car & Guest Buses (AC Tempo Traveller)",
        "Decorated luxury bridal car (Mercedes/Audi), plus 2 AC buses & tempo travellers for guest pickup and drop services.",
        "₹ 35,000", "btn_s11", "Transportation & Guest Fleet", 35000
    )

    # --- SERVICE 12 (Fixed with proper Ghodi, Buggy & Horse Carriage Image) ---
    render_service_card(
        12, "Royal Baraat: Ghodi, Buggy & Band",
        "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=600&q=80",
        "Royal Decorated Ghodi, Buggy & Brass Band",
        "Grand royal decorated Ghodi/Buggy for groom entry, traditional brass band team, lighting umbrella (Fanos), and fireworks.",
        "₹ 22,000", "btn_s12", "Royal Baraat (Ghodi, Buggy & Band)", 22000
    )

    # --- SERVICE 13 ---
    render_service_card(
        13, "Vedic Priest & Ritual Services",
        "https://images.unsplash.com/photo-1607344645866-009c320c5ab8?auto=format&fit=crop&w=600&q=80",
        "Experienced Acharya & Complete Pooja Samagri",
        "Experienced purohits for kundli matching, muhurat checking, engagement, and wedding phera rituals with complete samagri.",
        "₹ 11,000", "btn_s13", "Vedic Priest & Ritual Services", 11000
    )

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
