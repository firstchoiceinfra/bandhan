import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Wedding Ecosystem | Bandhan",
    page_icon="🛍️",
    layout="wide"
)

# 2. Premium Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #FDFDFD;
    }
    .eco-header {
        color: #0F2027;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        font-size: 2.2rem;
    }
    .gold-text {
        color: #D4AF37;
    }
    
    /* Vendor Card Styling */
    .vendor-card {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.06);
        text-align: center;
        border-bottom: 3px solid #1A365D;
        margin-bottom: 20px;
        transition: transform 0.3s;
    }
    .vendor-card:hover {
        transform: translateY(-5px);
    }
    .vendor-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #1A365D;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    .vendor-rating {
        color: #F39C12;
        font-weight: bold;
        font-size: 0.9rem;
        margin-bottom: 10px;
    }
    .price-tag {
        color: #27AE60;
        font-weight: bold;
        background-color: #EAFDF0;
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
        margin-bottom: 15px;
    }
    
    /* Subtitles */
    .sub-text {
        font-size: 1.1rem;
        color: #555555;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Page Header
st.markdown("<h1 class='eco-header'>The Bandhan <span class='gold-text'>Wedding Ecosystem</span> 🛍️</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Plan your dream wedding with our verified, premium partners. From luxury venues to honeymoon packages, book everything in one click.</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. Dynamic Tabs for Ecosystem Categories
tab1, tab2, tab3, tab4 = st.tabs(["🏰 Luxury Venues", "🚗 Premium Rides", "👗 Designer Apparel", "✈️ Honeymoons"])

# --- TAB 1: Luxury Venues ---
with tab1:
    st.markdown("### **Handpicked Premium Venues**")
    v_col1, v_col2, v_col3 = st.columns(3)
    
    with v_col1:
        st.image("https://images.unsplash.com/photo-1519225421980-715cb0215aed?auto=format&fit=crop&w=500&q=80", use_container_width=True)
        st.markdown("""
            <div class="vendor-card">
                <div class="vendor-title">The Royal Orchid Banquet</div>
                <div class="vendor-rating">⭐⭐⭐⭐⭐ (4.9/5)</div>
                <div class="price-tag">Starts at $5,000 / day</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Request Quote", key="venue1", use_container_width=True)

    with v_col2:
        st.image("https://images.unsplash.com/photo-1469371670807-013ccf25f16a?auto=format&fit=crop&w=500&q=80", use_container_width=True)
        st.markdown("""
            <div class="vendor-card">
                <div class="vendor-title">Sunset Beach Resort (Destination)</div>
                <div class="vendor-rating">⭐⭐⭐⭐⭐ (4.8/5)</div>
                <div class="price-tag">Starts at $12,000 / package</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Request Quote", key="venue2", use_container_width=True)
        
    with v_col3:
        st.image("https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=500&q=80", use_container_width=True)
        st.markdown("""
            <div class="vendor-card">
                <div class="vendor-title">Heritage Palace Courtyard</div>
                <div class="vendor-rating">⭐⭐⭐⭐⭐ (5.0/5)</div>
                <div class="price-tag">Starts at $8,500 / day</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Request Quote", key="venue3", use_container_width=True)

# --- TAB 2: Premium Rides ---
with tab2:
    st.markdown("### **Arrive in Style**")
    r_col1, r_col2 = st.columns(2)
    
    with r_col1:
        st.image("https://images.unsplash.com/photo-1536531388554-7f123fcd1059?auto=format&fit=crop&w=600&q=80", use_container_width=True)
        st.markdown("""
            <div class="vendor-card">
                <div class="vendor-title">Vintage Rolls Royce (1960)</div>
                <div class="price-tag">$500 / 4 Hours</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Book Ride", key="ride1", type="primary")

    with r_col2:
        st.image("https://images.unsplash.com/photo-1503376712356-6552988147d3?auto=format&fit=crop&w=600&q=80", use_container_width=True)
        st.markdown("""
            <div class="vendor-card">
                <div class="vendor-title">Mercedes-Maybach S-Class</div>
                <div class="price-tag">$800 / Day</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Book Ride", key="ride2", type="primary")

# --- TAB 3: Designer Apparel ---
with tab3:
    st.info("Browse exclusive collections from top designers like Sabyasachi, Manish Malhotra, and international bespoke tailors. Virtual try-on (AR) coming soon!")
    # You can add more cards here similarly

# --- TAB 4: Honeymoons ---
with tab4:
    st.markdown("### **Premium Getaways**")
    st.image("https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?auto=format&fit=crop&w=1000&q=80", use_container_width=True)
    st.markdown("#### The Maldives Ultra-Luxury Experience")
    st.markdown("7 Days / 6 Nights | Private Water Villa | Personal Butler")
    st.button("View Honeymoon Itinerary", type="primary")
