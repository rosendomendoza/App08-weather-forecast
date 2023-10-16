import plotly.express as px
import streamlit as st


def get_data(days):
    # today = datetime.now().date().isoformat()

    dates = ["1968-05-07", "1968-05-08", "1968-05-09"]

    temperatures = [25, 30, 22]

    return [dates, temperatures]


st.set_page_config(layout="centered")

st.title("Weather Forecast for the next days ")

place = st.text_input(label="Place:", placeholder="Enter a place")

days = st.slider(label="Forecast Days:", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

type_data = st.selectbox(label="Select data to view: ",
                         options=["Temperature", "Sky"])

dates, temperatures = get_data(days)

st.subheader(f"{type_data} for the {days} next day(s) in {place}")

figure = px.line(x=dates, y=temperatures,
                 labels={"x": "Date","y": "Temperature (ºC)"})

st.plotly_chart(figure)
