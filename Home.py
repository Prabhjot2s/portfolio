import streamlit as st
import pandas as pd




st.set_page_config(layout='wide')
col1,col2=st.columns(2)

def structure(heading,description,images,sourcecode):
    st.title(heading)
    st.write(description)
    st.image(f"images/{images}")

    st.markdown(f"[Source Code ]({sourcecode})")

with col1:
    st.image("images/Photo.png",width=450)


with col2:

    st.title("Prabhjot Singh Chhabra")
    content="""
    Hello I am prabhjot i am learning python and solidity.
     With 4 years of experience in Python development, proficiency in C++ and SQL, 
     strong foundation in programming & database management is built.
   Have a solid understanding of machine learning algorithms and frameworks, including NumPy, PyTorch, and Matplotlib. Through my knowledge and experience with these tools, was able to develop and implement data-driven solutions that have improved business outcomes and increased efficiency."""
    st.info(content)

st.write("Below You can find some of the apps I have built in Python. Feel free to contact me")

col3,empty_col,col4=st.columns([1.5,0.5,1.5])

data=pd.read_csv("data.csv",sep=";")


with col3:
    for index,rows in data[0:10].iterrows():
        structure(rows['title'],rows['description'],rows['image'],rows['url'])

with col4:
    for index, rows in data[10:].iterrows():
            structure(rows['title'], rows['description'], rows['image'], rows["url"])

