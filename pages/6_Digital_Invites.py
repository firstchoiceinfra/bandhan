import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Digital E-Invites | Bandhan",
    page_icon="💌",
    layout="wide"
)

# 2. Premium Creative CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #FCFBF9;
    }
    .invite-header {
        background: -webkit-linear-gradient(45deg, #8E2DE2, #4A00E0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Georgia', serif;
        font-weight: 900;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 10px;
    }
    .template-card {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.08);
        text-align: center;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    .template-card:hover {
        border: 2px solid #4A00E0;
        transform: translateY(-5px);
    }
    .highlight {
        color: #D4AF37;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("<h1 class='invite-header'>Design Your Royal E-Invite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:1.2rem; color:#555;'>Create stunning promotional banners and animated video scripts for your big day.</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. Interactive Tabs for Different Formats
tab1, tab2 = st.tabs(["🖼️ Static Promotional Banners", "🎬 Animated Video Invites"])

# --- TAB 1: Promotional Banners / Brochures ---
with tab1:
    st.markdown("### **1. Select a Banner Theme**")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='template-card'>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1544928147-79a2dbc1f389?auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("#### Royal Heritage")
        theme1 = st.button("Select Royal", key="t1", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='template-card'>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("#### Modern Minimalist")
        theme2 = st.button("Select Modern", key="t2", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col3:
        st.markdown("<div class='template-card'>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1465495976277-4387d4b0b4c6?auto=format&fit=crop&w=400&q=80", use_container_width=True)
        st.markdown("#### Floral Elegance")
        theme3 = st.button("Select Floral", key="t3", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>### **2. Enter Your Layout Details**", unsafe_allow_html=True)
    with st.form("banner_form"):
        f_col1, f_col2 = st.columns(2)
        groom_name = f_col1.text_input("Groom's Name", placeholder="e.g., Rahul")
        bride_name = f_col2.text_input("Bride's Name", placeholder="e.g., Anjali")
        wedding_date = st.date_input("Wedding Date")
        venue_text = st.text_input("Venue / Location", placeholder="e.g., The Royal Orchid Banquet, Nagpur")
        
        generate_banner = st.form_submit_button("🎨 Generate Banner Layout", type="primary")
        
        if generate_banner:
            with st.spinner("Rendering your high-quality promotional banner..."):
                time.sleep(2)
            st.success("✅ Banner Generated Successfully!")
            st.info(f"✨ **{groom_name} & {bride_name}** ✨\n\nJoyfully invite you to celebrate their union on **{wedding_date}** at **{venue_text}**.")
            st.button("⬇️ Download HD Brochure (PDF/PNG)")

# --- TAB 2: Animated Video Invites ---
with tab2:
    st.markdown("### **Generate an Animated Video Script**")
    st.write("Our AI will generate a personalized storyboard and script for your animated wedding video.")
    
    v_col1, v_col2 = st.columns(2)
    with v_col1:
        story_style = st.selectbox("Video Style & Animation", ["Traditional Storybook", "Cinematic 3D", "2D Cartoon Animation", "Premium Gold Typography"])
    with v_col2:
        music_vibe = st.selectbox("Background Music Vibe", ["Classical Instrumental", "Bollywood Romantic", "Soft Acoustic", "Upbeat & Fun"])
        
    how_we_met = st.text_area("Tell us briefly how you met (Our AI will animate this story):", placeholder="We met in college...")
    
    if st.button("🎬 Generate Animated Storyboard", type="primary"):
        with st.spinner("AI is crafting your animated sequence..."):
            time.sleep(2.5)
        
        st.success("✅ Animated Video Script Ready for Production!")
        
        st.markdown(f"""
        <div style='background-color: white; padding: 20px; border-radius: 10px; border-left: 5px solid #4A00E0;'>
            <h4>🎥 Video Storyboard Plan</h4>
            <p><b>Style:</b> {story_style} | <b>Music:</b> {music_vibe}</p>
            <ul>
                <li><b>Scene 1 (0:00 - 0:05):</b> Beautiful animated intro revealing the names in gold letters.</li>
                <li><b>Scene 2 (0:05 - 0:15):</b> A visual representation of how you met: <i>"{how_we_met}"</i></li>
                <li><b>Scene 3 (0:15 - 0:25):</b> Transition to the wedding venue details with elegant floating particles.</li>
                <li><b>Scene 4 (0:25 - 0:30):</b> 'Save the Date' final frame.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.button("⚙️ Send to Rendering Engine (Export MP4)")
