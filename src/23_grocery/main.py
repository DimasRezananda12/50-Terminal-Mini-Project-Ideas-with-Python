import json
import os

print("🛒 Welcome to the Grocery List Manager!")
print("Organize your shopping trip easily.")
print("-" * 50)

DATA_FILE = "grocery_list.json"

def load_list():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return []

def save_list(groceries):
    with open(DATA_FILE, "w") as f:
        json.dump(groceries, f, indent=4)

def view_list(groceries):
    print("\n  🛍️  Your Grocery List:")
    if not groceries:
        print("     List is empty. Time to plan some meals! 🍽️")
    else:
        for i, item in enumerate(groceries, 1):
            status = "✅" if item["bought"] else "🛒"
            print(f"     {i}. {status} {item['name']} (Qty: {item['quantity']})")
    print("-" * 50)

def main():
    groceries = load_list()
    
    while True:
        view_list(groceries)
        print("\n  Options:")
        print("  1. ➕ Add an item")
        print("  2. ✔️  Mark item as bought")
        print("  3. 🗑️  Remove an item")
        print("  4. 🧹 Clear entire list")
        print("  5. 🚪 Exit")
        
        choice = input("\n  Enter choice (1-5): ").strip()
        
        if choice == "1":
            name = input("  Enter item name: ").strip()
            if not name:
                print("  Warning: Item name cannot be empty.")
                continue
                
            qty = input("  Enter quantity (e.g., 2, 1kg, 3 bunches): ").strip()
            if not qty:
                qty = "1"
                
            groceries.append({"name": name, "quantity": qty, "bought": False})
            save_list(groceries)
            print("  Item added!")
            
        elif choice == "2":
            if not groceries:
                print("  List is empty.")
                continue
            try:
                idx = int(input("  Enter item number to mark bought: "))
                if 1 <= idx <= len(groceries):
                    groceries[idx - 1]["bought"] = True
                    save_list(groceries)
                    print("  Item marked as bought!")
                else:
                    print("  Warning: Invalid item number.")
            except ValueError:
                print("  Warning: Please enter a valid number.")
                
        elif choice == "3":
            if not groceries:
                print("  List is empty.")
                continue
            try:
                idx = int(input("  Enter item number to remove: "))
                if 1 <= idx <= len(groceries):
                    deleted = groceries.pop(idx - 1)
                    save_list(groceries)
                    print(f"  Removed: '{deleted['name']}'")
                else:
                    print("  Warning: Invalid item number.")
            except ValueError:
                print("  Warning: Please enter a valid number.")
                
        elif choice == "4":
            confirm = input("  Are you sure you want to clear the whole list? (yes/no): ").strip().lower()
            if confirm in ('y', 'yes'):
                groceries = []
                save_list(groceries)
                print("  List cleared.")
                
        elif choice == "5":
            print("\n  👋 Happy shopping! See you later.")
            break
            
        else:
            print("  Warning: Invalid choice. Try again.")

if __name__ == "__main__":
    main()
