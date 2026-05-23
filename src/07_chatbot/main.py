import random
import time

print("🤖 Welcome to PyBot — Your Terminal Chatbot!")
print("Type 'quit' anytime to exit the chat.")
print("-" * 50)
print()

# Bot's name and personality
BOT_NAME = "PyBot"

# Response rules: keyword -> list of possible replies
RESPONSES = {
    # Greetings
    ("hello", "hi", "hey", "halo", "hei"): [
        "Hey there! 👋 How's it going?",
        "Hello! 😊 Great to see you!",
        "Hi! I'm PyBot, your friendly terminal companion!",
    ],
    # How are you
    ("how are you", "how r you", "how are u", "what's up", "sup", "apa kabar"): [
        "I'm doing great, thanks for asking! 😄 What about you?",
        "Feeling fantastic! Ready to chat anytime. 🚀",
        "All circuits running smoothly! 🤖",
    ],
    # Name
    ("your name", "who are you", "nama kamu", "siapa kamu"): [
        f"I'm {BOT_NAME}! A simple chatbot built with Python. 🐍",
        f"The name's {BOT_NAME}. Nice to meet you! 😊",
    ],
    # Age
    ("how old", "your age", "umur kamu", "berapa umur"): [
        "I was born the moment someone ran this script. So... just now? 😂",
        "Age is just a number, but I'd say I'm forever young! ✨",
    ],
    # Joke
    ("joke", "funny", "laugh", "lucu", "cerita lucu"): [
        "Why do programmers prefer dark mode? 🌑\nBecause light attracts bugs! 🐛",
        "Why did the programmer quit his job? ➡️\nBecause he didn't get arrays! 😂",
        "What's a computer's favorite snack? 🍪 Microchips!",
        "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads. 😅",
    ],
    # Python
    ("python", "coding", "programming", "code", "ngoding"): [
        "Python is awesome! 🐍 Simple, readable, and super powerful.",
        "Ah, Python! My favorite language. print('Hello World') is all you need to start! 😄",
        "Python devs be like: 'Why use 10 lines when 2 will do?' 🚀",
    ],
    # Weather
    ("weather", "cuaca", "rain", "sunny", "hujan"): [
        "I can't check the weather, but I hope it's sunny wherever you are! ☀️",
        "I'm just a chatbot, no weather API here 😅 — check your phone!",
    ],
    # Food
    ("food", "hungry", "eat", "makan", "lapar", "dinner", "lunch", "breakfast"): [
        "I don't eat, but if I could, I'd choose pizza! 🍕",
        "Sounds like it's snack time! 🍜 Go grab something yummy!",
        "My favorite food? Probably... data. 😂",
    ],
    # Thanks
    ("thank", "thanks", "terima kasih", "makasih", "thx"): [
        "You're welcome! 😊 Always happy to help.",
        "No problem at all! That's what I'm here for. 🤖",
        "Anytime! Feel free to chat more. 💬",
    ],
    # Bye
    ("bye", "goodbye", "see you", "sampai jumpa", "dadah", "ciao"): [
        "Goodbye! 👋 Come back anytime!",
        "See you later! It was great chatting with you. 😊",
        "Bye-bye! Take care! 🌟",
    ],
    # Love
    ("love", "i love you", "cinta", "suka"): [
        "Aww, that's sweet! 💕 I like you too (in a very robot-y way 🤖).",
        "Love? A strong word for a terminal session! But I appreciate it 😄",
    ],
    # Help
    ("help", "bantuan", "what can you do"): [
        "I can chat, tell jokes, talk about Python, and more!\nJust type naturally and I'll do my best to respond. 😊",
    ],
    # Music
    ("music", "song", "lagu", "musik"): [
        "I can't hear music, but I imagine I'd love lo-fi beats while coding! 🎧",
        "Beep boop... that's my kind of music! 🎵",
    ],
    # Bored
    ("bored", "boring", "bosan", "jenuh"): [
        "Then let's chat! 😄 Ask me a joke, or tell me something fun!",
        "Boredom? Never heard of it! Let's talk Python 🐍 or tell you a joke!",
    ],
}

# Fallback responses when nothing matches
FALLBACKS = [
    "Hmm, I'm not sure I understand that. 🤔 Can you rephrase?",
    "Interesting! Tell me more. 💬",
    "I'm still learning! That one's a bit above my pay grade 😅",
    "Ooh, I don't know about that one. Maybe ask Google? 🔍",
    "My circuits are confused 🤖 — try asking something else!",
]

def get_response(user_input):
    user_input_lower = user_input.lower()
    for keywords, replies in RESPONSES.items():
        if any(kw in user_input_lower for kw in keywords):
            return random.choice(replies)
    return random.choice(FALLBACKS)

def typing_effect(text, delay=0.03):
    """Simulate bot 'typing' before responding."""
    print(f"  {BOT_NAME} is typing", end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()
    print(f"  🤖 {BOT_NAME}: {text}")

# ── Main Chat Loop ──
while True:
    try:
        user_input = input("\n  You: ").strip()
    except EOFError:
        break

    if not user_input:
        print(f"  🤖 {BOT_NAME}: Say something! I'm all ears (well, all code). 👂")
        continue

    if user_input.lower() in ("quit", "exit", "q"):
        typing_effect("It was great talking to you! Goodbye! 👋")
        break

    response = get_response(user_input)
    typing_effect(response)
