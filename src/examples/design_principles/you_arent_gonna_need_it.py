"""
YAGNI (You Aren’t Gonna Need It).

Just write what you need at the moment, not what might become handy... maybe.
"""


# Bad example
class WeatherStation:
    def __init__(self):
        self.temperature: float | None = None
        self.humidity: float | None = None
        self.pressure: float | None = None
        self.wind_speed: float | None = None  # not used yet
        self.future_feature: float | None = None  # not used yet


# Good example
class WeatherStation:
    def __init__(self, temperature: float, humidity: float, pressure: float):
        self.temp = temperature
        self.humidity = humidity
        self.pressure = pressure
