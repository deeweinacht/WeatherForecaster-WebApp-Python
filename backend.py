import requests

API_KEY = 'a6e5c24f4c3a18f0e44dfae3c9a54de8'


def get_forecast(location, days=1, scale='Celsius'):
    """
    This method uses the openweathermap API to retrieve a dictionary of
    forecast data at the given location over the specified length of time.
    :param location: str
    :param days: int
    :param scale: str
    :return: dict
    """
    if scale == 'Celsius':
        units = 'metric'
    elif scale == 'Fahrenheit':
        units = 'imperial'
    else:
        pass
    num_records = 8 * days  # every 3 hours, 8 records per day

    url = 'https://api.openweathermap.org/data/2.5/forecast?' \
          f'q={location}&' \
          f'appid={API_KEY}&' \
          f'cnt={num_records}&' \
          f'units={units}'
    response = requests.get(url)
    forecast_data = response.json()
    forecast_data = forecast_data['list']

    return forecast_data
