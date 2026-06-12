# Simple Calculator

This is a basic command-line calculator written in Python. It lets you pick two numbers and perform one of four operations on them — addition, subtraction, multiplication, or division.

## How it works

When you run `main.py`, it first prints the developer name and the current date and time. Then it shows a menu with the available operations and asks you to enter two numbers and choose what you want to do with them. Based on your input, it calls the matching function from `utils.py` and prints the result. If you type something that doesn't match any operation, it just tells you the command is invalid.

## Project structure

- **src/main.py** — The entry point. Handles user input, displays the menu, and calls the right utility function depending on what operation the user picks.
- **src/utils.py** — Contains the four math functions: `add`, `subtract`, `multiply`, and `divide`. The divide function has a small safety check so it won't crash if you try to divide by zero.

## Supported operations

- Addition
- Subtraction
- Multiplication
- Division (with divide-by-zero handling)

## Running the project

Just navigate to the `src` folder and run:

```
python main.py
```

It will walk you through the rest from there.
