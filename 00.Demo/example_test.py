import pytest
import numpy as np
from beartype import beartype


@beartype
def calculate_mean(numbers: list[float]) -> float:
    """Calculate mean with type checking"""
    return float(np.mean(numbers))

def test_calculate_mean():
    """Test with normal values"""
    result = calculate_mean([1.0, 2.0, 3.0, 4.0, 5.0])
    assert result == 3.0

def test_calculate_mean_with_integers():
    """Test with integers (should be converted to float)"""
    result = calculate_mean([1, 2, 3, 4, 5])
    assert result == 3.0

def test_calculate_mean_empty_list():
    """Test edge case"""
    with pytest.raises(ValueError):
        calculate_mean([])
