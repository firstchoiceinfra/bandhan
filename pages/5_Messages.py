import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Messages | Bandhan",
    page_icon="💬",
    layout="wide"
)

# 2. Premium CSS for Layout
st.markdown("""
    <style>
    .stApp {
        background-color: #FDFDFD;
    }
    .chat-header {
        color: #1A365D;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        font-size: 2rem;
        margin-bottom: 0px;
    }
    .status-dot {
        height: 12px;
        width: 12px;
        background-color: #27AE60;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar for Chat List (Contacts)
st.sidebar.markdown("## 💬 Your Conversations")
st.sidebar.markdown("---")

# Dynamic Contact Selection
contact = st.sidebar.radio(
    "Select a Match to chat with:",
    ["Priya Sharma (98% Match)", "Aisha Khan (94% Match)", "Bandhan Premium Support"]
)

# Extract just the name for the header
contact_name = contact.split(" (")[0]

# 4. Main Chat Area Header
st.markdown(f"<h1 class='chat-header'>{contact_name}</h1>", unsafe_allow_html=True)
st.markdown("<span class='status-dot'></span><span style='color:gray;'>Online Now</span>", unsafe_allow_html=True)
st.markdown("---")

# 5. Session State to store chat history dynamically for the selected contact
chat_key = f"chat_{contact_name}"

if chat_key not in st.session_state:
    if "Support" in contact_name:
        st.session_state[chat_key] = [{"role": "assistant", "content": "Hello! Welcome to Bandhan Premium Support. How can I assist you with your wedding planning today?"}]
    else:
        st.session_state[chat_key] = [{"role": "assistant", "content": f"Hi there! I saw we have a high AI compatibility score. How are you doing?"}]

# 6. Display Chat History
for message in st.session_state[chat_key]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 7. Chat Input Field (Bottom of the screen)
if prompt := st.chat_input(f"Message {contact_name}..."):
    
    # Add User Message to screen
    st.session_state[chat_key].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # Simulate typing delay and automated response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("*(typing...)*")
        time.sleep(1.5) # Artificial delay for realism
        
        # Mock responses based on the contact
        if "Support" in contact_name:
            reply = "Thank you for reaching out. A premium relationship manager will call you shortly."
        else:
            reply = "That sounds wonderful! I would love to know more about your interests. Shall we connect on a quick call this weekend?"
            
        message_placeholder.markdown(reply)
        
    # Save the assistant response to state
    st.session_state[chat_key].append({"role": "assistant", "content": reply})
