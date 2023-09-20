
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
from PIL import Image

st.set_page_config(
    page_title="Kisaan Madat Suvidha",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

button_style = """
        <style>
        .stButton > button {
            color: blue;
            background: '#0e1117';
            width: 180px;
            height: 50px;
            border: 2px solid #4CAF50;
        }
        </style>
        """
st.markdown(button_style, unsafe_allow_html=True)
st.sidebar.header("")
#st.image('banner.png')
placeholder = st.empty()

h1, h2 = st.columns([2,1])
with h1:
    st.title('Interactive Dashboard')
with h2:
    st.title('Control Interface')
st.write("")

col1, col2, col3,col4,col5,col6 = st.columns(6)
col1.metric(":clock1: Time", "17:25:31", "")
#col2.metric(":1234: Packet Count", "106", "")
col3.metric(":computer: Select Field Number","4", "")
col5.button('Enter Manual Control')
col6.button('Enter AI Control')
st.write("")


col1, col2, col3,col4,col5,col6 = st.columns(6)
col1.metric(":thermometer: Air Temperature", "28 °C", "-1 °C")
col2.metric(":arrow_down: Air Humidity", "3 g/m^3", "-0.8 g/m^3")
col3.metric("Rainfall Indicator","PRESENT")

st.write("")
st.write("")
uploaded_file = st.file_uploader("Choose a CSV File for instant analysis")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)