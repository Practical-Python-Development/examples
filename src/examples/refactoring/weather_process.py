"""Read weather data and calculate average temperature and horizontal wind speed"""

import csv
import math
import numpy as np
import pandas as pd


def celcius_to_fahrenheit(temperature, threshold):
    """ Convert temperature in Celcius to Fahrenheit if it is over the threshold """
    t = []
    for temp in temperature:
        if temp > threshold:
            t.append(temp * 1.8 + 32)  # convert Celsius to Fahrenheit
        else:
            t.append(temp)
    return t

weather_data = pd.read_csv("./../../../data/weather_data.csv")
number_of_stations = len(weather_data["station"])
#print(weather_data)
#print(number_of_stations)

temperature = celcius_to_fahrenheit(weather_data["temp"], 25)
#z = sum(temperature)
#print("sum", sum(temperature))
print("Average temperature", np.mean(temperature) if len(temperature) else 1)


# Calculate average horizontal wind speed
sum_wind_speed = 0
for i in range(0, number_of_stations):
    sum_wind_speed += math.sqrt(
        weather_data["wind_u"][i] ** 2 + weather_data["wind_v"][i] ** 2
    )
avg_wind_speed = sum_wind_speed / number_of_stations
print("Average horizontal sum_wind_speed", avg_wind_speed)
