"""This script is badly written on purpose to demonstrate refactoring."""

import pandas as pd

TEMP_THRESHOLD_C = 25

WEATHER_DATA_PATH = "./../../../data/weather_data.csv"

OFFSET_C_TO_F = 32

FACTOR_C_TO_F = 1.8


def celsius_to_fahrenheit(temperature):
    temps_converted = temperature.copy()
    mask = temperature > TEMP_THRESHOLD_C
    temps_converted[mask] = temps_converted[mask] * FACTOR_C_TO_F + OFFSET_C_TO_F
    return temps_converted





def read_weather_data():
    obs = pd.read_csv(WEATHER_DATA_PATH)
    return obs


def compute_mean_wind_speed(obs):
    horizontal_wind_speed = (obs["wind_u"] ** 2 + obs["wind_v"] ** 2) **0.5
    return horizontal_wind_speed.mean()

def main():
    records = read_weather_data()
    records["temp"] = celsius_to_fahrenheit(records["temp"])
    mean_wind_speed = compute_mean_wind_speed(records)
    print("sum", records["temp"].sum())
    print("avg", records["temp"].mean())
    print("mean", mean_wind_speed)

if __name__ == "__main__":
    main()

