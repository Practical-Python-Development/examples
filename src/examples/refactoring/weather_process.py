"""This script is badly written on purpose to demonstrate refactoring."""
import csv
import math


OPEN_WEATHER_DATA = './../../../data/weather_data.csv'
TEMP_THRESHOLD_C = 25
FACTOR_C_TO_F = 1.8
OFFSET_C_TO_F = 32


def convert_temperature(obs: list[list[str | float]]) -> list[float]:
    """Convert temps above threshold to Farenheit."""
    temps = []
    for record in obs:
        if float(record[1])> TEMP_THRESHOLD_C:
            temps.append(float(record[1]) * FACTOR_C_TO_F + OFFSET_C_TO_F)
        else:
            temps.append(float(record[1]))
    return temps

def sum_temperatures(temps: list[float]) -> float:
    """Return total of all temperatures."""
    return sum(temps)


def read_observations() -> list[list[str | float]]:
    """Read observations from CSV file."""
    r = open(OPEN_WEATHER_DATA)
    station_data = list(csv.reader(r))
    r.close()
    station_data = station_data[1:]
    return [[record[0], record[1], record[2], record[3], record[4]]
            for record in station_data
    ]


def compute_mean_wind_speed(records: list[list[str | float]]) -> float:
    total_wind_speed = 0
    for record in records:
        u = float(record[3])
        v = float(record[4])
        total_wind_speed += math.sqrt(u * u + v * v)
    return total_wind_speed / len(records)


def main():
    records = read_observations()
    converted_temps = convert_temperature(records)
    total_temp = sum_temperatures(converted_temps)
    mean_wind_speed = compute_mean_wind_speed(records)
    print('sum', total_temp)
    print('avg', total_temp / (len(converted_temps) if len(converted_temps) else 1))
    print('wind', mean_wind_speed)

if __name__ == '__main__':
    main()