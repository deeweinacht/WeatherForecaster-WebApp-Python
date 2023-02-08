import streamlit as st
import plotly.express as px

st.title('Upcoming Weather')
location = st.text_input('Location: ')
forecast_days = st.slider('Days to display:', min_value=1, max_value=7,
                 help='Slide to select the number of days to forecast')
forecast_type = st.selectbox('Select forecast type: ',
                             ('Temperature', 'Sky'))
if forecast_type == 'Temperature':
    st.radio('Temperature Scale', ('Celsius', 'Fahrenheit'),
             key='scale', horizontal=True)
st.subheader(f'{location} {forecast_type} for the next {forecast_days} days')

# fig = px.line(x, y, labels)
# st.plotly_chart():
