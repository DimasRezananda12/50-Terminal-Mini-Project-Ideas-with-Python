import time

print("🤑 Welcome to Who Wants to Be a Millionaire!")
print("Answer all 10 questions correctly to win $1,000,000!")
print("-" * 60)

# Prize ladder
PRIZE_LADDER = [
    "$100",
    "$200",
    "$300",
    "$500",
    "$1,000",
    "$2,000",
    "$4,000",
    "$8,000",
    "$16,000",
    "$32,000",
    "$64,000",
    "$125,000",
    "$250,000",
    "$500,000",
    "$1,000,000"
]

# Questions: (question, options, correct_answer_key)
QUESTIONS = [
    {
        "question": "What is the capital city of Indonesia?",
        "options": {"A": "Bandung", "B": "Surabaya", "C": "Jakarta", "D": "Medan"},
        "answer": "C"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": {"A": "5", "B": "6", "C": "7", "D": "8"},
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": {"A": "CO2", "B": "O2", "C": "H2O", "D": "NaCl"},
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": {"A": "Venus", "B": "Jupiter", "C": "Saturn", "D": "Mars"},
        "answer": "D"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": {"A": "Charles Dickens", "B": "William Shakespeare", "C": "Jane Austen", "D": "Mark Twain"},
        "answer": "B"
    },
    {
        "question": "What is 15 x 15?",
        "options": {"A": "200", "B": "215", "C": "225", "D": "250"},
        "answer": "C"
    },
    {
        "question": "Which country invented pizza?",
        "options": {"A": "France", "B": "Greece", "C": "Spain", "D": "Italy"},
        "answer": "D"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": {"A": "Atlantic Ocean", "B": "Pacific Ocean", "C": "Indian Ocean", "D": "Arctic Ocean"},
        "answer": "B"
    },
    {
        "question": "Which element has the atomic number 1?",
        "options": {"A": "Helium", "B": "Oxygen", "C": "Hydrogen", "D": "Carbon"},
        "answer": "C"
    },
    {
        "question": "In what year did World War II end?",
        "options": {"A": "1943", "B": "1944", "C": "1945", "D": "1946"},
        "answer": "C"
    },
    {
        "question": "What is the longest river in the world?",
        "options": {"A": "Amazon", "B": "Nile", "C": "Yangtze", "D": "Mississippi"},
        "answer": "B"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": {"A": "Oxygen", "B": "Nitrogen", "C": "Carbon Dioxide", "D": "Hydrogen"},
        "answer": "C"
    },
    {
        "question": "How many bones are in the adult human body?",
        "options": {"A": "196", "B": "206", "C": "216", "D": "226"},
        "answer": "B"
    },
    {
        "question": "What is the speed of light (approximately)?",
        "options": {"A": "300,000 km/s", "B": "150,000 km/s", "C": "450,000 km/s", "D": "200,000 km/s"},
        "answer": "A"
    },
    {
        "question": "What is the most spoken language in the world?",
        "options": {"A": "English", "B": "Spanish", "C": "Hindi", "D": "Mandarin Chinese"},
        "answer": "D"
    },
]

# Safe havens (if player quits after reaching these, they keep the prize)
SAFE_HAVENS = [4, 9, 14]  # index (0-based), corresponds to $1,000 / $32,000 / $1,000,000

lifelines = {
    "50:50": True,
    "Phone a Friend": True,
    "Ask the Audience": True,
}

def show_lifelines():
    available = [name for name, available in lifelines.items() if available]
    if available:
        print(f"  💡 Available lifelines: {' | '.join(available)}")
    else:
        print("  💡 No lifelines remaining.")

def use_5050(options, correct_answer):
    """Removes two wrong answers."""
    wrong_keys = [k for k in options if k != correct_answer]
    import random
    removed = random.sample(wrong_keys, 2)
    reduced = {k: v for k, v in options.items() if k not in removed}
    print("  🔀 50:50 used! Two wrong answers have been removed.")
    return reduced

def use_phone_a_friend(correct_answer):
    """Friend gives a hint (usually correct, sometimes uncertain)."""
    import random
    if random.random() < 0.8:
        print(f"  📞 Your friend says: \"I'm pretty sure it's {correct_answer}!\"")
    else:
        keys = ["A", "B", "C", "D"]
        guess = random.choice(keys)
        print(f"  📞 Your friend is unsure and guesses: \"{guess}\"")

