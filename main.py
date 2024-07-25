import streamlit as st
import plotly.express as px
from backend import get_data
st.title('Weather Forecast for the Next Days')
place = st.text_input('Place')
days = st.slider('Forecast Days', 1, 5,help='Select the number of days you want to know the weather forecast for')
option = st.selectbox('select data to view', ('Temperature',"sky"))

st.subheader(f"{option} for the next {days} days in {place}")
try:
    if place:
        filtered_data = get_data(place,days)


        if option == "Temperature":
            temperatures = [dict["main"]["temp"]/ 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates,y=temperatures,labels={'x':'Date','y':'Temperature'})
            st.plotly_chart(figure) 
        
        if option == "sky":
            images= {"clear":"images/clear.png","clouds":"images/clouds.png","rain":"images/rain.png","snow":"images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]   
            st.image(image_paths,width=115)
except KeyError:
    st.write("No data available for this location")
    
