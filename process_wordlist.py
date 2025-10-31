#!/usr/bin/env python3

import re
from pathlib import Path

def process_wordlist(file_path):
    """Process wordlist to split multi-word entries and add individual words at the end"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    single_words = []
    additional_words = set()
    
    for line in lines:
        # Check if line contains multiple words (spaces, hyphens, underscores)
        if ' ' in line or '-' in line or '_' in line:
            # Split into individual words
            words = re.split(r'[\s\-_]+', line)
            words = [w.strip() for w in words if w.strip()]
            
            if len(words) > 1:
                # Keep the first word in main list
                single_words.append(words[0])
                # Add remaining words to additional set
                for word in words[1:]:
                    if word.lower() not in ['the', 'and', 'or', 'of', 'in', 'on', 'at', 'to', 'for', 'with']:
                        additional_words.add(word)
            else:
                single_words.append(line)
        else:
            single_words.append(line)
    
    # Remove duplicates while preserving order
    seen = set()
    unique_single_words = []
    for word in single_words:
        if word.lower() not in seen:
            seen.add(word.lower())
            unique_single_words.append(word)
    
    # Add additional words at the end
    for word in sorted(additional_words):
        if word.lower() not in seen:
            unique_single_words.append(word)
    
    return unique_single_words

def main():
    # Process technologies_list.txt
    tech_file = Path("technologies_list.txt")
    if tech_file.exists():
        print(f"Processing {tech_file}...")
        processed = process_wordlist(tech_file)
        
        # Write back to file
        with open(tech_file, 'w', encoding='utf-8') as f:
            for word in processed:
                f.write(word + '\n')
        
        print(f"Processed {len(processed)} words")
    
    # Process other wordlist files
    for file_path in ["mega_wordlist.txt", "technologies_extended_list.txt", "documentation_words.txt"]:
        file_obj = Path(file_path)
        if file_obj.exists():
            print(f"Processing {file_path}...")
            processed = process_wordlist(file_obj)
            
            with open(file_obj, 'w', encoding='utf-8') as f:
                for word in processed:
                    f.write(word + '\n')
            
            print(f"Processed {len(processed)} words")

if __name__ == "__main__":
    main()