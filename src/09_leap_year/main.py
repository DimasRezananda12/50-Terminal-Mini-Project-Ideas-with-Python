print("🗓️  Welcome to the Leap Year Checker!")
print("Find out if any year is a leap year — and learn why!")
print("-" * 55)

def is_leap_year(year):
    """
    A year is a leap year if:
    - It is divisible by 4
    - EXCEPT if it is divisible by 100
    - UNLESS it is also divisible by 400
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def explain_leap_year(year):
    """Provide a step-by-step explanation of the leap year check."""
    print(f"\n  📋 Step-by-step check for {year}:")

    if year % 400 == 0:
        print(f"  ✅ {year} ÷ 400 = {year // 400} (no remainder) → Leap Year!")
    elif year % 100 == 0:
        print(f"  ✅ {year} ÷ 4 = {year // 4} (no remainder)")
        print(f"  ❌ {year} ÷ 100 = {year // 100} (no remainder) → NOT a Leap Year!")
    elif year % 4 == 0:
        print(f"  ✅ {year} ÷ 4 = {year // 4} (no remainder)")
        print(f"  ✅ {year} ÷ 100 ≠ 0 → Leap Year!")
    else:
        print(f"  ❌ {year} ÷ 4 has remainder {year % 4} → NOT a Leap Year!")

def days_in_year(year):
    return 366 if is_leap_year(year) else 365

def next_leap_year(year):
    """Find the next leap year after the given year."""
    y = year + 1
    while not is_leap_year(y):
        y += 1
    return y

def prev_leap_year(year):
    """Find the previous leap year before the given year."""
    y = year - 1
    while y > 0 and not is_leap_year(y):
        y -= 1
    return y if y > 0 else None

def leap_years_in_range(start, end):
    """Return all leap years between start and end (inclusive)."""
    return [y for y in range(start, end + 1) if is_leap_year(y)]

def show_fun_facts(year):
    """Show fun facts about the year."""
    print(f"\n  📅 Fun Facts about {year}:")
    print(f"  • Days in {year}: {days_in_year(year)}")

    if is_leap_year(year):
        print(f"  • February {year} has 29 days 🎉")
        print(f"  • People born on Feb 29, {year} are called 'Leaplings'! 🐸")
    else:
        print(f"  • February {year} has 28 days")

    prev = prev_leap_year(year)
    nxt = next_leap_year(year)
    if prev:
        print(f"  • Previous leap year: {prev}")
    print(f"  • Next leap year: {nxt}")

# ── Main App Loop ──
while True:
    print()
    print("  What would you like to do?")
    print("  1. 🔍 Check a single year")
    print("  2. 📆 Check a range of years")
    print("  3. 📖 Learn how leap years work")
    print("  4. ❌ Exit")
    print()

    choice = input("  Enter 1, 2, 3, or 4: ").strip()

    if choice == "1":
        # Single year check
        while True:
            try:
                year = int(input("\n  Enter a year (e.g. 2024): "))
                if year < 1:
                    print("  ⚠️  Please enter a positive year.")
                    continue
                break
            except ValueError:
                print("  ⚠️  Invalid input. Please enter a whole number.")

        print()
        if is_leap_year(year):
            print(f"  ✅ {year} IS a Leap Year! 🎉")
        else:
            print(f"  ❌ {year} is NOT a Leap Year.")

        explain_leap_year(year)
        show_fun_facts(year)

    elif choice == "2":
        # Range check
        while True:
            try:
                start = int(input("\n  Enter start year: "))
                end = int(input("  Enter end year: "))
                if start < 1 or end < 1:
                    print("  ⚠️  Years must be positive.")
                    continue
                if start > end:
                    print("  ⚠️  Start year must be less than or equal to end year.")
                    continue
                break
            except ValueError:
                print("  ⚠️  Invalid input. Please enter whole numbers.")

        leaps = leap_years_in_range(start, end)
        print(f"\n  📆 Leap years between {start} and {end}:")

        if leaps:
            # Display in rows of 8
            for i in range(0, len(leaps), 8):
                row = leaps[i:i + 8]
                print("  " + "  ".join(str(y) for y in row))
            print(f"\n  Total: {len(leaps)} leap year(s) found.")
        else:
            print("  None found in this range.")

    elif choice == "3":
        # Educational section
        print()
        print("  ─" * 28)
        print("  📖 HOW LEAP YEARS WORK")
        print("  ─" * 28)
        print("""
  The Earth takes approximately 365.25 days to orbit the Sun.
  To account for this extra 0.25 days, we add an extra day
  (February 29) every 4 years — this is a Leap Year.

  The Rules:
  ┌─────────────────────────────────────────────────────────┐
  │  1. If the year is divisible by 4   → Leap Year ✅      │
  │  2. BUT if also divisible by 100    → NOT Leap Year ❌  │
  │  3. UNLESS also divisible by 400   → Leap Year ✅       │
  └─────────────────────────────────────────────────────────┘

  Examples:
  • 2024 → ÷4 ✅, ÷100 ❌ → Leap Year ✅
  • 1900 → ÷4 ✅, ÷100 ✅, ÷400 ❌ → NOT a Leap Year ❌
  • 2000 → ÷4 ✅, ÷100 ✅, ÷400 ✅ → Leap Year ✅
  • 2023 → ÷4 ❌ → NOT a Leap Year ❌
        """)

    elif choice == "4":
        print("\n  👋 Thanks for using the Leap Year Checker! See you next time!")
        break

    else:
        print("  ⚠️  Invalid choice. Please enter 1, 2, 3, or 4.")
