import random

# Word list
words = ['python', 'flask', 'docker', 'server', 'linux', 'github', 'script', 'debug']

# Choose a random word
secret_word = random.choice(words)
guessed_word = ['_'] * len(secret_word)
guessed_letters = []
attempts_left = 6

print("🎮 Welcome to Guess the Word!")
print("🔤 Guess the letters of the secret word.")

# Game loop
while attempts_left > 0 and '_' in guessed_word:
    print("\nCurrent word:", ' '.join(guessed_word))
    print("Guessed letters:", ' '.join(guessed_letters))
    print(f"❤️ Attempts left: {attempts_left}")
    
    guess = input("Enter a letter: ").lower()
    
    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet letter.")
        continue
    
    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
        for i, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts_left -= 1

# Result
if '_' not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Game Over! The word was:", secret_word)
