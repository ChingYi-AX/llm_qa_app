import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Quickstart App")
st.title('Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    client = OpenAI()
    system_msg = f"You provide suggestions to enhance the correctness of a given German text."
    llm = "gpt-4-turbo-preview"

    st.info(client.chat.completions.create(
        model=llm,
        temperature=0.5,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": input_text},
        ],
        # functions=function_descriptions,
        # function_call="auto",
    ))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'The German text for QA?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)