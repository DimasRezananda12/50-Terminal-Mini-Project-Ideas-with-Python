print("🔐 Welcome to the Caesar Cipher!")
print("Encrypt and decrypt messages using the Caesar Cipher technique.")
print("-" * 60)
print()

# ── Info ──
INFO = """
  The Caesar Cipher is one of the oldest encryption techniques.
  It works by shifting each letter in the message by a fixed
  number of positions in the alphabet.

  Example (shift = 3):
    Plain:    A B C D E F ...
    Cipher:   D E F G H I ...

    'HELLO' → 'KHOOR'   (encrypt, shift +3)
    'KHOOR' → 'HELLO'   (decrypt, shift -3)

  Only letters are shifted; numbers and symbols stay the same.
"""

def caesar_cipher(text, shift, mode="encrypt"):
    """Encrypt or decrypt text using Caesar Cipher."""
    if mode == "decrypt":
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)  # Non-alpha chars unchanged
    return ''.join(result)

def brute_force(ciphertext):
    """Try all 25 possible shifts and display results."""
    print(f"\n  Brute-force decryption of: '{ciphertext}'")
    print(f"  {'─' * 55}")
    print(f"  {'Shift':<8} {'Decrypted Text'}")
    print(f"  {'─' * 55}")
    for shift in range(1, 26):
        decrypted = caesar_cipher(ciphertext, shift, mode="decrypt")
        print(f"  {shift:<8} {decrypted}")
    print(f"  {'─' * 55}")

def frequency_analysis(text):
    """Show letter frequency distribution of the text."""
    text_upper = text.upper()
    freq = {}
    total_letters = 0
    for char in text_upper:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
            total_letters += 1

    if total_letters == 0:
        print("  No letters found in text.")
        return

    print(f"\n  Letter frequency analysis ({total_letters} letters total):")
    print(f"  {'─' * 40}")
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_freq:
        bar = "█" * count
        pct = count / total_letters * 100
        print(f"  {letter}: {bar:<30} {count:>3} ({pct:>5.1f}%)")

    most_common = sorted_freq[0][0]
    # In English, 'E' is the most common letter
    # Likely shift = (most_common - 'E') % 26
    suggested_shift = (ord(most_common) - ord('E')) % 26
    print(f"\n  Most common letter: {most_common}")
    print(f"  If this is English text, the cipher shift is likely: {suggested_shift}")
    print(f"  (Based on 'E' being the most common English letter)")

# ── Main Loop ──
while True:
    print("  What would you like to do?")
    print("  1. 🔒 Encrypt a message")
    print("  2. 🔓 Decrypt a message")
    print("  3. 🔨 Brute-force decrypt (try all 25 shifts)")
    print("  4. 📊 Frequency analysis")
    print("  5. 📖 How does Caesar Cipher work?")
    print("  6. ❌ Exit")

    choice = input("\n  Enter 1–6: ").strip()

    if choice == "1":
        message = input("\n  Enter message to encrypt: ")
        if not message.strip():
            print("  Warning: Please enter a message.")
            continue
        while True:
            try:
                shift = int(input("  Enter shift (1–25): "))
                if 1 <= shift <= 25:
                    break
                print("  Warning: Shift must be between 1 and 25.")
            except ValueError:
                print("  Warning: Please enter a whole number.")

        encrypted = caesar_cipher(message, shift, "encrypt")
        print(f"\n  Original:  {message}")
        print(f"  Shift:     {shift}")
        print(f"  Encrypted: {encrypted}")

    elif choice == "2":
        message = input("\n  Enter message to decrypt: ")
        if not message.strip():
            print("  Warning: Please enter a message.")
            continue
        while True:
            try:
                shift = int(input("  Enter shift used to encrypt (1–25): "))
                if 1 <= shift <= 25:
                    break
                print("  Warning: Shift must be between 1 and 25.")
            except ValueError:
                print("  Warning: Please enter a whole number.")

        decrypted = caesar_cipher(message, shift, "decrypt")
        print(f"\n  Encrypted: {message}")
        print(f"  Shift:     {shift}")
        print(f"  Decrypted: {decrypted}")

    elif choice == "3":
        message = input("\n  Enter ciphertext to brute-force: ")
        if not message.strip():
            print("  Warning: Please enter a message.")
            continue
        brute_force(message)

    elif choice == "4":
        message = input("\n  Enter text to analyze: ")
        if not message.strip():
            print("  Warning: Please enter a message.")
            continue
        frequency_analysis(message)

    elif choice == "5":
        print(INFO)

    elif choice == "6":
        break
    else:
        print("  Warning: Please enter a number between 1 and 6.")

    print()

print("  Goodbye! Keep your secrets safe! 🔐")
