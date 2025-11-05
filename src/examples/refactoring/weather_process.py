"""This script is badly written on purpose to demonstrate refactoring."""

from pathlib import Path
import pandas as pd



WEATHER_DATA_PATH = Path(__file__).parents[3]/"data"/"weather_data.csv"
TEMP_THRESHOLD_CEL = 25.0
OFFSET_C_TO_F = 32.0
TEMP_C_TO_F = 1.8


def read_observations() -> pd.DataFrame:
    """Read observations from CSV file."""
    obs = pd.read_csv(WEATHER_DATA_PATH)
    return obs

def convert_temperatures(temps: pd.Series) -> pd.Series:
    """Convert temps above threshold to Fahrenheit.

    :param temps: Temperatures to convert.
    :param threshold: Temperature threshold. Defaults to 25.0
    :param factor: Temperature factor. Defaults to 1.8
    :param offset: Temperature offset in Fahrenheit. Defaults to 32.
    """
    temps_converted = temps.copy()
    mask = temps > TEMP_THRESHOLD_CEL
    temps_converted[mask] = temps[mask] * TEMP_C_TO_F + OFFSET_C_TO_F
    return temps_converted



def compute_mean_wind_speed(obs: pd.DataFrame) -> float:
    """Compute mean horizontal wind speed magnitude."""
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