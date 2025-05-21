from art import logo

print(logo)


def find_highest_bidder(bids_dict):
    # Find the highest bidder
    max_bid = 0
    winner = ""

    for bidder in bids_dict:
        bid_amount = bids_dict[bidder]

        if int(bid_amount) > max_bid:
            max_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${max_bid}")


# Populate the dictionary with the bids.
bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    new_bidder = input("Are there any other bidders? Type 'Y' or 'N': ").upper()

    if new_bidder == "N":
        continue_bidding = False
        find_highest_bidder(bids)
    else:
        print("\n" * 20)
