# Juggle Ball

A fast-paced arcade game where you control a yellow paddle to juggle bouncing balls. Each successful bounce increases your score, and every third bounce adds a new ball to the challenge. How many balls can you juggle at once?

## AI Development Disclaimer

This game was developed entirely using AI assistance tools:
- Game design and implementation guided by Claude (Anthropic)
- Code structure and organization suggested by AI
- Bug fixes and improvements made through AI collaboration

This project serves as an example of what can be achieved through human-AI collaboration in game development.

## Features

- **Dynamic Ball Physics**: Balls bounce realistically with increasing challenge
- **Score Multipliers**: Score points based on the number of balls you're juggling
- **High Score System**: Top 5 scores are saved locally
- **Smooth Controls**: Intuitive mouse-based paddle movement
- **Progressive Difficulty**: New balls are added as you play

## Installation

### Requirements
- Python 3.x
- Pygame

### Setup

1. Install Python from [python.org](https://python.org)

2. Build the game:

**Windows:**
```powershell
.\build.ps1
```

**macOS/Linux:**
```bash
chmod +x build.sh  # Make script executable (first time only)
./build.sh
```

The executable will be created in the `dist` directory.

## How to Play

1. **Start Screen**
   - Click "Play" to start a new game
   - Click "High Scores" to view the leaderboard

2. **During Game**
   - Move your mouse to control the yellow paddle
   - Keep the red balls bouncing
   - Score increases with each bounce
   - Every third bounce spawns a new ball
   - Game ends if any ball hits the bottom

3. **High Scores**
   - Enter your name if you achieve a top 5 score
   - View the leaderboard to see the best players

## Controls

- **Mouse Movement**: Control paddle
- **Left Click**: Menu navigation
- **Enter**: Submit high score name
- **Escape**: Return from high scores screen

## Project Structure

```
juggle-ball/
├── juggle_ball.py         # Main game file
├── src/
│   ├── ball.py           # Ball physics and behavior
│   ├── paddle.py         # Paddle controls and collision
│   ├── high_scores.py    # High score management
│   └── screens/          # Game screen implementations
│       ├── start_screen.py
│       ├── game_over_screen.py
│       └── high_scores_screen.py
```

## Development

The game is built with Python and Pygame, focusing on:
- Smooth gameplay mechanics
- Progressive difficulty scaling
- Local high score persistence
- Clean screen management

High scores are saved in `juggle_ball_high_scores.json` in the game directory.

## License

This project is open source and available under the MIT License. 