text = input("Enter a sentence: ")

vowels = 0
consonants = 0
spaces = 0

for ch in text.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch == " ":
        spaces += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Spaces =", spaces)
print("Reverse =", text[::-1])