import streamlit as st
st.set_page_config(layout='wide')
col1,col2=st.columns(2)

with col1:
    st.image("images/Photo.png",width=500)

with col2:
    st.title("Prabhjot Singh Chhabra")
    content="""
    Hello I am prabhjot i am learning python and solidity """
    st.info(content)