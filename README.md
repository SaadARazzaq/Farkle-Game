# Farkle Game

## Overview
Farkle is a popular dice game where players take turns rolling six dice to score points. The objective is to be the first player to reach 10,000 points. This Python-based version of Farkle features a graphical user interface (GUI) created with the Tkinter library. The game allows multiple human and AI players to compete.

![image](https://github.com/SaadARazzaq/Farkle-Game/assets/123338307/3808b02e-1b36-4c84-8f13-1a836cb10156)

## Features
- GUI-based gameplay using Tkinter
- Supports multiple human and AI players
- Dynamic status updates and score tracking
- Handles scoring combinations and game logic
- End-of-game winner announcement

## Requirements
- Python 3.x
- `tkinter` library (usually included with Python)

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the game script.
3. Navigate to the directory where the script is located.

## How to Play
1. Open your terminal or command prompt.
2. Run the script using Python:
    ```sh
    python farkle.py
    ```
3. Follow the on-screen prompts to start the game.

## Game Instructions
### Starting the Game
- When the game starts, you will be prompted to enter the number of human players and AI players.
- Enter the names for human players.

### Gameplay
- Each player takes turns rolling six dice.
- After rolling, the player can choose scoring combinations from the list.
- Points are awarded based on the chosen combinations.
- The player can continue rolling the remaining dice or end their turn to bank the current score.
- If a player rolls and cannot make any scoring combinations, they "Farkle" and lose the points accumulated in that turn.

### Scoring Combinations
- `111` = 1000 points
- `666` = 600 points
- `555` = 500 points
- `444` = 400 points
- `333` = 300 points
- `222` = 200 points
- `1` = 100 points
- `5` = 50 points

### Ending the Turn
- Click "End Turn" to bank your current score and pass the turn to the next player.
- The game proceeds until a player reaches the target score of 10,000 points.
- The last round starts when a player reaches or exceeds 10,000 points.

### Winning the Game
- The game ends when all players have completed the last round.
- The player with the highest score at the end of the game is declared the winner.

### Game Outputs

![image](https://github.com/SaadARazzaq/Farkle-Game/assets/123338307/3b59ea35-2999-41ee-aae4-72781f2c189f)
![image](https://github.com/SaadARazzaq/Farkle-Game/assets/123338307/b46b96de-0ada-4500-a9a4-bee1ada40e4a)
![image](https://github.com/SaadARazzaq/Farkle-Game/assets/123338307/b8988bb2-b7a0-4998-bf35-26f3395a0d09)

## Developer Notes
- The game uses the Tkinter library to create the GUI.
- The game logic handles dice rolls, scoring, turn management, and end-of-game conditions.
- The `POINTS` dictionary defines the scoring combinations and their respective points.

## Future Enhancements
- Add more sophisticated AI player logic.
- Improve the user interface for better user experience.
- Add options for customizing game rules and target score.

---

Enjoy playing Farkle! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Happy gaming!
