#!/usr/bin/env -S python3
"""
Only calculates mean...
"""

import sys
import mean

if __name__ == "__main__":
    print(mean.calculate_mean(list(map(float, sys.argv[1:]))))
