print("🏛️  Welcome to the Roman Numeral Converter!")
print("Convert between Roman numerals and integers.")
print("-" * 52)

# ── Conversion Tables ──
INT_TO_ROMAN = [
    (1000, 'M'),  (900, 'CM'), (500, 'D'),  (400, 'CD'),
    (100,  'C'),  (90,  'XC'), (50,  'L'),  (40,  'XL'),
    (10,   'X'),  (9,   'IX'), (5,   'V'),  (4,   'IV'),
    (1,    'I'),
]

ROMAN_VALUES = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def int_to_roman(num):
    """Convert integer (1–3999) to Roman numeral string."""
    result = ''
    for value, symbol in INT_TO_ROMAN:
        while num >= value:
            result += symbol
            num -= value
    return result

def roman_to_int(roman):
    """Convert Roman numeral string to integer."""
    roman = roman.upper().strip()
    result = 0
    prev = 0
    for char in reversed(roman):
        if char not in ROMAN_VALUES:
            return None  # invalid character
        curr = ROMAN_VALUES[char]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    return result

def is_valid_roman(roman):
    """Basic validation of Roman numeral string."""
    import re
    roman = roman.upper().strip()
    # Valid Roman numeral pattern (1–3999)
    pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    return bool(re.match(pattern, roman)) and len(roman) > 0

def show_breakdown(num, roman):
    """Show how the number is broken down into Roman symbols."""
    print(f"\n  Breakdown of {num}:")
    remaining = num
    parts = []
    for value, symbol in INT_TO_ROMAN:
        count = remaining // value
        if count > 0:
            parts.append(f"  {value:>5} × {count} = {symbol * count}")
            remaining -= value * count
    for p in parts:
        print(p)
    print(f"  {'─' * 20}")
    print(f"  Result: {roman}")

def range_table(start, end):
    """Print a table of Roman numerals for a range."""
    print(f"\n  {'Integer':<10} {'Roman':<15}")
    print("  " + "─" * 25)
    for n in range(start, end + 1):
        print(f"  {n:<10} {int_to_roman(n):<15}")

# ── Main Loop ──
while True:
    print("\n  What would you like to do?")
    print("  1. 🔢 Integer  →  Roman Numeral")
    print("  2. 🏛️  Roman Numeral  →  Integer")
    print("  3. 📋 Show a range table (e.g. 1–20)")
    print("  4. ❌ Exit")

    choice = input("\n  Enter 1, 2, 3, or 4: ").strip()

    if choice == "1":
        while True:
            try:
                num = int(input("\n  Enter an integer (1 – 3999): "))
                if 1 <= num <= 3999:
                    break
                print("  Warning: Please enter a number between 1 and 3999.")
            except ValueError:
                print("  Warning: Please enter a valid whole number.")
        roman = int_to_roman(num)
        print(f"\n  {num}  =  {roman}")
        show_breakdown(num, roman)

    elif choice == "2":
        roman_input = input("\n  Enter Roman numeral (e.g. XIV): ").strip().upper()
        if not roman_input:
            print("  Warning: Please enter a Roman numeral.")
            continue
        if not is_valid_roman(roman_input):
            print(f"  Warning: '{roman_input}' is not a valid Roman numeral (1–3999).")
            continue
        result = roman_to_int(roman_input)
        if result is None or result == 0:
            print("  Warning: Could not parse the Roman numeral.")
        else:
            print(f"\n  {roman_input}  =  {result}")
            # Show breakdown in reverse
            print(f"\n  Breakdown of {roman_input}:")
            prev = 0
            for char in reversed(roman_input):
                curr = ROMAN_VALUES[char]
                if curr < prev:
                    print(f"    {char} ({curr}) — subtracted (less than next)")
                else:
                    print(f"    {char} ({curr}) — added")
                prev = curr
            print(f"  Total: {result}")

    elif choice == "3":
        while True:
            try:
                start = int(input("\n  Start of range (min 1): "))
                end   = int(input("  End of range   (max 3999): "))
                if 1 <= start <= end <= 3999:
                    break
                print("  Warning: Invalid range. Start must be <= end, both between 1 and 3999.")
            except ValueError:
                print("  Warning: Please enter valid integers.")
        if end - start > 99:
            confirm = input(f"  This will print {end - start + 1} rows. Continue? (yes/no): ").strip().lower()
            if confirm not in ("yes", "y"):
                continue
        range_table(start, end)

    elif choice == "4":
        break
    else:
        print("  Warning: Invalid choice. Please enter 1, 2, 3, or 4.")

print("\n  Goodbye! Thanks for using the Roman Numeral Converter! 🏛️")
