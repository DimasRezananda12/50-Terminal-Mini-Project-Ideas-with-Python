import re
import os
import string

print("🔡 Welcome to the Word Counter!")
print("Analyze any text — type it in or load a file.")
print("-" * 52)

def analyze_text(text):
    """Return a full analysis dictionary for the given text."""
    # Basic counts
    char_total      = len(text)
    char_no_space   = len(text.replace(" ", "").replace("\n", "").replace("\t", ""))
    lines           = text.splitlines()
    line_count      = len(lines)
    paragraphs      = [p.strip() for p in re.split(r'\n\s*\n', text.strip()) if p.strip()]
    paragraph_count = len(paragraphs)

    # Words
    words = text.split()
    word_count = len(words)

    # Sentences (split on . ! ?)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)

    # Average words per sentence
    avg_words_per_sentence = word_count / sentence_count if sentence_count > 0 else 0

    # Unique words (case-insensitive, stripped of punctuation)
    clean_words = [w.strip(string.punctuation).lower() for w in words]
    clean_words = [w for w in clean_words if w]
    unique_words = set(clean_words)
    unique_word_count = len(unique_words)

    # Word frequency (top 10)
    freq = {}
    for w in clean_words:
        freq[w] = freq.get(w, 0) + 1

    # Filter out common stop words for "interesting" top words
    STOP_WORDS = {
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to",
        "for", "of", "with", "is", "was", "are", "were", "it", "this",
        "that", "be", "as", "by", "from", "not", "i", "you", "he",
        "she", "we", "they", "my", "your", "his", "her", "our", "its"
    }
    content_freq = {w: c for w, c in freq.items() if w not in STOP_WORDS}
    top_words = sorted(content_freq.items(), key=lambda x: x[1], reverse=True)[:10]

    # Longest and shortest word
    if clean_words:
        longest  = max(clean_words, key=len)
        shortest = min(clean_words, key=len)
    else:
        longest = shortest = "N/A"

    # Reading time estimate (avg 200 words per minute)
    read_min = word_count / 200
    read_sec = int((read_min % 1) * 60)
    read_min = int(read_min)

    return {
        "char_total": char_total,
        "char_no_space": char_no_space,
        "word_count": word_count,
        "unique_word_count": unique_word_count,
        "sentence_count": sentence_count,
        "line_count": line_count,
        "paragraph_count": paragraph_count,
        "avg_words_per_sentence": avg_words_per_sentence,
        "longest": longest,
        "shortest": shortest,
        "top_words": top_words,
        "read_min": read_min,
        "read_sec": read_sec,
    }

def display_results(stats):
    print("\n  " + "=" * 50)
    print("  📊 TEXT ANALYSIS RESULTS")
    print("  " + "=" * 50)
    print(f"  Characters (with spaces):   {stats['char_total']:>8,}")
    print(f"  Characters (no spaces):     {stats['char_no_space']:>8,}")
    print(f"  Words:                       {stats['word_count']:>7,}")
    print(f"  Unique words:                {stats['unique_word_count']:>7,}")
    print(f"  Sentences:                   {stats['sentence_count']:>7,}")
    print(f"  Lines:                       {stats['line_count']:>7,}")
    print(f"  Paragraphs:                  {stats['paragraph_count']:>7,}")
    print(f"  Avg words/sentence:          {stats['avg_words_per_sentence']:>7.1f}")
    print(f"  Longest word:           {stats['longest']:>13}")
    print(f"  Shortest word:          {stats['shortest']:>13}")
    print(f"  Est. reading time:      {stats['read_min']}m {stats['read_sec']}s")

    if stats["top_words"]:
        print("\n  🏆 Top 10 content words:")
        for i, (word, count) in enumerate(stats["top_words"], 1):
            bar = "█" * min(count, 20)
            print(f"  {i:>2}. {word:<20} {bar} ({count})")
    print("  " + "=" * 50)

# ── Main Loop ──
while True:
    print("\n  What do you want to analyze?")
    print("  1. 📝 Type or paste text")
    print("  2. 📂 Load from a .txt file")
    print("  3. ❌ Exit")

    choice = input("\n  Enter 1, 2, or 3: ").strip()

    if choice == "1":
        print("\n  Type/paste your text below.")
        print("  When done, type END on a new line and press Enter:\n")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        text = "\n".join(lines)

        if not text.strip():
            print("  Warning: No text entered.")
            continue

        stats = analyze_text(text)
        display_results(stats)

    elif choice == "2":
        filepath = input("  Enter file path (e.g. C:\\Users\\you\\file.txt): ").strip().strip('"')
        if not os.path.isfile(filepath):
            print(f"  Error: File not found: {filepath}")
            continue
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            print(f"  Loaded {len(text):,} characters from file.")
            stats = analyze_text(text)
            display_results(stats)
        except Exception as e:
            print(f"  Error reading file: {e}")

    elif choice == "3":
        break
    else:
        print("  Warning: Please enter 1, 2, or 3.")

print("\n  Goodbye! Thanks for using the Word Counter! 👋")
