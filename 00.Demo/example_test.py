"""
Unit tests for 00.Demo
"""

import numpy as np
import pytest
from beartype import beartype


@beartype
def calculate_mean(numbers: list[float]) -> float:
    """Calculate mean with type checking"""
    return float(np.mean(numbers))


def test_calculate_mean() -> None:
    """Test with normal values"""
    result = calculate_mean([1.0, 2.0, 3.0, 4.0, 5.0])
    assert result == 3.0


def test_calculate_mean_with_integers() -> None:
    """Test with integers (should be converted to float)"""
    result = calculate_mean([1, 2, 3, 4, 5])
    assert result == 3.0


def test_calculate_mean_empty_list() -> None:
    """Test edge case"""
    with pytest.raises(ValueError):
        calculate_mean([])
