"""This script is badly written on purpose to demonstrate refactoring."""

import numpy as np
from pathlib import Path
import pandas as pd

WEATHER_DATA_FILE = Path(__file__).parents[3] / "data" / "weather_data.csv"
CONVERT_TEMPERATURE_THRESHOLD = 25


def read_observed_data() -> pd.DataFrame:
    """Read observed weather data of different stations from a .csv file."""
    weather_data = pd.read_csv(WEATHER_DATA_FILE)
    return weather_data


def convert_fahrenheit_to_celsius(
    all_stations_obs_temp: pd.Series,
    conversion_threshold: float = CONVERT_TEMPERATURE_THRESHOLD
) -> pd.Series:
    """Convert temperature values from Fahrenheit to Celsius, in case the temperature value exceeds a conversion
    threshold.

    :param all_stations_obs_temp: Observed weather data of different stations available in the .csv file.
    :param conversion_threshold: Conversion threshold from Fahrenheit to Celsius. It is 25 Fahreneit per default.
    """
    converted_temp = all_stations_obs_temp.copy()
    conversion_mask = all_stations_obs_temp > conversion_threshold
    converted_temp[conversion_mask] = all_stations_obs_temp * 1.8 + 32

    return converted_temp


def sum_temperature_all_stations(observed_data_temp : pd.Series) -> float:
    """Calculates the sum of the temperature values from all stations.

    :param observed_data_temp: Observed weather data of different stations.
    """
    return sum(observed_data_temp)


def average_wind_speed(observed_data: pd.DataFrame) -> float:
    """Calculates the average wind speed across all stations from the observed wind's u- and v-component.
    """
    wind_speed = np.sqrt(observed_data["wind_u"] ** 2 + observed_data["wind_v"] ** 2)
    return wind_speed.mean()


def main():
    all_stations_data = read_observed_data()
    all_stations_data["temp"] = convert_fahrenheit_to_celsius(all_stations_data["temp"])
    temperature_sum = sum_temperature_all_stations(all_stations_data["temp"])
    wind_speed = average_wind_speed(all_stations_data)
    print("sum", temperature_sum)
    print("avg", all_stations_data["temp"].mean())
    print("wind", wind_speed / len(all_stations_data))


if __name__ == "__main__":
    main()