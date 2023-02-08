"""

"""

import streamlit as st
import plotly.express as px
from backend import get_forecast
import datetime


# Set up page, add widgets and labels
st.set_page_config(page_title='Weather Forecaster')
st.title('Upcoming Weather')
location = st.text_input('Location: ', help='Enter a city name')
temp_scale = st.radio('Temperature Scale', ('Celsius', 'Fahrenheit'),
                      key='scale', horizontal=True)
forecast_days = st.slider('Days to display:', min_value=1, max_value=5,
                          help='Slide to select the number of '
                               'days to forecast')
forecast_type = st.selectbox('Select forecast type: ',
                             ('Temperature', 'Conditions'))
st.header(f'{location} {forecast_type} for the next {forecast_days} days')


if location:
    try:
        forecast_data = get_forecast(location,
                                     days=forecast_days, scale=temp_scale)
        dates = [datetime.datetime.fromisoformat(dic['dt_txt'])
                 for dic in forecast_data]
        match forecast_type:
            case 'Temperature':
                temperature_data = [dic['main']['temp']
                                    for dic in forecast_data]
                fig = px.line(x=dates, y=temperature_data, markers=True,
                              labels={'x': 'Date',
                                      'y': f'Temperature ({temp_scale})'})
                st.plotly_chart(fig)

            case 'Conditions':
                images_dict = {'Clear': 'images/clear.png',
                               'Clouds': 'images/cloudy.png',
                               'Rain': 'images/rain.png',
                               'Snow': 'images/snow.png'}
                conditions_data = \
                    [dic['weather'][0]['main'] for dic in forecast_data]
                conditions_with_dates = zip(dates, conditions_data)

                for condition in conditions_with_dates:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader(condition[0].strftime('%A %B %d %y'))
                        st.write(condition[0].strftime('%I:%M %p'))
                        st.write(condition[1])
                    with col2:
                        st.write('')
                        st.image(images_dict[condition[1]], width=200)

    except KeyError:
        st.write('Please enter a valid city name!')
