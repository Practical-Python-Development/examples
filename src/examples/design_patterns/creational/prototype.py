"""Example for a factory."""


import copy
from abc import ABC, abstractmethod


# --- Prototype Interface ---
class WeatherModel(ABC):

    @abstractmethod
    def clone(self):
        pass


# --- Concrete Prototype: Satellite Model ---
class SatelliteModel(WeatherModel):

    def __init__(self, resolution, orbit, calibration):
        self.resolution = resolution
        self.orbit = orbit
        self.calibration = calibration

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"SatelliteModel(res={self.resolution}, orbit={self.orbit}, cal={self.calibration})"


# --- Concrete Prototype: Ground Station Model ---
class GroundStationModel(WeatherModel):

    def __init__(self, location, sensors):
        self.location = location
        self.sensors = sensors

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"GroundStationModel(loc={self.location}, sensors={self.sensors})"


def main():
    # --- Client Code ---
    satellite = SatelliteModel("1km", "polar", {"temp": "calibrated"})
    clone_satellite = satellite.clone()

    ground = GroundStationModel("Hamburg", ["temp", "humidity", "wind"])
    clone_ground = ground.clone()

    print("Satellite:")
    print("Original:", satellite)
    print("Clone   :", clone_satellite)

    print("Ground:")
    print("Original:", ground)
    print("Clone   :", clone_ground)


if __name__ == '__main__':
    main()
