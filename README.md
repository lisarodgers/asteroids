# Asteroids — Boot.dev Game Development Project

This repository contains my implementation of the **Asteroids** game built as part of the Boot.dev coursework.  
The project walks through core game development concepts using **Python**, **Pygame**, and structured programming practices.

Boot.dev provides the requirements and incremental assignments; this repository represents my working version of the full project.

---

## 🎮 Project Overview

The goal of this assignment series is to implement a simplified version of the classic **Asteroids** arcade game.  
Throughout the project, various features are added step-by-step, including:

- Player ship movement, rotation, and physics
- Shooting mechanics (bullets / shots)
- Randomly generated asteroids with splitting behavior
- Collision detection between objects
- Sprite groups for rendering and updates
- A basic game loop with timing (FPS control)
- Logging game state snapshots for debugging and automated testing
- Clean object-oriented architecture

The final result is a functional, minimal Asteroids clone written in Python.

---

## 🧰 Technologies Used

- **Python 3**
- **Pygame**
- Boot.dev-provided modules and instructions
- JSON Lines logging (`game_state.jsonl`)
- Git & GitHub for version control

---

## 🚀 How to Run

Make sure you have Python and Pygame installed:

```bash
pip install pygame
Then run the game:

bash
Copy code
python main.py
Use the following controls (as implemented in the course):

Arrow keys / WASD — Move and rotate the ship

Spacebar — Shoot

Colliding with an asteroid ends the game

📁 Project Structure
cpp
Copy code
main.py
constants.py
player.py
asteroid.py
asteroidfield.py
shot.py
logger.py
game_state.jsonl  (auto-generated)
README.md
Boot.dev tests rely on certain output and behavior, such as:

Printing game startup information

Maintaining consistent sprite groups

Calling log_state() inside the game loop

📝 Purpose
This code is educational and is written specifically to complete the Boot.dev Game Development path.
It is not intended to be a full-featured game, but a guided learning project.

If you’re enrolled in Boot.dev, please follow their academic honesty guidelines and do not copy code without understanding it.

📜 License
This project is released under the MIT license to allow simple sharing and learning.

🙌 Acknowledgments
Thanks to Boot.dev for providing the curriculum, testing framework, and project scaffolding.