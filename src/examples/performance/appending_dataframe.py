"""
Showcase why repeatedly concatenating DataFrames is slow.

This module compares:
    - repeatedly concatenating small DataFrames inside a loop (slow)
    - collecting data first and concatenating once (fast)

Key lesson:
    DataFrames are not designed for incremental growth.
    Repeated concatenation causes repeated memory allocation and copying.
    Always collect first, then concatenate once.
"""

import pandas as pd

from src.examples.performance.utils import timeit


@timeit
def bad_repeated_concat(num_rows: int):
    """
    Build a DataFrame by repeatedly concatenating small DataFrames.

    Why this is slow:
    - Each pd.concat creates a brand-new DataFrame
    - All existing data is copied every iteration
    - Results in quadratic time complexity

    This is the modern equivalent of the old df.append anti-pattern.
    """
    df = pd.DataFrame(columns=["a"])

    for i in range(num_rows):
        new_row = pd.DataFrame({"a": [i]})
        df = pd.concat([df, new_row], ignore_index=True)

    return df


@timeit
def good_collect_then_concat(num_rows: int):
    """
    Collect rows first and concatenate once.

    Why this is fast:
    - Python lists are efficient for appends
    - DataFrame allocation happens only once
    - Linear time complexity
    """
    dfs = []

    for i in range(num_rows):
        dfs.append(pd.DataFrame({"a": [i]}))

    return pd.concat(dfs, ignore_index=True)


@timeit
def best_collect_dicts_then_create(num_rows: int):
    """
    Collect row data as dictionaries and create the DataFrame once.

    Why this is fastest:
    - No intermediate DataFrames
    - Minimal overhead
    - Recommended pattern when building data row by row
    """
    rows = []

    for i in range(num_rows):
        rows.append({"a": i})

    return pd.DataFrame(rows)


def main():
    num_rows = 20_000

    bad_repeated_concat(num_rows)
    good_collect_then_concat(num_rows)
    best_collect_dicts_then_create(num_rows)


if __name__ == "__main__":
    main()
