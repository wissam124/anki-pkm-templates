# PKM SJ Anki templates

This repository contains the source and generated files for the PKM SJ Basic,
Cloze, Math, and Programming card templates. Each note type has one shared HTML
template pair and separate Minimal, Solarized, and Nord stylesheets.

## Generate the templates

Run the generator from the repository root:

```sh
python3 generate.py
```

It writes all copy-ready files to:

- `templates/` for Anki's Front Template and Back Template boxes.
- `styles/css/` for Anki's Styling box.

The generator uses only the Python standard library. To verify that committed
outputs still match their sources without changing files, run:

```sh
python3 generate.py --check
```

## Edit a template

Do not edit generated files directly; regeneration will overwrite them.

- Edit card HTML in `src/templates/`.
- Edit shared card behaviour in `src/templates/enhance.html`.
- Edit common layout in `src/styles/base.css`.
- Edit colours in `src/styles/themes/`.
- Edit note-type-specific rules in `src/styles/variants/`.

After making a change, run the generator and copy the relevant generated files
into Anki.

Run the regression checks with:

```sh
python3 -m unittest discover
```

## Files to copy into Anki

First copy the HTML pair for the note type:

| Note type | Front Template | Back Template |
| --- | --- | --- |
| Basic | `templates/pkm-sj-basic-front.html` | `templates/pkm-sj-basic-back.html` |
| Cloze | `templates/pkm-sj-cloze-front.html` | `templates/pkm-sj-cloze-back.html` |
| Math | `templates/pkm-sj-math-front.html` | `templates/pkm-sj-math-back.html` |
| Programming | `templates/pkm-sj-programming-front.html` | `templates/pkm-sj-programming-back.html` |

Then choose one stylesheet for that note type:

| Note type | Minimal | Solarized | Nord |
| --- | --- | --- | --- |
| Basic | `styles/css/pkm-sj-basic-minimal.css` | `styles/css/pkm-sj-basic-solarized.css` | `styles/css/pkm-sj-basic-nord.css` |
| Cloze | `styles/css/pkm-sj-cloze-minimal.css` | `styles/css/pkm-sj-cloze-solarized.css` | `styles/css/pkm-sj-cloze-nord.css` |
| Math | `styles/css/pkm-sj-math-minimal.css` | `styles/css/pkm-sj-math-solarized.css` | `styles/css/pkm-sj-math-nord.css` |
| Programming | `styles/css/pkm-sj-programming-minimal.css` | `styles/css/pkm-sj-programming-solarized.css` | `styles/css/pkm-sj-programming-nord.css` |

Changing theme requires replacing only the content of Anki's Styling box; the
front and back templates stay the same.

When installing or updating a note type:

1. Back up the existing Anki Front Template, Back Template, and Styling boxes.
2. Copy both HTML files and one stylesheet from the same repository revision.
3. Confirm the comment at the top of each generated file names the intended
   note type and theme, and that all three comments show the same build ID.
4. Preview both sides with ordinary text, wide content, tags, and night mode.

The expected note-type fields are:

- Basic: `Front`, `Back`, `Source`, and `Section` (`Back` is required).
- Cloze: `Text`, `Extra`, `Source`, and `Section`.
- Math: `Front`, `Back`, `Extra`, `Source`, and `Section` (`Back` is required).
- Programming: `Front`, `Back`, `Question Source Code`, `Answer Source Code`,
  `Source`, and `Section`. At least `Back` or `Answer Source Code` should be
  populated so the answer divider is not followed by an empty answer.

The generated HTML contains its complete JavaScript, and each generated
stylesheet is self-contained. Anki does not need access to the source directory
or to the generator. Nord uses Rubik when it is installed and otherwise falls
back to Inter or the platform sans-serif fonts; it does not reference external
font files.

The `{{edit:...}}` and `{{clickable:Tags}}` filters continue to require the
corresponding Anki add-ons on clients where those custom filters are used.

Programming source-code fields use the template's own code box. Org-exported
syntax-colour spans are preserved, while Org's source-container, `pre`, and
`code` backgrounds, spacing, fonts, and wrapping are normalized by the template.

The shared size defaults can be adjusted independently with
`--font-size-answer`, `--font-size-extra`, `--font-size-metadata`, and
`--font-size-code`. They default to the backward-compatible
`--font-size-small` value.

Fields preserve the natural size of wide content, including MathJax equations,
and provide horizontal scrolling when it does not fit within the card.
