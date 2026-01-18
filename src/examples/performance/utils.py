"""Utility functions for performance examples."""

import time
from functools import wraps


def timeit(func):
    """
    Decorate a function to be timed.

    :param func: The function to decorate
    :return: the result of the decorated function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function."""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__}: {end - start:.6f} seconds")
        return result

    return wrapper
