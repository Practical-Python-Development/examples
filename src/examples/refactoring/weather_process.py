"""This script is badly written on purpose to demonstrate refactoring."""

import pandas as pd

PATH_WEATHER_DATA = "./../../../data/weather_data.csv"
TEMP_THRESHOLD_C = 25
OFFSET_C_TO_K = 32
FACTOR_C_TO_F = 1.8


def convert_celsius_to_fahrenheit(temperatures_c: pd.Series) -> pd.Series:
    """Convert temperatures above a threshold from Celsius to Fahrenheit."""
    temperatures_c = temperatures_c.copy()
    mask = temperatures_c < TEMP_THRESHOLD_C
    temperatures_c[mask] = temperatures_c[mask] * FACTOR_C_TO_F + OFFSET_C_TO_K
    return temperatures_c


def read_weather_data() -> pd.DataFrame:
    return pd.read_csv(PATH_WEATHER_DATA)


def calculate_horizontal_wind_speed_mean(station_data: pd.DataFrame) -> pd.Series:
    horizontal_wind_speed = (
        station_data["wind_u"] ** 2 + station_data["wind_v"] ** 2
    ) ** 0.5
    return horizontal_wind_speed.mean()


def main():
    station_data = read_weather_data()
    temperatures = convert_celsius_to_fahrenheit(station_data["temp"])
    horizontal_wind_speed_mean = calculate_horizontal_wind_speed_mean(station_data)

    print("sum", temperatures.sum())
    print("avg", temperatures.mean())
    print("wind", horizontal_wind_speed_mean)


if __name__ == "__main__":
    main()
