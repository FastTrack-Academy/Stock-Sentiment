import random

# Variables
target_number = random.randint(1, 20)
attempts = 5

# Function to check guess
def check_guess(guess, target_number):
    if guess < target_number:
        return "Too low! Try again."
    elif guess > target_number:
        return "Too high! Try again."
    else:
        return "Correct! You guessed it!"

# Loop for attempts
for attempt in range(attempts):
    user_input = input(f"Attempt {attempt + 1}/{attempts}: Enter your guess: ")
    if user_input.isdigit():
        guess = int(user_input)
        result = check_guess(guess, target_number)
        print(result)

        if attempt == attempts - 2:  # Second last attempt hint
            print("Hint: The number is even!" if target_number % 2 == 0 else "Hint: The number is odd!")

        if guess == target_number:
            break
    else:
        print("Invalid input. Please enter a valid number.")

if guess != target_number:
    print(f"Sorry, the correct number was {target_number}.")
