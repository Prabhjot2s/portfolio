import streamlit as st
from send_email import send_email
st.header("Contact Me")

with st.form(key='form'):
    emalfrom=st.text_input("Your Email address",placeholder="Enter your Email Address")
    subject=st.selectbox(label='What do you want to discuss', options=['Job position', 'Freelancing', 'Other'])

    raw_content=st.text_area("Your message",placeholder="Happy to hear from you",height=300)


    content=f"""\
Subject: New email from website regarding {subject}

From: {emalfrom}
{raw_content}
"""

    button=st.form_submit_button(label='Send')
    if button:
        send_email(content)


