"""This script is badly written on purpose to demonstrate refactoring."""

import pandas as pd
from pathlib import Path

PATH_TO_WEATHER_DATA = Path(__file__).parents[3] / "data" / "weather_data.csv"

OFFSET_C_TO_F = 32

FACTOR_C_TO_F = 1.8

TEMP_THRESHOLD_C = 25

def read_observations(data_path: Path = PATH_TO_WEATHER_DATA) -> pd.DataFrame:
    """ Read observations from CSV file."""
    obs = pd.read_csv(data_path)
    return obs


def convert_temperatures(
        temps: pd.Series,
        threshold: float = TEMP_THRESHOLD_C,
        factor: float = FACTOR_C_TO_F,
        offset: float = OFFSET_C_TO_F
) -> pd.Series:
    """
    Convert temperatures above a certain threshold to Fahrenheit.

    :param temps: Temperatures to convert.
    :param threshold: Temperature threshold. Default is 25 degrees.
    :param factor: Temperature factor. Default is 1.8.
    :param offset: Temperature offset in Fahrenheit. Default is 32.
    """
    temps_converted = temps.copy()
    mask = temps > threshold
    temps_converted[mask] = temps[mask] * FACTOR_C_TO_F + OFFSET_C_TO_F
    return temps_converted


def compute_mean_windspeed(obs: pd.DataFrame) -> float:
    """ Compute mean horizontal wind speed magnitude."""
    horizontal_wind_speed = (obs["wind_u"] ** 2 + obs["wind_v"] ** 2) ** 0.5
    return horizontal_wind_speed.mean()


def main():
    records = read_observations()
    records["temp"] = convert_temperatures(records["temp"])
    mean_wind_speed = compute_mean_windspeed(records)
    print("sum", records["temp"].sum())
    print("avg", records["temp"].mean())
    print("wind", mean_wind_speed)

if __name__ == "__main__":
    main()