"""Example for a factory."""


from abc import ABC, abstractmethod


# Product Interface
class WeatherParser(ABC):

    @abstractmethod
    def parse(self, raw_data: str) -> dict:
        pass


# Concrete Products
class SatelliteParser(WeatherParser):

    def __init__(self, orbit: str, resolution: str):
        self.orbit = orbit
        self.resolution = resolution
        print(f"SatelliteParser initialized with orbit={orbit}, resolution={resolution}")

    def parse(self, raw_data: str) -> dict:
        return {"source": "satellite", "orbit": self.orbit,
                "resolution": self.resolution, "data": raw_data.upper()}


class RadarParser(WeatherParser):

    def __init__(self, frequency: float):
        self.frequency = frequency
        print(f"RadarParser initialized with frequency={frequency} GHz")

    def parse(self, raw_data: str) -> dict:
        return {"source": "radar", "frequency": self.frequency,
                "data": raw_data.lower()}


class GroundStationParser(WeatherParser):

    def __init__(self, location: str, sensors: list[str]):
        self.location = location
        self.sensors = sensors
        print(f"GroundStationParser initialized at {location} with sensors={sensors}")

    def parse(self, raw_data: str) -> dict:
        return {"source": "ground", "location": self.location,
                "sensors": self.sensors, "data": raw_data[::-1]}


# Creator Interface
class ParserFactory(ABC):

    @abstractmethod
    def create_parser(self) -> WeatherParser:
        pass


# Concrete Factories
class SatelliteFactory(ParserFactory):

    def create_parser(self) -> WeatherParser:
        # Factory decides orbit/resolution
        return SatelliteParser(orbit="polar", resolution="1km")

class RadarFactory(ParserFactory):

    def create_parser(self) -> WeatherParser:
        # Factory decides frequency
        return RadarParser(frequency=5.6)

class GroundStationFactory(ParserFactory):

    def create_parser(self) -> WeatherParser:
        # Factory decides location/sensors
        return GroundStationParser(location="Hamburg", sensors=["temp", "humidity", "wind"])


# Client Code
def process_weather(factory: ParserFactory, raw_data: str):
    parser = factory.create_parser()  # client doesn’t know about orbit/frequency/location
    result = parser.parse(raw_data)
    print("Processed:", result)


def main():
    # Example usage
    process_weather(SatelliteFactory(), "Cloud data")
    process_weather(RadarFactory(), "Rain data")
    process_weather(GroundStationFactory(), "Wind data")


if __name__ == '__main__':
    main()
