from art import logo
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(player, number_of_cards):
    """Returns a number of cards from the deck and places them in the player hand."""
    for _ in range (number_of_cards):
        player.append(random.choice(cards))

def calculate_score(player):
    """Calculate the total score of the player, checks if he got a blackjack and switch the value of the ACE
    in case the score goes over 21."""
    if sum(player) == 21 and len(player) == 2:
        return 0 
    if 11 in player and sum(player) > 21:
        player.remove(11)
        player.append(1)
    return sum(player)

def compare_score(user_score, computer_score):
    if user_score == computer_score:
      return "Draw 🙃"
    elif computer_score == 0:
      return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
      return "Win with a Blackjack 😎"
    elif user_score > 21:
      return "You went over. You lose 😭"
    elif computer_score > 21:
      return "Opponent went over. You win 😁"
    elif user_score > computer_score:
      return "You win 😃"
    else:
      return "You lose 😤"
    
def blacjack():
   
   print(logo)

   player_hand = []
   dealer_hand = []
   end_of_game = False

   deal_cards(player_hand, 2)
   deal_cards(dealer_hand, 2)
   

   while not end_of_game:
      player_score = calculate_score(player_hand)
      dealer_score = calculate_score(dealer_hand)
      print(f"    Your cards: {player_hand}, total score {calculate_score(player_hand)}")
      print(f"    Computer's first card: {dealer_hand[0]}")

      if player_score == 0 or dealer_score == 0 or player_score > 21:
          end_of_game = True
          print(f"    Your final hand: {player_hand}, final score: {player_score}")
          print(f"    Computer's final hand: {dealer_hand}, computer's final score: {dealer_score}")
          print(compare_score(player_score, dealer_score))
      else:
         if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
            deal_cards(player_hand, 1)
         else:
            end_of_game = True
            print(f"    Your final hand: {player_hand}, final score: {player_score}")
            print(f"    Computer's final hand: {dealer_hand}, computer's final score: {dealer_score}")
            print(compare_score(player_score, dealer_score))

blacjack()
         

# initial_input = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()

# end_of_game = True
# if initial_input == "y":
#     end_of_game = False
#     print(logo)

# while not end_of_game:
    
#     player_hand = []
#     player_score = 0
#     dealer_hand = []
#     dealer_score = 0
#     player_final_choice = False

#     deal_cards(player_hand, 2)
#     player_score = calculate_score(player_hand)
#     deal_cards(dealer_hand, 2)
#     dealer_score = calculate_score(dealer_hand)

#     print(f"    Your cards: {player_hand}, total score {calculate_score(player_hand)}")
#     print(f"    Computer's first card: {dealer_hand[0]}")

#     while not player_final_choice:
#       if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
#           (deal_cards(player_hand, 1))
#           player_score = calculate_score(player_hand)
#           print(f"    Your cards: {player_hand}, total score {calculate_score(player_hand)}")
#           print(f"    Computer's first card: {dealer_hand[0]}")
#           if player_score > 21:
#               player_final_choice = True
#       else:
#           player_final_choice = True
    
#     while dealer_score <= 16:
#         deal_cards(dealer_hand, 1)
#         dealer_score = calculate_score(dealer_hand)

#     print(f"    Your final hand: {player_hand}, final score: {player_score}")
#     print(f"    Computer's final hand: {dealer_hand}, computer's final score: {dealer_score}")

#     if player_score > 21:
#         print("You went over. You Lose")
#     elif dealer_score > 21:
#         print("Computer went over. You Win")
#     elif player_score == dealer_score:
#         print("It's a Draw")
#     elif player_score > dealer_score:
#         print("You Win")
#     elif player_score < dealer_score:
#         print("You Lose")
    
#     if input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == "n":
#         end_of_game = True

