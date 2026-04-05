#!/usr/bin/env -S python3
"""
Sortings demo
"""

from beartype import beartype
import random
from counting_container import CountingList, CountingOrdered
import sortings

if __name__ == "__main__":
    raw_data = list(range(1000))
    random.shuffle(raw_data)
    data: CountingList[CountingOrdered[int]] = CountingList(
        [CountingOrdered(e) for e in raw_data]
    )
    sortings.builtin_sort(data)
    print(
        f"Comps: {CountingOrdered.comparisons()}, Swaps: {CountingList.likely_swaps()}"
    )
