import streamlit as st

# 1. Page Configuration (सबसे ऊपर होना चाहिए)
st.set_page_config(
    page_title="Bandhan | Premium Matrimony & Ecosystem",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium Custom CSS (मल्टीनेशनल लुक के लिए)
st.markdown("""
    <style>
    /* मेन बैकग्राउंड और फॉन्ट */
    .stApp {
        background-color: #FAFAFA;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* हेडिंग स्टाइल (Royal Blue & Gold) */
    h1 {
        color: #0F2027;
        font-weight: 700;
        letter-spacing: 1px;
    }
    
    /* प्रीमियम कार्ड्स */
    .feature-box {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        text-align: center;
        border-bottom: 4px solid #D4AF37; /* Premium Gold border */
        transition: transform 0.3s ease;
    }
    .feature-box:hover {
        transform: translateY(-5px);
    }
    
    /* सब-हेडिंग और टैगलाइन */
    .tagline {
        font-size: 1.5rem;
        color: #555555;
        font-weight: 300;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Hero Section (Top Header & Image)
col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title("Bandhan.com 💍")
    st.markdown("""
        <p class="tagline">
        <b>रिश्ते वही, सोच नई।</b><br>
        दुनिया का पहला AI-पावर्ड मैट्रिमोनियल प्लेटफॉर्म और वेडिंग इकोसिस्टम। <br>
        सही जीवनसाथी चुनने से लेकर, शादी के मंडप और हनीमून तक—सब कुछ एक ही जगह।
        </p>
    """, unsafe_allow_html=True)
    
    # Call to action button
    st.button("अपना प्रीमियम प्रोफाइल बनाएँ (Free)", type="primary", use_container_width=True)

with col2:
    # प्रीमियम कपल/वेडिंग इमेज
    st.image("https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=800&q=80", 
             caption="The Perfect Match Awaits", use_container_width=True)

st.markdown("<hr style='border: 1px solid #EAEAEA;'>", unsafe_allow_html=True)

# 4. Features Section (Ecosystem & AI)
st.markdown("<h2 style='text-align: center; color: #1A365D;'>The Bandhan Ecosystem</h2><br>", unsafe_allow_html=True)

f_col1, f_col2, f_col3 = st.columns(3, gap="medium")

with f_col1:
    st.image("https://images.unsplash.com/photo-1573164713988-8665fc963095?auto=format&fit=crop&w=500&q=80", use_container_width=True)
    st.markdown("""
        <div class="feature-box">
            <h3 style='color:#D4AF37;'>🤖 AI Matchmaking</h3>
            <p>हमारी स्मार्ट AI तकनीक आपके व्यक्तित्व, पसंद और आदतों का विश्लेषण करके सबसे सटीक और योग्य रिश्ते सुझाती है।</p>
        </div>
    """, unsafe_allow_html=True)

with f_col2:
    st.image("https://images.unsplash.com/photo-1519225421980-715cb0215aed?auto=format&fit=crop&w=500&q=80", use_container_width=True)
    st.markdown("""
        <div class="feature-box">
            <h3 style='color:#D4AF37;'>🛍️ Complete Ecosystem</h3>
            <p>डिजाइनर कपड़े, लग्जरी गाड़ियां, बैंक्वेट हॉल, और कैटरिंग। शादी की हर ज़रूरत के लिए हमारे वेरिफाइड वेंडर्स उपलब्ध हैं।</p>
        </div>
    """, unsafe_allow_html=True)

with f_col3:
    st.image("https://images.unsplash.com/photo-1520854221256-17451cc331bf?auto=format&fit=crop&w=500&q=80", use_container_width=True)
    st.markdown("""
        <div class="feature-box">
            <h3 style='color:#D4AF37;'>🔒 100% Secure</h3>
            <p>आधार और पैन वेरिफिकेशन। आपकी तस्वीरें और जानकारी पूरी तरह से सुरक्षित हैं, आप तय करते हैं कि किसे क्या दिखाना है।</p>
        </div>
    """, unsafe_allow_html=True)

# 5. Footer Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; color: #888888; padding: 20px;'>
        <p>Bandhan.com © 2026 | Matrimony • Planning • Vendors • Honeymoon</p>
    </div>
""", unsafe_allow_html=True)
