import json
import os
import datetime

print("💸 Welcome to the Expense Tracker!")
print("Monitor your spending and manage your budget.")
print("-" * 50)

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def format_currency(amount):
    return f"${amount:,.2f}"

def view_expenses(expenses):
    print("\n  📊 Expense Summary:")
    if not expenses:
        print("     No expenses recorded yet. Good job saving! 💰")
    else:
        total = sum(exp["amount"] for exp in expenses)
        
        # Calculate by category
        categories = {}
        for exp in expenses:
            cat = exp["category"]
            categories[cat] = categories.get(cat, 0) + exp["amount"]
            
        print(f"     Total Spent: {format_currency(total)}")
        print("\n     By Category:")
        for cat, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            print(f"       - {cat:<15}: {format_currency(amount)}")
    print("-" * 50)

def main():
    expenses = load_expenses()
    
    while True:
        view_expenses(expenses)
        print("\n  Options:")
        print("  1. ➕ Add an expense")
        print("  2. 📜 View detailed history")
        print("  3. 🗑️  Clear all expenses")
        print("  4. ❌ Exit")
        
        choice = input("\n  Enter choice (1-4): ").strip()
        
        if choice == "1":
            try:
                amount = float(input("  Enter amount: $"))
                if amount <= 0:
                    print("  Warning: Amount must be positive.")
                    continue
                    
                description = input("  Enter description (e.g., Lunch, Bus ticket): ").strip()
                category = input("  Enter category (e.g., Food, Transport, Entertainment): ").strip().capitalize()
                
                if not description or not category:
                    print("  Warning: Description and Category cannot be empty.")
                    continue
                    
                date = datetime.date.today().isoformat()
                
                expenses.append({
                    "date": date,
                    "description": description,
                    "category": category,
                    "amount": amount
                })
                save_expenses(expenses)
                print(f"  ✅ Expense added: {format_currency(amount)} for {description}.")
                
            except ValueError:
                print("  Warning: Invalid amount.")
                
        elif choice == "2":
            print("\n  📜 Expense History:")
            print("  " + "-" * 60)
            if not expenses:
                print("  No expenses yet.")
            else:
                print(f"  {'Date':<12} | {'Category':<15} | {'Description':<20} | {'Amount'}")
                print("  " + "-" * 60)
                # Show most recent first
                for exp in reversed(expenses):
                    print(f"  {exp['date']:<12} | {exp['category']:<15} | {exp['description'][:18]:<20} | {format_currency(exp['amount'])}")
            print("  " + "-" * 60)
            
        elif choice == "3":
            confirm = input("  Are you sure you want to clear ALL expenses? This cannot be undone. (yes/no): ").strip().lower()
            if confirm in ('y', 'yes'):
                expenses = []
                save_expenses(expenses)
                print("  🗑️  All expenses cleared.")
                
        elif choice == "4":
            print("\n  👋 Keep tracking those finances! See you later.")
            break
            
        else:
            print("  Warning: Invalid choice. Try again.")

if __name__ == "__main__":
    main()
