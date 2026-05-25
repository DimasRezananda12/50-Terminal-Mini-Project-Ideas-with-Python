print("🚇 Welcome to the NYC MetroCard Calculator!")
print("Plan your NYC subway trips and find the best MetroCard deal.")
print("-" * 58)

# ── NYC MetroCard Pricing (as of 2024) ──
SINGLE_RIDE_FARE   = 2.90   # per swipe (pay-per-ride)
UNLIMITED_7_DAY    = 34.00  # 7-day unlimited pass
UNLIMITED_30_DAY   = 132.00 # 30-day unlimited pass
MIN_PURCHASE       = 5.50   # minimum initial purchase
BONUS_THRESHOLD    = 5.50   # purchases of $5.50+ get 5% bonus
BONUS_RATE         = 0.05   # 5% free bonus rides

def calc_bonus(amount):
    """Calculate bonus rides credit for an add-value purchase."""
    if amount >= BONUS_THRESHOLD:
        return round(amount * BONUS_RATE, 2)
    return 0.0

def rides_from_amount(amount):
    """How many rides can you get from a given dollar amount?"""
    bonus = calc_bonus(amount)
    total = amount + bonus
    return int(total // SINGLE_RIDE_FARE), round(total, 2)

def cost_for_rides(num_rides):
    """How much do you need to load to get exactly N rides?"""
    # We need: amount * (1 + bonus_rate) >= num_rides * fare
    # amount >= (num_rides * fare) / (1 + bonus_rate)
    needed = (num_rides * SINGLE_RIDE_FARE) / (1 + BONUS_RATE)
    # Round up to nearest cent
    import math
    needed = math.ceil(needed * 100) / 100
    return max(needed, MIN_PURCHASE)

def best_option(rides_per_day, days):
    """Compare pay-per-ride vs unlimited for a given usage."""
    total_rides = rides_per_day * days

    # Pay-per-ride cost
    ppr_cost = total_rides * SINGLE_RIDE_FARE

    # Unlimited options
    if days <= 7:
        unlim_cost_7  = UNLIMITED_7_DAY
        unlim_cost_30 = UNLIMITED_30_DAY
    elif days <= 30:
        weeks_needed = -(-days // 7)  # ceiling division
        unlim_cost_7  = weeks_needed * UNLIMITED_7_DAY
        unlim_cost_30 = UNLIMITED_30_DAY
    else:
        months_needed = -(-days // 30)
        unlim_cost_7  = -(-days // 7) * UNLIMITED_7_DAY
        unlim_cost_30 = months_needed * UNLIMITED_30_DAY

    return ppr_cost, unlim_cost_7, unlim_cost_30

def format_dollar(amount):
    return f"${amount:,.2f}"

# ── Main Loop ──
while True:
    print("\n  What would you like to calculate?")
    print("  1. 🎟️  How many rides from a loaded amount?")
    print("  2. 💵  How much to load for N rides?")
    print("  3. 📊  Pay-per-ride vs Unlimited — which is better?")
    print("  4. 🔁  Add-value bonus calculator")
    print("  5. ❌  Exit")

    choice = input("\n  Enter 1–5: ").strip()

    if choice == "1":
        while True:
            try:
                amount = float(input("\n  Amount to load ($): $"))
                if amount < MIN_PURCHASE:
                    print(f"  Warning: Minimum purchase is {format_dollar(MIN_PURCHASE)}.")
                    continue
                break
            except ValueError:
                print("  Warning: Please enter a valid dollar amount.")

        bonus = calc_bonus(amount)
        total = amount + bonus
        rides, total = rides_from_amount(amount)
        leftover = round(total - rides * SINGLE_RIDE_FARE, 2)

        print(f"\n  Amount loaded:      {format_dollar(amount)}")
        if bonus > 0:
            print(f"  5% bonus credit:  + {format_dollar(bonus)}")
            print(f"  Total credit:       {format_dollar(total)}")
        print(f"  Fare per ride:      {format_dollar(SINGLE_RIDE_FARE)}")
        print(f"  Rides you get:      {rides} rides")
        print(f"  Leftover balance:   {format_dollar(leftover)}")

    elif choice == "2":
        while True:
            try:
                rides = int(input("\n  Number of rides needed: "))
                if rides < 1:
                    print("  Warning: Please enter at least 1 ride.")
                    continue
                break
            except ValueError:
                print("  Warning: Please enter a whole number.")

        needed = cost_for_rides(rides)
        bonus = calc_bonus(needed)
        total = needed + bonus
        actual_rides = int(total // SINGLE_RIDE_FARE)

        print(f"\n  Rides needed:       {rides}")
        print(f"  Minimum to load:    {format_dollar(needed)}")
        if bonus > 0:
            print(f"  5% bonus credit:  + {format_dollar(bonus)}")
            print(f"  Total credit:       {format_dollar(total)}")
            print(f"  Actual rides:       {actual_rides} (may be slightly more due to bonus)")

    elif choice == "3":
        while True:
            try:
                rpd = float(input("\n  Avg rides per day: "))
                days = int(input("  Number of days: "))
                if rpd <= 0 or days <= 0:
                    print("  Warning: Values must be positive.")
                    continue
                break
            except ValueError:
                print("  Warning: Please enter valid numbers.")

        ppr, unlim7, unlim30 = best_option(rpd, days)
        total_rides = rpd * days

        print(f"\n  Planning for {total_rides:.0f} total rides over {days} day(s):")
        print(f"  {'─' * 45}")
        print(f"  Pay-per-ride:             {format_dollar(ppr)}")
        print(f"  7-Day Unlimited pass(es): {format_dollar(unlim7)}")
        print(f"  30-Day Unlimited pass:    {format_dollar(unlim30)}")
        print(f"  {'─' * 45}")

        best = min(ppr, unlim7, unlim30)
        if best == ppr:
            print(f"  Best option: Pay-per-ride! Save vs 7-day: {format_dollar(unlim7 - ppr)}")
        elif best == unlim7:
            print(f"  Best option: 7-Day Unlimited! Save vs pay-per-ride: {format_dollar(ppr - unlim7)}")
        else:
            print(f"  Best option: 30-Day Unlimited! Save vs pay-per-ride: {format_dollar(ppr - unlim30)}")

        # Break-even info
        breakeven_7  = UNLIMITED_7_DAY  / SINGLE_RIDE_FARE
        breakeven_30 = UNLIMITED_30_DAY / SINGLE_RIDE_FARE
        print(f"\n  Break-even points:")
        print(f"  7-Day pass pays off after:  {breakeven_7:.1f} rides")
        print(f"  30-Day pass pays off after: {breakeven_30:.1f} rides")

    elif choice == "4":
        while True:
            try:
                amount = float(input("\n  Amount to add ($): $"))
                if amount <= 0:
                    print("  Warning: Amount must be positive.")
                    continue
                break
            except ValueError:
                print("  Warning: Please enter a valid dollar amount.")

        bonus = calc_bonus(amount)
        total = amount + bonus
        print(f"\n  Amount added:     {format_dollar(amount)}")
        if bonus > 0:
            print(f"  5% bonus:       + {format_dollar(bonus)}")
            print(f"  Total credit:     {format_dollar(total)}")
            print(f"  Extra rides:      {int(bonus // SINGLE_RIDE_FARE)} free ride(s) from bonus")
        else:
            print(f"  No bonus (minimum {format_dollar(BONUS_THRESHOLD)} required for 5% bonus)")

    elif choice == "5":
        break
    else:
        print("  Warning: Please enter a number between 1 and 5.")

print("\n  Goodbye! Safe travels on the subway! 🚇")
