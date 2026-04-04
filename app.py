import streamlit as st
from main import SimpleAI   # Import your AI class

# Create AI instance
ai = SimpleAI()

st.title("AI Task Assistant")

# Text input field
user_input = st.text_input("Ask me something:")

# Respond when user types
if user_input:
    if "hello" in user_input.lower():
        st.write(ai.greet())
    elif "math" in user_input.lower():
        st.write(ai.do_math(5, 7))  # later you can parse numbers
    elif "time" in user_input.lower():
        st.write(ai.tell_time())
    elif "suggest" in user_input.lower():
        st.write(ai.decide_action())
    else:
        st.write("I don't understand yet, but I'm learning!")
