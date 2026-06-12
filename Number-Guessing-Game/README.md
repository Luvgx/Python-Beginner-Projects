# Number Guessing Game 🎯

A simple command-line Number Guessing Game built using Python.

The computer randomly selects a number, and the player must guess it. The game provides hints such as **Too High**, **Too Low**, **Very Close**, and **Far Away** to help the player find the correct number.

## Features

* 🎮 Three difficulty levels:

  * Easy (1 - 50)
  * Medium (1 - 100)
  * Hard (1 - 500)

* 🔢 Random number generation using Python's `random` module

* 📈 Attempt counter

* 🔥 Smart hints:

  * Very Close!
  * Too Low!
  * Too High!
  * Far Away!

* ✅ Input validation for out-of-range guesses

* 🔄 Play Again option

* 🧩 Function-based code structure

## Concepts Used

* Functions
* Loops (`while`)
* Conditional Statements (`if`, `elif`, `else`)
* User Input
* Random Module
* Variables
* Basic Game Logic

## How to Run

1. Clone the repository

```bash
git clone <repository-link>
```

2. Open the project folder

```bash
cd Number-Guessing-Game
```

3. Run the program

```bash
python guessing_game.py
```

## Example Gameplay

```text
===== Number Guessing Game =====

---Select difficulty---

Easy(1 to 50) = e
Medium(1 to 100) = m
Hard(1 to 500) = h

Enter mode: e

Please enter a number between 1 and 50.

Attempt # 1
Enter your guess : 25

Too Low!

Attempt # 2
Enter your guess : 40

Very Close!

Attempt # 3
Enter your guess : 42

Congratulations!
You guessed the number in 3 attempts.
```

## Future Improvements

* Error handling using try-except
* High score system
* Limited attempts mode
* Multiplayer mode
* Difficulty customization

## Author

**Siddhant Tripathi**

Built as part of my Python learning and GitHub portfolio journey.
