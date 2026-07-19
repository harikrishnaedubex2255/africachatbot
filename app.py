import streamlit as st
import time

# 1. Page Configuration & Theme
st.set_page_config(
    page_title="Text Intelligence Assistant", 
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Sidebar Layout for Controls & Settings
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/6125/6125691.png", width=80)
    st.title("Control Panel")
    st.markdown("Configure your AI model settings and active pipelines below.")
    st.write("---")
    
    # Simulated settings to make the UI feel production-ready
    st.subheader("⚙️ Model Configuration")
    selected_model = st.selectbox(
        "Select Model Architecture",
        ["Llama 3 (8B) - Fast", "Mixtral 8x7B - Instruct", "Gemma 7B - Standard"]
    )
    
    st.slider("Temperature (Creativity)", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
    st.slider("Max Output Tokens", min_value=256, max_value=4096, value=1024, step=128)
    
    st.write("---")
    st.caption("⚡ Powered by Streamlit & Groq Acceleration")

# 3. Main Interface Header
st.title("🧠 Text Intelligence & Chat Assistant")
st.markdown(
    "Welcome! This interface is designed for real-time text processing, testing application logic, "
    "and monitoring agent responses. Toggle settings in the sidebar to alter model behaviors."
)

# Visual KPI Metrics Dashboard at the top
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Model Status", value="Ready", delta="Online")
with col2:
    st.metric(label="Avg Response Time", value="0.14s", delta="-0.02s")
with col3:
    st.metric(label="Context Window Used", value="4%", delta="0.2k tokens")

st.write("---")

# 4. Initialize Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Hello! I am your Text Intelligence Assistant. The interface, sidebar configurations, and chat layouts are active. How can I help you build today?"
        }
    ]

# 5. Display past messages inside a neat container layout
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 6. Handle New User Input
if user_prompt := st.chat_input("Ask a question or provide text analysis parameters..."):
    # Display user message instantly
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    # Save user message to history
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Generate a simulated response with a typing animation
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = (
            f"Successfully processed input with **{selected_model}**!\n\n"
            f"Your input context was parsed securely. The pipeline state memory remains stable, "
            f"and variables are tracking perfectly. We're fully prepared to shift this container to a production API endpoint."
        )
        
        # Simulate text streaming
        current_text = ""
        for char in full_response:
            current_text += char
            response_placeholder.markdown(current_text + "▌")
            time.sleep(0.01)
        response_placeholder.markdown(full_response)
        
    # Save assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
