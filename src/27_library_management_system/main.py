import json
import os
import datetime

print("📚 Welcome to the Library Management System!")
print("Manage your personal collection of books.")
print("-" * 50)

DATA_FILE = "library.json"

def load_library():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return []

def save_library(library):
    with open(DATA_FILE, "w") as f:
        json.dump(library, f, indent=4)

def view_library(library):
    print("\n  📖 Your Library:")
    if not library:
        print("     No books in your library yet.")
    else:
        # Sort by title
        sorted_lib = sorted(library, key=lambda x: x['title'].lower())
        for i, book in enumerate(sorted_lib, 1):
            status = "🟢 Available" if book["available"] else f"🔴 Borrowed by {book['borrower']}"
            print(f"     {i}. {book['title']} by {book['author']} [{status}]")
    print("-" * 50)

def main():
    library = load_library()
    
    while True:
        view_library(library)
        print("\n  Options:")
        print("  1. ➕ Add a new book")
        print("  2. 📤 Lend a book")
        print("  3. 📥 Return a book")
        print("  4. 🗑️  Remove a book")
        print("  5. ❌ Exit")
        
        choice = input("\n  Enter choice (1-5): ").strip()
        
        if choice == "1":
            title = input("  Enter book title: ").strip()
            author = input("  Enter book author: ").strip()
            
            if title and author:
                library.append({
                    "title": title,
                    "author": author,
                    "available": True,
                    "borrower": None,
                    "date_borrowed": None
                })
                save_library(library)
                print(f"  ✅ '{title}' added to the library!")
            else:
                print("  Warning: Title and author cannot be empty.")
                
        elif choice == "2":
            if not library:
                print("  Library is empty.")
                continue
                
            sorted_lib = sorted(library, key=lambda x: x['title'].lower())
            
            try:
                idx = int(input("  Enter book number to lend: ")) - 1
                if 0 <= idx < len(sorted_lib):
                    book = sorted_lib[idx]
                    
                    if not book["available"]:
                        print(f"  ❌ '{book['title']}' is already borrowed by {book['borrower']}.")
                        continue
                        
                    borrower = input("  Who is borrowing this book? ").strip()
                    if borrower:
                        # Update the actual book in the main list
                        for b in library:
                            if b["title"] == book["title"] and b["author"] == book["author"]:
                                b["available"] = False
                                b["borrower"] = borrower
                                b["date_borrowed"] = datetime.date.today().isoformat()
                                break
                        save_library(library)
                        print(f"  📤 Lent '{book['title']}' to {borrower}.")
                    else:
                        print("  Warning: Borrower name cannot be empty.")
                else:
                    print("  Warning: Invalid book number.")
            except ValueError:
                print("  Warning: Please enter a valid number.")
                
        elif choice == "3":
            # Show only borrowed books
            borrowed = [b for b in library if not b["available"]]
            if not borrowed:
                print("  No books are currently borrowed.")
                continue
                
            print("\n  Borrowed Books:")
            for i, b in enumerate(borrowed, 1):
                print(f"  {i}. {b['title']} (Borrowed by {b['borrower']} on {b['date_borrowed']})")
                
            try:
                idx = int(input("\n  Enter book number being returned: ")) - 1
                if 0 <= idx < len(borrowed):
                    book_returning = borrowed[idx]
                    
                    for b in library:
                        if b["title"] == book_returning["title"] and b["author"] == book_returning["author"]:
                            b["available"] = True
                            b["borrower"] = None
                            b["date_borrowed"] = None
                            break
                            
                    save_library(library)
                    print(f"  📥 '{book_returning['title']}' has been returned and is available again.")
                else:
                    print("  Warning: Invalid book number.")
            except ValueError:
                print("  Warning: Please enter a valid number.")
                
        elif choice == "4":
            if not library:
                print("  Library is empty.")
                continue
                
            sorted_lib = sorted(library, key=lambda x: x['title'].lower())
            
            try:
                idx = int(input("  Enter book number to remove: ")) - 1
                if 0 <= idx < len(sorted_lib):
                    book = sorted_lib[idx]
                    # Remove from original list
                    library = [b for b in library if not (b["title"] == book["title"] and b["author"] == book["author"])]
                    save_library(library)
                    print(f"  🗑️  Removed '{book['title']}' from library.")
                else:
                    print("  Warning: Invalid book number.")
            except ValueError:
                print("  Warning: Please enter a valid number.")
                
        elif choice == "5":
            print("\n  👋 Happy reading! See you later.")
            break
            
        else:
            print("  Warning: Invalid choice. Try again.")

if __name__ == "__main__":
    main()
