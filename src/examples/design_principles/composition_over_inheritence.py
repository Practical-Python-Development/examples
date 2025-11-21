"""
Composition over Inheritance.

You don't have to inherit from everything, were you want functionality, just have an instance with those capabilities.
"""


# Bad example
class CSVExporter:
    def export(self, data: dict, filename: str) -> None:
        with open(filename, "w") as f:
            f.write(",".join(data.keys()) + "\n")
            f.write(",".join(str(v) for v in data.values()) + "\n")

class WeatherStation(CSVExporter):  # Inheritance
    def __init__(self, temp: float, humidity: float):
        self.temp = temp
        self.humidity = humidity

    def collect_data(self) -> dict:
        return {"temperature": self.temp, "humidity": self.humidity}

# Usage
station = WeatherStation(22.5, 65.0)
station.export(station.collect_data(), "weather.csv")



# Good example
from abc import ABC, abstractmethod

class Exporter(ABC):
    @abstractmethod
    def export(self, data: dict, filename: str) -> None:
        ...


class CSVExporter(Exporter):
    def export(self, data: dict, filename: str) -> None:
        with open(filename, "w") as f:
            f.write(",".join(data.keys()) + "\n")
            f.write(",".join(str(v) for v in data.values()) + "\n")

class JSONExporter(Exporter):
    def export(self, data: dict, filename: str) -> None:
        import json
        with open(filename, "w") as f:
            json.dump(data, f)

class WeatherStation:
    def __init__(self, temp: float, humidity: float, exporter: Exporter) -> None:
        self.temp = temp
        self.humidity = humidity
        self.exporter = exporter  # Composition

    def collect_data(self) -> dict:
        return {"temperature": self.temp, "humidity": self.humidity}

    def save(self, filename: str) -> None:
        self.exporter.export(self.collect_data(), filename)

# Usage
station_csv = WeatherStation(22.5, 65.0, exporter=CSVExporter())
station_csv.save("weather.csv")

station_json = WeatherStation(22.5, 65.0, exporter=JSONExporter())
station_json.save("weather.json")

