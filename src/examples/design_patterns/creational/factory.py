"""Example for a factory."""


from abc import ABC, abstractmethod


# Product Interface
class WeatherParser(ABC):
    @abstractmethod
    def parse(self, raw_data: str) -> dict:
        pass


# Concrete Products
class SatelliteParser(WeatherParser):
    def parse(self, raw_data: str) -> dict:
        # Simulated parsing logic
        return {"source": "satellite", "temperature": -50, "humidity": 10}


class RadarParser(WeatherParser):
    def parse(self, raw_data: str) -> dict:
        return {"source": "radar", "temperature": 15, "humidity": 65}


class GroundStationParser(WeatherParser):
    def parse(self, raw_data: str) -> dict:
        return {"source": "ground", "temperature": 20, "humidity": 55}


# Creator
class ParserFactory(ABC):
    @abstractmethod
    def create_parser(self) -> WeatherParser:
        pass


# Concrete Creators
class SatelliteFactory(ParserFactory):
    def create_parser(self) -> WeatherParser:
        return SatelliteParser()


class RadarFactory(ParserFactory):
    def create_parser(self) -> WeatherParser:
        return RadarParser()


class GroundStationFactory(ParserFactory):
    def create_parser(self) -> WeatherParser:
        return GroundStationParser()


# Client Code
def process_weather(factory: ParserFactory, raw_data: str):
    parser = factory.create_parser()
    parsed = parser.parse(raw_data)
    print(f"Source: {parsed['source']}, Temp: {parsed['temperature']}°C, Humidity: {parsed['humidity']}%")


def main():
    # Example usage
    process_weather(SatelliteFactory(), "SAT_RAW")
    process_weather(RadarFactory(), "RADAR_RAW")
    process_weather(GroundStationFactory(), "GROUND_RAW")


if __name__ == '__main__':
    main()
