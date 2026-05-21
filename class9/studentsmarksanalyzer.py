# Student Marks Analyzer

marks = []

# Function to enter marks
def enter_marks():

    n = int(input("How many subjects? "))

    for i in range(n):
        mark = int(input(f"Enter marks for Subject {i+1}: "))
        marks.append(mark)

# Function to calculate total and average
def calculate_result():

    if len(marks) == 0:
        print("No marks entered.")
    else:
        total = sum(marks)
        average = total / len(marks)

        print(f"\nTotal Marks = {total}")
        print(f"Average Marks = {average:.2f}")

# Function to find highest and lowest marks
def highest_lowest():

    if len(marks) == 0:
        print("No marks entered.")
    else:
        print(f"Highest Marks = {max(marks)}")
        print(f"Lowest Marks = {min(marks)}")

# Main Program
while True:

    print("\n===== STUDENT MARKS ANALYZER =====")
    print("1. Enter Marks")
    print("2. Calculate Total & Average")
    print("3. Find Highest & Lowest")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        enter_marks()

    elif choice == '2':
        calculate_result()

    elif choice == '3':
        highest_lowest()

    elif choice == '4':
        print("Program Ended.")
        break

    else:
        print("Invalid Choice! Try Again.")