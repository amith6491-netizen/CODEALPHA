import random

# Predefined list of words
words = ["python", "computer", "program", "hangman", "developer"]

# Randomly choose a word
chosen_word = random.choice(words)

# Create a list of underscores
display = ["_"] * len(chosen_word)

incorrect_guesses = 0
max_attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")
print("You have 6 incorrect guesses allowed.\n")

# Game loop
while incorrect_guesses < max_attempts and "_" in display:
    print("Word:", " ".join(display))
    guess = input("Guess a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in chosen_word:
        print("Correct guess! ✅\n")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        incorrect_guesses += 1
        print("Wrong guess! ❌")
        print("Attempts left:", max_attempts - incorrect_guesses, "\n")

# Result
if "_" not in display:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("💀 Game Over! The word was:", chosen_word)
