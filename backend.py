import requests
API_KEY = '141710af2113bab9f55ef73e1bcd33d5'


def get_forecast(location, forecast_days=1, forecast_type=None,
                 scale='Celsius'):
    if scale == 'Celsius':
        units = 'metric'
    elif scale == 'Fahrenheit':
        units = 'imperial'
    else:
        pass
    url = 'https://api.openweathermap.org/data/2.5/forecast?' \
          f'q={location}&' \
          f'appid={API_KEY}&' \
          f'units={units}'
    response = requests.get(url)
    data = response.json()
    num_records = 8*forecast_days  # every 3 hours, 8 records per day
    data = data["list"][:num_records]

    match forecast_type:
        case 'Temperature':
            forecast_data = [dic['main']['temp'] for dic in data]
        case 'Conditions':
            forecast_data = [dic['weather'][0]['main'] for dic in data]

    return forecast_data


if __name__=='__main__':
    print(get_forecast(location='Tokyo', forecast_days=3, forecast_type='Temperature'))