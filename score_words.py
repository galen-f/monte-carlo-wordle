# We'll score 5-letter words using the user's per-position letter values.
# To make this runnable now, I'm including a seed list of common, valid Wordle-guess words
# skewed toward strong letters. You can replace/extend `candidate_words` with your full word list
# to recompute instantly.

from collections import defaultdict
import ast

# Load positional values dynamically
pos_vals = []
with open("position_letter_counts.txt") as f:
    for line in f:
        if line.strip():
            # Each line looks like: Position 0: {'S': 366, ...}
            _, dict_str = line.split(":", 1)
            pos_vals.append(ast.literal_eval(dict_str.strip()))

def score_word(word: str) -> int:
    word = word.upper()
    if len(word) != 5: 
        return -1
    total = 0
    for i, ch in enumerate(word):
        total += pos_vals[i].get(ch, 0)
    return total

# Seed list of common valid guesses (heavily letter-frequency-biased).
with open("./guesses.txt") as f:
    candidate_words = [w.strip().upper() for w in f if len(w.strip()) == 5]

# Deduplicate and keep only alphabetic 5-letter words to be safe
cand = []
seen = set()
for w in candidate_words:
    w = w.upper()
    if len(w) == 5 and w.isalpha() and w not in seen:
        seen.add(w)
        cand.append(w)

scored = [(w, score_word(w)) for w in cand]
scored.sort(key=lambda x: x[1], reverse=True)


# # Print out all top ten scorers
# print(scored[:10])

vowels = ['A', 'E', 'I', 'O', 'U']
# Print only first 10 words with VOWEL_COUNT vowel(s)
count = 0
VOWEL_COUNT = 2
for word, score in scored:
    if sum(1 for ch in word if ch in vowels) == VOWEL_COUNT:
        print(word, score)
        count += 1
    if count >= 10:
        break
