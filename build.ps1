# Create virtual environment if it doesn't exist
if (-not (Test-Path "venv")) {
    python -m venv venv
}

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies if needed
if (-not (Test-Path "venv\installed_requirements")) {
    pip install -r requirements.txt
    New-Item -Path "venv\installed_requirements" -ItemType File
}

# Create dist directory if it doesn't exist
if (-not (Test-Path "dist")) {
    New-Item -Path "dist" -ItemType Directory
}

# Build executable using PyInstaller
pyinstaller --onefile `
            --name "juggle_ball" `
            --collect-all pygame `
            --hidden-import pygame `
            --log-level DEBUG `
            juggle_ball.py

Write-Host "Build complete! Executable is in dist\juggle_ball.exe" 