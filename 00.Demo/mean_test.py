"""
Unit tests for 00.Demo
"""

import pytest
import mean


def test_calculate_mean() -> None:
    """Test with normal values"""
    result = mean.calculate_mean([1.0, 2.0, 3.0, 4.0, 5.0])
    assert result == 3.0


def test_calculate_mean_with_integers() -> None:
    """Test with integers (should be converted to float)"""
    result = mean.calculate_mean([1, 2, 3, 4, 5])
    assert result == 3.0


def test_calculate_mean_empty_list() -> None:
    """Test edge case"""
    with pytest.raises(ValueError):
        mean.calculate_mean([])
