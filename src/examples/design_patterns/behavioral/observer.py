"""Example for an observer."""
from __future__ import annotations

from abc import ABC, abstractmethod


class WeatherSubject(ABC):

    @abstractmethod
    def attach(self, observer: WeatherObserver) -> None:
        pass

    @abstractmethod
    def detach(self, observer: WeatherObserver) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class WeatherStation(WeatherSubject):
    def __init__(self):
        self._observers: list[WeatherObserver] = []
        self._temperature: float = 0.0

    def attach(self, observer: WeatherObserver) -> None:
        self._observers.append(observer)

    def detach(self, observer: WeatherObserver) -> None:
        self._observers.remove(observer)

    def set_temperature(self, temp: float) -> None:
        self._temperature = temp
        self.notify()

    def get_temperature(self) -> float:
        return self._temperature

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)


class WeatherObserver(ABC):

    @abstractmethod
    def update(self, subject: WeatherStation) -> None:
        pass


class TemperatureDisplay(WeatherObserver):
    def update(self, subject: WeatherStation) -> None:
        print(f"Temperature Display: {subject.get_temperature()}°C")


class AlertSystem(WeatherObserver):
    def update(self, subject: WeatherStation) -> None:
        if subject.get_temperature() < 0:
            print("Alert System: Freezing warning!")
        else:
            print("Alert System: Conditions normal.")


# --- Client Code ---
def main():
    station = WeatherStation()
    display = TemperatureDisplay()
    alert = AlertSystem()

    station.attach(display)
    station.attach(alert)

    station.set_temperature(5)
    station.set_temperature(-2)


if __name__ == '__main__':
    main()
