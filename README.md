# PKM SJ Anki templates

This directory contains the source and generated files for the PKM SJ Basic,
Cloze, Math, and Programming card templates.

## Generate the templates

Run the generator from the repository root:

```sh
python3 pkm-sj/generate.py
```

It writes all copy-ready files to:

- `pkm-sj/templates/` for Anki's Front Template and Back Template boxes.
- `pkm-sj/styles/css/` for Anki's Styling box.

The generator uses only the Python standard library. To verify that committed
outputs still match their sources without changing files, run:

```sh
python3 pkm-sj/generate.py --check
```

## Edit a template

Do not edit generated files directly; regeneration will overwrite them.

- Edit card HTML in `pkm-sj/src/templates/`.
- Edit shared card behaviour in `pkm-sj/src/templates/enhance.html`.
- Edit common layout in `pkm-sj/src/styles/base.css`.
- Edit colours in `pkm-sj/src/styles/themes/`.
- Edit note-type-specific rules in `pkm-sj/src/styles/variants/`.

After making a change, run the generator and copy the relevant generated files
into Anki.

## Files to copy into Anki

| Note type | Front Template | Back Template | Styling |
| --- | --- | --- | --- |
| Basic | `templates/pkm-sj-basic-front.html` | `templates/pkm-sj-basic-back.html` | `styles/css/pkm-sj-basic.css` |
| Basic Solarized | `templates/pkm-sj-basic-solarized-front.html` | `templates/pkm-sj-basic-solarized-back.html` | `styles/css/pkm-sj-basic-solarized.css` |
| Cloze | `templates/pkm-sj-cloze-front.html` | `templates/pkm-sj-cloze-back.html` | `styles/css/pkm-sj-cloze.css` |
| Cloze Solarized | `templates/pkm-sj-cloze-solarized-front.html` | `templates/pkm-sj-cloze-solarized-back.html` | `styles/css/pkm-sj-cloze-solarized.css` |
| Math | `templates/pkm-sj-math-front.html` | `templates/pkm-sj-math-back.html` | `styles/css/pkm-sj-math.css` |
| Math Solarized | `templates/pkm-sj-math-solarized-front.html` | `templates/pkm-sj-math-solarized-back.html` | `styles/css/pkm-sj-math-solarized.css` |
| Programming | `templates/pkm-sj-programming-front.html` | `templates/pkm-sj-programming-back.html` | `styles/css/pkm-sj-programming.css` |

The generated templates intentionally contain their complete JavaScript and
CSS. Anki does not need access to the source directory or to the generator.

The `{{edit:...}}` and `{{clickable:Tags}}` filters continue to require the
corresponding Anki add-ons on clients where those custom filters are used.
