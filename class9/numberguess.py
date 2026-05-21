# Number Guessing Game

import random

scores = []

# Function to play the game
def play_game():

    number = random.randint(1, 100)
    attempts = 0

    print("\nGuess the number between 1 and 100")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > number:
            print("Too High!")

        elif guess < number:
            print("Too Low!")

        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            scores.append(attempts)
            break

# Function to display scores
def show_scores():

    if len(scores) == 0:
        print("No scores available.")
    else:
        print("\nScore History:")
        for i in range(len(scores)):
            print(f"Game {i+1}: {scores[i]} attempts")

        print(f"Best Score: {min(scores)} attempts")

# Main Program
while True:

    print("\n===== NUMBER GUESSING GAME =====")
    print("1. Play Game")
    print("2. Show Scores")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        play_game()

    elif choice == '2':
        show_scores()

    elif choice == '3':
        print("Thanks for Playing!")
        break

    else:
        print("Invalid Choice! Try Again.")