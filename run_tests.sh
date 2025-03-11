#!/bin/bash

# Activate the virtual environment
source venv/Scripts/activate

# Run the test suite
pytest

# Check the result of pytest and return the corresponding exit code
if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed!"
    exit 1
fi