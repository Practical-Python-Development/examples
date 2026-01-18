"""
Showcase views vs. copies in pandas.

This module demonstrates:
    - slicing that creates a copy
    - explicit copying
    - how easy it is to accidentally duplicate large amounts of data

Key lesson:
    Copies cost time and memory.
    pandas often copies data even when it looks like a view.
"""

import numpy as np
import pandas as pd

from src.examples.performance.utils import timeit


@timeit
def column_slice(df: pd.DataFrame):
    """
    Select a subset of columns using column indexing.

    Important:
    - This often creates a new DataFrame
    - Underlying data may be copied
    - Do not assume this is a cheap view
    """
    return df[["a", "b"]]


@timeit
def loc_column_slice(df: pd.DataFrame):
    """
    Select columns using .loc.

    Important:
    - Semantically clearer
    - Still may create a copy
    - Not guaranteed to be a view
    """
    return df.loc[:, ["a", "b"]]


@timeit
def explicit_copy(df: pd.DataFrame):
    """
    Explicitly create a copy of a DataFrame.

    Important:
    - Guarantees data isolation
    - Most expensive option
    - Use only when necessary
    """
    return df[["a", "b"]].copy()


def main():
    num_rows = 1_000_000
    df = pd.DataFrame({
        "a": np.random.rand(num_rows),
        "b": np.random.rand(num_rows),
        "c": np.random.rand(num_rows),
    })

    column_slice(df)
    loc_column_slice(df)
    explicit_copy(df)


if __name__ == "__main__":
    main()
