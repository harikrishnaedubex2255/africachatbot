import streamlit as st
import time

# 1. Setup Streamlit Page Settings
st.set_page_config(page_title="Chatbot Preview", page_icon="🤖")
st.title("🤖 Chatbot Local Preview")
st.caption("Running locally to test the user interface and chat history container.")

# 2. Initialize Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hey there! I am your local preview bot. Try typing something below to see how the UI handles messages!"}
    ]

# 3. Display past messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle New User Input
if user_prompt := st.chat_input("Type a test message..."):
    # Display user message instantly
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    # Save user message to history
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Generate a simulated response with a typewriter/streaming effect
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = f"Received your message: \"{user_prompt}\"! The UI structure, state memory, and scrolling are working perfectly. Ready to connect the API next."
        
        # Simulate text streaming
        current_text = ""
        for char in full_response:
            current_text += char
            response_placeholder.markdown(current_text + "▌")
            time.sleep(0.015)
        response_placeholder.markdown(full_response)
        
    # Save assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})