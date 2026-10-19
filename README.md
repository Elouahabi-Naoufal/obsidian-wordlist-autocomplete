<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>




<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]




<!-- PROJECT TITLE BLOCK -->
<br />
<div align="center">
  <a href="https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete">
    <h3 align="center">Wordlist Autocomplete</h3>
  </a>

  <p align="center">
    An Obsidian plugin that suggests words from your own JSON wordlists, ranked by match quality
    and by what you have picked before.
    <br />
    <a href="https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete"><strong>Read the source »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete/issues">Report Bug</a>
    &middot;
    <a href="https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete/issues">Request Feature</a>
  </p>
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>




<!-- ABOUT THE PROJECT -->
## About The Project

Wordlist Autocomplete adds editor suggestions to Obsidian from wordlists you control. Point it at a
folder of JSON files, enable the ones you want, and every word you type brings up matches from all of
them at once — each labelled with the domain and category carried in the JSON.

It is deliberately generic. There is no bundled vocabulary and no bundled spelling dictionary: `data.json`
in this repository is an empty `{}` seed, and everything after that is yours. That makes it useful for
domain jargon, a house style guide, a personal glossary, or a controlled vocabulary for a project.

How matching works, in the order the code applies it:

| Match | Rule | Example |
|-------|------|---------|
| `prefix` | Word starts with what you typed | `orac` → `Oracle` |
| `shorthand` | Word with its vowels stripped, after the first letter, equals your input | `orcl` → `Oracle` |
| `contains` | Word contains your input anywhere | `base` → `Database` |

Suggestions are capped at 10 per keystroke and sorted by match type first, so prefix hits always sit above
`contains` hits. Within a match type the order comes from your settings, and every suggestion shows its
`domain` and `category` chips so you can tell which wordlist a hit came from.

Beyond the suggestion popup, the plugin registers five commands that act on the whole file:

* **Correct current file** — tokenizes the note, skips words already in the dictionary and words that look
  like ordinary grammatical variations (`-s`, `-ed`, `-ing`, `-tion`, …), then matches what is left against
  the wordlists by shorthand first and by Levenshtein distance ≤ 2 second. Candidates above 0.6 confidence
  appear in a modal with checkboxes; accepted ones are rewritten.
* **Convert file to lowercase / uppercase**, **Capitalize first letter**, **Convert to sentence case** —
  whole-file text transforms.

