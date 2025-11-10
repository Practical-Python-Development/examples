"""This script is reads in observational data to convert temperatures from Celsius to Fahrenheit
and to compute the mean wind speed."""

from pathlib import Path
import pandas as pd

PATH_WEATHER_DATA = Path(__file__).parents[3]/"data"/"weather_data.csv"
OFFSET_C_TO_F = 32
FACTOR_C_TO_F = 1.8
TEMP_THRESHOLD_C = 25


def read_in_observations() -> pd.DataFrame:
    """Read observations from CSV file."""
    obs = pd.read_csv(PATH_WEATHER_DATA)
    return obs


def convert_temps(temps: pd.Series) -> pd.Series:
    """Convert temperatures above threshold from Celsius to Fahrenheit"""
    temps_converted = temps.copy()
    mask = temps > TEMP_THRESHOLD_C
    temps_converted[mask] = temps[mask] * FACTOR_C_TO_F + OFFSET_C_TO_F
    return temps_converted


def compute_mean_wind_speed(obs: pd.DataFrame) -> float:
    """Compute mean horizontal wind speed."""
    horizontal_wind_speed = (obs["wind_u"] ** 2 + obs["wind_v"] ** 2) ** 0.5
    return horizontal_wind_speed.mean()


def main():
    records = read_in_observations()
    records["temp"] = convert_temps(records["temp"] )
    mean_wind_speed = compute_mean_wind_speed(records)
    print("sum", records["temp"].sum())
    print("avg", records["temp"].mean())
    print("wind", mean_wind_speed)

if __name__ == "__main__":
    main()