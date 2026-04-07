import streamlit as st
from transformers import pipeline

# Title
st.title("Realistic AI Chatbot")

# Load Hugging Face model (with token from secrets)
@st.cache_resource
def load_model():
    HF_API_TOKEN = st.secrets["HF_API_TOKEN"]  # must match Secrets Manager key
    return pipeline(
        "text-generation",
        model="facebook/blenderbot-400M-distill",
        use_auth_token=HF_API_TOKEN
    )

generator = load_model()

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")

# User input
user_input = st.text_input("Type your message:", key="input")

if user_input:
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Generate bot response
    response = generator(user_input, max_length=200, do_sample=True)[0]["generated_text"]

    # Add bot message
    st.session_state["messages"].append({"role": "bot", "content": response})

    # Rerun to show new messages
    st.experimental_rerun()
