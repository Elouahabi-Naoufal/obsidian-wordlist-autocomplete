# Wordlist Autocomplete Plugin

An Obsidian plugin that provides intelligent autocomplete suggestions from JSON wordlist files with domain and category metadata.

## Features

- **Smart Triggering**: Autocomplete after typing 3+ letters
- **JSON Wordlists**: Support for structured wordlist files with metadata
- **Contextual Learning**: Learns from your word choices and prioritizes based on context
- **Flexible Matching**: Prefix, shorthand (e.g., 'orcl' → 'Oracle'), and contains matching
- **Rich Metadata**: Display domain and category information for each suggestion
- **Customizable Ranking**: Sort by relevance, frequency, or alphabetically
- **Case Preservation**: Maintains your input case style

## Installation

### From Community Plugins (Recommended)
1. Open Obsidian Settings
2. Go to Community Plugins and disable Safe Mode
3. Browse and search for "Wordlist Autocomplete"
4. Install and enable the plugin

### Manual Installation
1. Download the latest release files (`main.js`, `manifest.json`, `styles.css`)
2. Create folder `VaultFolder/.obsidian/plugins/wordlist-autocomplete/`
3. Copy the files into this folder
4. Reload Obsidian and enable the plugin

## JSON Wordlist Format

```json
{
  "word": {
    "domain": "Technology",
    "category": "Programming",
    "frequency": 5
  },
  "example": {
    "domain": "General",
    "category": "Common",
    "frequency": 1
  }
}
```

## Usage

1. Configure wordlist folder in plugin settings
2. Enable desired JSON files
3. Start typing - suggestions appear after 3+ letters
4. Use Enter or Space to accept suggestions

## Complete Settings Guide

### Basic Settings
- **Minimum Letters to Trigger** (1-10): Number of characters needed before autocomplete appears
- **Dictionary Folder**: Select folder containing your JSON wordlist files
- **Enable Shorthand Matching**: Allow typing 'orcl' to match 'Oracle'
- **Preserve Case**: Match your input case style in suggestions
- **Enable Space to Accept**: Use Space key to accept suggestions (in addition to Enter)
- **Enable Personalized Suggestions**: Learn from your word choices and prioritize based on context

### Global Suggestion Order
Choose primary sorting method:
- **File Order**: Sort by the order files appear in settings
- **Category Order**: Sort by custom category priority within each file
- **Frequency**: Sort by word frequency (higher frequency first)
- **Alphabetical**: Sort suggestions alphabetically

### Dictionary File Management
- **Enable/Disable Files**: Toggle individual JSON files on/off
- **Drag & Drop Reordering**: Change file priority by dragging
- **Category Order**: Set custom priority for categories within each file
- **Enable All/Disable All**: Bulk toggle all dictionary files

### Advanced Features
- **File Correction Command**: Scan and correct misspelled words in current file
- **Text Transformation Commands**:
  - Convert to lowercase
  - Convert to uppercase
  - Capitalize first letter
  - Convert to sentence case
- **Contextual Learning**: Remembers word usage patterns and context
- **Match Types**: Supports prefix, shorthand, and contains matching
- **Rich Metadata Display**: Shows domain and category for each suggestion

## Creating Your Own Wordlists

### Step 1: Generate Words with ChatGPT

Use this prompt structure with ChatGPT:

```
Create a list of words for [DOMAIN] in the category [CATEGORY]. 
Format the output as:
-CATEGORY-
[frequency][word]
[frequency][word]
...

Example for Technology domain, Programming category:
-PROGRAMMING-
9algorithm
8function
7variable
6loop
5array
```

### Step 2: Collect Categories

1. Copy ChatGPT output to a `.txt` file
2. Generate multiple categories for your domain
3. Append all categories to the same file

### Step 3: Convert to JSON

Use this Python script to convert your `.txt` file to JSON:

```python
import json
import re

def convert_to_json(txt_file, domain_name):
    with open(txt_file, 'r') as f:
        content = f.read()
    
    result = {}
    current_category = ""
    
    for line in content.strip().split('\n'):
        line = line.strip()
        if line.startswith('-') and line.endswith('-'):
            current_category = line[1:-1]
        elif line and current_category:
            match = re.match(r'(\d+)(.+)', line)
            if match:
                frequency = int(match.group(1))
                word = match.group(2).strip()
                result[word] = {
                    "domain": domain_name,
                    "category": current_category,
                    "frequency": frequency
                }
    
    output_file = f"{domain_name.lower().replace(' ', '_')}.json"
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"Created {output_file} with {len(result)} words")

# Usage
convert_to_json("technology_words.txt", "Technology")
```

## Building from Source

```bash
npm install
npm run build
```

## License

MIT