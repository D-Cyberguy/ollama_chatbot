from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant, Please respond to the queries"),
    ("user", "Question: {question}")
])

# Streamlit UI
st.title('Hello! How may I assist you today?')
input_text = st.text_input("Enter your question")

# Only run if input is provided
if input_text:
    llm = Ollama(model="gemma:2b")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    response = chain.invoke({"question": input_text})
    st.write(response)
