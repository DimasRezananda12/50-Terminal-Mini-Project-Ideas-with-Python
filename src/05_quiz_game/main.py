import random
import time

print("❓ Welcome to the Ultimate Quiz Game!")
print("Test your knowledge across different categories!")
print("-" * 55)

# Question bank organized by category
QUESTION_BANK = {
    "🌍 Geography": [
        {"q": "What is the largest country by area?", "options": ["A. USA", "B. China", "C. Russia", "D. Canada"], "answer": "C"},
        {"q": "Which country has the most natural lakes?", "options": ["A. USA", "B. Canada", "C. Finland", "D. Brazil"], "answer": "B"},
        {"q": "What is the capital of Australia?", "options": ["A. Sydney", "B. Melbourne", "C. Brisbane", "D. Canberra"], "answer": "D"},
        {"q": "Which continent is the driest on Earth?", "options": ["A. Africa", "B. Asia", "C. Antarctica", "D. Australia"], "answer": "C"},
    ],
    "🔬 Science": [
        {"q": "What is the powerhouse of the cell?", "options": ["A. Nucleus", "B. Ribosome", "C. Mitochondria", "D. Vacuole"], "answer": "C"},
        {"q": "What gas do humans exhale?", "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Helium"], "answer": "C"},
        {"q": "What is the hardest natural substance?", "options": ["A. Gold", "B. Iron", "C. Quartz", "D. Diamond"], "answer": "D"},
        {"q": "What planet has the most moons?", "options": ["A. Jupiter", "B. Saturn", "C. Uranus", "D. Neptune"], "answer": "B"},
    ],
    "📚 History": [
        {"q": "Who was the first president of the USA?", "options": ["A. Abraham Lincoln", "B. Thomas Jefferson", "C. George Washington", "D. John Adams"], "answer": "C"},
        {"q": "In which year did the Titanic sink?", "options": ["A. 1908", "B. 1910", "C. 1912", "D. 1915"], "answer": "C"},
        {"q": "Which ancient wonder was located in Egypt?", "options": ["A. Colosseum", "B. Great Pyramid of Giza", "C. Parthenon", "D. Stonehenge"], "answer": "B"},
        {"q": "Who invented the telephone?", "options": ["A. Thomas Edison", "B. Nikola Tesla", "C. Alexander Graham Bell", "D. Albert Einstein"], "answer": "C"},
    ],
    "🎬 Pop Culture": [
        {"q": "Which movie features the character 'Simba'?", "options": ["A. Bambi", "B. Jungle Book", "C. Tarzan", "D. The Lion King"], "answer": "D"},
        {"q": "What is the best-selling video game of all time?", "options": ["A. Tetris", "B. Minecraft", "C. GTA V", "D. Wii Sports"], "answer": "B"},
        {"q": "Which band sang 'Bohemian Rhapsody'?", "options": ["A. The Beatles", "B. Led Zeppelin", "C. Queen", "D. Pink Floyd"], "answer": "C"},
        {"q": "What color is the Twitter (X) bird logo (original)?", "options": ["A. Red", "B. Green", "C. Blue", "D. Black"], "answer": "C"},
    ],
}

def choose_category():
    categories = list(QUESTION_BANK.keys())
    print("\n📂 Choose a category:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    print(f"  {len(categories) + 1}. 🎲 Random Mix")

    while True:
        try:
            choice = int(input("\nEnter category number: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1], QUESTION_BANK[categories[choice - 1]]
            elif choice == len(categories) + 1:
                # Mix all questions
                all_q = []
                for q_list in QUESTION_BANK.values():
                    all_q.extend(q_list)
                return "🎲 Random Mix", all_q
            else:
                print("  ⚠️  Invalid choice. Please try again.")
        except ValueError:
            print("  ⚠️  Please enter a number.")

def ask_question(q_data, q_num, total):
    print(f"\n{'─' * 55}")
    print(f"  Question {q_num} of {total}")
    print(f"{'─' * 55}")
    print(f"\n  {q_data['q']}\n")
    for option in q_data["options"]:
        print(f"    {option}")
    print()

    while True:
        answer = input("  Your answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        print("  ⚠️  Please enter A, B, C, or D.")

def show_score_bar(score, total):
    filled = int((score / total) * 20)
    bar = "█" * filled + "░" * (20 - filled)
    percentage = int((score / total) * 100)
    print(f"\n  Progress: [{bar}] {percentage}%")

def get_grade(score, total):
    percentage = (score / total) * 100
    if percentage == 100:
        return "🏆 Perfect Score! You're a GENIUS!"
    elif percentage >= 80:
        return "🥇 Excellent! Outstanding performance!"
    elif percentage >= 60:
        return "🥈 Good job! Above average!"
    elif percentage >= 40:
        return "🥉 Not bad! Keep studying!"
    else:
        return "📚 Keep practicing! You'll do better next time!"

# --- Main Game Loop ---
play_again = True
while play_again:
    category_name, questions = choose_category()
    questions = random.sample(questions, min(5, len(questions)))  # pick 5 random questions
    total = len(questions)
    score = 0
    wrong_answers = []

    print(f"\n🎯 Category: {category_name}")
    print(f"📝 You will answer {total} questions. Let's begin!\n")
    time.sleep(1)

    for idx, q_data in enumerate(questions, 1):
        user_answer = ask_question(q_data, idx, total)

        if user_answer == q_data["answer"]:
            print("  ✅ Correct! Well done!")
            score += 1
        else:
            correct_option = next(opt for opt in q_data["options"] if opt.startswith(q_data["answer"]))
            print(f"  ❌ Wrong! The correct answer was: {correct_option}")
            wrong_answers.append({
                "question": q_data["q"],
                "your_answer": user_answer,
                "correct": correct_option
            })

        show_score_bar(score, total)
        time.sleep(0.5)

    # Final Results
    print(f"\n{'=' * 55}")
    print("  🏁 QUIZ COMPLETE!")
    print(f"{'=' * 55}")
    print(f"\n  Final Score: {score} / {total}")
    print(f"  {get_grade(score, total)}")

    if wrong_answers:
        print(f"\n  📋 Review — Questions you got wrong:")
        for wa in wrong_answers:
            print(f"\n    ❓ {wa['question']}")
            print(f"    Your answer: {wa['your_answer']} | Correct: {wa['correct']}")

    print()
    again = input("  🔄 Play again? (yes / no): ").strip().lower()
    if again not in ["yes", "y"]:
        play_again = False

print("\n  👋 Thanks for playing the Quiz Game! See you next time!")
