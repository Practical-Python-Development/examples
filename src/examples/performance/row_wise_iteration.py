"""
Showcase row-wise operations vs. vectorization in pandas.

This module demonstrates three ways of computing the same result:
    - iterating row by row with iterrows (very slow)
    - using DataFrame.apply (still Python-level, slower)
    - using vectorized column operations (fast, runs in C)

Key lesson:
    pandas is optimized for column-wise (vectorized) operations.
    Row-wise operations force pandas back into slow Python loops.
"""

import numpy as np
import pandas as pd

from src.examples.performance.utils import timeit


@timeit
def iterrows_sum(df: pd.DataFrame):
    """
    Sum columns 'a' and 'b' row by row using iterrows().

    Why this is slow:
    - iterrows() creates a pandas Series for each row
    - Each iteration happens in Python
    - Massive overhead for large DataFrames
    """
    result = []
    for _, row in df.iterrows():
        result.append(row["a"] + row["b"])
    return result


@timeit
def apply_sum(df: pd.DataFrame):
    """
    Sum columns 'a' and 'b' using DataFrame.apply(axis=1).

    Why this is still slow:
    - apply() with axis=1 still loops in Python
    - Slightly cleaner syntax, but similar performance issues
    - Acceptable only for small DataFrames or complex logic
    """
    return df.apply(lambda row: row["a"] + row["b"], axis=1)


@timeit
def vectorized_sum(df: pd.DataFrame):
    """
    Sum columns 'a' and 'b' using vectorized operations.

    Why this is fast:
    - Operates on entire columns at once
    - Computation happens in optimized C/NumPy code
    - No Python-level loop
    """
    return df["a"] + df["b"]


def main():
    num_rows = 200_000
    df = pd.DataFrame({
        "a": np.random.rand(num_rows),
        "b": np.random.rand(num_rows),
    })

    iterrows_sum(df)
    apply_sum(df)
    vectorized_sum(df)


if __name__ == "__main__":
    main()
