balance = 5000

print("Current Balance =", balance)

withdraw = int(input("Enter amount to withdraw: "))

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)
else:
    print("Insufficient Balance")