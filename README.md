# WeatherForecaster-WebApp-Python

This web application provides a visual dashboard of the upcoming weather for
any given city.

    Copyright (C) 2023  Dee Weinacht

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

**Description:**
This app makes use of the openweathermap API (www.openweathermap.org) to 
provide a weather forecast for up to the next 5 days in 3 hour intervals.
The interface is provided with a streamlit web application.


**Using the app:**  
After installing all requirements, a local streamlit instance can be started 
by entering 'streamlit run main.py' into a terminal from the WeatherForecaster
root directory.

Alternatively, the web application can be accessed directly from streamlit 
at: https://deeweinacht-weatherforecaster-webapp-python-main-wvb0at.streamlit.app/

To receive a forecast:
1. Enter a city name in the 'Location' box
2. Select a temperature scale using the radio buttons
3. Select the number of days to forecast, using the slider
4. Select the forecast type from the dropdown, either 'Temperature' or 'Conditions.'
    

**Dependencies:**
- plotly v.5.13.0 licensed with MIT
- requests v.2.28.2 licensed with Apache 2.0
- streamlit v.1.17.0 licensed with Apache 2.0
