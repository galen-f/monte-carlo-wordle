# Answers are all possible wordle answer about 2000 words.
with open("./answers.txt") as f:
    ANSWERS = [w.strip().upper() for w in f if len(w.strip()) == 5]
    LETTER_COUNTS = {letter: 0 for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    for word in ANSWERS:
        for letter in set(word):
            LETTER_COUNTS[letter] += 1
    
    #Sort letter counts by values
    sorted_letter_counts = dict(sorted(LETTER_COUNTS.items(), key=lambda item: item[1], reverse=True))
    print(sorted_letter_counts)

    # Output the most common letter in each position [0-4] to a file
    with open("position_letter_counts.txt", "w") as out_file:
        for i in range(5):
            position_counts = {letter: 0 for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
            for word in ANSWERS:
                position_counts[word[i]] += 1
            sorted_position_counts = dict(sorted(position_counts.items(), key=lambda item: item[1], reverse=True))
            out_file.write(f"Position {i}: {sorted_position_counts}\n")