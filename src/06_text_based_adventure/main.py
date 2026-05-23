import random
import time

# ─────────────────────────────────────────
#   UTILITIES
# ─────────────────────────────────────────

def slow_print(text, delay=0.03):
    """Print text character by character for dramatic effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def separator(char="─", length=55):
    print(char * length)

def pause():
    input("\n  [Press ENTER to continue...]\n")

# ─────────────────────────────────────────
#   PLAYER SETUP
# ─────────────────────────────────────────

def create_player():
    separator("═")
    slow_print("  ⚔️  WELCOME TO: THE LOST KINGDOM  ⚔️")
    slow_print("  A Text-Based Adventure Game")
    separator("═")
    print()
    name = input("  Enter your hero's name: ").strip() or "Hero"

    print("\n  Choose your class:")
    print("    1. 🗡️  Warrior  — High HP, decent attack")
    print("    2. 🔮  Mage     — Low HP, powerful magic")
    print("    3. 🏹  Ranger   — Balanced, high dodge chance")
    print()

    class_map = {
        "1": {"class": "Warrior", "emoji": "🗡️",  "hp": 120, "attack": 20, "dodge": 0.10},
        "2": {"class": "Mage",    "emoji": "🔮",  "hp": 70,  "attack": 35, "dodge": 0.15},
        "3": {"class": "Ranger",  "emoji": "🏹",  "hp": 90,  "attack": 25, "dodge": 0.25},
    }

    while True:
        choice = input("  Enter 1, 2, or 3: ").strip()
        if choice in class_map:
            stats = class_map[choice]
            break
        print("  ⚠️  Invalid choice. Please enter 1, 2, or 3.")

    player = {
        "name": name,
        "class": stats["class"],
        "emoji": stats["emoji"],
        "hp": stats["hp"],
        "max_hp": stats["hp"],
        "attack": stats["attack"],
        "dodge": stats["dodge"],
        "gold": 0,
        "potions": 2,
        "inventory": [],
        "xp": 0,
        "level": 1,
    }

    print(f"\n  ✅ Welcome, {player['name']} the {player['class']} {player['emoji']}!")
    print(f"  ❤️  HP: {player['hp']} | ⚔️  ATK: {player['attack']} | 🎯 Dodge: {int(player['dodge']*100)}%")
    pause()
    return player

# ─────────────────────────────────────────
#   COMBAT
# ─────────────────────────────────────────

def combat(player, enemy):
    separator()
    slow_print(f"  ⚠️  A wild {enemy['name']} {enemy['emoji']} appears!")
    slow_print(f"  👾 {enemy['name']} HP: {enemy['hp']} | ATK: {enemy['attack']}")
    separator()

    while player["hp"] > 0 and enemy["hp"] > 0:
        print(f"\n  ❤️  Your HP: {player['hp']} / {player['max_hp']}  |  👾 {enemy['name']} HP: {enemy['hp']}")
        print()
        print("  What do you do?")
        print("    1. ⚔️  Attack")
        print("    2. 🧪 Use Potion")
        print("    3. 🏃 Try to Flee")

        action = input("\n  Enter 1, 2, or 3: ").strip()

        if action == "1":
            # Player attacks
            dmg = random.randint(player["attack"] - 5, player["attack"] + 5)
            enemy["hp"] -= dmg
            slow_print(f"\n  ⚔️  You deal {dmg} damage to {enemy['name']}!")

            if enemy["hp"] <= 0:
                break

            # Enemy attacks back
            if random.random() < player["dodge"]:
                slow_print(f"  💨 You dodged the {enemy['name']}'s attack!")
            else:
                e_dmg = random.randint(enemy["attack"] - 3, enemy["attack"] + 3)
                player["hp"] -= e_dmg
                player["hp"] = max(0, player["hp"])
                slow_print(f"  💥 {enemy['name']} hits you for {e_dmg} damage!")

        elif action == "2":
            if player["potions"] > 0:
                heal = random.randint(25, 40)
                player["hp"] = min(player["hp"] + heal, player["max_hp"])
                player["potions"] -= 1
                slow_print(f"\n  🧪 You drink a potion and recover {heal} HP!")
                slow_print(f"  ❤️  HP is now: {player['hp']} | Potions left: {player['potions']}")
                # Enemy still attacks
                e_dmg = random.randint(enemy["attack"] - 3, enemy["attack"] + 3)
                player["hp"] -= e_dmg
                player["hp"] = max(0, player["hp"])
                slow_print(f"  💥 {enemy['name']} hits you for {e_dmg} damage while you were drinking!")
            else:
                slow_print("  ❌ You have no potions left!")

        elif action == "3":
            if random.random() < 0.4:
                slow_print("\n  🏃 You successfully fled from the battle!")
                return "fled"
            else:
                slow_print("\n  ❌ You couldn't escape!")
                e_dmg = random.randint(enemy["attack"] - 3, enemy["attack"] + 3)
                player["hp"] -= e_dmg
                player["hp"] = max(0, player["hp"])
                slow_print(f"  💥 {enemy['name']} hits you for {e_dmg} as you tried to flee!")
        else:
            print("  ⚠️  Invalid action. Enter 1, 2, or 3.")

    if player["hp"] <= 0:
        return "defeat"

    # Victory!
    gold_reward = enemy["gold"]
    xp_reward = enemy["xp"]
    player["gold"] += gold_reward
    player["xp"] += xp_reward

    slow_print(f"\n  🏆 You defeated {enemy['name']}!")
    slow_print(f"  💰 +{gold_reward} Gold  |  ⭐ +{xp_reward} XP")

    # Level up check
    if player["xp"] >= player["level"] * 50:
        player["level"] += 1
        player["attack"] += 5
        player["max_hp"] += 15
        player["hp"] = min(player["hp"] + 15, player["max_hp"])
        slow_print(f"\n  🌟 LEVEL UP! You are now Level {player['level']}!")
        slow_print(f"  ⚔️  Attack +5 | ❤️  Max HP +15")

    return "victory"

# ─────────────────────────────────────────
#   STORY ROOMS
# ─────────────────────────────────────────

def room_forest(player):
    separator("═")
    slow_print("  🌲 THE DARK FOREST")
    separator("═")
    slow_print("\n  You step into a dense, dark forest.")
    slow_print("  Strange sounds echo around you.")
    slow_print("  A goblin jumps out from behind a tree!\n")

    goblin = {"name": "Goblin", "emoji": "👺", "hp": 40, "attack": 10, "gold": 15, "xp": 20}
    result = combat(player, goblin)

    if result == "defeat":
        return False

    pause()

    slow_print("  Further in, you find an old chest.")
    slow_print("  You open it and find a rusty sword and 10 gold!")
    player["gold"] += 10
    player["inventory"].append("Rusty Sword")
    slow_print(f"  💰 Gold: {player['gold']} | 🎒 Inventory: {player['inventory']}")
    pause()
    return True

def room_cave(player):
    separator("═")
    slow_print("  🪨 THE DARK CAVE")
    separator("═")
    slow_print("\n  You enter a damp, dark cave.")
    slow_print("  Water drips from the ceiling.\n")
    slow_print("  You see two paths ahead:")
    print("    1. 🔦 The lit tunnel (safer-looking)")
    print("    2. 🌑 The dark tunnel (mysterious)")
    print()

    choice = input("  Which path do you take? (1 or 2): ").strip()

    if choice == "1":
        slow_print("\n  You follow the lit tunnel and find a merchant!")
        slow_print("  🧙 Merchant: 'Potions for sale! 20 gold each.'")

        if player["gold"] >= 20:
            buy = input("  Buy a potion? (yes/no): ").strip().lower()
            if buy in ["yes", "y"]:
                player["gold"] -= 20
                player["potions"] += 1
                slow_print(f"  ✅ You bought a potion! Potions: {player['potions']}")
        else:
            slow_print("  💸 You don't have enough gold to buy anything.")
        pause()

    else:
        slow_print("\n  You step into the dark tunnel... and trigger a trap!")
        trap_dmg = random.randint(15, 25)
        player["hp"] -= trap_dmg
        player["hp"] = max(0, player["hp"])
        slow_print(f"  💥 You take {trap_dmg} trap damage! HP: {player['hp']}")

        if player["hp"] <= 0:
            return False

        slow_print("  But you find a hidden treasure chest! +30 Gold 🎉")
        player["gold"] += 30
        pause()

    slow_print("  Deep in the cave, a TROLL blocks your path!\n")
    troll = {"name": "Cave Troll", "emoji": "👹", "hp": 80, "attack": 18, "gold": 30, "xp": 40}
    result = combat(player, troll)

    if result == "defeat":
        return False
    pause()
    return True

def room_castle(player):
    separator("═")
    slow_print("  🏰 THE DARK CASTLE")
    separator("═")
    slow_print("\n  You arrive at the ominous Dark Castle.")
    slow_print("  The drawbridge lowers before you...\n")
    slow_print("  Inside the throne room, the DARK LORD awaits!")
    slow_print("  '⚡ You dare challenge me?! Foolish hero!'\n")

    dark_lord = {"name": "Dark Lord", "emoji": "🧙‍♂️", "hp": 150, "attack": 28, "gold": 100, "xp": 100}
    result = combat(player, dark_lord)

    if result == "defeat":
        return False

    slow_print("\n  The Dark Lord collapses to the ground!")
    slow_print("  The castle begins to crumble...")
    slow_print("  You grab the legendary treasure and escape! 💎")
    player["gold"] += 50
    player["inventory"].append("Legendary Crown")
    pause()
    return True

# ─────────────────────────────────────────
#   MAIN GAME
# ─────────────────────────────────────────

def show_status(player):
    separator()
    print(f"  🦸 {player['name']} | {player['emoji']} {player['class']} | Lv.{player['level']}")
    print(f"  ❤️  HP: {player['hp']}/{player['max_hp']} | ⚔️  ATK: {player['attack']} | 💰 Gold: {player['gold']}")
    print(f"  🧪 Potions: {player['potions']} | ⭐ XP: {player['xp']} | 🎒 {player['inventory']}")
    separator()

def ending_screen(player, won):
    separator("═")
    if won:
        slow_print("  🎉 ✨ CONGRATULATIONS! ✨ 🎉", delay=0.05)
        slow_print(f"\n  {player['name']} has saved the kingdom!")
        slow_print("  Songs will be sung of your bravery for generations.")
    else:
        slow_print("  💀 GAME OVER 💀", delay=0.05)
        slow_print(f"\n  {player['name']} has fallen in battle...")
        slow_print("  The kingdom remains in darkness... for now.")

    print()
    show_status(player)
    separator("═")

def main():
    player = create_player()

    slow_print(f"\n  📖 STORY: The Dark Lord has stolen the Sacred Crown")
    slow_print("  and shrouded the kingdom in eternal darkness.")
    slow_print(f"  Only {player['name']} can stop him...")
    pause()

    rooms = [
        ("🌲 Dark Forest", room_forest),
        ("🪨 Dark Cave", room_cave),
        ("🏰 Dark Castle", room_castle),
    ]

    for room_name, room_func in rooms:
        show_status(player)
        slow_print(f"  📍 Next location: {room_name}")
        pause()

        success = room_func(player)

        if not success:
            ending_screen(player, won=False)
            return

    ending_screen(player, won=True)

main()
