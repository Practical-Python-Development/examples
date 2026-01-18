"""
Showcase chained indexing vs. explicit .loc assignment.

This module demonstrates:
    - chained indexing, which may create hidden copies
    - proper .loc assignment, which is explicit and safe

Key lesson:
    Always use .loc for assignment in pandas.
    Chained indexing is ambiguous, slower, and error-prone.
"""

import numpy as np
import pandas as pd

from src.examples.performance.utils import timeit


@timeit
def chained_indexing(df: pd.DataFrame):
    """
    Assign values using chained indexing.

    Why this is bad:
    - May operate on a temporary copy
    - Can silently fail
    - Causes unnecessary memory allocations
    """
    df[df["a"] > 0.5]["b"] = 0


@timeit
def loc_assignment(df: pd.DataFrame):
    """
    Assign values using .loc.

    Why this is good:
    - Explicit and unambiguous
    - Avoids hidden copies
    - Faster and safer
    """
    df.loc[df["a"] > 0.5, "b"] = 0


def main():
    df = pd.DataFrame({
        "a": np.random.rand(1_000_000),
        "b": np.random.rand(1_000_000),
    })

    chained_indexing(df.copy())
    loc_assignment(df.copy())


if __name__ == "__main__":
    main()
