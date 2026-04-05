"""
Sorting algorithms
"""


def builtin_sort(data):
    """
    Standard library sorting algorithm


    :param data: data to sort inplace
    :type data: list[BasicType] or other indexable sequence[BasicType]
    """
    if isinstance(data, list):
        data.sort()
    else:  # assume it is counting container
        data._array.sort()
