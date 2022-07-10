from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
bids = {}
is_done = False
print(logo)

def auction_winner(bidder_record):
    highest_bid = 0
    winner = ""
    for bidder in bidder_record:
        bidder_amount = bidder_record[bidder]
        if bidder_amount > highest_bid:
            highest_bid = bidder_amount
            winner = bidder 
    print(f"The winner is {winner} with the bid of ${highest_bid}")

while not is_done:
    print("Welcome to the secret auction program.")
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    bids[name] = price
    if other_bidders == "yes":
        clear()
    elif other_bidders == "no":
        is_done = True
        auction_winner(bids)