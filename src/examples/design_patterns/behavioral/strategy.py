"""Example for a strategy."""

from abc import ABC, abstractmethod


class ForecastStrategy(ABC):

    @abstractmethod
    def forecast(self, temperature: float, humidity: float) -> str:
        pass


class SimpleForecast(ForecastStrategy):
    def forecast(self, temperature: float, humidity: float) -> str:
        return f"Simple forecast: Temp={temperature}°C, Hum={humidity}%"


class RainForecast(ForecastStrategy):
    def forecast(self, temperature: float, humidity: float) -> str:
        if humidity > 70:
            return "Rain forecast: High chance of rain."
        return "Rain forecast: Low chance of rain."


class WindForecast(ForecastStrategy):
    def forecast(self, temperature: float, humidity: float) -> str:
        return f"Wind forecast: Expect gusts with temp={temperature}°C."


class WeatherReport:
    def __init__(self, strategy: ForecastStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ForecastStrategy):
        self._strategy = strategy

    def generate(self, temperature: float, humidity: float) -> str:
        return self._strategy.forecast(temperature, humidity)


# --- Client Code ---
def main():
    report = WeatherReport(SimpleForecast())
    print(report.generate(20, 55))

    report.set_strategy(RainForecast())
    print(report.generate(20, 80))

    report.set_strategy(WindForecast())
    print(report.generate(15, 60))


if __name__ == '__main__':
    main()
