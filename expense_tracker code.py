"""
Expense Tracker
Goal: Users enter expense amounts (e.g., 100, 50, 20).
The program adds them up and displays the Total Spent.
Key skill: Math operations and accumulators (total = total + new_expense).
"""

total = 0  # the accumulator

while True:
    entry = input("Enter expense (or 'done' to finish): ")
    if entry.lower() == "done":
        break
    try:
        total = total + float(entry)  # add the new expense to the total
    except ValueError:
        print("Please enter a valid number.")

print(f"Total Spent: {total}")
