#  Pong Game (Python Turtle)

A classic **Pong game implementation** built with Python using the `turtle` graphics library.  
This project demonstrates **object-oriented programming**, basic **game loop design**, collision handling, and modular code organization.

---

##  Features

- Two-player Pong gameplay
- Smooth ball movement with dynamic speed increase
- Paddle collision detection
- Score tracking system
- Modular and readable codebase
- Keyboard-controlled paddles

---

##  Technologies Used

- **Python 3**
- **turtle** (built-in Python graphics library)
- **Object-Oriented Programming (OOP)**

---

##  Controls

| Player | Move Up | Move Down |
|------|--------|-----------|
| Left Paddle | `W` | `S` |
| Right Paddle | `O` | `L` |

---

##  Project Structure

pong-game

 * main.py # Entry point and main game loop
 * ball.py # Ball movement, speed, and collision logic
 * paddles.py # Paddle class and player controls
 * field.py # Game field rendering (center line and circle)
 * score.py # Scoreboard and score management
 * README.md # Project documentation


---

##  Module Overview

### `main.py`
* responsibilities:
- Initializes the game screen
- Creates all game objects
- Handles keyboard input
- Runs the main game loop
- Manages collision detection and scoring

---

### `ball.py`
* responsibilities:
- Controls ball movement and direction
- Handles wall and paddle collisions
- Increases speed after paddle hits
- Resets position after a score

---

### `paddles.py`
* responsibilities:
- Defines paddle shape and size
- Handles paddle movement with boundary checks
- Encapsulates player control logic

---

### `field.py`
* responsibilities:
- Draws the center dashed line
- Renders the center circle
- Manages visual layout of the playfield

---

### `score.py`
* responsibilities:
- Displays scores for both players
- Updates score after each point
- Clears and redraws the scoreboard dynamically

---

 Concepts Demonstrated

* Object-Oriented Design
* Game loop mechanics
* Event-driven keyboard input
* Collision detection
* Separation of concerns
* Modular programming



And at the end it is my path while creating and writing this project:
1. making screen
2. making field
3. making the player and its logic for moving
4. making the ball and its logic for moving
5. creating the logic for coming the ball back after hitting the wall
6. the logic for creating the new ball
7. creating score and logic for tracking score
8. aditing and adding the logic for speed of the ball.
