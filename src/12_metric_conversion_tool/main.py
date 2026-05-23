import math

print("📏 Welcome to the Metric Conversion Tool!")
print("Convert between common units of measurement.")
print("-" * 52)

CATEGORIES = {
    "Length": {
        "base": "meter",
        "units": {"kilometer": 1000, "meter": 1, "centimeter": 0.01, "millimeter": 0.001,
                  "mile": 1609.344, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254}
    },
    "Weight": {
        "base": "kilogram",
        "units": {"tonne": 1000, "kilogram": 1, "gram": 0.001, "milligram": 0.000001,
                  "pound": 0.453592, "ounce": 0.0283495}
    },
    "Temperature": {
        "base": "special",
        "units": {"celsius": None, "fahrenheit": None, "kelvin": None}
    },
    "Volume": {
        "base": "liter",
        "units": {"cubic meter": 1000, "liter": 1, "milliliter": 0.001,
                  "gallon (US)": 3.78541, "pint (US)": 0.473176, "fluid ounce": 0.0295735}
    },
    "Speed": {
        "base": "m/s",
        "units": {"m/s": 1, "km/h": 1/3.6, "mph": 0.44704, "knot": 0.514444}
    },
}

def convert_temp(value, from_u, to_u):
    if from_u == "celsius":
        c = value
    elif from_u == "fahrenheit":
        c = (value - 32) * 5 / 9
    else:
        c = value - 273.15
    if to_u == "celsius":
        return c
    elif to_u == "fahrenheit":
        return c * 9 / 5 + 32
    else:
        return c + 273.15

def convert(value, from_u, to_u, cat):
    if cat["base"] == "special":
        return convert_temp(value, from_u, to_u)
    return value * cat["units"][from_u] / cat["units"][to_u]

while True:
    print("\n  Choose a category:")
    cats = list(CATEGORIES.keys())
    for i, c in enumerate(cats, 1):
        print(f"  {i}. {c}")
    print("  0. Exit")

    try:
        ch = int(input("\n  Enter number: "))
    except ValueError:
        print("  Warning: Please enter a number.")
        continue

    if ch == 0:
        break
    if not (1 <= ch <= len(cats)):
        print("  Warning: Invalid choice.")
        continue

    cat_name = cats[ch - 1]
    cat_data = CATEGORIES[cat_name]
    units = list(cat_data["units"].keys())

    print(f"\n  Category: {cat_name}")
    print("  From unit:")
    for i, u in enumerate(units, 1):
        print(f"    {i}. {u}")

    while True:
        try:
            fi = int(input("  Select (number): ")) - 1
            if 0 <= fi < len(units):
                break
        except ValueError:
            pass
        print("  Warning: Invalid choice.")
    from_unit = units[fi]

    print(f"  To unit:")
    for i, u in enumerate(units, 1):
        print(f"    {i}. {u}")

    while True:
        try:
            ti = int(input("  Select (number): ")) - 1
            if 0 <= ti < len(units):
                break
        except ValueError:
            pass
        print("  Warning: Invalid choice.")
    to_unit = units[ti]

    while True:
        try:
            value = float(input(f"\n  Enter value in {from_unit}: "))
            break
        except ValueError:
            print("  Warning: Please enter a valid number.")

    result = convert(value, from_unit, to_unit, cat_data)
    print(f"\n  Result: {value:,.6g} {from_unit} = {result:,.6g} {to_unit}")

    show_all = input("  Show all conversions? (yes / no): ").strip().lower()
    if show_all in ("yes", "y"):
        for u in units:
            if u == from_unit:
                continue
            r = convert(value, from_unit, u, cat_data)
            print(f"    -> {r:,.6g} {u}")

print("\n  Goodbye! Thanks for using the Metric Conversion Tool!")
