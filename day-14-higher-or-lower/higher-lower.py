import random
from art import logo
from art import vs
from game_data import data

def select_option(list):
    new_option = {}
    new_option.update(random.choice(list))
    return new_option

def compare(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "a"
    else:
        return "b"

def higher_lower_game():
    option_a = select_option(data)
    option_b = select_option(data)
    player_score = 0
    end_of_game = False

    print(logo)
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

    while end_of_game == False:
        if input("Who has more followers? Type 'A' or 'B': ").lower() == compare(option_a, option_b):
            player_score += 1
        else:
            end_of_game = True
            print(f"Sorry, that's wrong. Final score: {player_score}")
            break
        option_a.update(option_b)
        while option_a == option_b:
          option_b = select_option(data)
          

        print(logo)
        print(f"You're right! Current score: {player_score}")
        print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
        print(vs)
        print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

higher_lower_game()