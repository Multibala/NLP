import streamlit as st
import utils

st.title('NLP project')
st.subheader('Message summarizer application ')

message = st.text_area(label='Enter your text',placeholder='type here ..',height = 150)
btn = st.button('Summarize')
if btn:
    
    res = utils.get_summarize_text(message)

    st.text_area(label= 'summary text' ,value = res,disabled = True)


