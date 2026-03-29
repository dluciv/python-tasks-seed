#!/bin/bash

result=$(uv run python -O ./calculator.py 1 2 3)

if [[ $result == "2.0" ]]; then
  echo Ok!
else
  echo Fail!
  exit 1
fi
