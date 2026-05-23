import random

print("♣️  Welcome to Blackjack!")
print("Standard casino rules: Hit, Stand, Double Down, or Split.")
print("-" * 55)

SUITS = ["♠️", "♥️", "♦️", "♣️"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}

def create_deck(num_decks=2):
    deck = [(rank, suit) for _ in range(num_decks) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def hand_value(hand):
    value = sum(VALUES[card[0]] for card in hand)
    aces = sum(1 for card in hand if card[0] == "A")
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def format_hand(hand):
    return "  ".join(f"{r}{s}" for r, s in hand)

def display_table(dealer_hand, player_hands, active_idx=0, hide_dealer=True):
    print("\n" + "─" * 55)
    if hide_dealer:
        print(f"  Dealer: {dealer_hand[0][0]}{dealer_hand[0][1]}  [hidden]")
    else:
        print(f"  Dealer: {format_hand(dealer_hand)}  (Total: {hand_value(dealer_hand)})")
    for i, hand in enumerate(player_hands):
        marker = " ◄" if i == active_idx and hide_dealer else ""
        label = f"Hand {i+1}" if len(player_hands) > 1 else "You"
        print(f"  {label}: {format_hand(hand)}  (Total: {hand_value(hand)}){marker}")
    print("─" * 55)

def get_bet(balance):
    while True:
        try:
            bet = int(input(f"\n  Balance: ${balance} | Place your bet: $"))
            if 1 <= bet <= balance:
                return bet
            print("  Warning: Bet must be between $1 and your balance.")
        except ValueError:
            print("  Warning: Please enter a number.")

def player_turn(deck, hand, bet, balance, hand_label=""):
    label = f" ({hand_label})" if hand_label else ""
    can_double = len(hand) == 2 and balance >= bet
    can_split = len(hand) == 2 and VALUES[hand[0][0]] == VALUES[hand[1][0]] and balance >= bet

    while hand_value(hand) < 21:
        actions = ["H=Hit", "S=Stand"]
        if can_double:
            actions.append("D=Double Down")
        if can_split:
            actions.append("SP=Split")

        display_table.__doc__  # just a placeholder
        print(f"\n  Your hand{label}: {format_hand(hand)}  (Total: {hand_value(hand)})")
        print(f"  Actions: {' | '.join(actions)}")
        action = input("  Choose: ").strip().upper()

        if action in ("H", "HIT"):
            hand.append(deck.pop())
            if hand_value(hand) > 21:
                print(f"  BUST! Hand total: {hand_value(hand)} 💥")
                return [hand], [bet], balance
            can_double = False
            can_split = False

        elif action in ("S", "STAND"):
            break

        elif action in ("D", "DOUBLE") and can_double:
            balance -= bet
            bet *= 2
            hand.append(deck.pop())
            print(f"  Double Down! Drew: {hand[-1][0]}{hand[-1][1]} | New total: {hand_value(hand)}")
            break

        elif action in ("SP", "SPLIT") and can_split:
            hand2 = [hand.pop()]
            hand.append(deck.pop())
            hand2.append(deck.pop())
            balance -= bet
            print(f"\n  Split! Playing two hands for ${bet} each.")
            hands1, bets1, balance = player_turn(deck, hand, bet, balance, "Hand 1")
            hands2, bets2, balance = player_turn(deck, hand2, bet, balance, "Hand 2")
            return hands1 + hands2, bets1 + bets2, balance

        else:
            print("  Warning: Invalid action.")

    return [hand], [bet], balance

def dealer_turn(deck, dealer_hand):
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    return dealer_hand

def evaluate(player_hand, dealer_hand, bet, initial_two_cards):
    p = hand_value(player_hand)
    d = hand_value(dealer_hand)

    if p > 21:
        return -bet, "BUST"
    if d > 21:
        return bet, "Dealer BUST — You WIN! 🎉"
    if p == 21 and len(player_hand) == 2 and initial_two_cards:
        return int(bet * 1.5), "BLACKJACK! 🃏🎉"
    if p > d:
        return bet, "You WIN! 🎉"
    if p < d:
        return -bet, "Dealer wins. 😞"
    return 0, "PUSH (tie) — Bet returned. 🤝"

# ── Main Game ──
balance = 200
deck = create_deck()

print(f"\n  Starting balance: ${balance}")
print("  (Deck refreshes automatically when low)")

while balance > 0:
    if len(deck) < 20:
        deck = create_deck()
        print("\n  🔀 Deck reshuffled.")

    bet = get_bet(balance)
    balance -= bet

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    display_table(dealer_hand, [player_hand], hide_dealer=True)

    # Check for immediate blackjack
    initial_two = True
    if hand_value(player_hand) == 21:
        print("\n  BLACKJACK! ♣️🎉")
        dealer_hand = dealer_turn(deck, dealer_hand)
        winnings, msg = evaluate(player_hand, dealer_hand, bet, initial_two)
        balance += bet + winnings
        print(f"  {msg}")
        print(f"  Balance: ${balance}")
    else:
        player_hands, bets, balance = player_turn(deck, player_hand, bet, balance, "")

        # Dealer plays only if at least one player hand isn't bust
        any_alive = any(hand_value(h) <= 21 for h in player_hands)
        if any_alive:
            print("\n  --- Dealer's Turn ---")
            dealer_hand = dealer_turn(deck, dealer_hand)
            print(f"  Dealer: {format_hand(dealer_hand)}  (Total: {hand_value(dealer_hand)})")

        total_change = 0
        for i, (ph, pb) in enumerate(zip(player_hands, bets)):
            label = f"Hand {i+1}" if len(player_hands) > 1 else "Your hand"
            winnings, msg = evaluate(ph, dealer_hand, pb, initial_two and len(player_hands) == 1)
            balance += pb + winnings
            total_change += winnings
            print(f"\n  {label}: {format_hand(ph)} (Total: {hand_value(ph)})")
            print(f"  {msg} (${'+' if winnings >= 0 else ''}{winnings})")

        print(f"\n  Balance: ${balance}")

    if balance <= 0:
        print("\n  You're out of chips! Game over. 😢")
        break

    again = input("\n  Play another round? (yes / no): ").strip().lower()
    if again not in ("yes", "y"):
        break

print(f"\n  Thanks for playing Blackjack! Final balance: ${balance} 👋")