There is also optional personalization, off by default. When enabled, every accepted suggestion records the
word, the word before it and the word after it. Later, a word you have picked before is boosted 5× when the
preceding word matches and 1.5× when the following word matches. The history lives in
`.obsidian/plugins/wordlist-autocomplete/personalized-suggestions.json`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Obsidian][Obsidian.com]][Obsidian-url]
* [![TypeScript][TypeScript.com]][TypeScript-url]
* [![esbuild][esbuild.com]][esbuild-url]
* [![JavaScript][JavaScript.com]][JavaScript-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Obsidian 0.15.0 or later.
* At least one JSON wordlist in your vault (see [Usage](#usage)). There is no bundled wordlist.
* Node.js 18+ and npm, only if you intend to build from source.

### Installation

**From the community plugin registry** — this plugin is listed in Obsidian's community plugins, so the
normal path applies:

1. Open **Settings → Community plugins** and turn off Restricted mode if it is on.
2. Browse the list, or search for **Wordlist Autocomplete**.
3. Click **Install**, then **Enable**.

Obsidian downloads the released `main.js`, `manifest.json` and `styles.css` into
`<vault>/.obsidian/plugins/wordlist-autocomplete/`.

**Manual installation** — if you are testing a local build:

1. Copy `main.js`, `manifest.json` and `styles.css` into
   `<vault>/.obsidian/plugins/wordlist-autocomplete/` (create the folder if needed).
2. Reload Obsidian, then enable the plugin under **Settings → Community plugins**.

**Building from source** — note that this repository ships the esbuild bundle, not the TypeScript source:

```sh
git clone https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete.git
cd obsidian-wordlist-autocomplete
npm install
npm run build     # -> main.js
```

`npm run build` expects `main.ts`, `esbuild.config.mjs` and `version-bump.mjs`, none of which are in the
tree at the moment, so the build fails until those are restored. See the roadmap below.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Wordlist format

A wordlist is a flat JSON object. Keys are the words as you want them spelled in the note; values carry the
metadata used for display and ranking:

```json
{
  "Oracle": {
    "domain": "Technology",
    "category": "Databases",
    "frequency": 9
  },
  "SQLAlchemy": {
    "domain": "Technology",
    "category": "Databases",
    "frequency": 4
  },
  "conventional_commit": {
    "domain": "Git",
    "category": "Workflow",
    "frequency": 6
  }
}
```

Only `word` (the key) is required. Missing `frequency` defaults to `1`, and missing `domain`/`category`
render as empty chips.

### Getting started

1. Create a folder in your vault for wordlists, for example `Wordlists/`.
2. Drop one or more JSON files in it using the format above.
3. Open **Settings → Wordlist Autocomplete**, set **Dictionary folder** to that folder. The plugin scans
   every `.json` file in it and lists them, all disabled by default.
4. Toggle on the files you want. Drag the handle on the left of a row to change its priority.
5. Type three letters (or whatever your threshold is) in any note. Suggestions appear inline.

### Settings

| Setting | Type | Default | What it does |
|---------|------|---------|--------------|
| Minimum letters to trigger | Slider, 1–10 | 3 | Characters required before the popup opens |
| Enable shorthand matching | Toggle | on | Allow `orcl` → `Oracle` |
| Preserve case | Toggle | off | Insert the suggestion in the case style you were typing |
| Enable Space to accept | Toggle | off | Accept the highlighted suggestion with Space, not just Enter |
| Enable personalized suggestions | Toggle | off | Learn from accepted suggestions and boost them next time |
| Dictionary folder | Folder dropdown | — | Which vault folder to scan for JSON wordlists |
| Global suggestion order | Dropdown | File order | `File order`, `Category order`, `Frequency` or `Alphabetical` |

Per file you get an enable toggle and a **Category order** button that opens a modal for ranking the
categories inside that particular wordlist. **Enable All** / **Disable All** sit above the list.

### Ranking in practice

The comparator is strictly layered, so changing the global order only matters once the earlier layers tie:

1. Match type — `prefix`, then `shorthand`, then `contains`.
2. Personal score, when personalization is on.
3. Shorter word first.
4. Your chosen global order.
5. Alphabetical, as the final tiebreak.

Accepting a suggestion inserts the word **and a trailing space**, so typing `orac` then Enter gives you
`Oracle ` ready for the next word.

### Commands

Run these from the command palette with a note open:

| Command | Effect |
|---------|--------|
| Wordlist Autocomplete: Correct current file | Modal listing likely misspellings, apply selected fixes |
| Wordlist Autocomplete: Convert file to lowercase | Lowercase the whole note |
| Wordlist Autocomplete: Convert file to uppercase | Uppercase the whole note |
| Wordlist Autocomplete: Capitalize first letter | Sentence-cases the note |
| Wordlist Autocomplete: Convert to sentence case | Sentence-cases the note |

The correction pass is deliberately conservative: it skips exact matches, skips anything whose stem is in the
dictionary under a common English suffix, and requires confidence above 0.6 before offering a change.

### Building a wordlist

Any source works — an existing glossary, a `wordfreq` list, a glossary exported from a book. The compact
format that is easiest to generate by hand or by asking a model for a list is `[frequency][word]` per line
under `-CATEGORY-` headers:

```
-DATABASES-
9Oracle
7PostgreSQL
4SQLAlchemy
-GIT-
8commit
6rebase
```

A short converter turns that into the JSON the plugin expects:

```python
import json
import re

def convert_to_json(txt_file, domain_name):
    result, current_category = {}, ""
    with open(txt_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("-") and line.endswith("-"):
                current_category = line[1:-1]
            elif line and current_category:
                match = re.match(r"(\d+)(\w.*)", line)
                if match:
                    result[match.group(2)] = {
                        "domain": domain_name,
                        "category": current_category,
                        "frequency": int(match.group(1)),
                    }
    out = f"{domain_name.lower().replace(' ', '_')}.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"Created {out} with {len(result)} words")

convert_to_json("technology_words.txt", "Technology")
```

Put the resulting file in your wordlist folder, go back to the settings tab, and enable it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

Shipping in 1.0.0:

- [x] Editor suggestions from any number of enabled JSON wordlists
- [x] Three-tier matching: prefix, vowel-stripped shorthand, contains
- [x] Domain and category chips on every suggestion, drawn from the wordlist metadata
- [x] Configurable trigger length, shorthand toggle, case preservation, Space-to-accept
- [x] Per-file enable, drag reordering and per-file category priority
- [x] Optional personalization with preceding/following word context
- [x] File-wide correction pass with a review modal
- [x] Four file-wide case transformation commands
- [x] Listed in the Obsidian community plugin registry, manifest version 1.0.0 / minAppVersion 0.15.0

Known gaps in the current tree:

- [ ] The TypeScript source is not published — only the esbuild output `main.js` is committed, and
      `.gitignore` lists `main.js` while it is also shipped. `main.ts`, `esbuild.config.mjs` and
      `version-bump.mjs` referenced by `package.json` are missing, so `npm run build` and `npm run version`
      do not run.
- [ ] The **Capitalize first letter** command calls the same sentence-case function as
      **Convert to sentence case**, so it does not do what its name says.
- [ ] Personalized data is written through `vault.adapter` to an absolute
      `.obsidian/plugins/wordlist-autocomplete/` path, but `manifest.json` declares
      `isDesktopOnly: false`. On mobile that write fails and personalization silently resets.
- [ ] Accepted suggestions always append a trailing space; there is no setting to turn that off.
- [ ] No tests and no sample wordlist larger than the empty `data.json`.

See the [open issues](https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Releases are cut by bumping `manifest.json`, adding the entry to `versions.json`, tagging, and letting
Obsidian pick up the attached `main.js`, `manifest.json` and `styles.css`.

### Top contributors:

<a href="https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Elouahabi-Naoufal/obsidian-wordlist-autocomplete" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Naoufal Elouahabi - [LinkedIn](https://www.linkedin.com/in/elouahabi-naoufal/) - elouahabi-naoufal1@gmail.com

Project Link: [https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete](https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Obsidian](https://obsidian.md/) and the [sample plugin](https://github.com/obsidianmd/obsidian-sample-plugin)
* [esbuild](https://esbuild.github.io/)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Elouahabi-Naoufal/obsidian-wordlist-autocomplete.svg?style=for-the-badge
[contributors-url]: https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Elouahabi-Naoufal/obsidian-wordlist-autocomplete.svg?style=for-the-badge
[forks-url]: https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete/network/members
[stars-shield]: https://img.shields.io/github/stars/Elouahabi-Naoufal/obsidian-wordlist-autocomplete.svg?style=for-the-badge
[stars-url]: https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete/stargazers
[issues-shield]: https://img.shields.io/github/issues/Elouahabi-Naoufal/obsidian-wordlist-autocomplete.svg?style=for-the-badge
[issues-url]: https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete/issues
[license-shield]: https://img.shields.io/github/license/Elouahabi-Naoufal/obsidian-wordlist-autocomplete.svg?style=for-the-badge
[license-url]: https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/elouahabi-naoufal/
[Obsidian.com]: https://img.shields.io/badge/Obsidian-7C3AED?style=for-the-badge&logo=obsidian&logoColor=white
[Obsidian-url]: https://obsidian.md/
[TypeScript.com]: https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white
[TypeScript-url]: https://www.typescriptlang.org/
[esbuild.com]: https://img.shields.io/badge/esbuild-FFCF00?style=for-the-badge&logo=esbuild&logoColor=black
[esbuild-url]: https://esbuild.github.io/
[JavaScript.com]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[JavaScript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript