import random

def play_game():
    words = ["apple", "banana", "orange", "grape", "pineapple"]
    secret_word = random.choice(words)
    guesses = []
    attempts = 6

    print("Welcome to the Guess the Word Game!")
    print("I have chosen a word. Can you guess what it is?")

    while attempts > 0:
        print("\nAttempts left:", attempts)
        hidden_word = ""
        for letter in secret_word:
            if letter in guesses:
                hidden_word += letter
            else:
                hidden_word += "_"
        
        print("Word:", hidden_word)
        
        if hidden_word == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break
        
        try:
            guess = input("Enter your guess (single letter or full word): ").lower()
        except ValueError:
            print("Invalid input. Please enter a valid letter or word.")
            continue
        
        if guess in guesses:
            print("You have already guessed that. Try again.")
        elif len(guess) == 1:
            guesses.append(guess)
            if guess not in secret_word:
                attempts -= 1
                print("Incorrect guess!")
        elif len(guess) > 1:
            if guess == secret_word:
                print("Congratulations! You guessed the word:", secret_word)
                break
            else:
                attempts -= 1
                print("Incorrect guess!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing!")

# Start the game
play_game()
