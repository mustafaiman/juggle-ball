#!/bin/bash

# Function to activate virtual environment based on OS
activate_venv() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        source venv/bin/activate
    else
        # Linux
        source venv/bin/activate
    fi
}

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python -m venv venv
fi

# Activate virtual environment
activate_venv

# Install dependencies if needed
if [ ! -f "venv/installed_requirements" ]; then
    pip install -r requirements.txt
    touch venv/installed_requirements
fi

# Create dist directory if it doesn't exist
mkdir -p dist

# Build executable using PyInstaller
pyinstaller --onefile \
            --name "juggle_ball" \
            --collect-all pygame \
            --hidden-import pygame \
            --log-level DEBUG \
            juggle_ball.py

echo "Build complete! Executable is in dist/juggle_ball" 