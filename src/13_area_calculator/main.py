import math

print("📐 Welcome to the Area Calculator!")
print("Calculate the area of various geometric shapes.")
print("-" * 50)

def area_circle(r):
    return math.pi * r ** 2

def area_rectangle(w, h):
    return w * h

def area_triangle(b, h):
    return 0.5 * b * h

def area_triangle_sss(a, b, c):
    """Heron's formula — area from 3 sides."""
    s = (a + b + c) / 2
    under = s * (s - a) * (s - b) * (s - c)
    if under < 0:
        return None
    return math.sqrt(under)

def area_square(s):
    return s ** 2

def area_trapezoid(a, b, h):
    return 0.5 * (a + b) * h

def area_ellipse(a, b):
    return math.pi * a * b

def area_parallelogram(b, h):
    return b * h

def area_rhombus(d1, d2):
    return 0.5 * d1 * d2

def area_sector(r, angle_deg):
    return math.pi * r ** 2 * (angle_deg / 360)

def get_float(prompt, positive=True):
    while True:
        try:
            val = float(input(f"  {prompt}: "))
            if positive and val <= 0:
                print("  Warning: Value must be greater than 0.")
                continue
            return val
        except ValueError:
            print("  Warning: Please enter a valid number.")

SHAPES = {
    "1": "Circle",
    "2": "Rectangle",
    "3": "Square",
    "4": "Triangle (base & height)",
    "5": "Triangle (3 sides — Heron's formula)",
    "6": "Trapezoid",
    "7": "Parallelogram",
    "8": "Ellipse",
    "9": "Rhombus (diagonals)",
    "10": "Sector (pie slice)",
}

while True:
    print("\n  Choose a shape:")
    for key, name in SHAPES.items():
        print(f"  {key:>2}. {name}")
    print("   0. Exit")

    choice = input("\n  Enter number: ").strip()

    if choice == "0":
        break

    if choice not in SHAPES:
        print("  Warning: Invalid choice. Please try again.")
        continue

    shape = SHAPES[choice]
    print(f"\n  Shape: {shape}")
    area = None

    if choice == "1":  # Circle
        r = get_float("Enter radius")
        area = area_circle(r)
        print(f"  Formula: π × r²  =  π × {r}²")

    elif choice == "2":  # Rectangle
        w = get_float("Enter width")
        h = get_float("Enter height")
        area = area_rectangle(w, h)
        print(f"  Formula: width × height  =  {w} × {h}")

    elif choice == "3":  # Square
        s = get_float("Enter side length")
        area = area_square(s)
        print(f"  Formula: side²  =  {s}²")

    elif choice == "4":  # Triangle base & height
        b = get_float("Enter base")
        h = get_float("Enter height")
        area = area_triangle(b, h)
        print(f"  Formula: ½ × base × height  =  ½ × {b} × {h}")

    elif choice == "5":  # Triangle 3 sides
        a = get_float("Enter side a")
        b = get_float("Enter side b")
        c = get_float("Enter side c")
        area = area_triangle_sss(a, b, c)
        if area is None:
            print("  Error: These side lengths do not form a valid triangle!")
            continue
        s = (a + b + c) / 2
        print(f"  Formula: Heron's: s={s:.4g}, sqrt(s(s-a)(s-b)(s-c))")

    elif choice == "6":  # Trapezoid
        a = get_float("Enter parallel side a")
        b = get_float("Enter parallel side b")
        h = get_float("Enter height")
        area = area_trapezoid(a, b, h)
        print(f"  Formula: ½ × (a + b) × h  =  ½ × ({a} + {b}) × {h}")

    elif choice == "7":  # Parallelogram
        b = get_float("Enter base")
        h = get_float("Enter height")
        area = area_parallelogram(b, h)
        print(f"  Formula: base × height  =  {b} × {h}")

    elif choice == "8":  # Ellipse
        a = get_float("Enter semi-major axis (a)")
        b = get_float("Enter semi-minor axis (b)")
        area = area_ellipse(a, b)
        print(f"  Formula: π × a × b  =  π × {a} × {b}")

    elif choice == "9":  # Rhombus
        d1 = get_float("Enter diagonal 1")
        d2 = get_float("Enter diagonal 2")
        area = area_rhombus(d1, d2)
        print(f"  Formula: ½ × d1 × d2  =  ½ × {d1} × {d2}")

    elif choice == "10":  # Sector
        r = get_float("Enter radius")
        angle = get_float("Enter angle in degrees (0-360)")
        area = area_sector(r, angle)
        print(f"  Formula: π × r² × (θ/360)  =  π × {r}² × ({angle}/360)")

    if area is not None:
        print(f"\n  Area = {area:.6g} square units")
        print(f"       ≈ {area:.2f} square units (rounded)")

print("\n  Goodbye! Thanks for using the Area Calculator!")
