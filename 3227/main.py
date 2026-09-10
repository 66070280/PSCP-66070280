"""P8"""
def main():
    """P8"""
    card = input().upper()
    value = card[:-1]
    suit = card[-1]

    if value == "A":
        value = "ace"
    elif value == "J":
        value = "jack"
    elif value == "Q":
        value = "queen"
    elif value == "K":
        value = "king"

    if suit == "D":
        suit = "diamonds"
    elif suit == "H":
        suit = "hearts"
    elif suit == "S":
        suit = "spades"
    elif suit == "C":
        suit = "clubs"
    print(value + " of " + suit)
main()
