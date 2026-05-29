import json
import os
import datetime

print("🏦 Welcome to the Bank Account Manager!")
print("Manage your balance and transaction history securely.")
print("-" * 50)

DATA_FILE = "account_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return {"balance": 0.0, "history": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def format_currency(amount):
    return f"${amount:,.2f}"

def log_transaction(data, type, amount):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["history"].append({
        "timestamp": timestamp,
        "type": type,
        "amount": amount,
        "balance_after": data["balance"]
    })

def main():
    data = load_data()
    
    while True:
        print(f"\n  💰 Current Balance: {format_currency(data['balance'])}")
        print("\n  What would you like to do?")
        print("  1. 💵 Deposit")
        print("  2. 💸 Withdraw")
        print("  3. 📜 View Transaction History")
        print("  4. ❌ Exit")
        
        choice = input("\n  Enter 1-4: ").strip()
        
        if choice == "1":
            try:
                amount = float(input("  Enter deposit amount: $"))
                if amount <= 0:
                    print("  Warning: Deposit amount must be positive.")
                    continue
                data["balance"] += amount
                log_transaction(data, "Deposit", amount)
                save_data(data)
                print(f"  ✅ Successfully deposited {format_currency(amount)}.")
            except ValueError:
                print("  Warning: Invalid amount.")
                
        elif choice == "2":
            try:
                amount = float(input("  Enter withdrawal amount: $"))
                if amount <= 0:
                    print("  Warning: Withdrawal amount must be positive.")
                    continue
                if amount > data["balance"]:
                    print("  ❌ Insufficient funds!")
                    continue
                data["balance"] -= amount
                log_transaction(data, "Withdrawal", amount)
                save_data(data)
                print(f"  ✅ Successfully withdrew {format_currency(amount)}.")
            except ValueError:
                print("  Warning: Invalid amount.")
                
        elif choice == "3":
            print("\n  📜 Transaction History:")
            print("  " + "-" * 55)
            if not data["history"]:
                print("  No transactions yet.")
            else:
                print(f"  {'Date & Time':<20} | {'Type':<12} | {'Amount':<10} | {'Balance'}")
                print("  " + "-" * 55)
                for t in reversed(data["history"][-10:]):  # Show last 10
                    print(f"  {t['timestamp']:<20} | {t['type']:<12} | {format_currency(t['amount']):<10} | {format_currency(t['balance_after'])}")
            print("  " + "-" * 55)
                
        elif choice == "4":
            print("\n  👋 Thank you for using Bank Account Manager!")
            break
            
        else:
            print("  Warning: Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
