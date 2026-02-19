import streamlit as st 
import pandas as pd
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import os
api_key = os.getenv("GROQ_API_KEY")  # .env me key set honi chahiye
llm = ChatGroq(model="openai/gpt-oss-120b", api_key=api_key)


st.title (" 📈CHAT WITH DATA ")


uploaded_file= st.file_uploader("Select any csv file",type=["csv"])

if uploaded_file:

    data= pd.read_csv(uploaded_file)
    st.write("### Preview Of Your Data ")
    st.dataframe(data.head(10))

    
    text_data= data.to_string()
    question=st.chat_input ("Ask anything about this data......")
    if question:
        with st.chat_message("user"):
         st.markdown(question)

        # Prepare Groq messages
        messages = [
              {"role": "user", "content": f"You are a data expert. Learn this data:\n{text_data}\nAnswer the question: {question}"}
              ]

        with st.spinner("Analyzing your data..."):
         response = llm.invoke(messages)

                           
        with st.chat_message("assistant"):
            st.markdown(response.content)
