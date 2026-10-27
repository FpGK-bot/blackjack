# Blackjack CLI

A command-line Blackjack game developed in Python, featuring interactive gameplay against an automated dealer.

This is a personal programming project created to practise Python fundamentals, develop problem-solving skills, and explore the implementation of game logic and user interaction.

**Project Status:** Work in Progress

## Overview

Blackjack CLI is a terminal-based implementation of the classic Blackjack card game. Players compete against a computer-controlled dealer, with the objective of achieving a hand value as close to 21 as possible without exceeding it.

The game uses a standard 52-card deck and includes card dealing, hand-value calculations, player decisions, and automated dealer actions.

## Features

The current implementation includes:

- **Card Deck:** A 52-card deck consisting of four suits.
- **Random Card Dealing:** Cards are randomly selected from the remaining deck.
- **Hand Value Calculation:** Numerical and face cards are assigned their respective values, with aces considered as either 1 or 11.
- **Interactive Gameplay:** Players can choose to hit or stand through terminal inputs.
- **Automated Dealer:** Dealer actions are handled by the program.
- **Game Status Updates:** The terminal displays dealt cards and the current hand values.
- **Replay Functionality:** Players are prompted to start another round after a game.
- **Timed Output:** Short delays between actions create a more gradual gameplay experience.

*Some gameplay mechanics and round outcomes are still being refined.*

## Technologies Used

- **Python 3** — Core programming language
- **random** — Randomized card selection
- **time** — Delays between game actions

The project uses only Python's standard library and requires no additional packages.

## Getting Started

### Requirements

- Python 3 installed on your computer
- A terminal or command-line interface

### Installation

1. Clone or download this repository.
2. Navigate to the project directory.
3. Run the Python script:

`python blackjack.py`

### How to Play

1. Start the game through the terminal.
2. Receive your initial cards and view your hand.
3. Choose **Hit** to receive another card or **Stand** to end your turn.
4. The dealer plays automatically once the player's turn is complete.
5. View the outcome and choose whether to play again.

## Learning Objectives

This project provides an opportunity to practise and develop several programming concepts:

- **Python fundamentals:** Variables, functions, loops, and conditional statements.
- **Data structures:** Using lists, dictionaries, and tuples to represent cards, decks, and hands.
- **Game logic:** Translating Blackjack rules into programming logic.
- **User interaction:** Handling player input and displaying game information in the terminal.
- **State management:** Tracking cards, hand values, and gameplay progression.
- **Problem-solving:** Breaking down a game into smaller functions and logical components.

## Development Status

The project is currently under development. The existing version implements the basic structure of a playable Blackjack game, but gameplay mechanics, round handling, and overall reliability are still being refined.

Future improvements may include more comprehensive rule handling, improved terminal presentation, and additional gameplay features.

---

*Developed as an independent Python learning project.*
