import random

# List of words
words = [
    "python",
    "computer",
    "programming",
    "developer",
    "machine"
]

# Select random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect attempts
max_attempts = 6
incorrect_attempts = 0

print("=" * 40)
print("       WELCOME TO HANGMAN")
print("=" * 40)

# Create hidden word
display_word = ["_"] * len(word)

while incorrect_attempts < max_attempts and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", guessed_letters)
    print("Remaining attempts:", max_attempts - incorrect_attempts)

    guess = input("Enter one letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check letter
    if guess in word:

        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:

        incorrect_attempts += 1
        print("Wrong guess!")

# Game result
if "_" not in display_word:

    print("\n" + "=" * 40)
    print("🎉 YOU WON!")
    print("The word was:", word)
    print("=" * 40)

else:

    print("\n" + "=" * 40)
    print("💀 GAME OVER!")
    print("The word was:", word)
    print("=" * 40)