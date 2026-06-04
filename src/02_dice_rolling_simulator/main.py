import random
import json
import os

print("🎲 Welcome to the Enhanced Dice Rolling Simulator!")
print("Roll the dice and track your statistics.")
print("-" * 50)

DATA_FILE = "dice_stats.json"

def load_stats():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return {"total_rolls": 0, "roll_counts": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}, "history": []}

def save_stats(stats):
    with open(DATA_FILE, "w") as f:
        json.dump(stats, f, indent=4)

def view_stats(stats):
    print("\n  📊 Dice Statistics:")
    print(f"     Total Rolls: {stats['total_rolls']}")
    if stats['total_rolls'] > 0:
        print("     Frequency:")
        for i in range(1, 7):
            count = stats['roll_counts'][str(i)]
            percentage = (count / stats['total_rolls']) * 100
            print(f"       Face {i}: {count} times ({percentage:.1f}%)")
        print(f"     Last 5 rolls: {stats['history'][-5:]}")
    print("-" * 50)

def main():
    stats = load_stats()
    
    while True:
        print("\n  Options:")
        print("  1. 🎲 Roll the Dice")
        print("  2. 📊 View Statistics")
        print("  3. 🗑️  Reset Statistics")
        print("  4. ❌ Exit")
        
        choice = input("\n  Enter choice (1-4): ").strip()
        
        if choice == "1":
            print("\n  Rolling... 🎲")
            result = random.randint(1, 6)
            print(f"  You rolled a {result}!")
            
            # Update stats
            stats["total_rolls"] += 1
            stats["roll_counts"][str(result)] += 1
            stats["history"].append(result)
            # Keep history from getting too huge, keep last 100
            if len(stats["history"]) > 100:
                stats["history"].pop(0)
                
            save_stats(stats)
            
        elif choice == "2":
            view_stats(stats)
            
        elif choice == "3":
            confirm = input("  Are you sure you want to reset all stats? (yes/no): ").lower()
            if confirm in ('y', 'yes'):
                stats = {"total_rolls": 0, "roll_counts": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}, "history": []}
                save_stats(stats)
                print("  Stats reset.")
                
        elif choice == "4":
            print("\n  👋 Thanks for playing!")
            break
        else:
            print("  Warning: Invalid choice.")

if __name__ == "__main__":
    main()