import streamlit as st 
import pandas as pd
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

llm= ChatGroq(model="openai/gpt-oss-120b")

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

        prompt= f'''You are a data expert learn the data {text_data} and 
                  provide the answer of the {question} '''
        
        with st.spinner("Analyzing your data..."):
           response=llm.invoke(prompt)
                           
           with st.chat_message("assistant"):
            st.markdown(response.content)
