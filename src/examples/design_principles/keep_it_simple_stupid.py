"""
KISS (Keep It Simple, Stupid).

Sometimes something very smart, but it might get too smart. It should be understandable by everyone.
"""


# Bad example
def forecast(temp: float, humidity: float) -> str:
    return ("Storm likely", "No storm")[not (temp > 30 and humidity > 70)]


# Good example
def forecast(temp: float, humidity: float) -> str:
    if temp > 30 and humidity > 70:
        return "Storm likely"
    return "No storm"
