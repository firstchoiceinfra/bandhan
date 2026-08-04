import streamlit as st
import time

# 1. Page Configuration (सबसे ऊपर होना चाहिए)
st.set_page_config(
    page_title="AI Matchmaking | Bandhan",
    page_icon="🧬",
    layout="wide"
)

# 2. Premium Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #FAFAFA;
    }
    .header-text {
        color: #0F2027;
        font-family: 'Trebuchet MS', sans-serif;
        font-weight: 800;
        font-size: 2.2rem;
    }
    .gold-text {
        color: #D4AF37;
    }
    
    /* Profile Card Styling */
    .profile-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-top: 3px solid #1A365D;
        margin-bottom: 20px;
    }
    .match-score {
        color: #27AE60;
        font-weight: bold;
        font-size: 1.2rem;
        margin-bottom: 5px;
    }
    .profile-name {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1A365D;
        margin-bottom: 5px;
    }
    .profile-details {
        color: #666666;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Page Header
st.markdown("<h1 class='header-text'>Bandhan <span class='gold-text'>AI Matchmaking</span> 🧬</h1>", unsafe_allow_html=True)
st.markdown("Our proprietary AI algorithm analyzes 50+ data points to find your perfect match.")
st.markdown("---")

# 4. Sidebar for Manual Filters
st.sidebar.header("🎯 Refine Search")
age_filter = st.sidebar.slider("Age Range", 21, 60, (24, 32))
religion_filter = st.sidebar.multiselect("Religion", ["Hindu", "Muslim", "Sikh", "Christian", "Jain"], default=["Hindu"])
income_filter = st.sidebar.selectbox("Minimum Income", ["Any", "$50k+", "$100k+", "$200k+"])
st.sidebar.button("Apply Filters", type="primary", use_container_width=True)

# 5. The AI Matching Simulation
if 'ai_run' not in st.session_state:
    st.session_state.ai_run = False

col1, col2 = st.columns([1, 4])
with col1:
    run_ai = st.button("🚀 Run AI Smart Search", type="primary", use_container_width=True)

if run_ai:
    with st.spinner('AI is analyzing behavioral traits and preferences...'):
        time.sleep(2) # AI के सोचने का एनिमेशन (2 सेकंड)
        st.session_state.ai_run = True

# 6. Displaying Matches
if st.session_state.ai_run:
    st.success("✅ AI Analysis Complete. Here are your highly-compatible matches.")
    
    # Mock Data for Profiles
    profiles = [
        {
            "name": "Priya Sharma", "age": 27, "profession": "Software Engineer", 
            "location": "Mumbai, India", "match": "98%", "img": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "Aisha Khan", "age": 26, "profession": "Architect", 
            "location": "Dubai, UAE", "match": "94%", "img": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "Neha Patel", "age": 28, "profession": "Investment Banker", 
            "location": "London, UK", "match": "91%", "img": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80"
        }
    ]
    
    # Create rows of profiles
    p_col1, p_col2, p_col3 = st.columns(3)
    cols = [p_col1, p_col2, p_col3]
    
    for i, profile in enumerate(profiles):
        with cols[i]:
            st.image(profile["img"], use_container_width=True)
            st.markdown(f"""
                <div class="profile-card">
                    <div class="match-score">⭐ {profile['match']} AI Match</div>
                    <div class="profile-name">{profile['name']}, {profile['age']}</div>
                    <div class="profile-details">
                        💼 <b>Profession:</b> {profile['profession']}<br>
                        📍 <b>Location:</b> {profile['location']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Action Buttons
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.button("Send Request", key=f"req_{i}", type="primary", use_container_width=True)
            with btn_col2:
                st.button("View Profile", key=f"view_{i}", use_container_width=True)
else:
    st.info("👈 Click on 'Run AI Smart Search' to let our algorithm find your perfect matches, or use the sidebar filters for manual searching.")
