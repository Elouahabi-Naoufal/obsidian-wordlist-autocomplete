# Wordlist Autocomplete Plugin

This Obsidian plugin provides autocomplete suggestions from multiple .txt wordlist files after typing 3 or more letters.

## Features

- Triggers autocomplete after typing 3 or more letters (configurable)
- Supports multiple .txt wordlist files
- User-configurable file selection in settings
- Shows up to 10 matching suggestions
- Case-insensitive matching
- Automatic deduplication of words across files
- **Shorthand matching**: Type "orcl" to match "Oracle" (removes vowels except first letter)

## Installation

1. Copy the plugin files to your vault's `.obsidian/plugins/wordlist-autocomplete/` folder
2. Enable the plugin in Obsidian settings
3. Place your .txt wordlist files in the vault root
4. Configure which files to use in the plugin settings

## Configuration

1. Go to Settings → Community Plugins → Wordlist Autocomplete
2. Adjust the minimum letters trigger (1-10)
3. Add your wordlist filenames (one per line) in the "Wordlist files" setting

## Usage

Simply start typing any word with the configured number of letters, and the plugin will show matching suggestions from all selected wordlists. Use arrow keys to navigate and Enter to select a suggestion.

**Shorthand Examples:**
- Type "orcl" → suggests "Oracle"
- Type "mcrsft" → suggests "Microsoft" 
- Type "appl" → suggests "Apple"
- Type "dtbs" → suggests "Database"

## Building

```bash
npm install
npm run build
```