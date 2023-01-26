import requests
from twilio.rest import Client

# TODO: change twilio_client, api_key, and message to personally applicable information

# ----------------------------- Get Twilio API -----------------------

twilio_client = Client('twilio account sid', 'twilio authentication token')

# ------------------------------ Get Weather API data -------------------------
# endpoint and key
OPENWEATHERMAP_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = 'YOUR API KEY HERE'

# api parameters
parameters = {
    'lat': '40.13',
    'lon': '-56.4',
    'appid': api_key,
    'units': 'imperial',
}

# fetch api data
OWM_api = requests.get(OPENWEATHERMAP_ENDPOINT, params=parameters)
OWM_api.raise_for_status()

# format api data into usable dicts
five_day_forecast = OWM_api.json()['list']
# slice dict into needed size for rain forecast
forecast_slice = five_day_forecast[:3]

# retrieve data from dict
temperature = five_day_forecast[0]['main']['temp']
feels_like = five_day_forecast[0]['main']['feels_like']
wind_speed = five_day_forecast[0]['wind']['speed']
wind_gusts = five_day_forecast[0]['wind']['gust']

# ------------------------ Default Message Structure ---------------------

temperature_message = f'The current temperature is {temperature} degrees, feels like {feels_like} degrees.'
# precipitation_message between
wind_message = f'Wind speeds of {wind_speed}mph with gusts of {wind_gusts}mph present.'

# ------------------------- Precipitation Function -----------------------

# dictionary with possible weather conditions
precip_dict = {
    'thunder': 'Thunderstorms expected today.',
    'drizzling': 'Drizzling expected today. Bring an umbrella or water-resistant clothing!',
    'raining': 'Rain is expected today. Bring an umbrella or water-resistant clothing!',
    'snowing': 'Snow is expected today. Wear warm, water-resistant clothing.',
    'misty': 'Mist expected today.',
    'smoky': 'Smoke cover expected today. Avoid going outside, and wear a mask if it is necessary to.',
    'hazy': 'Haze expected today.',
    'foggy': 'Fog cover expected today.',
    'clear': 'Clear skies expected!',
    'cloudy': 'Cloud cover expected today.'
}


# function that determines what condition applies for today
def precipitation_check():
    precipitation = False
    for forecast in forecast_slice:
        rain_check = forecast['weather'][0]['id']
        if rain_check < 300:
            precipitation = 'thunder'
        elif rain_check < 400:
            precipitation = 'drizzling'
        elif rain_check < 600:
            precipitation = 'raining'
        elif rain_check < 700:
            precipitation = 'snowing'
        elif rain_check == 701:
            precipitation = 'misty'
        elif rain_check == 711:
            precipitation = 'smoky'
        elif rain_check == 721:
            precipitation = 'hazy'
        elif rain_check == 741:
            precipitation = 'foggy'
        elif rain_check == 800:
            precipitation = 'clear'
        elif rain_check < 800:
            precipitation = 'cloudy'
    return precipitation


precipitation_message = precip_dict[precipitation_check()]

# Alternative setup: remove above function and just use below code for simplified forecast
# precipitation_message = f"Expected weather: {five_day_forecast[1]['weather'][0]['description']}."

# ------------------------ Send SMS message -------------------------------

message = twilio_client.messages \
    .create(
    body=f'''{temperature_message}
{precipitation_message}
{wind_message}''',
    from_='your twilio phone number',
    to='your personal phone number'
)
