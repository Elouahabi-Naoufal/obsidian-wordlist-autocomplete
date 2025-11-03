with open('1000.txt', 'r') as f:
    words = set(f.read().split())

with open('unique_1000.txt', 'w') as f:
    f.write('\n'.join(sorted(words)))