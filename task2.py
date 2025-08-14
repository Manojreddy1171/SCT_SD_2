import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

attempts = 0  # Track number of guesses

while True:
    try:
        # Get user guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Compare guess with the secret number
        if guess < secret_number:
            print("Too low! 📉 Try again.")
        elif guess > secret_number:
            print("Too high! 📈 Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
            break
    except ValueError:
        print("⚠️ Please enter a valid number.")
