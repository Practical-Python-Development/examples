"""
Showcase the performance impact of data types in pandas.

This module compares groupby performance on:
    - object dtype (Python strings)
    - category dtype (integer codes + lookup table)

Key lesson:
    Choosing the right dtype can drastically improve
    both memory usage and performance.
"""

import numpy as np
import pandas as pd

from src.examples.performance.utils import timeit


@timeit
def groupby_object(df: pd.DataFrame):
    """
    Group by a column with object dtype.

    Why this is slower:
    - Comparisons are Python-level string operations
    - High memory usage
    """
    return df.groupby("city").size()


@timeit
def groupby_category(df: pd.DataFrame):
    """
    Group by a column with category dtype.

    Why this is faster:
    - Internally uses integer codes
    - Less memory
    - Faster comparisons
    """
    return df.groupby("city").size()


def main():
    num_rows = 1_000_000
    string_multiply = 10
    cities = ["Berlin" * string_multiply, "Paris" * string_multiply, "Rome" * string_multiply, "Madrid" * string_multiply]

    df = pd.DataFrame({
        "city": np.random.choice(cities, size=num_rows)
    })

    df_cat = df.copy()
    df_cat["city"] = df_cat["city"].astype("category")

    print(f'Memory usage of uncategorized: {df['city'].memory_usage(deep=True)} Bytes')
    print(f'Memory usage of categorized: {df_cat['city'].memory_usage(deep=True)} Bytes')
    print(f'Memory reduction by a factor of {df['city'].memory_usage(deep=True) / df_cat['city'].memory_usage(deep=True)}')
    # The effect will be bigger for longer strings

    groupby_object(df)
    groupby_category(df_cat)


if __name__ == "__main__":
    main()
