import json
import os

print("☎️  Welcome to the Contact Book!")
print("Keep your friends and family's details organized.")
print("-" * 50)

DATA_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return []

def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def view_contacts(contacts):
    print("\n  📇 Your Contacts:")
    if not contacts:
        print("     No contacts saved yet.")
    else:
        # Sort alphabetically by name
        sorted_contacts = sorted(contacts, key=lambda x: x['name'].lower())
        for i, c in enumerate(sorted_contacts, 1):
            print(f"     {i}. {c['name']}")
            print(f"        📱 Phone: {c['phone']}")
            if c.get('email'):
                print(f"        📧 Email: {c['email']}")
    print("-" * 50)

def main():
    contacts = load_contacts()
    
    while True:
        print("\n  Options:")
        print("  1. ➕ Add new contact")
        print("  2. 📜 View all contacts")
        print("  3. 🔍 Search contact")
        print("  4. 🗑️  Delete contact")
        print("  5. ❌ Exit")
        
        choice = input("\n  Enter choice (1-5): ").strip()
        
        if choice == "1":
            name = input("  Name: ").strip()
            phone = input("  Phone Number: ").strip()
            email = input("  Email (optional): ").strip()
            
            if name and phone:
                contacts.append({
                    "name": name,
                    "phone": phone,
                    "email": email
                })
                save_contacts(contacts)
                print(f"  ✅ Contact '{name}' saved successfully!")
            else:
                print("  Warning: Name and Phone Number are required.")
                
        elif choice == "2":
            view_contacts(contacts)
            
        elif choice == "3":
            query = input("  Search by name or phone: ").strip().lower()
            results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
            
            if results:
                print(f"\n  🔍 Found {len(results)} matching contact(s):")
                for c in results:
                    print(f"     👤 {c['name']} | 📱 {c['phone']} | 📧 {c.get('email', '-')}")
            else:
                print("  No contacts found.")
                
        elif choice == "4":
            if not contacts:
                print("  No contacts to delete.")
                continue
                
            sorted_contacts = sorted(contacts, key=lambda x: x['name'].lower())
            view_contacts(sorted_contacts)
            
            try:
                idx = int(input("\n  Enter contact number to delete: ")) - 1
                if 0 <= idx < len(sorted_contacts):
                    contact_to_remove = sorted_contacts[idx]
                    contacts.remove(contact_to_remove)
                    save_contacts(contacts)
                    print(f"  🗑️  Deleted '{contact_to_remove['name']}'.")
                else:
                    print("  Warning: Invalid contact number.")
            except ValueError:
                print("  Warning: Please enter a valid number.")
                
        elif choice == "5":
            print("\n  👋 Goodbye! Keep in touch.")
            break
            
        else:
            print("  Warning: Invalid choice. Try again.")

if __name__ == "__main__":
    main()
