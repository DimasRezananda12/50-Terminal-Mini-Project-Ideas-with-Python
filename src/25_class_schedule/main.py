import json
import os

print("📝 Welcome to the Class Schedule Manager!")
print("Keep your academic life organized.")
print("-" * 50)

DATA_FILE = "schedule.json"
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def load_schedule():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    # Initialize empty schedule for each day
    return {day: [] for day in DAYS}

def save_schedule(schedule):
    with open(DATA_FILE, "w") as f:
        json.dump(schedule, f, indent=4)

def view_schedule(schedule):
    print("\n  🗓️  Your Weekly Schedule:")
    empty = True
    for day in DAYS:
        if schedule[day]:
            empty = False
            print(f"\n     {day.upper()}:")
            # Sort classes by time
            sorted_classes = sorted(schedule[day], key=lambda x: x['time'])
            for cls in sorted_classes:
                print(f"       ⏰ {cls['time']} | 📚 {cls['subject']} | 🚪 Room: {cls['room']}")
    
    if empty:
        print("\n     Your schedule is empty. Enjoy the free time! 🌴")
    print("-" * 50)

def main():
    schedule = load_schedule()
    
    while True:
        view_schedule(schedule)
        print("\n  Options:")
        print("  1. ➕ Add a class")
        print("  2. 🗑️  Remove a class")
        print("  3. ❌ Exit")
        
        choice = input("\n  Enter choice (1-3): ").strip()
        
        if choice == "1":
            print("\n  Days:")
            for i, day in enumerate(DAYS, 1):
                print(f"  {i}. {day}")
                
            try:
                day_idx = int(input("\n  Select day (1-7): ")) - 1
                if 0 <= day_idx < 7:
                    day = DAYS[day_idx]
                    time_str = input("  Enter time (e.g., 09:00 AM): ").strip()
                    subject = input("  Enter subject: ").strip()
                    room = input("  Enter room/location: ").strip()
                    
                    if time_str and subject:
                        schedule[day].append({
                            "time": time_str,
                            "subject": subject,
                            "room": room if room else "TBA"
                        })
                        save_schedule(schedule)
                        print("  ✅ Class added to your schedule!")
                    else:
                        print("  Warning: Time and Subject are required.")
                else:
                    print("  Warning: Invalid day selection.")
            except ValueError:
                print("  Warning: Please enter a valid number.")
                
        elif choice == "2":
            print("\n  Days:")
            for i, day in enumerate(DAYS, 1):
                print(f"  {i}. {day}")
                
            try:
                day_idx = int(input("\n  Select day (1-7): ")) - 1
                if 0 <= day_idx < 7:
                    day = DAYS[day_idx]
                    classes = schedule[day]
                    
                    if not classes:
                        print(f"  No classes scheduled on {day}.")
                        continue
                        
                    print(f"\n  Classes on {day}:")
                    sorted_classes = sorted(classes, key=lambda x: x['time'])
                    for i, cls in enumerate(sorted_classes, 1):
                        print(f"  {i}. {cls['time']} - {cls['subject']}")
                        
                    cls_idx = int(input("\n  Select class to remove: ")) - 1
                    if 0 <= cls_idx < len(sorted_classes):
                        # Find the actual dictionary to remove since we sorted a copy
                        to_remove = sorted_classes[cls_idx]
                        schedule[day].remove(to_remove)
                        save_schedule(schedule)
                        print(f"  ✅ Removed {to_remove['subject']}.")
                    else:
                        print("  Warning: Invalid class selection.")
                else:
                    print("  Warning: Invalid day selection.")
            except ValueError:
                print("  Warning: Please enter a valid number.")
                
        elif choice == "3":
            print("\n  👋 Have a great semester!")
            break
            
        else:
            print("  Warning: Invalid choice. Try again.")

if __name__ == "__main__":
    main()
