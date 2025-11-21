"""
Separation of Concerns.

Let a function/class just do one thing.
"""


# Bad example
def run_pipeline():
    ...
    # Download data
    # Clean data
    # Forecast
    # Plot results
    # Send email


# Good example
def download_data(): ...
def clean_data(): ...
def forecast(): ...
def plot_results(): ...
def send_email(): ...

def run_pipeline():
    data = download_data()
    clean = clean_data(data)
    prediction = forecast(clean)
    plot_results(prediction)
    send_email()
