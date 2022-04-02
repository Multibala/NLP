import streamlit as st
import utils 
utils.setup()
st.title('NLP project')
st.subheader('Message spam or not spam classifier application ')

message = st.text_area(label='Enter your message',placeholder='type here ..',height=150)
btn = st.button('Analyze')
if btn:
    res = utils.analyze(message)
    if 'spam' == res:
        st.error('spam')
    else:
        st.success('not spam')



