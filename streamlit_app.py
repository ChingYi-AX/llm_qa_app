import streamlit as st
import os
from openai import OpenAI

# from config import OPENAI_API_KEY

st.set_page_config(page_title="Quickstart App")
st.title("Text Quality Assurance App")

OPENAI_API_KEY = st.sidebar.text_input("OpenAI API Key")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


def generate_response(input_text):
    os.environ.get("OPENAI_API_KEY")
    client = OpenAI()
    system_msg = f"You provide English suggestion to enhance the correctness of the given German text."
    llm = "gpt-4-turbo-preview"
    completion = client.chat.completions.create(
        model=llm,
        temperature=0.5,
        # response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": input_text},
        ],
        # functions=function_descriptions,
        # function_call="auto",
    )
    output = completion.choices[0].message.content
    st.info(output)


with st.form("my_form"):
    text = st.text_area("Enter text:", "The German text for QA?")
    submitted = st.form_submit_button("Submit")
    if not OPENAI_API_KEY.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and OPENAI_API_KEY.startswith('sk-'):
        generate_response(text)
