"""This script is badly written on purpose to demonstrate refactoring."""

import csv, math

WEATHER_DATA_FILE = "./../../../data/weather_data.csv"
CONVERT_TEMPERATURE_THRESHOLD = 25


def convert_fahrenheit_to_celsius(all_stations_obs_data):
    station_temp = []
    for station_data in all_stations_obs_data:
        if float(station_data[1]) > CONVERT_TEMPERATURE_THRESHOLD:
            station_temp.append(float(station_data[1]) * 1.8 + 32)
        else:
            station_temp.append(float(station_data[1]))
    return station_temp


def sum_temperature_all_stations(list_stations_temp):
    sum_temp_value = 0
    for temp in list_stations_temp:
        sum_temp_value += temp
    return sum_temp_value


weather_data = open(WEATHER_DATA_FILE)
list_weather_data = list(csv.reader(weather_data))
weather_data.close()
station_measured_data = list_weather_data[1:]
all_stations_data = []
for single_station in list_weather_data:
    all_stations_data.append([single_station[0], single_station[1], single_station[2], single_station[3], single_station[4]])
converted_temperature = convert_fahrenheit_to_celsius(all_stations_data)
temperature_sum = sum_temperature_all_stations(converted_temperature)
print("sum", temperature_sum)
print("avg", temperature_sum / (len(converted_temperature) if len(converted_temperature) else 1))
wind_speed = 0
for station in list_weather_data:
    u_wind = float(station[3])
    v_wind = float(station[4])
    wind_speed += math.sqrt(u_wind * u_wind + v_wind * v_wind)
print("wind", wind_speed / len(list_weather_data))
