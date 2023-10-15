import streamlit as st


st.set_page_config(layout="centered")

st.title("Weather Forecast for the next days ")

place = st.text_input(label="Place:", placeholder="Enter a place")

days = st.slider(label="Forecast Days:", min_value=1, max_value=5, help="Select the number of forecasted days" )

type_data = st.selectbox(label="Select data to view: ",
                         options=["Temperature", "Sky"])

st.subheader(f"{type_data} for the {days} next day(s) in {place}")
