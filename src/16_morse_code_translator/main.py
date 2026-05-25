print("🆘 Welcome to the Morse Code Translator!")
print("Translate text to Morse code and vice versa.")
print("-" * 52)

# ── Morse Code Dictionary ──
TEXT_TO_MORSE = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.',
    'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',   'J': '.---',
    'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',   'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',  ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/',
}

MORSE_TO_TEXT = {v: k for k, v in TEXT_TO_MORSE.items()}

def text_to_morse(text):
    result = []
    for char in text.upper():
        if char in TEXT_TO_MORSE:
            result.append(TEXT_TO_MORSE[char])
        else:
            result.append('?')  # Unknown character
    return ' '.join(result)

def morse_to_text(morse):
    result = []
    words = morse.strip().split(' / ')
    for word in words:
        letters = word.strip().split()
        for symbol in letters:
            if symbol in MORSE_TO_TEXT:
                result.append(MORSE_TO_TEXT[symbol])
            else:
                result.append('?')
        result.append(' ')
    return ''.join(result).strip()

def validate_morse(morse):
    """Check if the input looks like morse code."""
    allowed = set('. - / ')
    return all(c in allowed for c in morse)

def display_morse_table():
    print("\n  📋 Morse Code Reference Table:")
    print("  " + "─" * 48)
    letters = [(k, v) for k, v in TEXT_TO_MORSE.items() if k.isalpha()]
    # Display in 4 columns
    for i in range(0, len(letters), 4):
        row = letters[i:i+4]
        line = "  ".join(f"  {k}: {v:<8}" for k, v in row)
        print(line)
    print()
    numbers = [(k, v) for k, v in TEXT_TO_MORSE.items() if k.isdigit()]
    print("  " + "  ".join(f"{k}: {v}" for k, v in numbers))
    print("  " + "─" * 48)

# ── Main Loop ──
while True:
    print("\n  What would you like to do?")
    print("  1. 🔤 Text  →  Morse Code")
    print("  2. 📡 Morse Code  →  Text")
    print("  3. 📋 Show Morse Reference Table")
    print("  4. ❌ Exit")

    choice = input("\n  Enter 1, 2, 3, or 4: ").strip()

    if choice == "1":
        text = input("\n  Enter text to translate: ")
        if not text.strip():
            print("  Warning: Please enter some text.")
            continue
        result = text_to_morse(text)
        print(f"\n  Input:  {text}")
        print(f"  Morse:  {result}")
        print("\n  Legend: letters separated by space, words by  /")

    elif choice == "2":
        print("\n  Enter Morse code (use . and -, separate letters")
        print("  with space, separate words with  /  ):")
        morse = input("  Morse: ").strip()
        if not morse:
            print("  Warning: Please enter some Morse code.")
            continue
        if not validate_morse(morse):
            print("  Warning: Invalid characters detected. Use only . - and /")
            continue
        result = morse_to_text(morse)
        print(f"\n  Morse: {morse}")
        print(f"  Text:  {result}")

    elif choice == "3":
        display_morse_table()

    elif choice == "4":
        break
    else:
        print("  Warning: Invalid choice. Please enter 1, 2, 3, or 4.")

print("\n  Goodbye! Thanks for using the Morse Code Translator! 👋")
