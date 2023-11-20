import plotly.express as px
import streamlit as st
from backend import get_data
import time



def run_again():
    st.session_state.location = None
    st.session_state.index = None
    st.session_state.type_view = None


st.set_page_config(layout="centered",
                   page_title="Tiny Weather Forecast",
                   initial_sidebar_state="collapsed",
                   page_icon="images/web_icon.png")

st.title("Tiny Weather Forecast for the next days ")

place = st.text_input(label="Place:", placeholder="Enter a place",
                      key='location', value=None)

days = st.slider(label="Forecast Days:", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

type_view = st.selectbox(label="Select data to view: ", key='type_view',
                         options=["Temperature", "Sky"], index=None)

process_button = st.empty()
press_button = False

if place and type_view:
    press_button = process_button.button(label="Process", type="primary")

if press_button:
    try:
        process_button.empty()
        place = st.session_state['location'].title()
        time_view, data = get_data(place, days, type_view)

        st.subheader(f"{type_view} for the next {days} days in {place}")

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
        st.error("The location entered does not exist")
        # time.sleep(1)

    time.sleep(1)
    st.button(label="Run Again", type="primary", on_click=run_again)


# st.session_state