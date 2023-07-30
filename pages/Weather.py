import pandas as pd
import streamlit as st
import requests
import plotly.express as pt
from functions.backend import data



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.header("Weather forecast for next days")
city=st.text_input(label="city name")
forecast_days=st.slider(label="Forecast Days",min_value=1,max_value=5)
drop_down=st.selectbox(label="Select Data to view",options=["Temperature","Sky"])

st.subheader(f"{drop_down} for next {forecast_days} in {city}")
try:
    if city:
        graph = data(city, forecast_days, drop_down)

        if drop_down=='Temperature':
            line=pt.line(data_frame=graph,x='Time',y='Temperature')
            st.plotly_chart(line)

        elif drop_down=='Sky':
            imagess=[f'functions/images/{value}.png' for value in graph['Temperature']]
            st.image(imagess,width=115,caption=[value for value in graph['Temperature']])

except KeyError:
    st.text("Enter a valid city name")


