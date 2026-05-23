import random

print("♣️  Welcome to Baby Blackjack!")
print("Get as close to 21 as possible without going over.")
print("Simplified rules: No splitting or doubling down.")
print("-" * 50)

# ── Card Setup ──
SUITS = ["♠️", "♥️", "♦️", "♣️"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}

def create_deck():
    deck = [(rank, suit) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def hand_value(hand):
    value = sum(VALUES[card[0]] for card in hand)
    aces = sum(1 for card in hand if card[0] == "A")
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_hand(name, hand, hide_second=False):
    if hide_second:
        cards = f"{hand[0][0]}{hand[0][1]}  [hidden]"
        print(f"  {name}: {cards}")
    else:
        cards = "  ".join(f"{r}{s}" for r, s in hand)
        print(f"  {name}: {cards}  (Total: {hand_value(hand)})")

def play_round(deck, balance):
    bet = 0
    while True:
        try:
            bet = int(input(f"\n  Your balance: ${balance}. Place your bet: $"))
            if 1 <= bet <= balance:
                break
            print("  Warning: Bet must be between $1 and your balance.")
        except ValueError:
            print("  Warning: Please enter a valid number.")

    # Deal initial cards
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("\n  --- Initial Deal ---")
    display_hand("Dealer", dealer_hand, hide_second=True)
    display_hand("You   ", player_hand)

    # Check for player blackjack
    if hand_value(player_hand) == 21:
        print("\n  BLACKJACK! You win instantly! 🃏🎉")
        return balance + int(bet * 1.5)

    # Player's turn
    while hand_value(player_hand) < 21:
        action = input("\n  Hit or Stand? (H / S): ").strip().upper()
        if action in ("H", "HIT"):
            player_hand.append(deck.pop())
            display_hand("You   ", player_hand)
            if hand_value(player_hand) > 21:
                print("  BUST! You went over 21. 💥")
                return balance - bet
        elif action in ("S", "STAND"):
            break
        else:
            print("  Warning: Please type H to Hit or S to Stand.")

    player_total = hand_value(player_hand)

    # Dealer's turn
    print("\n  --- Dealer's Turn ---")
    display_hand("Dealer", dealer_hand)
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        display_hand("Dealer", dealer_hand)

    dealer_total = hand_value(dealer_hand)

    # Result
    print("\n  --- Result ---")
    display_hand("You   ", player_hand)
    display_hand("Dealer", dealer_hand)

    if dealer_total > 21:
        print("  Dealer BUST! You WIN! 🎉")
        return balance + bet
    elif player_total > dealer_total:
        print("  You WIN! 🎉")
        return balance + bet
    elif player_total < dealer_total:
        print("  Dealer wins. 😞")
        return balance - bet
    else:
        print("  It's a PUSH (tie)! 🤝 Bet returned.")
        return balance

# ── Main Game ──
balance = 100
print(f"\n  Starting balance: ${balance}")

while balance > 0:
    deck = create_deck()
    balance = play_round(deck, balance)
    print(f"\n  Current balance: ${balance}")

    if balance <= 0:
        print("\n  You're out of money! Game over. 😢")
        break

    again = input("\n  Play another round? (yes / no): ").strip().lower()
    if again not in ("yes", "y"):
        break

print(f"\n  Thanks for playing Baby Blackjack! Final balance: ${balance} 👋")
