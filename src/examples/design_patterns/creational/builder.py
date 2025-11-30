"""Example for a builder."""


from abc import ABC, abstractmethod
from dataclasses import dataclass


# --- Product ---
@dataclass
class WeatherReport:
    temperature: float = None
    humidity: float = None
    wind_speed: float = None
    precipitation: float = None

    def __str__(self):
        return (f"Weather Report -> Temp: {self.temperature}°C, "
                f"Humidity: {self.humidity}%, "
                f"Wind: {self.wind_speed} km/h, "
                f"Precipitation: {self.precipitation} mm")


# --- Abstract Builder ---
class WeatherReportBuilder(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def add_temperature(self, temp: float):
        pass

    @abstractmethod
    def add_humidity(self, hum: float):
        pass

    @abstractmethod
    def add_wind_speed(self, wind: float):
        pass

    @abstractmethod
    def add_precipitation(self, precip: float):
        pass

    @abstractmethod
    def build(self) -> WeatherReport:
        pass


# --- Concrete Builder 1: Detailed Report ---
class DetailedWeatherReportBuilder(WeatherReportBuilder):

    def __init__(self):
        self.reset()

    def reset(self):
        self.report = WeatherReport()

    def add_temperature(self, temp: float):
        self.report.temperature = temp

    def add_humidity(self, hum: float):
        self.report.humidity = hum

    def add_wind_speed(self, wind: float):
        self.report.wind_speed = wind

    def add_precipitation(self, precip: float):
        self.report.precipitation = precip

    def build(self) -> WeatherReport:
        product = self.report
        self.reset()
        return product


# --- Concrete Builder 2: Minimal Report ---
class MinimalWeatherReportBuilder(WeatherReportBuilder):

    def __init__(self):
        self.reset()

    def reset(self):
        self.report = WeatherReport()

    def add_temperature(self, temp: float):
        self.report.temperature = temp

    def add_humidity(self, hum: float):
        self.report.humidity = hum

    # Minimal builder ignores wind and precipitation
    def add_wind_speed(self, wind: float):
        pass

    def add_precipitation(self, precip: float):
        pass

    def build(self) -> WeatherReport:
        product = self.report
        self.reset()
        return product


# --- Director ---
class WeatherReportDirector:

    def __init__(self, builder: WeatherReportBuilder):
        self.builder = builder

    def construct_standard_report(self, temp: float, hum: float, wind: float, precip: float):
        self.builder.add_temperature(temp)
        self.builder.add_humidity(hum)
        self.builder.add_wind_speed(wind)
        self.builder.add_precipitation(precip)
        return self.builder.build()

    def construct_minimal_report(self, temp: float, hum: float):
        self.builder.add_temperature(temp)
        self.builder.add_humidity(hum)
        return self.builder.build()


def main():
    # --- Client Code ---
    detailed_builder = DetailedWeatherReportBuilder()
    director = WeatherReportDirector(detailed_builder)
    report1 = director.construct_standard_report(20, 55, 30, 5)
    print(report1)

    minimal_builder = MinimalWeatherReportBuilder()
    director = WeatherReportDirector(minimal_builder)
    report2 = director.construct_minimal_report(22, 60)
    print(report2)


if __name__ == '__main__':
    main()
