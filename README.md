# Wordlist Autocomplete Plugin

This Obsidian plugin provides autocomplete suggestions from your `mega_wordlist.txt` file after typing exactly 3 letters.

## Features

- Triggers autocomplete after typing 3 or more letters
- Uses the `mega_wordlist.txt` file in your vault root
- Shows up to 10 matching suggestions
- Case-insensitive matching

## Installation

1. Copy the plugin files to your vault's `.obsidian/plugins/wordlist-autocomplete/` folder
2. Enable the plugin in Obsidian settings
3. Make sure your `mega_wordlist.txt` file is in the vault root

## Usage

Simply start typing any word with 3 or more letters, and the plugin will show matching suggestions from your wordlist. Use arrow keys to navigate and Enter to select a suggestion.

## Building

```bash
npm install
npm run build
```