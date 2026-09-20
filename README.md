# Personal Expense Tracker

A console-based expense tracker built in pure Python — no external data libraries required (except Matplotlib for the optional chart export). Built to practice object-oriented programming, file persistence, and error handling from Cisco's Python Essentials 1 & 2.

## Features

- Add expenses with input validation (rejects non-numeric amounts, re-prompts instead of crashing)
- View all recorded expenses
- Delete an expense by index
- Filter expenses by category
- Filter expenses by date range
- Summary report: total spent, and totals broken down by category
- Export a bar chart of spending by category (Matplotlib)
- Persistent storage — expenses are saved to a JSON file and reloaded automatically on the next run

## How to Run

```bash
python3 expense_tracker.py
```

Requires Python 3.9+ and Matplotlib (`pip install matplotlib`) for the chart export feature.

## Example

```
1. Add expense
2. View all expenses
3. Delete expense
4. Filter by category
5. Show summary
6. Export spending chart
7. Save and exit
Choose an option: 5
Total spent: 57.5
By category: {'Food': 12.5, 'Transport': 45.0}
```

## Project Structure

- `Expense` — represents a single expense (amount, category, date, description)
- `ExpenseTracker` — manages the collection: add, delete, filter, summarize, save/load, export chart
- `get_expense_input()` — handles user input and validation
- `main()` — the interactive menu loop

## What I Learned Building This

<!-- TODO — write this yourself, in your own words. Some things to consider:
- What was the hardest bug you had to fix, and how did you figure it out?
- What's the difference between a class and an instance, in your own words?
- Why does JSON persistence need to convert objects to dictionaries and back?
- What surprised you about how Python indentation affects behavior (e.g. return statements)?
-->

## What I'd Improve Next

<!-- TODO — write this yourself. Ideas to consider (only if they're genuinely true for you):
- Better date validation (currently accepts any string as a date)
- Editing an existing expense instead of only delete + re-add
- A proper CLI framework instead of raw input()
- Unit tests
-->

## Author

Simon — [GitHub](https://github.com/simonpet369-spec)
