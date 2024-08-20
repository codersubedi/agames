import random

def gameManager():
    # Initialize players and deck
    players = [Player("You"), Player("Bot")]
    deck = create_deck()

    # Game loop
    while True:
        # Deal cards
        for player in players:
            player.hand = deal_cards(deck, 3)

        # Blind option
        if players[0].is_human:
            blind = input("Do you want to play blind? (y/n): ").lower()
            if blind == "y":
                players[0].is_blind = True

        # Bid
        current_bid = 0
        current_bidder = 1  # Bot starts
        while True:
            player = players[current_bidder]
            if player.is_human:
                bid = int(input("Your turn to bid: "))
            else:
                bid = random.randint(current_bid + 1, min(current_bid * 2, 500))  # Adjust bot bidding logic
            if bid > current_bid:
                current_bid = bid
                current_bidder = (current_bidder + 1) % 2
            else:
                break

        # Showdown
        for player in players:
            if not player.is_blind:
                print(player.name, player.hand)
        # Determine winner based on hand rankings

        # End game or continue?

def create_deck():
    # Create a standard deck of 52 cards
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank} of {suit}")
    return deck

def deal_cards(deck, num_cards):
    hand = []
    for _ in range(num_cards):
        card = random.choice(deck)
        deck.remove(card)
        hand.append(card)
    return hand

class Player:
    def __init__(self, name, is_human=False):
        self.name = name
        self.hand = []
        self.is_human = is_human
        self.is_blind = False

# Example usage
gameManager()