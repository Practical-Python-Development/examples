"""Example for a composite."""


from abc import ABC, abstractmethod


class WeatherComponent(ABC):

    @abstractmethod
    def display(self) -> None:
        pass


class WeatherStation(WeatherComponent):

    def __init__(self, name: str, temperature: float):
        self.name = name
        self.temperature = temperature

    def display(self) -> None:
        print(f"Station {self.name}: {self.temperature}°C")


class WeatherRegion(WeatherComponent):

    def __init__(self, name: str):
        self.name = name
        self.children: list[WeatherComponent] = []

    def add(self, component: WeatherComponent) -> None:
        self.children.append(component)

    def remove(self, component: WeatherComponent) -> None:
        self.children.remove(component)

    def display(self) -> None:
        print(f"Region {self.name}:")
        for child in self.children:
            child.display()


def main():
    station1 = WeatherStation("Hamburg", 5)
    station2 = WeatherStation("Berlin", 3)
    station3 = WeatherStation("Munich", -2)

    north_region = WeatherRegion("Northern Germany")
    north_region.add(station1)
    north_region.add(station2)

    south_region = WeatherRegion("Southern Germany")
    south_region.add(station3)

    germany = WeatherRegion("Germany")
    germany.add(north_region)
    germany.add(south_region)

    # Client treats everything uniformly
    germany.display()


if __name__ == '__main__':
    main()
