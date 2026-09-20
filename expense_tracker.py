"""
Personal Expense Tracker
-------------------------
A simple console-based expense tracker built with pure Python
(no external data libraries except Matplotlib for the optional chart export).

Features:
    - Add expenses with input validation
    - View, delete, and filter expenses (by category or date range)
    - Persist data to a JSON file between runs
    - Summarize total spending, overall and by category
    - Export a bar chart of spending by category

Author: Simon
"""

import json
import matplotlib.pyplot as plt


class Expense:
    """Represents a single expense entry."""

    def __init__(self, amount: float, category: str, date: str, description: str) -> None:
        """
        Create a new Expense.

        Args:
            amount: The amount spent.
            category: The spending category (e.g. "Food", "Transport").
            date: The date of the expense, as a string in "YYYY-MM-DD" format.
            description: A short note describing the expense.
        """
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __str__(self) -> str:
        """Return a human-readable representation of the expense."""
        return f"{self.amount}, {self.category}, {self.date}, {self.description}"

    def to_dict(self) -> dict:
        """Convert this expense into a plain dictionary (for JSON storage)."""
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description,
        }


class ExpenseTracker:
    """Manages a collection of Expense objects, with persistence and reporting."""

    def __init__(self) -> None:
        """Create an empty expense tracker."""
        self.items: list[Expense] = []

    def add_expense(self, expense: Expense) -> None:
        """Add a new expense to the tracker."""
        self.items.append(expense)

    def delete_expense(self, index: int) -> None:
        """
        Remove the expense at the given index and print a confirmation.

        Args:
            index: The position of the expense to delete (0-based).
        """
        removed = self.items[index]
        del self.items[index]
        print(f"Deleted: {removed}")

    def filter_by_category(self, category: str) -> list[Expense]:
        """Return a new list of expenses matching the given category."""
        return [item for item in self.items if item.category == category]

    def filter_by_date_range(self, start_date: str, end_date: str) -> list[Expense]:
        """
        Return expenses with a date between start_date and end_date (inclusive).

        Note: works correctly for "YYYY-MM-DD" formatted date strings,
        since that format sorts the same alphabetically and chronologically.
        """
        return [item for item in self.items if start_date <= item.date <= end_date]

    def total_spent(self) -> float:
        """Return the sum of all expense amounts."""
        return sum(item.amount for item in self.items)

    def total_by_category(self) -> dict:
        """Return a dictionary mapping each category to its total amount spent."""
        totals: dict = {}
        for item in self.items:
            if item.category in totals:
                totals[item.category] += item.amount
            else:
                totals[item.category] = item.amount
        return totals

    def export_chart(self, filename: str) -> None:
        """Save a bar chart of spending by category to the given filename."""
        totals = self.total_by_category()
        categories = list(totals.keys())
        amounts = list(totals.values())

        plt.figure(figsize=(8, 5))
        plt.bar(categories, amounts, color="steelblue")
        plt.title("Spending by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Spent")
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
        print(f"Chart saved to {filename}")

    def save_to_file(self, filename: str) -> None:
        """Save all expenses to a JSON file."""
        data = [item.to_dict() for item in self.items]
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_from_file(self, filename: str) -> None:
        """Load expenses from a JSON file, appending them to this tracker."""
        with open(filename, "r") as f:
            data = json.load(f)

        for entry in data:
            self.items.append(
                Expense(entry["amount"], entry["category"], entry["date"], entry["description"])
            )


def get_expense_input() -> Expense:
    """
    Prompt the user for expense details and return a new Expense object.

    Keeps re-asking for the amount until a valid number is entered.
    """
    while True:
        try:
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print("Invalid value, please enter a number.")

    category = input("Enter the category: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    return Expense(amount, category, date, description)


def main() -> None:
    """Run the interactive expense tracker menu."""
    tracker = ExpenseTracker()
    save_file = "expense.json"

    try:
        tracker.load_from_file(save_file)
        print("Previous expenses loaded!")
    except FileNotFoundError:
        print("No saved file found - starting fresh.")

    while True:
        print("\n1. Add expense")
        print("2. View all expenses")
        print("3. Delete expense")
        print("4. Filter by category")
        print("5. Show summary")
        print("6. Export spending chart")
        print("7. Save and exit")

        choice = input("Choose an option: ")

        if choice == "1":
            tracker.add_expense(get_expense_input())
            print("Expense added!")

        elif choice == "2":
            for item in tracker.items:
                print(item)

        elif choice == "3":
            index = int(input("Enter the index of the expense to delete: "))
            tracker.delete_expense(index)

        elif choice == "4":
            category = input("Enter category to filter: ")
            for item in tracker.filter_by_category(category):
                print(item)

        elif choice == "5":
            print("Total spent:", tracker.total_spent())
            print("By category:", tracker.total_by_category())

        elif choice == "6":
            tracker.export_chart("spending_chart.png")

        elif choice == "7":
            tracker.save_to_file(save_file)
            print("Goodbye!")
            break

        else:
            print("Invalid option, please choose 1-7.")


if __name__ == "__main__":
    main()
