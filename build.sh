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
            --name catch_game \
            --collect-all pygame \
            --hidden-import pygame \
            --log-level DEBUG \
            catch_game.py

echo "Build complete! Executable is in dist/catch_game" 