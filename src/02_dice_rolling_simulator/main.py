import random

print("🎲 Welcome to the Dice Rolling Simulator! 🎲")

keep_playing = True

while keep_playing:
    
    print("\nRolling the dice...")
  
    dice_value = random.randint(1, 6)
    
    print(f"Result: {dice_value}")
 
    if dice_value == 6:
        print("🎉 Jackpot! You rolled the highest number!")
    elif dice_value == 1:
        print("😬 Ouch, a 1! Better luck next roll.")
    else:
        print("👍 Solid roll! It's okay!")

    user_choice = input("\nDo you want to roll again? (yes / no): ").lower()
   
    if user_choice == "yes" or user_choice == "y":
        print("Let's go again!")
        # The loop will naturally restart from the top
    elif user_choice == "no" or user_choice == "n":
        keep_playing = False
        print("Thanks for playing! See you next time! 👋")
    else:
        print("Invalid input. I will assume you want to quit. Goodbye!")
        keep_playing = False