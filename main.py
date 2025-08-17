import streamlit as st
import plotly.express as px
import streamlit as st
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"The {option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
            st.info("This is not a city or a place, please put in a real place")


        if option == "Sky":
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png",
                      "Rain":"images/rain.png", "Snow":"images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            captions = [dict["dt_txt"] for dict in filtered_data]
            for img, caption in zip(image_paths, captions):
                st.image(img, width=115, caption=caption)
    except KeyError:
        st.info("This place is not a existing place. Maybe you have made a typo? Please put in an existing city or place.")