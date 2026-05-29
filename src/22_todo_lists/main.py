import json
import os

print("📋 Welcome to your To-Do List!")
print("Keep track of what you need to get done.")
print("-" * 50)

DATA_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def view_tasks(tasks):
    print("\n  📝 Your Tasks:")
    if not tasks:
        print("     No tasks yet! You're all caught up. 🎉")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["completed"] else "❌"
            print(f"     {i}. [{status}] {task['title']}")
    print("-" * 50)

def main():
    tasks = load_tasks()
    
    while True:
        view_tasks(tasks)
        print("\n  Options:")
        print("  1. ➕ Add a task")
        print("  2. ✔️  Mark task as complete")
        print("  3. 🗑️  Delete a task")
        print("  4. 🚪 Exit")
        
        choice = input("\n  Enter choice (1-4): ").strip()
        
        if choice == "1":
            title = input("  Enter task description: ").strip()
            if title:
                tasks.append({"title": title, "completed": False})
                save_tasks(tasks)
                print("  Task added!")
            else:
                print("  Warning: Task cannot be empty.")
                
        elif choice == "2":
            if not tasks:
                print("  No tasks to complete.")
                continue
            try:
                task_num = int(input("  Enter task number to complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    save_tasks(tasks)
                    print("  Task marked as complete!")
                else:
                    print("  Warning: Invalid task number.")
            except ValueError:
                print("  Warning: Please enter a valid number.")
                
        elif choice == "3":
            if not tasks:
                print("  No tasks to delete.")
                continue
            try:
                task_num = int(input("  Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"  Deleted task: '{deleted['title']}'")
                else:
                    print("  Warning: Invalid task number.")
            except ValueError:
                print("  Warning: Please enter a valid number.")
                
        elif choice == "4":
            print("\n  👋 See you later! Don't forget your tasks!")
            break
            
        else:
            print("  Warning: Invalid choice. Try again.")

if __name__ == "__main__":
    main()
