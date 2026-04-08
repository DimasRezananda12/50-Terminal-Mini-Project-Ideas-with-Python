import random

fortunes = [
    "Hari ini adalah hari keberuntunganmu!",
    "Sesuatu yang mengejutkan akan datang segera.",
    "Kerja kerasmu akan segera membuahkan hasil.",
    "Jangan takut untuk mencoba hal baru hari ini.",
    "Seseorang sedang memikirkan hal baik tentangmu."
]

fortune_today = random.choice(fortunes)

print("🥠 Membuka Fortune Cookie-mu...")
print(f"Pesan untukmu: {fortune_today}")