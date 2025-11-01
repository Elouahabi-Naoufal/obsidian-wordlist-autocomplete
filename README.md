# Wordlist Autocomplete Plugin

This Obsidian plugin provides autocomplete suggestions from JSON wordlist files with domain and category metadata.

## Features

- Triggers autocomplete after typing 3 or more letters
- Uses JSON files with domain and category metadata
- Shows up to 10 matching suggestions with metadata display
- Filter suggestions by domain or category
- Rank suggestions by relevance, frequency, or alphabetically
- Shorthand matching (e.g., 'orcl' matches 'Oracle')
- Case preservation

## Installation

1. Copy the plugin files to your vault's `.obsidian/plugins/wordlist-autocomplete/` folder
2. Enable the plugin in Obsidian settings
3. Select JSON wordlist files in plugin settings

## JSON Format

Wordlist files should be in JSON format:
```json
{
  "word": {
    "domain": "Domain Name",
    "category": "Category Name",
    "frequency": 1
  }
}
```

## Usage

Start typing any word with 3+ letters to see suggestions with domain and category metadata. Use filters in settings to narrow results by domain or category.

## Settings

- **Domain Filter**: Show only words from specific domains
- **Category Filter**: Show only words from specific categories  
- **Ranking Method**: Sort by relevance, frequency, or alphabetically
- **Shorthand Matching**: Enable vowel-removal matching
- **Case Preservation**: Match input case in suggestions

## Building

```bash
npm install
npm run build
```