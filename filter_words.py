import json

with open('unique_1000.txt', 'r') as f:
    words = [word.strip() for word in f if len(word.strip()) > 3]

words_json = {word: {"domain": "General", "category": "Common Words"} for word in words}

with open('filtered_1000.json', 'w') as f:
    json.dump(words_json, f, indent=2)