# from langchain_community.llms import Ollama
# llm = Ollama(model="llama2")
# llm.invoke("how can langsmith help with testing?")

import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI(openai_api_key = "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")

st.title('인공지능 시인')


title = st.text_input('시의 주제는?',)
st.write('시의 주제는?', title)
st.button("Reset", type="primary")

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성중'):    
        st.write('시')