import streamlit as st

st.title("My Simple File Share Website")

# CHANGE THESE WORDS TO YOUR SECRET LOGIN DETAILS
MY_USER = "student"
MY_PASS = "english123"

# Create the login boxes on the screen
user_input = st.text_input("Enter Username")
pass_input = st.text_input("Enter Password", type="password")

# Check if the username and password are correct
if user_input == MY_USER and pass_input == MY_PASS:
    st.success("You are logged in!")
    
    # Save the file in the website memory
    if 'saved_file_data' not in st.session_state:
        st.session_state['saved_file_data'] = None
    if 'saved_file_name' not in st.session_state:
        st.session_state['saved_file_name'] = ""

    # Box to upload a file from Device 1
    new_file = st.file_uploader("Step 1: Upload your file here")
    if new_file is not None:
        st.session_state['saved_file_data'] = new_file.getvalue()
        st.session_state['saved_file_name'] = new_file.name
        st.success("File uploaded successfully!")

    # Button to download the file on Device 2
    if st.session_state['saved_file_data'] is not None:
        st.write("---")
        st.write("Step 2: Download your file on your other device:")
        st.download_button(
            label="Click Here to Download File",
            data=st.session_state['saved_file_data'],
            file_name=st.session_state['saved_file_name']
        )
else:
    if user_input or pass_input:
        st.error("Wrong username or password. Try again.")
