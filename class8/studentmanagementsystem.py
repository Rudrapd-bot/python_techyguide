students = []

while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Display All")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student Added!")

    elif choice == "2":
        search = input("Enter name to search: ")

        if search in students:
            print("Student Found")
        else:
            print("Student Not Found")

    elif choice == "3":
        print("Student List:")
        for student in students:
            print(student)

    elif choice == "4":
        break

    else:
        print("Invalid Choice")