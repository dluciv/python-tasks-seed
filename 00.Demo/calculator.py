#!/usr/bin/env -S python3
"""
Only calculates mean...
"""

import sys
import mean

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide at least one number!", file=sys.stderr)
        sys.exit(1)

    print(mean.calculate_mean(list(map(float, sys.argv[1:]))))
