import json
import os

print("💖 Welcome to the Faves List Manager!")
print("Keep track of all your favorite things in one place.")
print("-" * 50)

DATA_FILE = "faves_list.json"

def load_faves():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return {}

def save_faves(faves):
    with open(DATA_FILE, "w") as f:
        json.dump(faves, f, indent=4)

def view_faves(faves):
    print("\n  🌟 Your Favorites:")
    if not faves:
        print("     No favorites added yet!")
    else:
        for category, items in faves.items():
            print(f"\n     {category.upper()}:")
            if not items:
                print("       - Empty")
            for item in items:
                print(f"       💖 {item}")
    print("-" * 50)

def main():
    faves = load_faves()
    
    while True:
        view_faves(faves)
        print("\n  Options:")
        print("  1. ➕ Add a favorite item")
        print("  2. 🗑️  Remove an item")
        print("  3. 📁 Add a new category")
        print("  4. ❌ Exit")
        
        choice = input("\n  Enter choice (1-4): ").strip()
        
        if choice == "1":
            if not faves:
                print("  Warning: Please add a category first (Option 3).")
                continue
                
            print("\n  Categories available:")
            categories = list(faves.keys())
            for i, cat in enumerate(categories, 1):
                print(f"  {i}. {cat}")
                
            try:
                cat_idx = int(input("\n  Select category number: ")) - 1
                if 0 <= cat_idx < len(categories):
                    category = categories[cat_idx]
                    item = input(f"  Enter your favorite {category}: ").strip()
                    if item:
                        faves[category].append(item)
                        save_faves(faves)
                        print("  ✅ Item added successfully!")
                    else:
                        print("  Warning: Item name cannot be empty.")
                else:
                    print("  Warning: Invalid category number.")
            except ValueError:
                print("  Warning: Please enter a valid number.")
                
        elif choice == "2":
            if not faves:
                print("  Warning: List is empty.")
                continue
                
            print("\n  Categories available:")
            categories = list(faves.keys())
            for i, cat in enumerate(categories, 1):
                print(f"  {i}. {cat}")
                
            try:
                cat_idx = int(input("\n  Select category number: ")) - 1
                if 0 <= cat_idx < len(categories):
                    category = categories[cat_idx]
                    items = faves[category]
                    
                    if not items:
                        print(f"  Warning: No items in {category}.")
                        continue
                        
                    print(f"\n  Items in {category}:")
                    for i, item in enumerate(items, 1):
                        print(f"  {i}. {item}")
                        
                    item_idx = int(input("\n  Select item number to remove: ")) - 1
                    if 0 <= item_idx < len(items):
                        removed = items.pop(item_idx)
                        save_faves(faves)
                        print(f"  ✅ Removed '{removed}'.")
                    else:
                        print("  Warning: Invalid item number.")
                else:
                    print("  Warning: Invalid category number.")
            except ValueError:
                print("  Warning: Please enter a valid number.")
                
        elif choice == "3":
            new_cat = input("  Enter new category name (e.g., Movies, Foods): ").strip()
            if new_cat:
                if new_cat not in faves:
                    faves[new_cat] = []
                    save_faves(faves)
                    print(f"  ✅ Category '{new_cat}' added!")
                else:
                    print("  Warning: Category already exists.")
            else:
                print("  Warning: Category name cannot be empty.")
                
        elif choice == "4":
            print("\n  👋 See you later! Keep enjoying your favorites.")
            break
            
        else:
            print("  Warning: Invalid choice. Try again.")

if __name__ == "__main__":
    main()
