import random
import json
import os

print("🔢 Enhanced Guess My Number!")
print("Try to guess the secret number in the fewest attempts.")
print("-" * 50)

DATA_FILE = "guess_scores.json"

def load_scores():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    # High scores for different ranges (least attempts = best)
    return {"10": None, "50": None, "100": None, "1000": None}

def save_scores(scores):
    with open(DATA_FILE, "w") as f:
        json.dump(scores, f, indent=4)

def view_scores(scores):
    print("\n  🏆 Best Scores (Fewest Attempts):")
    for range_max, best in scores.items():
        score_text = f"{best} attempts" if best else "No record yet"
        print(f"     1 to {range_max:<4}: {score_text}")
    print("-" * 50)

def play_game(max_num, scores):
    secret = random.randint(1, max_num)
    attempts = 0
    print(f"\n  I'm thinking of a number between 1 and {max_num}.")
    
    while True:
        try:
            guess = int(input("  Your guess: "))
            attempts += 1
            
            if guess < secret:
                print("  🔼 Too low!")
            elif guess > secret:
                print("  🔽 Too high!")
            else:
                print(f"  🎉 Correct! You guessed it in {attempts} attempts.")
                
                # Update high score if applicable
                range_key = str(max_num)
                if range_key in scores:
                    current_best = scores[range_key]
                    if current_best is None or attempts < current_best:
                        scores[range_key] = attempts
                        save_scores(scores)
                        print("  🌟 NEW HIGH SCORE for this difficulty!")
                break
        except ValueError:
            print("  Warning: Please enter a valid number.")

def main():
    scores = load_scores()
    
    while True:
        print("\n  Options:")
        print("  1. 🟢 Play Easy (1-10)")
        print("  2. 🟡 Play Medium (1-50)")
        print("  3. 🟠 Play Hard (1-100)")
        print("  4. 🔴 Play Expert (1-1000)")
        print("  5. 🏆 View High Scores")
        print("  6. ❌ Exit")
        
        choice = input("\n  Enter choice (1-6): ").strip()
        
        if choice == "1":
            play_game(10, scores)
        elif choice == "2":
            play_game(50, scores)
        elif choice == "3":
            play_game(100, scores)
        elif choice == "4":
            play_game(1000, scores)
        elif choice == "5":
            view_scores(scores)
        elif choice == "6":
            print("\n  👋 Thanks for playing!")
            break
        else:
            print("  Warning: Invalid choice.")

if __name__ == "__main__":
    main()
