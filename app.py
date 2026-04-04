import streamlit as st
from main import SimpleAI   # Import your AI class from main.py

# Create AI instance
ai = SimpleAI()

# Streamlit UI
st.title("AI Task Assistant")

st.write("Welcome! This is a simple AI agent you can interact with.")

if st.button("Greet"):
    st.write(ai.greet())

if st.button("Do Math (5 + 7)"):
    st.write(ai.do_math(5, 7))

if st.button("Tell Time"):
    st.write(ai.tell_time())

if st.button("Suggest Action"):
    st.write(ai.decide_action())
