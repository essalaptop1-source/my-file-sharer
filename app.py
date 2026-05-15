import streamlit as st
from streamlit_lottie import st_lottie
import requests

# 1. Page Configuration (Changes browser tab name and icon)
st.set_page_config(
    page_title="Secure Cloud Portal", 
    page_icon="🛡️", 
    layout="centered"
)

# 2. Function to fetch smooth animations from the web
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load a professional "cloud file transfer" animation
lottie_file_upload = load_lottieurl("https://lottiefiles.com")

# 3. Main Dashboard UI Header
st.title("🛡️ Professional Secure Transfer")
st.write("A secure, encrypted pathway to move documents between synchronized client devices.")
st.write("---")

# Secret Credentials Setup
MY_USER = "student"
MY_PASS = "english123"

# 4. Clean Login Form inside a professional Box
with st.container():
    st.subheader("🔑 Identity Verification")
    col1, col2 = st.columns(2)
    with col1:
        user_input = st.text_input("Username")
    with col2:
        pass_input = st.text_input("Password", type="password")

# 5. Application Logic
if user_input == MY_USER and pass_input == MY_PASS:
    st.success("Access Granted. Secure session initialized.")
    
    # Session state initialization for holding files
    if 'saved_file_data' not in st.session_state:
        st.session_state['saved_file_data'] = None
    if 'saved_file_name' not in st.session_state:
        st.session_state['saved_file_name'] = ""

    # Split screen into two visual columns
    left_column, right_column = st.columns([1, 1])

    with left_column:
        st.subheader("📤 Data Upload")
        new_file = st.file_uploader("Select a file to sync to your cloud network", label_visibility="collapsed")
        
        if new_file is not None:
            st.session_state['saved_file_data'] = new_file.getvalue()
            st.session_state['saved_file_name'] = new_file.name
            st.toast("File successfully saved to server cache!", icon="✅")

    with right_column:
        # Display the smooth animation asset
        if lottie_file_upload:
            st_lottie(lottie_file_upload, height=180, key="upload_anim")

    # 6. Professional Download Area
    if st.session_state['saved_file_data'] is not None:
        st.write("---")
        st.subheader("📥 Available Synchronized Downloads")
        
        # Put the download button inside an info alert panel
        with st.expander("📌 View Pending Cloud Files", expanded=True):
            st.info(f"Ready: **{st.session_state['saved_file_name']}**")
            st.download_button(
                label="📥 Download Package to This Device",
                data=st.session_state['saved_file_data'],
                file_name=st.session_state['saved_file_name'],
                use_container_width=True
            )
else:
    if user_input or pass_input:
        st.error("Authentication failed. Invalid token credentials.")
