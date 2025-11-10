"""This script reads in observational data, to convert temperatures from Celsius to Fahrenheit
and to compute the horizontal mean wind speed."""

from pathlib import Path
import pandas as pd

PATH_WEATHER_DATA = Path(__file__).parents[3]/"data"/"weather_data.csv"
OFFSET_C_TO_F = 32
FACTOR_C_TO_F = 1.8
TEMP_THRESHOLD_C = 25


def read_in_observations(data_path: Path = PATH_WEATHER_DATA) -> pd.DataFrame:
    """Read observations from CSV file."""
    obs = pd.read_csv(data_path)
    return obs


def convert_temps(
        temps: pd.Series,
        threshold: float = TEMP_THRESHOLD_C,
        factor: float = FACTOR_C_TO_F,
        offset: float = OFFSET_C_TO_F
    ) -> pd.Series:
    """
    Convert temperatures above threshold from Celsius to Fahrenheit

    :param temps: Temperatures to convert.
    :param threshold: Temperature threshold. Defaults to 25
    :param factor: Temperature factor. Defaults to 1.8
    :param offset: Temperature offset in Fahrenheit. Defaults to 32.
    """
    temps_converted = temps.copy()
    mask = temps > threshold
    temps_converted[mask] = temps[mask] * factor + offset
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