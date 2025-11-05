"""This script is badly written on purpose to demonstrate refactoring."""

import csv, math

TEMP_THRESHOLD_C = 25

WEATHER_DATA_PATH = "./../../../data/weather_data.csv"

OFFSET_C_TO_F = 32

FACTOR_C_TO_F = 1.8


def celcius_to_fahrenheit(a):
    t = []
    for i in a:
        if float(i[1]) > TEMP_THRESHOLD_C:
            t.append(float(i[1]) * FACTOR_C_TO_F + OFFSET_C_TO_F)
        else:
            t.append(float(i[1]))
    return t


def sum_temperatures(temps):
    sum = 0
    for t in temps:
        sum += t
    return sum


def read_weather_data():
    r = open(WEATHER_DATA_PATH)
    station_data = list(csv.reader(r))
    r.close()
    station_data = station_data[1:]
    records = []
    for record in station_data:
        records.append([record[0], record[1], record[2], record[3], record[4]])
    return records



y = celcius_to_fahrenheit(read_weather_data())
z = sum_temperatures(y)
print("sum", z)
print("avg", z / (len(y) if len(y) else 1))



def compute_mean_wind_speed(records):
    wind_speed = 0
    for record in records:
        u = float(record[3])
        v = float(record[4])
        ws += math.sqrt(u**2 + v**2)
    print("wind", wind_speed / len(records))



