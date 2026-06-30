units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5
else:
    bill = (100 * 5) + ((units - 100) * 8)

print("Electricity Bill = ₹", bill)