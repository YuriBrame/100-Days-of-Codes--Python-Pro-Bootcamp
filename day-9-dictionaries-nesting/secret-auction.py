# Code made to run in replit.com
# from replit import clear

from art import logo


print(logo)
print("Welcome to the Auction House!")

end_of_auction = False
participants = {}

while not end_of_auction:
    
    highest_bid = 0
    highest_bider = ""

    name = input("What's your name?")
    bid = input("What's you bid? $")
    participants[name] = int(bid)
    more_participants = input("Are there any other participants? Type 'yes' or 'no' ").lower()

    if more_participants == "no":
        end_of_auction = True

        for participant in participants:
            bid_ammount = participants[participant]
            if bid_ammount > highest_bid:
              highest_bid = bid_ammount
              highest_bider = participant
        print(f"The winner is {highest_bider} with a bid of ${highest_bid}")
    # elif more_participants == "yes":
    #     clear()