from collections import Counter

# Read file
with open('output.txt', 'r') as f:
    content = f.read()

# Get characters
characters = content.split()

# Count characters
counter = Counter(characters)

# Get most common characters
most_common_characters = counter.most_common()

# Write to file
with open('stats.txt', 'w') as f:
    for character, count in most_common_characters:
        f.write(f'{character}: {count}\n')