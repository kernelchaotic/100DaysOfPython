import os

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to the Secret Auction Program.")

bidding_pool = {}
bidding_finished = False

while not bidding_finished:

    def add_bidder(bidder_name, bidder_bid):
        bidding_pool[bidder_name] = bidder_bid

    name = input("What is your name?:  ")
    bidding = int(input("What is your bid?:  $"))
    add_bidder(name, bidding)
    more_bidders = input("Are there any other bidders? Type \'yes\' or \'no\'.\n").lower()
    if more_bidders == "no" or more_bidders == "n":
        bidding_finished = True
    os.system("clear")


def finding_highest_bid():
    highest_bid = 0
    winner = ""
    for bidder in bidding_pool:
        bid = bidding_pool[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
        else:
            continue
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


finding_highest_bid()
