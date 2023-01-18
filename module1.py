from asyncio import streams

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
import openai 
import streamlit as st
from streamlit_chat import message

openai.api_key = "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"
# Creating a function which will generate the calls from the api
def generate_response (prompt):
    completions = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = prompt,
    max_tokens = 1024,
    n = 1,
    stop = None,
    temperature = 0.5,

)
    message = completions.choices[0].text
    return message
    
st.title("ChatBot educatif  :  AlgoBot")
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []
def get_text():
    input_text = st.text_input("You: ","Bonjour ,Comment vas-tu?", key="input")
    return input_text 
user_input = get_text()

if user_input:

    output = generate_response (user_input)
# store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
