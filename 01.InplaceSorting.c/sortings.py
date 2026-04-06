"""
Sorting algorithms
"""

from __future__ import annotations
from typing import MutableSequence, Any

def builtin_sort(data: MutableSequence[Any]):
    """
    Standard library sorting algorithm


    :param data: data to sort inplace
    :type data: list[BasicType] or other indexable sequence[BasicType]
    """
    if isinstance(data, list):
        data.sort()
    else:  # assume it is counting container
        # TODO: скормить корректно, или оставить эту идею, и
        # сделать less & swap
        data._array.sort()
