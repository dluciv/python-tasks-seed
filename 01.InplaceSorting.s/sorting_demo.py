#!/usr/bin/env -S python3
"""
Sortings demo
"""

from comp_swap_container import CompSwapList
import sortings

if __name__ == "__main__":
    # trivial_sort2
    data: CompSwapList[int] = CompSwapList([2, 1])
    sortings.trivial_sort2(data)
    print(f"Comps: {data.comps}, Swaps: {data.swaps}")
