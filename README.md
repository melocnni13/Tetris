# Tetris in Terminal

A classic Tetris game implemented in Python, running in the terminal with colorful graphics.

## Features

- 🎮 **7 classic shapes** (I, O, T, L, J, S, Z)
- 🎨 **Colored blocks** (each piece has its own color)
- 👻 **Ghost piece** (shows where the piece will land)
- ⏩ **Next piece preview**
- 💾 **Hold piece mechanic**
- 📊 **Score system** (100 points per line)
- ⚡ **Increasing speed** (every 200 points)
- 🔄 **Full game reset** after Game Over
- ⌨️ **Keyboard controls**

## Controls

| Key | Action |
|-----|--------|
| A | Move Left |
| D | Move Right |
| W | Rotate |
| S | Fast Drop |
| H | Hold Piece |
| Q | Quit Game |

## How to Play

1. Run the script
2. Press `1` in the menu to start
3. Move and rotate pieces to complete horizontal lines
4. Each completed line gives 100 points
5. Game speeds up as you score more points
6. Game ends when pieces reach the top

## Requirements

- Python 3.x
- `keyboard` library

## Installation

```bash
pip install keyboard
python tetris.py
Author

Created as a learning project — a step from Snake to Pong to Tetris.

License

Feel free to use, modify, and learn from this code!
