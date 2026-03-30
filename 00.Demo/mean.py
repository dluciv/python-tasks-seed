"""
Unit tests for 00.Demo
"""

import numpy as np
from beartype import beartype


@beartype
def calculate_mean(numbers: list[int | float]) -> float:
    """Calculate mean with type checking"""
    if len(numbers) == 0:
        raise ValueError()
    return float(np.mean(numbers))
