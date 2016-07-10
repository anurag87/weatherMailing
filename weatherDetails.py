import requests


def get_forecast():
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    url += 'q=Bangalore&units=imperial&appid=********************'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    forecast = "Wonderla forecast for today is "
    forecast += description + " with min temperature of " + str(int(temp_min)) + " F"
    forecast += " and max temperature of " + str(int(temp_max)) + " F ."

    return forecast
