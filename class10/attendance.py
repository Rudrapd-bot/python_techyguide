# =========================================
# ATTENDANCE MANAGEMENT SYSTEM
# Concepts Used:
# Set, File Handling
# =========================================

import os

FILE_NAME = "attendance.txt"

# Set stores unique student names
attendance_set = set()

# -----------------------------------
# Load Attendance From File
# -----------------------------------
def load_attendance():

    global attendance_set

    if os.path.exists(FILE_NAME):

        file = open(FILE_NAME, "r")

        for line in file:

            student = line.strip()

            attendance_set.add(student)

        file.close()

# -----------------------------------
# Save Attendance To File
# -----------------------------------
def save_attendance():

    file = open(FILE_NAME, "w")

    for student in attendance_set:

        file.write(student + "\n")

    file.close()

# -----------------------------------
# Mark Attendance
# -----------------------------------
def mark_attendance():

    student = input("Enter Student Name: ")

    # Set automatically removes duplicates
    if student in attendance_set:

        print("\nAttendance Already Marked!\n")

    else:

        attendance_set.add(student)

        save_attendance()

        print("\nAttendance Marked Successfully!\n")

# -----------------------------------
# Display Attendance
# -----------------------------------
def display_attendance():

    if len(attendance_set) == 0:

        print("\nNo Attendance Records Found.\n")
        return

    print("\n========== ATTENDANCE LIST ==========")

    count = 1

    for student in attendance_set:

        print(f"{count}. {student}")

        count += 1

    print()

# -----------------------------------
# Remove Student Attendance
# -----------------------------------
def remove_attendance():

    student = input("Enter Student Name to Remove: ")

    if student in attendance_set:

        attendance_set.remove(student)

        save_attendance()

        print("\nAttendance Removed Successfully!\n")

    else:

        print("\nStudent Record Not Found.\n")

# -----------------------------------
# Clear Attendance
# -----------------------------------
def clear_attendance():

    attendance_set.clear()

    save_attendance()

    print("\nAll Attendance Records Cleared!\n")

# -----------------------------------
# Main Menu
# -----------------------------------
def menu():

    load_attendance()

    while True:

        print("""
========== ATTENDANCE MANAGEMENT SYSTEM ==========

1. Mark Attendance
2. Display Attendance
3. Remove Attendance
4. Clear Attendance
5. Exit

=================================================
""")

        choice = input("Enter Your Choice: ")

        if choice == "1":

            mark_attendance()

        elif choice == "2":

            display_attendance()

        elif choice == "3":

            remove_attendance()

        elif choice == "4":

            clear_attendance()

        elif choice == "5":

            print("\nThank You for Using Attendance System!")
            break

        else:

            print("\nInvalid Choice! Try Again.\n")

# -----------------------------------
# Program Start
# -----------------------------------
menu()