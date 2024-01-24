bid = {}
newbidder = True

def add_bid():
  name = input("Please enter your name:\n")
  amount =int(input("Please enter your bid:\n"))
  bid[name] = amount

def find_winner(bid):
  print(f"{max(bid, key=bid.get)} has won the auction with a bid of {max(bid.values())}$")

while newbidder:
  add_bid()
  test = input("Are there any other bidders? (y/n)\n")
  if test == "n":
    newbidder = False
  #clear()
find_winner(bid)