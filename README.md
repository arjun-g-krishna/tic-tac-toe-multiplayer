# tic-tac-toe-multiplayer

A multiplayer tic-tac-toe game written in Python using TCP sockets for network communication.

## Description

This project implements a classic tic-tac-toe game that allows two players to play against each other over a network connection. One player hosts the game, and another player connects to play. The game uses Python's socket programming and threading to handle real-time multiplayer gameplay.

## Features

- **Network Multiplayer**: Play with another person over TCP connection
- **Real-time Gameplay**: Moves are synchronized between players instantly
- **Turn-based System**: Players alternate turns (X goes first)
- **Win Detection**: Automatically detects wins (rows, columns, diagonals) and ties
- **Input Validation**: Prevents invalid moves and out-of-bounds errors
- **Visual Board Display**: ASCII-based board representation in the terminal

## Requirements

- Python 3.x
- No external dependencies (uses standard library only)

## How to Play

### Step 1: Start the Host

On the first computer (or terminal), run the host script:

```bash
python host.py
```

This will:

- Start a server on `localhost:3000`
- Wait for a player to connect
- Assign you as Player X (goes first)

### Step 2: Connect as Second Player

On the second computer (or another terminal), run the connect script:

```bash
python connect.py
```

This will:

- Connect to the host at `localhost:3000`
- Assign you as Player O (goes second)
- Start the game

### Step 3: Make Moves

When it's your turn, enter your move in the format: `row,column`

- Rows and columns are indexed from 0 to 2
- Example: `0,0` places your marker in the top-left corner
- Example: `1,1` places your marker in the center
- Example: `2,2` places your marker in the bottom-right corner

**Board Layout:**

```
(0,0) | (0,1) | (0,2)
------|-------|------
(1,0) | (1,1) | (1,2)
------|-------|------
(2,0) | (2,1) | (2,2)
```

### Game Rules

1. Player X always goes first
2. Players alternate turns
3. A player wins by getting three of their markers in a row (horizontally, vertically, or diagonally)
4. If all 9 squares are filled without a winner, the game is a tie
5. Invalid moves (out of bounds or occupied squares) are rejected

## Configuration

To play over a network (not just localhost):

1. **In `host.py`**, change the host parameter:

   ```python
   game.host_game('0.0.0.0', 3000)  # Listen on all interfaces
   ```

2. **In `connect.py`**, change the host parameter to the host's IP address:

   ```python
   game.connect_to_game('192.168.1.100', 3000)  # Replace with actual IP
   ```

3. Ensure the port (default: 3000) is open in your firewall

## Code Structure

### TicTacToe Class

The main game logic is implemented in the `TicTacToe` class, which includes:

- `__init__()`: Initializes the game board and state
- `host_game(host, port)`: Hosts a game server
- `connect_to_game(host, port)`: Connects to a hosted game
- `handle_connection(client)`: Manages the game loop and player turns
- `apply_move(move, player)`: Applies a move to the board and checks for game end
- `check_valid_move(move)`: Validates player moves
- `check_if_won()`: Checks for winning conditions
- `print_board()`: Displays the current board state

## Example Gameplay

```
 |   |
---------
 |   |
---------
 |   |
Enter a move in the format (row,column): 1,1

 |   |
---------
 | X |
---------
 |   |

 |   |
---------
 | X |
---------
O |   |

... (game continues)

X | O | X
---------
O | X | O
---------
O | X | X
You win
```

## Limitations

- Currently configured for localhost play by default
- No GUI (terminal-based only)
- No game replay or move history
- No AI opponent option
- Requires manual network configuration for remote play
