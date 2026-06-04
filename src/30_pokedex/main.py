import json
import os

print("🔎 Welcome to your Personal Pokédex!")
print("Catch 'em all and record their details.")
print("-" * 50)

DATA_FILE = "pokedex.json"

# Starter data just in case the file is empty
STARTER_POKEMON = [
    {"id": 1, "name": "Bulbasaur", "type": "Grass/Poison", "hp": 45, "description": "A strange seed was planted on its back at birth."},
    {"id": 4, "name": "Charmander", "type": "Fire", "hp": 39, "description": "The flame on its tail indicates Charmander's life force."},
    {"id": 7, "name": "Squirtle", "type": "Water", "hp": 44, "description": "Its shell is not just for protection. It's used for swimming at high speeds."},
    {"id": 25, "name": "Pikachu", "type": "Electric", "hp": 35, "description": "When several of these POKéMON gather, their electricity could build and cause lightning storms."}
]

def load_pokedex():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    # If no file exists, initialize with starters and save
    save_pokedex(STARTER_POKEMON)
    return STARTER_POKEMON

def save_pokedex(pokedex):
    with open(DATA_FILE, "w") as f:
        json.dump(pokedex, f, indent=4)

def view_pokemon(p):
    print("\n" + "=" * 40)
    print(f"  [{p['id']:03d}] {p['name'].upper()}")
    print("-" * 40)
    print(f"  Type: {p['type']}")
    print(f"  Base HP: {p['hp']}")
    print(f"\n  Description: {p['description']}")
    print("=" * 40)

def main():
    pokedex = load_pokedex()
    
    while True:
        print("\n  Options:")
        print("  1. 📖 View all registered Pokémon")
        print("  2. 🔍 Search Pokémon by Name or ID")
        print("  3. 🔴 Add a new Pokémon to Pokédex")
        print("  4. ❌ Exit")
        
        choice = input("\n  Enter choice (1-4): ").strip()
        
        if choice == "1":
            print("\n  📱 Registered Pokémon:")
            sorted_dex = sorted(pokedex, key=lambda x: x['id'])
            for p in sorted_dex:
                print(f"     [{p['id']:03d}] {p['name']} ({p['type']})")
                
        elif choice == "2":
            query = input("  Enter Pokémon Name or ID to search: ").strip().lower()
            found = None
            
            for p in pokedex:
                if str(p['id']) == query or p['name'].lower() == query:
                    found = p
                    break
                    
            if found:
                view_pokemon(found)
            else:
                print("  Pokémon not found in your Pokédex.")
                
        elif choice == "3":
            try:
                pk_id = int(input("  Enter Pokémon ID (e.g., 150): "))
                # Check if ID already exists
                if any(p['id'] == pk_id for p in pokedex):
                    print("  Warning: A Pokémon with this ID is already registered.")
                    continue
                    
                name = input("  Name: ").strip().capitalize()
                pk_type = input("  Type (e.g., Fire/Flying): ").strip()
                hp = int(input("  Base HP: "))
                desc = input("  Short Description: ").strip()
                
                if name and pk_type:
                    pokedex.append({
                        "id": pk_id,
                        "name": name,
                        "type": pk_type,
                        "hp": hp,
                        "description": desc
                    })
                    save_pokedex(pokedex)
                    print(f"  ✅ Data for {name} registered successfully!")
                else:
                    print("  Warning: Name and Type cannot be empty.")
            except ValueError:
                print("  Warning: ID and HP must be numbers.")
                
        elif choice == "4":
            print("\n  👋 Goodbye! Keep exploring!")
            break
            
        else:
            print("  Warning: Invalid choice. Try again.")

if __name__ == "__main__":
    main()
