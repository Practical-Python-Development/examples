"""This script is badly written on purpose to demonstrate refactoring."""

import pandas as pd
from pathlib import Path


PATH_TO_WEATHER_DATA = Path(__file__).parents[3] / "data" / "weather_data.csv"

OFFSET_C_TO_F = 32

FACTOR_F_TO_C = 1.8

TEMPERATURE_THRESHOLD_C = 25


def read_observations() -> pd.DataFrame:
    """Read weather data from csv file"""
    data: DataFrame = pd.read_csv(PATH_TO_WEATHER_DATA)
    return data


def convert_temperatures(
    temps: pd.Series,
    threshold: float = TEMPERATURE_THRESHOLD_C,
    factor: float = FACTOR_F_TO_C,
    offset: float = OFFSET_C_TO_F,
) -> pd.Series:
    """
    Convert temperatures above threshold to Fahrenheit

    :param temps: temperatures above threshold
    :param threshold: temperature threshold. Defaults to 25.0 C
    :param factor: factor to convert temperatures above threshold to Fahrenheit. defaults to 1.8
    :param offset: temperature offset in Fahrenheit. Defaults to 32
    """
    temps_converted = temps.copy()    # To avoid SettingWithCopyWarning
    mask = temps > threshold
    temps_converted[mask] = temps[mask] * factor + offset
    return temps_converted


def calculate_wind_speed(obs: pd.DataFrame) -> float:
    """Calculate mean horizontal wind speed"""
    horizontal_wind_speed = (obs['wind_u'] ** 2 + obs['wind_v'] ** 2) ** 0.5
    return horizontal_wind_speed.mean()


def main():
    records = read_observations()
    records["temp"] = convert_temperatures(records["temp"])
    mean_wind_speed = calculate_wind_speed(records)
    print("sum", records["temp"].sum())
    print("avg", records["temp"].mean())
    print("wind", mean_wind_speed)

if __name__ == "__main__":
    main()