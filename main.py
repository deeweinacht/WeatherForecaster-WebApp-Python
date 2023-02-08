import streamlit as st
import plotly.express as px
from backend import *

st.set_page_config(page_title='Weather Forecaster')
st.title('Upcoming Weather')
location = st.text_input('Location: ')
forecast_days = st.slider('Days to display:', min_value=1, max_value=5,
                          help='Slide to select the number of '
                               'days to forecast')
forecast_type = st.selectbox('Select forecast type: ',
                             ('Temperature', 'Conditions'))
if forecast_type == 'Temperature':
    temp_scale = st.radio('Temperature Scale', ('Celsius', 'Fahrenheit'),
             key='scale', horizontal=True)
st.subheader(f'{location} {forecast_type} for the next {forecast_days} days')


def get_forecast(days):
    dates = ['2023-1-2', '2023-1-3', '2023-1-4']
    temperatures = [10, 20, 30]
    return dates, temperatures

d, t = get_forecast(forecast_days)
fig = px.line(x=d, y=t,
              labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(fig)
