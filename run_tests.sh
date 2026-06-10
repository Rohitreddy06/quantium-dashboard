#!/bin/bash

echo "Activating virtual environment..."


# Windows Git Bash
if [ -f "venv/Scripts/python.exe" ]; then

    PYTHON="venv/Scripts/python.exe"

# Linux/Mac
elif [ -f "venv/bin/python" ]; then

    PYTHON="venv/bin/python"

else

    echo "Virtual environment not found"
    exit 1

fi


echo "Running test suite..."


$PYTHON -m pytest


if [ $? -eq 0 ]; then

    echo "All tests passed"
    exit 0

else

    echo "Tests failed"
    exit 1

fi