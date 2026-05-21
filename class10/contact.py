# =========================================
# CONTACT BOOK APPLICATION
# Concepts Used:
# Dictionary, File Handling
# =========================================

import os

FILE_NAME = "contacts.txt"

contacts = {}

# -----------------------------------
# Load Contacts From File
# -----------------------------------
def load_contacts():

    if os.path.exists(FILE_NAME):

        file = open(FILE_NAME, "r")

        for line in file:

            data = line.strip().split(",")

            if len(data) == 2:

                name = data[0]
                phone = data[1]

                contacts[name] = phone

        file.close()

# -----------------------------------
# Save Contacts To File
# -----------------------------------
def save_contacts():

    file = open(FILE_NAME, "w")

    for name, phone in contacts.items():

        file.write(f"{name},{phone}\n")

    file.close()

# -----------------------------------
# Add Contact
# -----------------------------------
def add_contact():

    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    contacts[name] = phone

    save_contacts()

    print("\nContact Saved Successfully!\n")

# -----------------------------------
# Display Contacts
# -----------------------------------
def display_contacts():

    if len(contacts) == 0:

        print("\nNo Contacts Found.\n")
        return

    print("\n========== CONTACT LIST ==========")

    for name, phone in contacts.items():

        print(f"""
Name  : {name}
Phone : {phone}
-------------------------
""")

# -----------------------------------
# Search Contact
# -----------------------------------
def search_contact():

    name = input("Enter Name to Search: ")

    if name in contacts:

        print(f"""
Contact Found!

Name  : {name}
Phone : {contacts[name]}
""")

    else:
        print("\nContact Not Found.\n")

# -----------------------------------
# Update Contact
# -----------------------------------
def update_contact():

    name = input("Enter Name to Update: ")

    if name in contacts:

        new_phone = input("Enter New Phone Number: ")

        contacts[name] = new_phone

        save_contacts()

        print("\nContact Updated Successfully!\n")

    else:
        print("\nContact Not Found.\n")

# -----------------------------------
# Delete Contact
# -----------------------------------
def delete_contact():

    name = input("Enter Name to Delete: ")

    if name in contacts:

        del contacts[name]

        save_contacts()

        print("\nContact Deleted Successfully!\n")

    else:
        print("\nContact Not Found.\n")

# -----------------------------------
# Main Menu
# -----------------------------------
def menu():

    load_contacts()

    while True:

        print("""
========== CONTACT BOOK APPLICATION ==========

1. Add Contact
2. Display Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

==============================================
""")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            display_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("\nThank You for Using Contact Book!")
            break

        else:
            print("\nInvalid Choice! Try Again.\n")

# -----------------------------------
# Program Start
# -----------------------------------
menu()