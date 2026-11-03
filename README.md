# Awesome WSP — Research Timeline

Interactive research background for weight-space programming, covering 28 representative works from 1992 to 2026.

- Chinese version: https://awesome-wsp.github.io/
- English version: https://awesome-wsp.github.io/en.html
- Use the language button at the top of either page to switch versions.
- Resource library: https://github.com/brighterr/awesome-wsp
- Click a paper to see its method, relationship to WSP, and primary source.
- Dates use first public release, with conference years separately labeled.
- Categories indicate conceptual relationships, not proven direct influence or citations.

## Research update — 2026-11-03

The expanded view adds 12 works to the initial 16, marks additions with diamonds, and separates five conceptual routes. The latest addition is AdderBoard (2026), a community challenge with distinct trained and hand-coded tracks, explicitly discussed in the WSP report. See [RESEARCH_NOTES.md](RESEARCH_NOTES.md) for inclusion decisions and methodological caveats. The editable diagram source is [timeline.fragment.html](timeline.fragment.html).

## Hosting

GitHub Pages publishes the root of `main`. `index.html` is self-contained and can also be opened offline. No build step, analytics, API keys, or external script requests are needed.

`index.html` retains the Chinese diagram. `en.html` is a separate, self-contained English version with the same 28 works, dates, categories, and source links. Both pages use relative language links so switching also works offline when the files are kept together.

For translation maintenance, edit `translations.en.json` and run `python3 build_english.py`. This regenerates `timeline.en.fragment.html` and `en.html` from the Chinese source and export, while adding the language button without altering the Chinese diagram. All entries must have translations before the generator succeeds.

## Credits

Visualization powered by D3 7.9.0 (ISC license). The bundled distribution retains its copyright notice; see THIRD_PARTY_LICENSES.md. Paper titles and linked materials remain the property of their respective authors. This site is an independent literature guide, not an official site of the WSP report authors.
