"""Example for an abstract factory."""


from abc import ABC, abstractmethod


# --- Abstract Products ---
class TemperatureSensor(ABC):

    @abstractmethod
    def read_temperature(self) -> float:
        pass


class HumiditySensor(ABC):

    @abstractmethod
    def read_humidity(self) -> float:
        pass


# --- Concrete Products ---
class SatelliteTemperatureSensor(TemperatureSensor):

    def read_temperature(self) -> float:
        return -50.0


class SatelliteHumiditySensor(HumiditySensor):

    def read_humidity(self) -> float:
        return 10.0


class GroundTemperatureSensor(TemperatureSensor):

    def read_temperature(self) -> float:
        return 20.0


class GroundHumiditySensor(HumiditySensor):

    def read_humidity(self) -> float:
        return 55.0


# --- Abstract Factory ---
class WeatherSensorFactory(ABC):

    @abstractmethod
    def create_temperature_sensor(self) -> TemperatureSensor:
        pass

    @abstractmethod
    def create_humidity_sensor(self) -> HumiditySensor:
        pass

# --- Concrete Factories ---
class SatelliteSensorFactory(WeatherSensorFactory):

    def create_temperature_sensor(self) -> TemperatureSensor:
        return SatelliteTemperatureSensor()

    def create_humidity_sensor(self) -> HumiditySensor:
        return SatelliteHumiditySensor()


class GroundSensorFactory(WeatherSensorFactory):

    def create_temperature_sensor(self) -> TemperatureSensor:
        return GroundTemperatureSensor()

    def create_humidity_sensor(self) -> HumiditySensor:
        return GroundHumiditySensor()


# --- Client Code ---
def monitor(factory: WeatherSensorFactory):
    temp_sensor = factory.create_temperature_sensor()
    hum_sensor = factory.create_humidity_sensor()
    print(f"Temperature: {temp_sensor.read_temperature()}°C")
    print(f"Humidity: {hum_sensor.read_humidity()}%")


def main():
    # Example usage
    monitor(SatelliteSensorFactory())
    monitor(GroundSensorFactory())


if __name__ == '__main__':
    main()
