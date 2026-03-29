#!/bin/bash

status=true

# ---------------------------------------------------

result=$(uv run python -O ./calculator.py 1 2 3)

if [[ $result == "2.0" ]]; then
  echo "Calculates mean"
else
  echo "Fails to calculate mean" >&2
  status=false
fi

# ---------------------------------------------------

uv run python -O ./calculator.py
err=$?

if [[ $err == "1" ]]; then
  echo "Returns 1 on empty args"
else
  echo "Does not return 1 on empty args" >&2
  status=false
fi

$status
