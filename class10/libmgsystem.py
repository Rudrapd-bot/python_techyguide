# =========================================
# LIBRARY MANAGEMENT SYSTEM
# Concepts Used:
# List, Tuple, Dictionary, File Handling
# =========================================

import os

FILE_NAME = "library_records.txt"

# -------------------------------
# Load books from file
# -------------------------------
books = {}

def load_books():
    global books

    if os.path.exists(FILE_NAME):
        file = open(FILE_NAME, "r")

        for line in file:
            data = line.strip().split(",")

            if len(data) == 4:
                book_id = data[0]
                title = data[1]
                author = data[2]
                status = data[3]

                books[book_id] = {
                    "title": title,
                    "author": author,
                    "status": status
                }

        file.close()

# -------------------------------
# Save books to file
# -------------------------------
def save_books():
    file = open(FILE_NAME, "w")

    for book_id, details in books.items():
        line = f"{book_id},{details['title']},{details['author']},{details['status']}\n"
        file.write(line)

    file.close()

# -------------------------------
# Add Book
# -------------------------------
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    # Tuple Example
    book_data = (title, author)

    books[book_id] = {
        "title": book_data[0],
        "author": book_data[1],
        "status": "Available"
    }

    save_books()

    print("\nBook Added Successfully!\n")

# -------------------------------
# Display Books
# -------------------------------
def display_books():

    if len(books) == 0:
        print("\nNo books available.\n")
        return

    print("\n========== BOOK LIST ==========")

    for book_id, details in books.items():

        print(f"""
Book ID : {book_id}
Title   : {details['title']}
Author  : {details['author']}
Status  : {details['status']}
--------------------------------
""")

# -------------------------------
# Issue Book
# -------------------------------
def issue_book():

    book_id = input("Enter Book ID to Issue: ")

    if book_id in books:

        if books[book_id]["status"] == "Available":

            books[book_id]["status"] = "Issued"

            save_books()

            print("\nBook Issued Successfully!\n")

        else:
            print("\nBook Already Issued.\n")

    else:
        print("\nBook ID Not Found.\n")

# -------------------------------
# Return Book
# -------------------------------
def return_book():

    book_id = input("Enter Book ID to Return: ")

    if book_id in books:

        if books[book_id]["status"] == "Issued":

            books[book_id]["status"] = "Available"

            save_books()

            print("\nBook Returned Successfully!\n")

        else:
            print("\nThis Book Was Not Issued.\n")

    else:
        print("\nBook ID Not Found.\n")

# -------------------------------
# Search Book
# -------------------------------
def search_book():

    name = input("Enter Book Title to Search: ").lower()

    found = False

    for book_id, details in books.items():

        if details["title"].lower() == name:

            found = True

            print(f"""
Book Found!
Book ID : {book_id}
Title   : {details['title']}
Author  : {details['author']}
Status  : {details['status']}
""")

    if not found:
        print("\nBook Not Found.\n")

# -------------------------------
# Main Menu
# -------------------------------
def menu():

    load_books()

    while True:

        print("""
========== LIBRARY MANAGEMENT SYSTEM ==========

1. Add Book
2. Display Books
3. Issue Book
4. Return Book
5. Search Book
6. Exit

==============================================
""")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            display_books()

        elif choice == "3":
            issue_book()

        elif choice == "4":
            return_book()

        elif choice == "5":
            search_book()

        elif choice == "6":
            print("\nThank You for Using Library System!")
            break

        else:
            print("\nInvalid Choice! Try Again.\n")

# -------------------------------
# Program Start
# -------------------------------
menu()