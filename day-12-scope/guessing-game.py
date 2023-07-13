import random

def choose_a_number():
    """Select a random number between 1 and 100"""
    number = random.randint(1, 100)
    return number

def selecting_difficulty():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return choice

def guessing_game():
    
    selected_number = choose_a_number()

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == "easy":
        number_of_guesses = 10
    else:
        number_of_guesses = 5


    while number_of_guesses > 0:
        print(f"You have {number_of_guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))

        if guess == selected_number:
            number_of_guesses = 0
            print(f"You got it! The answer was {selected_number}")
        if guess > selected_number:
            number_of_guesses -= 1
            print("Too high.")
            print("Guess again.")
        if guess < selected_number:
            number_of_guesses -= 1
            print("Too low.")
            print("Guess again.")

guessing_game()