import json
import requests
import datetime
import csv

BASE_URL = "https://api.openweathermap.org/data/2.5"

class OpenWeatherException(Exception):
    pass

class OpenWeather:
    def __init__(self, api_key):
        """Initialize the OpenWeather class with the API key

        Will initialize the OpenWeather class with the API key.  If the API key
        is not set, this will raise a OpenWeatherException
        """

        if api_key is None:
            raise OpenWeatherException("API key not set")

        self.api_key = api_key


    def current_weather_for_city(self, city):
        """Get current weather for a city

        Will return a dictionary with the current weather for a city.
        Currently does not handle API errors gracefully, so it's up to the
        calling application to detect 401s or the like.
        """

        url = f"{BASE_URL}/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        return json.loads(response.text)

    def weather_report(self, city, filename):
        if ".csv" not in filename:
            filename += ".csv"

        url = f"{BASE_URL}/forecast?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = json.loads(response.text)

        list_header = ['HOUR', 'MIN TEMP', 'MAX TEMP']
        list = []
        for x in data['list']:
            item = []
            timestamp = x['dt']
            time = datetime.datetime.fromtimestamp(timestamp)
            item.append(time.hour)  # add the hour to our item

            item.append(x['main']['temp_min'])  # add the min temp to our item
            item.append(x['main']['temp_max'])  # add max temp to item

            list.append(item)  # add item to our list

        with open(filename, 'x') as file:
            writer = csv.writer(file)
            writer.writerow(list_header)
            writer.writerows(list)
            file.close()
