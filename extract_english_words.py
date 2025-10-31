#!/usr/bin/env python3

import re

def extract_english_words(input_file, output_file):
    """Extract English words from raw text file and write to new file without duplicates"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Extract words using regex (letters only, minimum 2 characters)
    words = re.findall(r'\b[a-zA-Z]{2,}\b', text)
    
    # Convert to lowercase and remove duplicates while preserving order
    seen = set()
    unique_words = []
    
    for word in words:
        word_lower = word.lower()
        if word_lower not in seen:
            seen.add(word_lower)
            unique_words.append(word_lower)
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in sorted(unique_words):
            f.write(word + '\n')
    
    print(f"Extracted {len(unique_words)} unique words from {input_file}")
    print(f"Words written to {output_file}")

if __name__ == "__main__":
    extract_english_words("raw.txt", "english_language.txt")