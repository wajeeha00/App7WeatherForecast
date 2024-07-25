import streamlit as st

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place')
days = st.slider('Forecast Days', 1, 5,help='Select the number of days you want to know the weather forecast for')
option = st.selectbox('select data to view', ('Temperature',"sky"))

st.subheader(f"{option} for the next {days} days in {place}")