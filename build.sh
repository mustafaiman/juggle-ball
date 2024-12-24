#!/bin/bash

# Activate virtual environment
source activate.sh

# Install dependencies if needed
if [ ! -f "venv/installed_requirements" ]; then
    pip install -r requirements.txt
    touch venv/installed_requirements
fi

# Create dist directory if it doesn't exist
mkdir -p dist

# Build executable using PyInstaller
pyinstaller --onefile \
            --name juggle_ball \
            --collect-all pygame \
            --hidden-import pygame \
            --log-level DEBUG \
            juggle_ball.py

echo "Build complete! Executable is in dist/juggle_ball" 