import random


def play_hangman():
    words = ["python", "coding", "intern", "program", "hangman"]
    word = random.choice(words).lower()
    guessed = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect:
        display = " ".join(letter if letter in guessed else "_" for letter in word)
        print(f"\nWord: {display}")
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")

        if "_" not in display:
            print(f"Congratulations! You guessed the word: {word}")
            return

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess.")

    print(f"\nGame over! The word was: {word}")


if __name__ == "__main__":
    play_hangman()
