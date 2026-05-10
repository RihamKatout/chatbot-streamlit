import streamlit as st


# -----------------------------
# Page Title
# -----------------------------
st.title("Simple ChatGPT Style App")


# -----------------------------
# Initialize Chat History
# -----------------------------streamlit run chat_app.py
if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Display Previous Messages
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# Fake AI Response Function
# -----------------------------
def generate_response(user_input):

    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    elif "name" in user_input:
        return "Nice to meet you! I'm your local chatbot."

    elif "riham" in user_input:
        return "Nice to meet you Riham!"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that yet."
    
# -----------------------------
# User Input
# -----------------------------
prompt = st.chat_input("Type your message here...")


# -----------------------------
# When User Sends Message
# -----------------------------
if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = generate_response(prompt)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)