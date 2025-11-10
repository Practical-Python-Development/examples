"""This script is badly written on purpose to demonstrate refactoring."""

import csv, math

PATH_WEATHER_DATA = "./../../../data/weather_data.csv"
OFFSET_C_TO_F = 32
FACTOR_C_TO_F = 1.8
TEMP_THRESHOLD_C = 25


def convert_temps(obs):
    temps = []
    for records in obs:
        if float(records[1]) > TEMP_THRESHOLD_C:
            temps.append(float(records[1]) * FACTOR_C_TO_F + OFFSET_C_TO_F)
        else:
            temps.append(float(records[1]))
    return temps


def sum_temps(temps):
    sum_temps = 0
    for temp in temps:
        sum_temps += temp
    return sum_temps


def read_in_observations():
    read_in = open(PATH_WEATHER_DATA)
    station_data = list(csv.reader(read_in))
    read_in.close()
    station_data = station_data[1:]
    records = []
    for record in station_data:
        records.append([record[0], record[1], record[2], record[3], record[4]])
    return records


def compute_mean_wind_speed(records):
    total_wind_speed = 0
    for record in records:
        u = float(record[3])
        v = float(record[4])
        total_wind_speed += math.sqrt(u * u + v * v)
    return total_wind_speed / len(records)


def main():
    records = read_in_observations()
    converted_temps = convert_temps(records)
    total_temp = sum_temps(converted_temps)
    mean_wind_speed = compute_mean_wind_speed(records)
    print("sum", total_temp)
    print("avg", total_temp / (len(converted_temps) if len(converted_temps) else 1))
    print("wind", mean_wind_speed)

if __name__ == "__main__":
    main()