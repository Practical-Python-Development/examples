"""Example for a singleton."""


from __future__ import annotations  # Necessary to use class type insides of the class definition


class WeatherDatabase:

    __instance: WeatherDatabase | None = None
    __initialized: bool = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, connection_string="Central Weather DB"):
        if self.__initialized:
            return

        self.connection = f"Connection to {connection_string}"
        WeatherDatabase.__initialized = True

    def query(self, sql: str):
        return f"Executing '{sql}' on {self.connection}"


def main():
    # --- Client Code ---
    db1 = WeatherDatabase("Main Forecast DB")
    db2 = WeatherDatabase("Backup DB")  # !Ignored, still same instance!

    print(db1.query("SELECT * FROM forecasts"))
    print(db2.query("SELECT * FROM observations"))
    print("Same instance?", db1 is db2)  # True


if __name__ == '__main__':
    main()
