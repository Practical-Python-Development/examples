"""This script is badly written on purpose to demonstrate refactoring."""

# Imports
import csv
import math
import numpy as np

# Constants
THRESHOLD_TEMPERATURE: int = 25
SCALING_FACTOR: float = 1.8
TEMPERATURE_OFFSET: int = 32


# Functions
def celsius_to_fahrenheit(temperature_C: float) -> float:
    """
    Converts from degree Celsius to degree Fahrenheit.
    :param temperature_C: The temperature in Celsius
    :return: The temperature in Fahrenheit.
    """
    return (temperature_C * SCALING_FACTOR) + TEMPERATURE_OFFSET


def convert_station_temp_to_fahrenheit(
    weather_stations_data: str | list[str] | list[list[str]],
) -> list:
    """
    Converts the temperature at each station to Fahrenheit if it satisfies a temperature condition.
    :param weather_stations_data: The data of all stations.
    :return: List containing temperature values of each station.
    """
    weather_station_temperatures = []
    for weather_station in weather_stations_data:
        if float(weather_station[1]) > THRESHOLD_TEMPERATURE:
            weather_station_temperatures.append(
                celsius_to_fahrenheit(float(weather_station[1]))
            )
        else:
            weather_station_temperatures.append(float(weather_station[1]))
    return weather_station_temperatures


def sum_of_temperatures(station_temperatures: list) -> float:
    """
    Computes the sum of the station temperatures.
    :param station_temperatures: List containing temperatures of each station.
    :return: The sum of the temperatures as a floating point number.
    """
    return sum(station_temperatures)


def average_of_variables(station_data: list | list[list[str]]):
    """
    Takes the average of a list of station variables.
    :param station_data: A list of station variables.
    :return: The mean of the selected station variable.
    """
    return np.mean(station_data)


FILEPATH = open("./../../../data/weather_data.csv")
WEATHER_STATION_DATA = list(csv.reader(FILEPATH))
FILEPATH.close()
WEATHER_STATION_DATA = WEATHER_STATION_DATA[1:]  # Omit header

station_temperatures_fahrenheit = convert_station_temp_to_fahrenheit(
    WEATHER_STATION_DATA
)

sum_station_temperatures_fahrenheit = sum_of_temperatures(
    station_temperatures_fahrenheit
)

print(f"The sum is {sum_station_temperatures_fahrenheit}")
print(f"The average is {average_of_variables(station_temperatures_fahrenheit)}")
wind_speed = 0

for station in WEATHER_STATION_DATA:
    zonal_wind_component = float(station[3])
    meridional_wind_component = float(station[4])
    wind_speed += math.sqrt(zonal_wind_component**2 + meridional_wind_component**2)

print("wind", wind_speed / len(WEATHER_STATION_DATA))
