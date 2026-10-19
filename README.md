<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
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
    <a href="https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete"><strong>Explore the source »</strong></a>
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
is an empty `{}` seed, and everything after that is yours. That makes it useful for domain jargon, a house
style guide, a personal glossary, or a controlled vocabulary for a project.

Matching works in three tiers, in this order:

| Match | Rule | Example |
|-------|------|---------|
| `prefix` | Word starts with what you typed | `orac` → `Oracle` |
| `shorthand` | Word with its vowels stripped, after the first letter, equals your input | `orcl` → `Oracle` |
| `contains` | Word contains your input anywhere | `base` → `Database` |

Suggestions are capped at 10 per keystroke. Ordering is layered: match type first, then the personal
score when learning is enabled, then shorter words, then your chosen global order, then alphabetical.
Every suggestion shows its `domain` and `category` chips so you can tell which wordlist a hit came from.

Beyond the popup, the plugin registers five commands:

* **Correct current file** — tokenizes the note, skips exact dictionary matches and common grammatical
  variations (`-s`, `-ed`, `-ing`, `-tion`, …), then tries shorthand matching and Levenshtein distance
  ≤ 2. Candidates above 0.6 confidence appear in a modal with checkboxes; accepted ones are rewritten.
* **Convert file to lowercase / uppercase**, **Capitalize first letter**, **Convert to sentence case** —
  whole-file text transforms.

Optional personalization is off by default. When enabled, every accepted suggestion records the word, the
word before it and the word after it. A word you have picked before is boosted when the surrounding
context matches. The history lives in
`.obsidian/plugins/wordlist-autocomplete/personalized-suggestions.json`.

Accepting a suggestion inserts the word **and a trailing space**; with **Preserve case** enabled, the
inserted word follows the case style you were typing.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Obsidian][Obsidian.com]][Obsidian-url]
* [![JavaScript][JavaScript.com]][JavaScript-url]
* [![TypeScript][TypeScript.com]][TypeScript-url]
* [![esbuild][esbuild.com]][esbuild-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Obsidian 0.15.0 or newer.
* At least one JSON wordlist in your vault (see [Usage](#usage)). There is no bundled wordlist.
* Node.js and npm only if you intend to work on the bundle.

### Installation

**From a release**

1. Download `main.js`, `manifest.json` and `styles.css` from the latest GitHub release.
2. Create `<vault>/.obsidian/plugins/wordlist-autocomplete/`.
3. Copy the files into that folder.
4. Reload Obsidian, then enable **Wordlist Autocomplete** under **Settings → Community plugins**.

**From source**

```sh
git clone https://github.com/Elouahabi-Naoufal/obsidian-wordlist-autocomplete.git
cd obsidian-wordlist-autocomplete
```

`main.js` is the shipped esbuild bundle and is what Obsidian loads. Copy it, `manifest.json` and
`styles.css` into the plugin folder. The repository currently does **not** contain the esbuild config or
version-bump script referenced by `package.json`, and `main.ts` is an older, much smaller prototype that
uses a single `mega_wordlist.txt` file — it is not the source of the shipped `main.js`. Consequently
`npm run build` will not reproduce the bundle until the original build files are restored.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Wordlist format

A wordlist is a flat JSON object. Keys are the words as you want them spelled in the note; values carry
the metadata used for display and ranking:

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

Only the key is required. Missing `frequency` defaults to `1`, and missing `domain`/`category` render as
empty chips.

### Getting started

1. Create a folder in your vault for wordlists, for example `Wordlists/`.
2. Drop one or more JSON files in it using the format above.
3. Open **Settings → Wordlist Autocomplete**, set **Dictionary folder** to that folder. The plugin scans
   every `.json` file in it and lists them, all disabled by default.
4. Toggle on the files you want. Drag the handle on the left of a row to change its priority.
5. Type the minimum number of letters in any note. Suggestions appear inline.

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

### Commands

| Command | Effect |
|---------|--------|
| Wordlist Autocomplete: Correct current file | Modal listing likely misspellings; apply selected fixes |
| Wordlist Autocomplete: Convert file to lowercase | Lowercase the whole note |
| Wordlist Autocomplete: Convert file to uppercase | Uppercase the whole note |
| Wordlist Autocomplete: Capitalize first letter | Sentence-cases the note |
| Wordlist Autocomplete: Convert to sentence case | Sentence-cases the note |

The correction pass is deliberately conservative: it skips exact matches, skips anything whose stem is in
the dictionary under a common suffix, and requires confidence above 0.6 before offering a change.

### Building a wordlist

Any source works — an existing glossary, a frequency list, or a list exported from a book. One compact
format that is easy to generate by hand is `[frequency][word]` per line under `-CATEGORY-` headers:

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

Working today:

- [x] Editor suggestions from any number of enabled JSON wordlists
- [x] Three-tier matching: prefix, vowel-stripped shorthand, contains
- [x] Domain and category chips on every suggestion
- [x] Configurable trigger length, shorthand toggle, case preservation, Space-to-accept
- [x] Per-file enable, drag reordering and per-file category priority
- [x] Optional personalization with preceding/following word context
- [x] File-wide correction pass with a review modal
- [x] Four file-wide case transformation commands

Known gaps:

- [ ] The original build inputs are missing: `package.json` references `esbuild.config.mjs` and
      `version-bump.mjs`, but neither is in the repository, so `npm run build` and `npm run version` fail
- [ ] `main.ts` is a stale prototype and does not match the shipped `main.js`
- [ ] **Capitalize first letter** calls the same sentence-case function as **Convert to sentence case**,
      so it does not do what its name says
- [ ] Personalized data is written through `vault.adapter` to an absolute `.obsidian/plugins/...` path,
      while `manifest.json` declares `isDesktopOnly: false`; on mobile that write fails
- [ ] Accepted suggestions always append a trailing space; there is no setting to turn that off
- [ ] No tests and no sample wordlist larger than the empty `data.json`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create.
Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You
can also simply open an issue with the tag "enhancement". Don't forget to give the project a star!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

The most useful first contribution is restoring the missing build setup so `main.js` can be regenerated
from TypeScript. Releases are cut by bumping `manifest.json`, adding the entry to `versions.json`, tagging,
and attaching `main.js`, `manifest.json` and `styles.css` to the release.

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

* [Obsidian](https://obsidian.md/) and the [Obsidian sample plugin](https://github.com/obsidianmd/obsidian-sample-plugin)
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
[JavaScript.com]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[JavaScript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[TypeScript.com]: https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white
[TypeScript-url]: https://www.typescriptlang.org/
[esbuild.com]: https://img.shields.io/badge/esbuild-FFCF00?style=for-the-badge&logo=esbuild&logoColor=black
[esbuild-url]: https://esbuild.github.io/
