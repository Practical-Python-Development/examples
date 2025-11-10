"""This script is badly written on purpose to demonstrate refactoring."""

from pathlib import Path
import pandas as pd


PATH_WEATHER_DATA = Path(__file__).parents[3] / "data" / "weather_data.csv"
TEMP_THRESHOLD_C = 25
FACTOR_C_TO_F = 1.8
OFFSET_C_TO_F = 32


def read_observations(data_path: Path = PATH_WEATHER_DATA) -> pd.DataFrame:
    """Read observations from CSV file."""
    obs = pd.read_csv(data_path)
    return obs


def convert_temperatures(
    temps: pd.Series,
    threshold: float = TEMP_THRESHOLD_C,
) -> pd.Series:
    """
    Convert temps above given threshold to Fahrenheit.

    :param temps: Temperatures to convert.
    :param threshold: Threshold for converting to Fahrenheit. Defaults to 25.0
    """
    temps_converted = temps.copy()  # to avoid SettingWithCopyWarning
    mask = temps > TEMP_THRESHOLD_C
    temps_converted[mask] = temps[mask] * FACTOR_C_TO_F + OFFSET_C_TO_F
    return temps_converted


def compute_mean_wind_speed(obs: pd.DataFrame) -> float:
    """Compute mean horizontal wind speed from records."""
    horizontal_wind_speed = (obs["wind_u"] ** 2 + obs["wind_v"] ** 2) ** 0.5
    return horizontal_wind_speed.mean()


def main():
    records = read_observations()
    records["temp"] = convert_temperatures(records["temp"])
    mean_wind_speed = compute_mean_wind_speed(records)
    print("sum", records["temp"].sum())
    print("avg", records["temp"].mean())
    print("wind", mean_wind_speed)

if __name__ == "__main__":
    main()