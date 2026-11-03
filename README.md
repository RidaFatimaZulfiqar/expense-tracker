# Expense Tracker

A simple command-line Python program that lets you enter expense amounts and adds them up to show the **Total Spent**.

## Goal

Create a script where users enter expense amounts (for example, `100`, `50`, `20`). The program adds them up and displays the total spent.

## Key Skill

**Math operations and accumulators**: keeping a running total by adding each new value to it:

```python
total = total + new_expense
```

## Why It Matters

Accumulators are essential for understanding data processing and calculations in backend logic, such as totals, balances, counters, and reports.

## Features

- Enter as many expenses as you like
- Type `done` (in any letter case) to finish
- Invalid input (like letters) is caught and the program asks again instead of crashing
- Displays the final **Total Spent**

## Requirements

- Python 3.6 or later (uses f-strings)

No external libraries are needed.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python expense_tracker.py
```

On some systems you may need to use `python3` or `py` instead of `python`.

## Example

```text
Enter expense (or 'done' to finish): 100
Enter expense (or 'done' to finish): 50
Enter expense (or 'done' to finish): 20
Enter expense (or 'done' to finish): abc
Please enter a valid number.
Enter expense (or 'done' to finish): done
Total Spent: 170.0
```

## The Code

```python
total = 0

while True:
    entry = input("Enter expense (or 'done' to finish): ")
    if entry.lower() == "done":
        break
    try:
        total = total + float(entry)
    except ValueError:
        print("Please enter a valid number.")

print(f"Total Spent: {total}")
```

## How It Works

1. `total = 0` creates the accumulator that stores the running sum.
2. A `while True` loop keeps asking for input until the user is finished.
3. If the user types `done`, `break` exits the loop.
4. Otherwise, `float(entry)` converts the text to a number, and it is added to `total`.
5. If the text is not a valid number, `float()` raises a `ValueError`, and the `except` block prints a friendly message.
6. After the loop ends, the program prints the Total Spent.

## Concepts Practiced

- Variables and accumulators
- `while` loops and `break`
- User input with `input()`
- Type conversion with `float()`
- Error handling with `try` / `except`
- f-string formatting

## Possible Improvements

- Format the total to two decimal places (`{total:.2f}`)
- Reject negative amounts
- Add expense categories
- Save expenses to a file

## Project Structure

```text
pythonproject/
├── expense_tracker.py
└── README.md
```
