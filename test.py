#!/usr/bin/python3

import os
import sys

import openweather

api_key = os.environ.get("OPENWEATHER_API_KEY", None)

try:
    ow = openweather.OpenWeather(api_key)
except openweather.OpenWeatherException:
    print("You must set the environmental variable OPENWEATHER_API_KEY")
    sys.exit(1)

# data = ow.current_weather_for_city("Skibbereen, ie")

# location = data["name"]
# weather = data["weather"][0]
# print(f"{location}: {weather['main']} - {weather['description']}")


def biggest_dif(list_of_locations):
    # initialise major variable, will be using dictionary (or list?)
    current_temps = {}

    for city in list_of_locations:
        data = ow.current_weather_for_city(city)
        location = data["name"]
        current_temp = data["main"]["temp"]
        current_temps[location] = current_temp
        # items dict that will hold location as key and respective current temperature
        # i feel dictionary was the best way to store these, but some locations may have similar names
        # in which case a list of lists, or list of tuples would be ideal

    # could check that current_temps has content
    print(current_temps)
    # using python inbuilt max and min functions
    maximum = max(current_temps, key=current_temps.get)
    minimum = min(current_temps, key=current_temps.get)
    difference = current_temps[maximum] - current_temps[minimum]
    # Temperatures are already in metric (Celsius)
    print(f"{maximum} and {minimum} have the biggest difference of {difference} Celsius")


# Testing the Biggest Difference function
locations = ["Ireland", "Russia", "Nigeria"]
biggest_dif(locations)
