# Development Guide

## Project Structure
```
juggle-ball/
├── juggle_ball.py         # Main game file
├── src/
│   ├── ball.py           # Ball physics and behavior
│   ├── paddle.py         # Paddle controls and collision
│   ├── high_scores.py    # High score management
│   └── screens/          # Game screen implementations
```

## Setting Up Development Environment

1. Clone the repository:
```bash
git clone https://github.com/yourusername/juggle-ball.git
cd juggle-ball
```

2. Create and activate virtual environment:
```bash
# Windows
.\build.ps1

# macOS/Linux
chmod +x build.sh
./build.sh
```

## Building the Game

The game can be built using PyInstaller through our build scripts:
- `build.sh` for macOS/Linux
- `build.ps1` for Windows

## Release Process

1. Update version number
2. Create and push a new tag:
```bash
git tag v1.0.0
git push origin v1.0.0
```

3. GitHub Actions will automatically:
   - Build for all platforms
   - Create a release
   - Attach binaries 