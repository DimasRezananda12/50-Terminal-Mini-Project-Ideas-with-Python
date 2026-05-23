import random

print("🙈 Welcome to Truth or Dare!")
print("A party game for 2 or more players.")
print("-" * 50)

# ── Question / Dare Banks ──
TRUTHS = [
    "What's the most embarrassing thing that's ever happened to you?",
    "Have you ever lied to get out of trouble? What was it?",
    "What's the weirdest dream you've ever had?",
    "Who is your secret crush right now?",
    "What's the most childish thing you still do?",
    "Have you ever cheated on a test?",
    "What's something you've done that you hope your parents never find out about?",
    "What's your biggest fear?",
    "Have you ever stood someone up?",
    "What's the biggest lie you've ever told?",
    "What's a bad habit you have that nobody knows about?",
    "Have you ever pretended to be sick to avoid something?",
    "Who in this room would you trade lives with for a day?",
    "What's the most embarrassing song on your playlist?",
    "Have you ever read someone else's messages without them knowing?",
    "What's the worst gift you've ever received?",
    "Have you ever ghosted someone?",
    "What's the pettiest reason you've ever been angry at someone?",
    "What's something you're secretly proud of but embarrassed to admit?",
    "If you could undo one thing you said today, what would it be?",
]

DARES = [
    "Do your best impression of the person to your left for 30 seconds.",
    "Text your crush 'Hey, I've been thinking about you' right now.",
    "Speak in an accent for the next 3 rounds.",
    "Let the group look through your camera roll for 30 seconds.",
    "Do 20 jumping jacks right now.",
    "Call a random contact and sing 'Happy Birthday' to them.",
    "Eat a spoonful of the spiciest sauce available.",
    "Post an embarrassing selfie on your Instagram story for 1 hour.",
    "Tell an embarrassing story about yourself in under a minute.",
    "Do your best robot dance for 1 full minute.",
    "Talk in slow motion for the next 2 rounds.",
    "Let someone in the group send one text from your phone.",
    "Imitate another player until someone guesses who you are.",
    "Do a dramatic reading of the last text you sent.",
    "Wear your clothes inside out for the rest of the game.",
    "Say 'banana' after every sentence for the next 2 rounds.",
    "Pretend to be a news reporter and narrate what's happening right now.",
    "Call a family member and tell them you love them. Right now.",
    "Swap shoes with the person next to you for 2 rounds.",
    "Walk like a penguin to the other side of the room and back.",
]

def get_players():
    """Set up player names."""
    print()
    while True:
        try:
            count = int(input("  How many players? (2-8): "))
            if 2 <= count <= 8:
                break
            print("  Warning: Please enter a number between 2 and 8.")
        except ValueError:
            print("  Warning: Please enter a valid number.")

    players = []
    for i in range(1, count + 1):
        name = input(f"  Enter Player {i}'s name: ").strip() or f"Player {i}"
        players.append(name)

    print(f"\n  Players: {', '.join(players)}")
    print("  Let the game begin! \n")
    return players

def choose_truth_or_dare(player_name):
    """Ask the current player for their choice."""
    print("-" * 50)
    print(f"  It's {player_name}'s turn!")
    print()

    while True:
        choice = input("  Truth or Dare? (T / D): ").strip().upper()
        if choice in ("T", "TRUTH"):
            return "truth"
        elif choice in ("D", "DARE"):
            return "dare"
        else:
            print("  Warning: Please type T for Truth or D for Dare.")

def play_round(player_name, used_truths, used_dares):
    """Play one round for the current player."""
    choice = choose_truth_or_dare(player_name)

    if choice == "truth":
        available = [t for t in TRUTHS if t not in used_truths]
        if not available:
            used_truths.clear()
            available = TRUTHS[:]
        question = random.choice(available)
        used_truths.add(question)
        print(f"\n  TRUTH for {player_name}:")
        print(f"  {question}")

    else:
        available = [d for d in DARES if d not in used_dares]
        if not available:
            used_dares.clear()
            available = DARES[:]
        dare = random.choice(available)
        used_dares.add(dare)
        print(f"\n  DARE for {player_name}:")
        print(f"  {dare}")

    print()
    completed = input(f"  Did {player_name} complete it? (yes / skip): ").strip().lower()
    if completed in ("yes", "y"):
        print(f"  {player_name} completed the challenge! Well done!")
    else:
        print(f"  {player_name} chickened out! Better luck next time!")

# ── Main Game Loop ──
players = get_players()
used_truths = set()
used_dares = set()
current_index = 0
round_num = 1

while True:
    player = players[current_index]
    print(f"\n  {'=' * 50}")
    print(f"  Round {round_num} - Player: {player}")
    print(f"  {'=' * 50}")

    play_round(player, used_truths, used_dares)

    current_index = (current_index + 1) % len(players)
    if current_index == 0:
        round_num += 1

    print()
    again = input("  Continue to next player? (yes / no): ").strip().lower()
    if again not in ("yes", "y"):
        break

print("\n  Thanks for playing Truth or Dare!")
print(f"  You played {round_num - 1} full round(s) with {len(players)} players.")
print("  See you next time!")
