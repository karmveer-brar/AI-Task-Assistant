import streamlit as st
import re
import os
from openai import OpenAI
from main import SimpleAI  # your custom class

# Initialize your SimpleAI instance
ai = SimpleAI()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to call OpenAI
def ask_openai(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",   # or "gpt-4" if enabled
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("AI Task Assistant")
st.write("Welcome! This is a simple AI agent you can interact with.")

# Text input field
user_input = st.text_input("Ask me something:")

# Respond when user types
if user_input:
    text = user_input.lower()

    # Rule-based responses
    if "hello" in text or "hi" in text:
        st.write(ai.greet())

    elif "add" in text or "sum" in text or "calculate" in text:
        numbers = re.findall(r'\d+', user_input)
        if len(numbers) >= 2:
            result = int(numbers[0]) + int(numbers[1])
            st.write(f"The sum is {result}")
        else:
            st.write(ai.do_math(5, 7))  # fallback

    elif "time" in text or "clock" in text:
        st.write(ai.tell_time())

    elif "suggest" in text or "decide" in text or "choose" in text:
        st.write(ai.decide_action())

    else:
        # For everything else, ask OpenAI
        st.write(ask_openai(user_input))
