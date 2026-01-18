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
    cities = ["Berlin", "Paris", "Rome", "Madrid"]

    df = pd.DataFrame({
        "city": np.random.choice(cities, size=num_rows)
    })

    df_cat = df.copy()
    df_cat["city"] = df_cat["city"].astype("category")

    groupby_object(df)
    groupby_category(df_cat)


if __name__ == "__main__":
    main()
