import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

FILENAME = "expenses.csv"

# --- Helper Functions ---
def add_expense():
    amount = float(input("Enter amount: £"))
    category = input("Enter category (e.g. food, transport, shopping): ").capitalize()
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("✅ Expense added successfully!\n")

def view_expenses():
    try:
        df = pd.read_csv(FILENAME, names=["Date", "Category", "Amount", "Description"])
        print(df)
    except FileNotFoundError:
        print("No expenses recorded yet.\n")

def analyze_expenses():
    try:
        df = pd.read_csv(FILENAME, names=["Date", "Category", "Amount", "Description"])
        summary = df.groupby("Category")["Amount"].sum()
        print("\n💰 Total Spent by Category:\n")
        print(summary)

        # Plotting
        summary.plot(kind="bar", title="Expenses by Category")
        plt.ylabel("Amount (£)")
        plt.show()
    except FileNotFoundError: 
        print("No expenses to analyze.\n")

# --- Main Menu ---
def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            analyze_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
