import random

print("🫱 Welcome to Minigame Rock, Paper, Scissors!")
print("Do you want to quit? Type 'quit' anytime to exit the game.Otherwise,let's play the game!")
print("-" * 100)

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("\nEnter your choice (Rock, Paper, Scissors): ").lower()
    
    if user_choice == "quit":
        print("\n" + "=" * 40)
        print("FINAL SCORE")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing! See you next time. 👋")
        break 
        
    if user_choice not in options:
        print("Invalid choice! Please type Rock, Paper, or Scissors.")
        continue
        
    computer_choice = random.choice(options)
    
    print(f"🤖 Computer chose: {computer_choice.capitalize()}")
    
    if user_choice == computer_choice:
        print("Result: It's a Tie! 🤝")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("Result: You Win!")
        user_score += 1
    else:
        print("Result: Computer Wins!")
        computer_score += 1
        
    print(f"Current Score -> You: {user_score} | Computer: {computer_score}")