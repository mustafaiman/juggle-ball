#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Detect OS and activate accordingly
case "$(uname -s)" in
    MINGW*|CYGWIN*) # Windows
        source venv/Scripts/activate
        ;;
    *) # Linux, macOS, etc.
        source venv/bin/activate
        ;;
esac

# Install requirements if needed
if [ ! -f "venv/installed_requirements" ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
    touch venv/installed_requirements
fi

echo "Virtual environment activated! Use 'deactivate' to exit." 