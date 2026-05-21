# Recursive Factorial & Fibonacci Calculator

# Function to find factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function to generate Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Main menu-driven program
while True:
    print("\n===== MENU =====")
    print("1. Find Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Factorial option
    if choice == '1':
        num = int(input("Enter a number: "))

        if num < 0:
            print("Factorial does not exist for negative numbers.")
        else:
            result = factorial(num)
            print(f"Factorial of {num} = {result}")

    # Fibonacci option
    elif choice == '2':
        terms = int(input("Enter number of terms: "))

        if terms <= 0:
            print("Please enter a positive number.")
        else:
            print("Fibonacci Series:")
            for i in range(terms):
                print(fibonacci(i), end=" ")

    # Exit option
    elif choice == '3':
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please try again.")