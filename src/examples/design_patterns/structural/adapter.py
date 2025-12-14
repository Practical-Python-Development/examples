"""Example for an adapter."""


from abc import ABC, abstractmethod
import json


class WeatherData(ABC):

    @abstractmethod
    def get_temperature(self) -> float:
        pass

    @abstractmethod
    def get_humidity(self) -> float:
        pass


class SatelliteFeed:

    def __init__(self, json_data: str):
        self.data = json.loads(json_data)

    def read_json(self):
        return self.data


class GroundStationFeed:

    def __init__(self, csv_data: str):
        self.data = csv_data.split(",")  # "temp,humidity"

    def read_csv(self):
        return self.data


class SatelliteAdapter(WeatherData):

    def __init__(self, satellite_feed: SatelliteFeed):
        self.feed = satellite_feed

    def get_temperature(self) -> float:
        return float(self.feed.read_json()["temp"])

    def get_humidity(self) -> float:
        return float(self.feed.read_json()["humidity"])


class GroundStationAdapter(WeatherData):

    def __init__(self, ground_feed: GroundStationFeed):
        self.feed = ground_feed

    def get_temperature(self) -> float:
        return float(self.feed.read_csv()[0])

    def get_humidity(self) -> float:
        return float(self.feed.read_csv()[1])


def main():
    satellite = SatelliteFeed('{"temp": -50, "humidity": 10}')
    ground = GroundStationFeed("20,55")

    adapters = [SatelliteAdapter(satellite), GroundStationAdapter(ground)]

    for source in adapters:
        print(f"Temp={source.get_temperature()}°C, Hum={source.get_humidity()}%")


if __name__ == '__main__':
    main()
