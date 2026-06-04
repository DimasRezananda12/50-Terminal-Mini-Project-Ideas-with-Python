import random
import json
import os

print("✂️ 📄 🪨 Enhanced Rock, Paper, Scissors!")
print("Play against the computer and track your win rate.")
print("-" * 50)

DATA_FILE = "rps_stats.json"
OPTIONS = ["rock", "paper", "scissors"]
EMOJIS = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

def load_stats():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return {"wins": 0, "losses": 0, "ties": 0}

def save_stats(stats):
    with open(DATA_FILE, "w") as f:
        json.dump(stats, f, indent=4)

def view_stats(stats):
    total = stats['wins'] + stats['losses'] + stats['ties']
    print("\n  🏆 Your Lifetime Stats:")
    print(f"     Wins:   {stats['wins']} 🟢")
    print(f"     Losses: {stats['losses']} 🔴")
    print(f"     Ties:   {stats['ties']} ⚪")
    if total > 0:
        win_rate = (stats['wins'] / total) * 100
        print(f"     Win Rate: {win_rate:.1f}%")
    print("-" * 50)

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"

def main():
    stats = load_stats()
    
    while True:
        print("\n  Options:")
        print("  1. 🎮 Play a round")
        print("  2. 📊 View lifetime stats")
        print("  3. ❌ Exit")
        
        choice = input("\n  Enter choice (1-3): ").strip()
        
        if choice == "1":
            print("\n  Choose your weapon:")
            print("  1. 🪨 Rock")
            print("  2. 📄 Paper")
            print("  3. ✂️  Scissors")
            
            p_choice = input("  (1-3): ").strip()
            if p_choice == "1": player = "rock"
            elif p_choice == "2": player = "paper"
            elif p_choice == "3": player = "scissors"
            else:
                print("  Warning: Invalid choice.")
                continue
                
            computer = random.choice(OPTIONS)
            
            print(f"\n  You:      {player.capitalize()} {EMOJIS[player]}")
            print(f"  Computer: {computer.capitalize()} {EMOJIS[computer]}")
            
            result = determine_winner(player, computer)
            if result == "win":
                print("  🎉 You win!")
                stats["wins"] += 1
            elif result == "lose":
                print("  💻 Computer wins!")
                stats["losses"] += 1
            else:
                print("  🤝 It's a tie!")
                stats["ties"] += 1
                
            save_stats(stats)
            
        elif choice == "2":
            view_stats(stats)
            
        elif choice == "3":
            print("\n  👋 Thanks for playing!")
            break
        else:
            print("  Warning: Invalid choice.")

if __name__ == "__main__":
    main()