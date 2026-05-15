import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time

# 1. Professional Web Layout Setup
st.set_page_config(
    page_title="NexusBot Hosting Panel", 
    page_icon="🤖", 
    layout="wide"
)

# Function to pull smooth animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Pulling a professional server/robot animation
lottie_server = load_lottieurl("https://lottiefiles.com")

# 2. Main Header
st.title("⚡ NexusBot 24/7 Cloud Hosting Control Panel")
st.write("Manage, deploy, and monitor your global Discord bots from an un-interruptible server hub.")
st.write("---")

# 3. Sidebar Configuration (Left Panel)
with st.sidebar:
    st.subheader("🌐 Server Selection")
    server_node = st.selectbox("Select Cloud Node", ["US-East Mainframe", "EU-West Backup", "Asia-Pacific Edge"])
    st.success(f"Connected to: {server_node}")
    
    st.write("---")
    st.subheader("🔑 Access Token")
    bot_token = st.text_input("Enter Discord Bot Token", type="password", placeholder="MTg0NjM5...")
    
    st.write("---")
    st.write("⚙️ *Server Framework: v2.4.1*")

# 4. Main Control Dashboard Layout (2 Columns)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Live Server Performance")
    
    # Mock system metrics bars
    cpu_usage = st.slider("Allocated CPU Core Usage", 0, 100, 34, disabled=True)
    st.progress(cpu_usage)
    
    ram_usage = st.slider("Memory Allocation (RAM)", 0, 100, 58, disabled=True)
    st.progress(ram_usage)

    st.write("---")
    st.subheader("🕹️ Bot Power Management")
    
    # Session state for tracking if bot is activated
    if "bot_online" not in st.session_state:
        st.session_state["bot_online"] = False

    # Start/Stop buttons
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("🚀 LAUNCH BOT ONLINE", use_container_width=True):
            if not bot_token:
                st.error("Cannot launch: Missing Discord Bot Token in sidebar!")
            else:
                st.session_state["bot_online"] = True
                st.toast("Bot code loaded into server container!", icon="⚙️")
                
    with btn_col2:
        if st.button("🛑 FORCE SHUTDOWN", use_container_width=True):
            st.session_state["bot_online"] = False
            st.toast("Server process terminated safely.", icon="🔒")

    # Current Status Box
    if st.session_state["bot_online"]:
        st.metric(label="Bot Running Status", value="ONLINE", delta="Active 24/7 Cloud Connection")
    else:
        st.metric(label="Bot Running Status", value="OFFLINE", delta="- Disconnected", delta_color="inverse")

with col2:
    st.subheader("🤖 Server Status")
    if lottie_server:
        st_lottie(lottie_server, height=200, key="server_anim")
    else:
        st.info("Loading animation graphics...")

# 5. Live Logs Terminal Layer
st.write("---")
st.subheader("📋 Core Engine Logs")
with st.container(border=True):
    if st.session_state["bot_online"]:
        st.code(
            f"[INFO] {time.strftime('%H:%M:%S')} - Connecting to Discord WebSocket gateway...\n"
            f"[SUCCESS] {time.strftime('%H:%M:%S')} - Authenticated securely with token successfully.\n"
            f"[INFO] {time.strftime('%H:%M:%S')} - Shard #0 ready. Listening for slash commands (/) 24/7.",
            language="bash"
        )
    else:
        st.code("[SYSTEM LOGS] Server is idling. Awaiting launch command token connection...", language="bash")
