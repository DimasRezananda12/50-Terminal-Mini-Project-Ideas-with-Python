import random
import datetime

print("🪐 Welcome to the Daily Horoscope!")
print("Discover what the stars have aligned for you today.")
print("-" * 50)

SIGNS = [
    {"name": "Capricorn", "emoji": "♑", "start": (12, 22), "end": (1, 19)},
    {"name": "Aquarius",  "emoji": "♒", "start": (1, 20),  "end": (2, 18)},
    {"name": "Pisces",    "emoji": "♓", "start": (2, 19),  "end": (3, 20)},
    {"name": "Aries",     "emoji": "♈", "start": (3, 21),  "end": (4, 19)},
    {"name": "Taurus",    "emoji": "♉", "start": (4, 20),  "end": (5, 20)},
    {"name": "Gemini",    "emoji": "♊", "start": (5, 21),  "end": (6, 20)},
    {"name": "Cancer",    "emoji": "♋", "start": (6, 21),  "end": (7, 22)},
    {"name": "Leo",       "emoji": "♌", "start": (7, 23),  "end": (8, 22)},
    {"name": "Virgo",     "emoji": "♍", "start": (8, 23),  "end": (9, 22)},
    {"name": "Libra",     "emoji": "♎", "start": (9, 23),  "end": (10, 22)},
    {"name": "Scorpio",   "emoji": "♏", "start": (10, 23), "end": (11, 21)},
    {"name": "Sagittarius","emoji": "♐", "start": (11, 22), "end": (12, 21)},
]

HOROSCOPES = [
    "Today is a great day to start that project you've been putting off. Energy is high!",
    "An unexpected encounter might bring a smile to your face today. Be open.",
    "Patience is key today. Take deep breaths and focus on what you can control.",
    "Your creativity is flowing. Write, draw, or simply brainstorm new ideas.",
    "A good day for financial planning. Look closely at your budget and future goals.",
    "Communication is highlighted. A heart-to-heart conversation will go well.",
    "You might feel a bit nostalgic. Reach out to an old friend to catch up.",
    "Focus on self-care today. Treat yourself to something you love.",
    "Hard work will pay off soon. Keep pushing forward and stay dedicated.",
    "A spontaneous decision might lead to a fun adventure today!",
    "Trust your intuition. It's guiding you in the right direction.",
    "Collaborating with others will bring success. Two heads are better than one."
]

def get_zodiac_sign(month, day):
    for sign in SIGNS:
        # Check if date falls within the sign's range
        start_m, start_d = sign["start"]
        end_m, end_d = sign["end"]
        
        if (month == start_m and day >= start_d) or (month == end_m and day <= end_d):
            return sign
            
        # Special case for Capricorn spanning two years
        if sign["name"] == "Capricorn":
            if (month == 12 and day >= 22) or (month == 1 and day <= 19):
                return sign
                
    return None

def get_daily_horoscope(sign_name):
    # Use current date + sign name as a seed so the horoscope stays the same for the whole day
    today_str = datetime.date.today().isoformat()
    seed_str = today_str + sign_name
    random.seed(seed_str)
    
    prediction = random.choice(HOROSCOPES)
    lucky_number = random.randint(1, 100)
    colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "White", "Black"]
    lucky_color = random.choice(colors)
    
    return prediction, lucky_number, lucky_color

def main():
    while True:
        try:
            print("\n  Enter your birth date to get your horoscope.")
            month = int(input("  Month (1-12): "))
            day = int(input("  Day (1-31): "))
            
            # Basic validation
            if not (1 <= month <= 12 and 1 <= day <= 31):
                print("  Warning: Invalid date. Try again.")
                continue
                
            sign = get_zodiac_sign(month, day)
            
            if sign:
                prediction, lucky_num, lucky_color = get_daily_horoscope(sign["name"])
                
                print(f"\n  ✨ Your Sign: {sign['name']} {sign['emoji']}")
                print("  " + "-" * 40)
                print(f"  🔮 Horoscope: {prediction}")
                print(f"  🍀 Lucky Number: {lucky_num}")
                print(f"  🎨 Lucky Color: {lucky_color}")
                print("  " + "-" * 40)
            else:
                print("  Warning: Could not determine sign. Check the date.")
                
            again = input("\n  Check another? (yes/no): ").strip().lower()
            if again not in ('y', 'yes'):
                break
                
        except ValueError:
            print("  Warning: Please enter valid numbers.")

    print("\n  May the stars guide you! 👋")

if __name__ == "__main__":
    main()
