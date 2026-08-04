import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration
st.set_page_config(
    page_title="Admin Dashboard | Bandhan",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Premium Admin CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #F4F6F9;
    }
    .admin-header {
        color: #1A365D;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 900;
        font-size: 2.5rem;
        margin-bottom: 0px;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-top: 4px solid #D4AF37;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("<h1 class='admin-header'>📊 Admin Control Center</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #666;'>Real-time overview of platform activity, user registrations, and ecosystem revenue.</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. Key Metrics (Top Row)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="👥 Total Users", value="12,543", delta="+324 this week")
with col2:
    st.metric(label="💎 Premium Members", value="3,210", delta="+85 this week")
with col3:
    st.metric(label="🛍️ Active Vendors", value="450", delta="+12 this week")
with col4:
    st.metric(label="💰 Ecosystem Revenue", value="$45,230", delta="+$4,500 this week")

st.markdown("<br><br>", unsafe_allow_html=True)

# 5. Charts Section (Data Visualization)
chart_col1, chart_col2 = st.columns(2, gap="large")

with chart_col1:
    st.markdown("### 📈 User Growth (Last 7 Days)")
    # Mock data for line chart
    chart_data = pd.DataFrame(
        np.random.randint(150, 300, size=(7, 1)), 
        columns=["New Registrations"],
        index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    )
    st.line_chart(chart_data)

with chart_col2:
    st.markdown("### 🛍️ Top Ecosystem Bookings")
    # Mock data for bar chart
    services_data = pd.DataFrame({
        "Bookings": [120, 95, 150, 80]
    }, index=["Venues", "Luxury Rides", "Apparel", "Honeymoons"])
    st.bar_chart(services_data)

st.markdown("---")

# 6. Recent Registrations Table
st.markdown("### 📋 Recent User Registrations")

# Mock Database Table
recent_users = pd.DataFrame({
    "User ID": ["#BND-1042", "#BND-1043", "#BND-1044", "#BND-1045", "#BND-1046"],
    "Name": ["Aarav Patel", "Priya Sharma", "Rohan Desai", "Neha Singh", "Vikram Rao"],
    "Age": [28, 26, 30, 27, 29],
    "Location": ["Mumbai, IN", "Delhi, IN", "London, UK", "Dubai, UAE", "New York, USA"],
    "Plan": ["Premium", "Free", "Free", "Premium", "Premium"],
    "Status": ["Verified ✅", "Pending ⏳", "Verified ✅", "Verified ✅", "Pending ⏳"]
})

# Displaying table with Streamlit's native dataframe UI
st.dataframe(recent_users, use_container_width=True, hide_index=True)

st.markdown("<br>", unsafe_allow_html=True)
st.button("📥 Download Full Report (CSV)", type="primary")
