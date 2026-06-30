score = 0

questions = [
    ["Capital of India?", "delhi"],
    ["2 + 2 ?", "4"],
    ["National Animal of India?", "tiger"]
]

for q in questions:
    answer = input(q[0] + " ")

    if answer.lower() == q[1]:
        score += 1

print("Your Score =", score, "out of", len(questions))

if score == len(questions):
    print("Excellent!")
elif score >= 2:
    print("Good!")
else:
    print("Need More Practice!")