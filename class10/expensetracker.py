# =========================================
# EXPENSE TRACKER
# Concepts Used:
# List, Tuple, File Handling
# =========================================

import os

FILE_NAME = "expenses.txt"

# List to store expense records
expenses = []

# -----------------------------------
# Load Expenses From File
# -----------------------------------
def load_expenses():

    if os.path.exists(FILE_NAME):

        file = open(FILE_NAME, "r")

        for line in file:

            data = line.strip().split(",")

            if len(data) == 2:

                item = data[0]
                amount = float(data[1])

                # Tuple Example
                expense = (item, amount)

                expenses.append(expense)

        file.close()

# -----------------------------------
# Save Expenses To File
# -----------------------------------
def save_expenses():

    file = open(FILE_NAME, "w")

    for item, amount in expenses:

        file.write(f"{item},{amount}\n")

    file.close()

# -----------------------------------
# Add Expense
# -----------------------------------
def add_expense():

    item = input("Enter Expense Item: ")

    amount = float(input("Enter Amount: "))

    # Tuple stores single expense
    expense = (item, amount)

    expenses.append(expense)

    save_expenses()

    print("\nExpense Added Successfully!\n")

# -----------------------------------
# Display Expenses
# -----------------------------------
def display_expenses():

    if len(expenses) == 0:

        print("\nNo Expenses Found.\n")
        return

    print("\n========== EXPENSE HISTORY ==========")

    count = 1

    for item, amount in expenses:

        print(f"{count}. {item} - ₹{amount}")

        count += 1

    print()

# -----------------------------------
# Calculate Total Spending
# -----------------------------------
def total_spending():

    total = 0

    for item, amount in expenses:

        total += amount

    print(f"\nTotal Spending = ₹{total}\n")

# -----------------------------------
# Delete Expense
# -----------------------------------
def delete_expense():

    display_expenses()

    if len(expenses) == 0:
        return

    num = int(input("Enter Expense Number to Delete: "))

    if 1 <= num <= len(expenses):

        removed = expenses.pop(num - 1)

        save_expenses()

        print(f"\nDeleted Expense: {removed[0]} - ₹{removed[1]}\n")

    else:

        print("\nInvalid Expense Number.\n")

# -----------------------------------
# Main Menu
# -----------------------------------
def menu():

    load_expenses()

    while True:

        print("""
========== EXPENSE TRACKER ==========

1. Add Expense
2. Display Expenses
3. Calculate Total Spending
4. Delete Expense
5. Exit

=====================================
""")

        choice = input("Enter Your Choice: ")

        if choice == "1":

            add_expense()

        elif choice == "2":

            display_expenses()

        elif choice == "3":

            total_spending()

        elif choice == "4":

            delete_expense()

        elif choice == "5":

            print("\nThank You for Using Expense Tracker!")
            break

        else:

            print("\nInvalid Choice! Try Again.\n")

# -----------------------------------
# Program Start
# -----------------------------------
menu()