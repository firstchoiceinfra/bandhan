import streamlit as st
from pymongo import MongoClient
import datetime

# --- DATABASE CONNECTION LOGIC ---
# Using st.cache_resource so it connects only once
@st.cache_resource
def init_connection():
    # You will add your MongoDB URL in Streamlit Secrets
    return MongoClient(st.secrets["MONGO_URI"])

client = init_connection()
db = client["bandhan_db"]
users_collection = db["users"]

# Function to save user data
def register_new_user(user_data):
    try:
        users_collection.insert_one(user_data)
        return True
    except Exception as e:
        st.error(f"Database Error: {e}")
        return False

# ... (Your existing Registration Form UI Code goes here) ...

# Inside your TAB 3 (Submit Button logic):
submit = st.button("Complete Registration & Enter Ecosystem", type="primary")

if submit:
    # Creating a dictionary of the user's input data
    new_user_profile = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "gender": gender,
        "religion": religion,
        "ai_match_enabled": ai_match,
        "registration_date": datetime.datetime.now()
    }
    
    # Save to MongoDB
    is_saved = register_new_user(new_user_profile)
    
    if is_saved:
        st.success("🎉 Registration Successful! Your data is securely saved in our database.")
        st.balloons()
