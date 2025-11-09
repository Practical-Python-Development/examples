"""This script is badly written on purpose to demonstrate refactoring."""

import csv, math
import pandas as pd
from pathlib import Path

TEMP_THRESHOLD = 25
PATH_WEATHER_DATA = "./../../../data/weather_data.csv"
FACTOR_C_TO_F = 1.8
OFFSET_C_TO_F = 32


def read_observations(data_path: Path = PATH_WEATHER_DATA) -> pd.DataFrame:
    """read observations from csv file"""
    obs = pd.read_csv(data_path)
    return obs


def convert_temp(
    temps: pd.Series,
    threshold: float = TEMP_THRESHOLD,
    factor: float = FACTOR_C_TO_F,
    offset: float = OFFSET_C_TO_F,
) -> pd.Series:
    """
    convert temps above threshold to Fahrenheit

    :param temps: series of temps
    :param threshold: temperature threshold
    :param factor: temperature factor
    :param offset: temperature offset
    """
    temps_converted = temps.copy()
    mask = temps > threshold
    temps_converted[mask] = temps[mask] * factor + offset
    return temps_converted


def compute_mean_wind_speed(obs: pd.DataFrame) -> float:
    """compute mean horizontal wind speed"""
    horizontal_wind_speed = (obs["wind_u"] ** 2 + obs["wind_v"] ** 2) ** 0.5
    return horizontal_wind_speed.mean()


def main():
    records = read_observations()
    records["temp"] = convert_temp(records["temp"])
    mean_wind_speed = compute_mean_wind_speed(records)
    print("sum", records["temp"].sum())
    print("avg", records["temp"].mean())
    print("wind", mean_wind_speed)


if __name__ == "__main__":
    main()
