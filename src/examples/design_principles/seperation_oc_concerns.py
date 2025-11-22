"""
Separation of Concerns.

Let a function/class just do one thing.
"""
from typing import Any


# Bad example
def run_pipeline():
    ...
    # Download data
    # Clean data
    # Forecast
    # Plot results
    # Send email


# Good example
def download_data() -> Any: ...
def clean_data(data: Any) -> Any: ...
def forecast(data: Any) -> Any: ...
def plot_results(data: Any): ...
def send_email(): ...

def run_pipeline():
    data = download_data()
    clean = clean_data(data)
    prediction = forecast(clean)
    plot_results(prediction)
    send_email()
