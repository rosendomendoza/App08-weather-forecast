import plotly.express as px
import streamlit as st
from backend import get_data

st.set_page_config(layout="centered")

st.title("Weather Forecast for the next days ")

place = st.text_input(label="Place:", placeholder="Enter a place")

days = st.slider(label="Forecast Days:", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

type_view = st.selectbox(label="Select data to view: ",
                         options=["Temperature", "Sky"])

if place:
    try:
        time_view, data = get_data(place, days, type_view)

        st.subheader(f"{type_view} for the {days} next day(s) in {place}")

        if type_view == "Temperature":
            figure = px.line(x=time_view, y=data,
                             labels={"x": f"Next {days} days", "y": "Temperature "
                                                                    "(ºC)"})
            st.plotly_chart(figure)

        if type_view == "Sky":
            images = {'Clear': "images/clear.png", 'Clouds': "images/cloud.png",
                      'Rain': "images/rain.png", 'Snow': "images/snow.png"}
            image_paths = [images[condition] for condition in data]
            st.image(image_paths, caption=time_view, width=115)
    except:
        st.write("The place entered not exist")