def use_ask_audience(options, correct_answer):
    """Audience mostly votes for the correct answer."""
    import random
    votes = {}
    remaining_percent = 100
    keys = list(options.keys())
    random.shuffle(keys)
    correct_percent = random.randint(50, 75)
    votes[correct_answer] = correct_percent
    remaining_percent -= correct_percent
    others = [k for k in keys if k != correct_answer]
    for i, key in enumerate(others):
        if i == len(others) - 1:
            votes[key] = remaining_percent
        else:
            share = random.randint(0, remaining_percent)
            votes[key] = share
            remaining_percent -= share
    print("  📊 Audience vote results:")
    for key in sorted(votes.keys()):
        bar = "█" * (votes[key] // 5)
        print(f"     {key}: {bar} {votes[key]}%")

current_prize = "$0"
winnings = "$0"

for i, q in enumerate(QUESTIONS):
    print(f"\n{'=' * 60}")
    print(f"  ❓ Question {i + 1} of {len(QUESTIONS)}")
    print(f"  💰 Playing for: {PRIZE_LADDER[i]}")
    if i > 0:
        # Determine guaranteed safe haven prize
        safe = "$0"
        for sh in SAFE_HAVENS:
            if i > sh:
                safe = PRIZE_LADDER[sh]
        print(f"  🛡️  Guaranteed: {safe}")
    print(f"{'=' * 60}")
    print(f"\n  {q['question']}\n")

    options = dict(q["options"])  # make a copy (for 50:50)

    for key, val in options.items():
        print(f"    {key}: {val}")

    show_lifelines()
    print()

    while True:
        user_input = input("  Your answer (A/B/C/D) or lifeline (50, Phone, Audience) or 'quit': ").strip().upper()

        if user_input == "QUIT":
            # Determine how much they walk away with
            walk_away = "$0"
            for sh in SAFE_HAVENS:
                if i > sh:
                    walk_away = PRIZE_LADDER[sh]
            print(f"\n  👋 You chose to walk away!")
            print(f"  💸 You walk away with: {walk_away}")
            exit()

        elif user_input == "50" and lifelines["50:50"]:
            lifelines["50:50"] = False
            options = use_5050(options, q["answer"])
            print()
            for key, val in options.items():
                print(f"    {key}: {val}")
            print()

        elif user_input == "PHONE" and lifelines["Phone a Friend"]:
            lifelines["Phone a Friend"] = False
            use_phone_a_friend(q["answer"])
            print()

        elif user_input == "AUDIENCE" and lifelines["Ask the Audience"]:
            lifelines["Ask the Audience"] = False
            use_ask_audience(options, q["answer"])
            print()

        elif user_input in ["A", "B", "C", "D"]:
            if user_input not in options:
                print("  ⚠️  That option was removed by 50:50! Choose from the remaining options.")
                continue

            print("\n  ⏳ Final answer?", end="")
            time.sleep(1)
            print(" ...", end="")
            time.sleep(1)
            print(" ...")
            time.sleep(1)

            if user_input == q["answer"]:
                current_prize = PRIZE_LADDER[i]
                print(f"  ✅ CORRECT! You've won {current_prize}!")
                if i in SAFE_HAVENS:
                    winnings = current_prize
                    print(f"  🛡️  You've reached a safe haven! {winnings} is now guaranteed.")
            else:
                # Determine walk-away amount (last safe haven)
                walk_away = "$0"
                for sh in SAFE_HAVENS:
                    if i > sh:
                        walk_away = PRIZE_LADDER[sh]
                print(f"  ❌ WRONG! The correct answer was {q['answer']}: {q['options'][q['answer']]}")
                print(f"  💔 You leave with: {walk_away}")
                exit()
            break
        else:
            print("  ⚠️  Invalid input. Please enter A, B, C, D or a lifeline name.")

print(f"\n{'🎉' * 20}")
print("  🏆 CONGRATULATIONS! You've won $1,000,000!")
print(f"{'🎉' * 20}")
