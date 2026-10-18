import { Plugin, Editor, EditorSuggest, EditorPosition, TFile, EditorSuggestTriggerInfo, EditorSuggestContext } from 'obsidian';

interface WordSuggestion {
	word: string;
}

class WordlistSuggest extends EditorSuggest<WordSuggestion> {
	plugin: WordlistAutocompletePlugin;
	words: string[] = [];

	constructor(plugin: WordlistAutocompletePlugin) {
		super(plugin.app);
		this.plugin = plugin;
		this.loadWordlist();
	}

	async loadWordlist() {
		try {
			const file = this.plugin.app.vault.getAbstractFileByPath('mega_wordlist.txt');
			if (file instanceof TFile) {
				const content = await this.plugin.app.vault.read(file);
				this.words = content.split(/\r?\n/).filter(word => word.trim().length > 0);
			}
		} catch (error) {
			console.error('Failed to load wordlist:', error);
		}
	}

	onTrigger(cursor: EditorPosition, editor: Editor): EditorSuggestTriggerInfo | null {
		const line = editor.getLine(cursor.line);
		const beforeCursor = line.substring(0, cursor.ch);
		
		// Match word characters at the end of the line before cursor
		const match = beforeCursor.match(/\b(\w{3,})$/);
		
		if (match) {
			return {
				start: { line: cursor.line, ch: cursor.ch - match[1].length },
				end: cursor,
				query: match[1]
			};
		}
		
		return null;
	}

	getSuggestions(context: EditorSuggestContext): WordSuggestion[] {
		const query = context.query.toLowerCase();
		
		return this.words
			.filter(word => word.toLowerCase().startsWith(query))
			.slice(0, 10) // Limit to 10 suggestions
			.map(word => ({ word }));
	}

	renderSuggestion(suggestion: WordSuggestion, el: HTMLElement): void {
		el.createEl('div', { text: suggestion.word });
	}

	selectSuggestion(suggestion: WordSuggestion, evt: MouseEvent | KeyboardEvent): void {
		const { context } = this;
		if (context) {
			const editor = context.editor;
			editor.replaceRange(suggestion.word, context.start, context.end);
		}
	}
}

export default class WordlistAutocompletePlugin extends Plugin {
	suggestor: WordlistSuggest;

	async onload() {
		this.suggestor = new WordlistSuggest(this);
		this.registerEditorSuggest(this.suggestor);
	}

	onunload() {
		// Cleanup is handled automatically by Obsidian
	}
}