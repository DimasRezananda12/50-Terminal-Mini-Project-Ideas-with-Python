import random

print("🔢 Welcome to Guess My Number!")
print("I'm thinking of a number... can you guess it?")
print("-" * 50)

def play_game():
    print("\n  Choose difficulty:")
    print("  1. Easy   — 1 to 50   (10 attempts)")
    print("  2. Medium — 1 to 100  (7 attempts)")
    print("  3. Hard   — 1 to 500  (8 attempts)")
    print("  4. Custom — You set the range and attempts")

    while True:
        diff = input("\n  Enter 1, 2, 3, or 4: ").strip()
        if diff == "1":
            lo, hi, max_attempts = 1, 50, 10
            break
        elif diff == "2":
            lo, hi, max_attempts = 1, 100, 7
            break
        elif diff == "3":
            lo, hi, max_attempts = 1, 500, 8
            break
        elif diff == "4":
            try:
                lo = int(input("  Min number: "))
                hi = int(input("  Max number: "))
                max_attempts = int(input("  Max attempts: "))
                if lo >= hi or max_attempts < 1:
                    print("  Warning: Invalid range or attempts. Try again.")
                    continue
                break
            except ValueError:
                print("  Warning: Please enter valid numbers.")
        else:
            print("  Warning: Please enter 1, 2, 3, or 4.")

    secret = random.randint(lo, hi)
    attempts = 0
    history = []

    print(f"\n  I'm thinking of a number between {lo} and {hi}.")
    print(f"  You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"  Attempts remaining: {remaining}")

        if history:
            print(f"  Your guesses so far: {history}")

        while True:
            try:
                guess = int(input(f"  Your guess ({lo}-{hi}): "))
                if lo <= guess <= hi:
                    break
                print(f"  Warning: Please guess between {lo} and {hi}.")
            except ValueError:
                print("  Warning: Please enter a whole number.")

        attempts += 1
        history.append(guess)
        diff_val = abs(guess - secret)

        if guess == secret:
            print(f"\n  CORRECT! The number was {secret}! 🎉")
            print(f"  You got it in {attempts} attempt(s)!")

            # Score rating
            ratio = attempts / max_attempts
            if ratio <= 0.3:
                print("  Rating: ⭐⭐⭐ Incredible!")
            elif ratio <= 0.6:
                print("  Rating: ⭐⭐ Nice work!")
            else:
                print("  Rating: ⭐ You made it!")
            return True

        elif guess < secret:
            hint = "Higher! ⬆️"
        else:
            hint = "Lower! ⬇️"

        # Warmth hint
        if diff_val <= 5:
            warmth = "🔥 Very hot!"
        elif diff_val <= 15:
            warmth = "☀️  Warm."
        elif diff_val <= 35:
            warmth = "❄️  Cold."
        else:
            warmth = "🧊 Freezing!"

        print(f"  {hint}  {warmth}\n")

    print(f"\n  Out of attempts! The number was {secret}. 😢")
    return False

# ── Main Loop ──
wins = 0
total = 0

while True:
    result = play_game()
    total += 1
    if result:
        wins += 1

    print(f"\n  Score: {wins} win(s) out of {total} game(s)")
    again = input("  Play again? (yes / no): ").strip().lower()
    if again not in ("yes", "y"):
        break

print(f"\n  Thanks for playing! Final score: {wins}/{total} 👋")
