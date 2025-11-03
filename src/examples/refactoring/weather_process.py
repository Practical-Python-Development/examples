"""This script is badly written on purpose to demonstrate refactoring."""

import csv, math

PATH_WEATHER_DATA = "./../../../data/weather_data.csv"
TEMP_THRESHOLD_C = 25
OFFSET_C_TO_K = 32
FACTOR_C_TO_F = 1.8


def convert_celsius_to_fahrenheit(a):
    t = []
    for i in a:
        if float(i[1]) > TEMP_THRESHOLD_C:
            t.append(float(i[1]) * FACTOR_C_TO_F + OFFSET_C_TO_K)
        else:
            t.append(float(i[1]))
    return t


def sum_temperatures(a):
    s = 0
    for i in a:
        s += i
    return s


def read_weather_data():
    file_handle = open(PATH_WEATHER_DATA)
    station_data = list(csv.reader(file_handle))
    file_handle.close()
    station_data = station_data[1:]  # remove header
    return station_data


def calculate_horizontal_wind_speed(station_data):
    horizontal_wind_speed = 0
    for i in station_data:
        u = float(i[3])
        v = float(i[4])
        horizontal_wind_speed += math.sqrt(u * u + v * v)
    return horizontal_wind_speed


def main():
    station_data = read_weather_data()
    temperatures = convert_celsius_to_fahrenheit(station_data)
    total_temperatures = sum_temperatures(temperatures)
    horizontal_wind_speed = calculate_horizontal_wind_speed(station_data)

    print("sum", total_temperatures)
    print("avg", total_temperatures / (len(temperatures) if len(temperatures) else 1))
    print("wind", horizontal_wind_speed / len(station_data))


if __name__ == '__main__':
    main()
