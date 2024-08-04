from collections import Counter

# Define the minimum length and count of the subsets
min_length = 3
min_count = 3

# Load the file
with open('output.txt', 'r') as f:
    content = f.read()

# Split the content into individual characters
characters = content.split()

# Generate all possible subsets of characters with a length of at least min_length
subsets = [' '.join(characters[i:j]) for i in range(len(characters)) for j in range(i+min_length, len(characters)+1)]

# Count the number of occurrences of each subset
counter = Counter(subsets)

# Write the result into a new file
with open('pattern_stats.txt', 'w') as f:
    for subset, count in counter.items():
        if count >= min_count:
            f.write(f'{subset}: {count}\n')