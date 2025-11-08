"""This script is badly written on purpose to demonstrate refactoring."""

import csv, math

WEATHER_DATA_FILE = "./../../../data/weather_data.csv"
CONVERT_TEMPERATURE_THRESHOLD = 25


def read_observed_data():
    weather_data = open(WEATHER_DATA_FILE)
    list_weather_data = list(csv.reader(weather_data))
    weather_data.close()
    list_weather_data = list_weather_data[1:]
    all_stations_data = []
    for single_station in list_weather_data:
        all_stations_data.append([single_station[0], single_station[1], single_station[2], single_station[3], single_station[4]])
    return all_stations_data


def convert_fahrenheit_to_celsius(all_stations_obs_data):
    station_temp = []
    for station_data in all_stations_obs_data:
        if float(station_data[1]) > CONVERT_TEMPERATURE_THRESHOLD:
            station_temp.append(float(station_data[1]) * 1.8 + 32)
        else:
            station_temp.append(float(station_data[1]))
    return station_temp


def sum_temperature_all_stations(observed_data_temp):
    sum_temp_value = 0
    for temp in observed_data_temp:
        sum_temp_value += temp
    return sum_temp_value


def average_wind_speed(observed_data):
    wind_speed = 0
    for station in observed_data:
        u_wind = float(station[3])
        v_wind = float(station[4])
        wind_speed += math.sqrt(u_wind * u_wind + v_wind * v_wind)
    return wind_speed


def main():
    all_stations_data = read_observed_data()
    converted_temperature = convert_fahrenheit_to_celsius(all_stations_data)
    temperature_sum = sum_temperature_all_stations(converted_temperature)
    wind_speed = average_wind_speed(all_stations_data)
    print("sum", temperature_sum)
    print("avg", temperature_sum / (len(converted_temperature) if len(converted_temperature) else 1))
    print("wind", wind_speed / len(all_stations_data))


if __name__ == "__main__":
    main()