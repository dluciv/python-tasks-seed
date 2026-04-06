"""
Алгоритмы сортировки
"""

from __future__ import annotations
from typing import Any
from comp_swap_container import CompSwapList


def trivial_sort2(data: CompSwapList[Any]):
    """
    Сортирует контейнер из 2 и менее элементов

    :param data: data to sort inplace
    :type data: MutableSequence[Ordered]
    """
    if len(data) <= 1:
        pass
    if len(data) > 2:
        raise ValueError("Просили не больше 2!")
    if data.less(1, 0):
        data.swap(0, 1)
