import json
import os

print("🍲 Welcome to the Recipe Book!")
print("Store and search your favorite cooking recipes.")
print("-" * 50)

DATA_FILE = "recipes.json"

def load_recipes():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return []

def save_recipes(recipes):
    with open(DATA_FILE, "w") as f:
        json.dump(recipes, f, indent=4)

def view_recipe(recipe):
    print("\n" + "=" * 40)
    print(f"  🍽️  {recipe['title'].upper()}")
    print("=" * 40)
    print("  🥕 INGREDIENTS:")
    for item in recipe['ingredients']:
        print(f"    - {item}")
    print("\n  👨‍🍳 INSTRUCTIONS:")
    for i, step in enumerate(recipe['instructions'], 1):
        print(f"    {i}. {step}")
    print("=" * 40)

def main():
    recipes = load_recipes()
    
    while True:
        print("\n  Options:")
        print("  1. ➕ Add a new recipe")
        print("  2. 📜 View all recipes")
        print("  3. 🔍 Search by ingredient")
        print("  4. ❌ Exit")
        
        choice = input("\n  Enter choice (1-4): ").strip()
        
        if choice == "1":
            title = input("  Recipe Name: ").strip()
            if not title:
                print("  Warning: Recipe name cannot be empty.")
                continue
                
            print("  Enter ingredients one by one (type 'done' to finish):")
            ingredients = []
            while True:
                item = input("    Ingredient: ").strip()
                if item.lower() == 'done':
                    break
                if item:
                    ingredients.append(item)
                    
            print("  Enter instructions step by step (type 'done' to finish):")
            instructions = []
            while True:
                step = input(f"    Step {len(instructions)+1}: ").strip()
                if step.lower() == 'done':
                    break
                if step:
                    instructions.append(step)
                    
            if ingredients and instructions:
                recipes.append({
                    "title": title,
                    "ingredients": ingredients,
                    "instructions": instructions
                })
                save_recipes(recipes)
                print(f"  ✅ Recipe '{title}' saved successfully!")
            else:
                print("  Warning: A recipe needs at least one ingredient and instruction step.")
                
        elif choice == "2":
            if not recipes:
                print("  No recipes found. Add some delicious meals first!")
                continue
                
            print("\n  📖 Your Recipe Collection:")
            for i, r in enumerate(recipes, 1):
                print(f"  {i}. {r['title']}")
                
            try:
                idx = int(input("\n  Enter recipe number to view details (or 0 to cancel): ")) - 1
                if 0 <= idx < len(recipes):
                    view_recipe(recipes[idx])
                elif idx != -1:
                    print("  Warning: Invalid recipe number.")
            except ValueError:
                print("  Warning: Please enter a valid number.")
                
        elif choice == "3":
            query = input("  Enter an ingredient to search for: ").strip().lower()
            results = []
            for r in recipes:
                for ing in r['ingredients']:
                    if query in ing.lower():
                        results.append(r)
                        break  # Found in this recipe, move to next recipe
                        
            if results:
                print(f"\n  🔍 Found {len(results)} recipe(s) containing '{query}':")
                for i, r in enumerate(results, 1):
                    print(f"  {i}. {r['title']}")
            else:
                print(f"  No recipes found containing '{query}'.")
                
        elif choice == "4":
            print("\n  👋 Happy cooking!")
            break
            
        else:
            print("  Warning: Invalid choice. Try again.")

if __name__ == "__main__":
    main()
