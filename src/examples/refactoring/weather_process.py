"""This script is badly written on purpose to demonstrate refactoring."""

import pandas as pd

TEMPERATURE_THRESHOLD = 25
WEATHER_DATA_FILE_PATH = "./../../../data/weather_data.csv"


def convert_temperature_to_fahrenheit(observed_temperature, threshold=TEMPERATURE_THRESHOLD):
    # Convert temperature above the threshold to Fahrenheit
    t = observed_temperature.copy()
    mask = observed_temperature > threshold
    t[mask] = t[mask] * 1.8 + 32
    return t


def calculate_mean_wind_speed(weather_data):
    # Calculate the mean wind speed
    wind_speed = (weather_data["wind_u"] ** 2 + weather_data["wind_v"] ** 2) ** 0.5
    return wind_speed.mean()


def main():
    weather_records = pd.read_csv(WEATHER_DATA_FILE_PATH)
    converted_temperatures = convert_temperature_to_fahrenheit(weather_records["temp"])
    mean_wind_speed = calculate_mean_wind_speed(weather_records)
    print("sum", converted_temperatures.sum())
    print("avg", converted_temperatures.mean())
    print("wind", mean_wind_speed)


if __name__ == "__main__":
    main()
