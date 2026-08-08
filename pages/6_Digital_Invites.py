import streamlit as st
import time
import base64

# =====================================================================
# 1. PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Digital E-Invites | Bandhan",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# 2. READ LOCAL LOGO (नया लोगो)
# =====================================================================
def get_base64_image(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e:
        return ""

main_logo_b64 = get_base64_image("896430.png")

# =====================================================================
# 3. 🔥 ANTI-FLASH & NEW LOGO SPLASH SCREEN 🔥
# =====================================================================
st.markdown(f"""
    <style>
    [data-testid="stSidebarNav"] {{ display: none !important; }}
    
    .stApp::before {{
        content: ""; 
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background-color: #0F2027; 
        background-image: url("data:image/png;base64,{main_logo_b64}"); 
        background-repeat: no-repeat; background-position: center; background-size: 350px; 
        z-index: 9999999; animation: fadeOutSplash 0.8s ease-in-out forwards; 
    }}
    @keyframes fadeOutSplash {{
        0% {{ opacity: 1; visibility: visible; }}
        60% {{ opacity: 1; visibility: visible; }} 
        100% {{ opacity: 0; visibility: hidden; pointer-events: none; }} 
    }}
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 4. 🔥 CUSTOM IMAGE-BASED SIDEBAR MENU (अब नए लोगो के साथ) 🔥
# =====================================================================
sidebar_html = f"""
<div class="app-sidebar-menu">
    <div style="text-align: center; margin-bottom: 20px; border-bottom: 1px solid rgba(212, 175, 55, 0.3); padding-bottom: 15px;">
        <img src="data:image/png;base64,{main_logo_b64}" style="max-width: 85%; height: auto; filter: drop-shadow(0px 4px 6px rgba(0,0,0,0.5));">
    </div>
    
    <a href="/" target="_top" class="menu-item"><div class="icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/1946/1946488.png" alt="Home"></div><div class="menu-text" style="color: #E2E8F0;">Home</div></a>
    <a href="Kundli_Match" target="_top" class="menu-item"><div class="icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/3652/3652191.png" alt="Kundli"></div><div class="menu-text" style="color: #E2E8F0;">Kundli Match</div></a>
    <a href="Registration" target="_top" class="menu-item"><div class="icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/2921/2921222.png" alt="Registration"></div><div class="menu-text" style="color: #E2E8F0;">Registration</div></a>
    <a href="Matchmaking" target="_top" class="menu-item"><div class="icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/1077/1077035.png" alt="Matchmaking"></div><div class="menu-text" style="color: #E2E8F0;">Matchmaking</div></a>
    <a href="Wedding_Services" target="_top" class="menu-item"><div class="icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/3159/3159303.png" alt="Services"></div><div class="menu-text" style="color: #E2E8F0;">Wedding Services</div></a>
    <a href="Verification_KYC" target="_top" class="menu-item"><div class="icon-circle"><img src="https://cdn-icons-png.flaticon.com/512/6928/6928929.png" alt="KYC"></div><div class="menu-text" style="color: #E2E8F0;">Verification KYC</div></a>
</div>
"""
st.sidebar.markdown(sidebar_html, unsafe_allow_html=True)

# =====================================================================
# 5. POWERFUL PREMIUM CSS
# =====================================================================
st.markdown("""
    <style>
    .stApp { background-color: #FCFBF9 !important; font-family: 'Helvetica Neue', sans-serif; }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F2027 0%, #203A43 50%, #2C5364 100%) !important;
        border-right: 3px solid #D4AF37 !important;
    }
    .app-sidebar-menu { display: flex; flex-direction: column; gap: 20px; padding-top: 5px; align-items: center; }
    .menu-item {
        display: flex; flex-direction: column; align-items: center; text-decoration: none !important;
        transition: transform 0.2s, background 0.3s; cursor: pointer; width: 90%; padding: 10px;
        border-radius: 12px; background-color: rgba(255, 255, 255, 0.05); border: 1px solid rgba(212, 175, 55, 0.2);
    }
    .menu-item:hover {
        transform: scale(1.05); background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%);
        border-color: #FBF5B7; box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4);
    }
    .menu-item:hover .menu-text { color: #0F2027 !important; font-weight: 900 !important; }
    .icon-circle {
        width: 65px; height: 65px; background-color: #FFFFFF; border-radius: 50%;
        display: flex; justify-content: center; align-items: center; margin-bottom: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .icon-circle img { width: 38px; height: 38px; object-fit: contain; }
    .menu-text { font-size: 0.95rem; font-weight: 700; text-align: center; font-family: 'Helvetica', sans-serif; letter-spacing: 0.5px; transition: color 0.3s; }
    
    /* E-Invite Specific Styles */
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
    .highlight { color: #D4AF37; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 6. PAGE CONTENT (E-Invites)
# =====================================================================
st.markdown("<h1 class='invite-header'>Design Your Royal E-Invite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:1.2rem; color:#555;'>Create stunning promotional banners and animated video scripts for your big day.</p>", unsafe_allow_html=True)
st.markdown("---")

# Interactive Tabs for Different Formats
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
