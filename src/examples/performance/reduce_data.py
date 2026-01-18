"""
Showcase why filtering early improves pandas performance.

This module compares:
    - performing an expensive groupby before filtering
    - filtering rows first, then grouping a smaller DataFrame

Key lesson:
    Reduce data size as early as possible.
    Groupby, joins, and aggregations scale with the amount of data.
"""

import numpy as np
import pandas as pd

from src.examples.performance.utils import timeit


@timeit
def group_then_filter(df: pd.DataFrame):
    """
    Group the entire DataFrame first, then filter the result.

    Why this is slower:
    - Groupby processes all rows
    - Aggregation work is done even for data that will be discarded
    """
    grouped = df.groupby("city", observed=True).mean()
    return grouped[grouped["value"] > 0.5]


@timeit
def filter_then_group(df: pd.DataFrame):
    """
    Filter rows first, then group a smaller DataFrame.

    Why this is faster:
    - Fewer rows enter the groupby
    - Less aggregation work
    - Same logical result
    """
    filtered = df[df["value"] > 0.5]
    return filtered.groupby("city", observed=True).mean()


def main():
    num_rows = 1_000_000
    cities = ["Berlin", "Paris", "Rome", "Madrid"]

    df = pd.DataFrame({
        "city": np.random.choice(cities, size=num_rows),
        "value": np.random.rand(num_rows),
        "other": np.random.rand(num_rows),
    })

    group_then_filter(df)
    filter_then_group(df)


if __name__ == "__main__":
    main()
