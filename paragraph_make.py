from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from langchain_groq import ChatGroq

import os
from constants import groq_key

# Set API key
os.environ["GROQ_API_KEY"] = groq_key

llm = ChatGroq(
    model="llama-3.3-70b-versatile",   # ✅ updated model
)

response = llm.invoke("Explain RAG in simple terms")
print(response.content)

def add_bg_from_url(url):
    page_bg_img = f'''
    <style>
    .stApp {{
    background-image: url("{url}");
    background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

add_bg_from_url("https://img.freepik.com/free-photo/fingers-note-report-journalist-filling_1150-1044.jpg?t=st=1774795561~exp=1774799161~hmac=58896b80739002a71896cbc2cb6ca35bd4601271559ce119b4d829d7c231dfb6&w=1480")

st.set_page_config(
    page_title="Paragraph Maker",
    page_icon=":pencil2:",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.header("Pagagraph Make")


def generate_pagagraphs(input_text, no_words, blog_style):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant that breaks down text into pagagraphs."),
            ("user", f"Please break the following text into pagagraphs with approximately {no_words} words each, in a {blog_style} style:\n\n{input_text}")
        ]
    )

    chain = prompt | llm
    response = chain.invoke({
        "input_text": input_text,
        "no_words": no_words,
        "blog_style": blog_style
    })

    return response.content


input_text = st.text_area("Enter your text here:")

col1, col2 = st.columns([2,2])

with col1:
    no_words = st.number_input("Number of words per paragraph:", min_value=1, value=900)
with col2:
    blog_style = st.selectbox("Select blog style:", ["Informative", "Conversational", "Formal", "Casual"])

if st.button("Generate Pagagraphs"):
    st.write("Generating pagagraphs...")
    pagagraphs = generate_pagagraphs(input_text, no_words, blog_style)
    st.subheader("Generated Pagagraphs:")
    st.write(pagagraphs)


