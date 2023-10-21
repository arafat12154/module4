import random
random_number = random.randint(1, 10)
num_guesses = 0
print("Welcome to the Number Guessing Game!")
while True:
    try:
        user_guess = int(input("Guess the number between 1 and 10: "))
        num_guesses += 1
        if user_guess == random_number:
            print(f"Correct! You guessed the number {random_number} in {num_guesses} guesses.")
            break
        elif user_guess < random_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 10.")
