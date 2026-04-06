import streamlit as st
import re
import requests
from main import SimpleAI  # your custom class

# Initialize your SimpleAI instance
ai = SimpleAI()

# Hugging Face API setup (Meta LLaMA-3 Instruct model via router)
HF_API_URL = "https://router.huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
HF_API_TOKEN = st.secrets["HF_API_TOKEN"]  # safely stored in Streamlit Cloud secrets

headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

# Function to call Hugging Face model safely
def ask_huggingface(question):
    payload = {"inputs": question}
    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()  # raise error if HTTP status != 200
        data = response.json()
        if isinstance(data, dict) and "generated_text" in data:
            return data["generated_text"]
        elif isinstance(data, list) and len(data) > 0 and "generated_text" in data[0]:
            return data[0]["generated_text"]
        elif "error" in data:
            return f"Model error: {data['error']}"
        else:
            return "The model did not return a valid response."
    except requests.exceptions.JSONDecodeError:
        return "Error: Hugging Face returned invalid JSON."
    except requests.exceptions.RequestException as e:
        return f"Connection error: {str(e)}"

# Streamlit UI
st.title("Free AI Task Assistant")
st.write("Welcome! This is a simple AI agent you can interact with.")

user_input = st.text_input("Ask me something:")

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
        # For everything else, ask Hugging Face
        st.write(ask_huggingface(user_input))
