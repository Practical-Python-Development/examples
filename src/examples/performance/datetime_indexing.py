"""
Showcase time series grouping using a DatetimeIndex and a monthly Grouper.

This module demonstrates:
    - grouping by month using a DatetimeIndex (recommended)
    - grouping by an extracted month column (less efficient)

Key lesson:
    pandas is optimized for time-based operations on DatetimeIndex.
    Use pd.Grouper instead of manually extracting date components.
"""

import datetime as dt

import numpy as np
import pandas as pd

from src.examples.performance.utils import timeit


@timeit
def groupby_month_with_grouper(df: pd.DataFrame):
    """
    Group time series data by month using pd.Grouper.

    Why this is fast and idiomatic:
    - Uses the DatetimeIndex directly
    - No additional columns created
    - pandas uses optimized time-based grouping
    """
    return df.groupby(pd.Grouper(freq="M")).sum()


@timeit
def groupby_month_with_column(df: pd.DataFrame):
    """
    Group time series data by extracting year and month into a column.

    Why this is slower:
    - Requires creating a new column
    - Involves Python-level datetime access
    - Uses object or integer grouping instead of time-aware grouping
    """
    tmp = df.copy()
    tmp["year"] = tmp.index.year
    tmp["month"] = tmp.index.month
    tmp["day"] = tmp.index.day
    return tmp.groupby(['year', 'month', 'day'])["value"].sum()


def main():
    num_days = 1_000_000

    date_index = pd.date_range(
        start=dt.date(2026, 1, 1),
        periods=num_days,
        freq="h"
    )

    df = pd.DataFrame(
        {"value": np.random.rand(num_days)},
        index=date_index
    )

    groupby_month_with_grouper(df)
    groupby_month_with_column(df)


if __name__ == "__main__":
    main()
