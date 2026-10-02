# Contributing

This guide is only useful if it is accurate today. Google moves settings, renames features and retires products constantly, so corrections are the most valuable contribution you can make.

> [!CAUTION]
> Never post your email address, phone number, verification codes or screenshots with personal details in an issue. The maintainers cannot recover Google accounts. If you are locked out, use [g.co/recover](https://g.co/recover) and ignore anyone who offers to do it for you.

## Report something outdated

[Open an issue](https://github.com/iAnonymous3000/google-hardening-guide/issues/new/choose) and pick **Outdated or wrong**. Include the section, what you see now, and a source. Cropped screenshots help.

## Standards for changes

1. **Source every claim.** Prefer Google's own help center, blogs and release notes. Use reputable security research or press only to fill gaps, and label it.
2. **Link the exact setting.** Use the deepest stable link on myaccount.google.com, myactivity.google.com or Gmail settings, and test it while signed in.
3. **Tag the level.** Baseline is for everyone and costs nothing. Enhanced takes more effort or a purchase. Maximum trades convenience for safety.
4. **Explain why in one line.** People follow advice they understand.
5. **Write plainly.** Short sentences, active voice, and no jargon without a definition. No em or en dashes: use a period, a comma or a new sentence. CI enforces this.
6. **Date loosely.** Use month and year, or "since mid-2026", rather than exact dates.
7. **Stay vendor neutral.** Recommend standards such as FIDO2 and passkeys before brands. No affiliate links.

## Visuals

The diagrams in `assets/` are light and dark SVGs generated from [`scripts/build_visuals.py`](scripts/build_visuals.py). Edit the script, never the SVGs, then run:

```sh
python3 scripts/build_visuals.py --check
```

`--check` measures every label with a wide fallback font, so text cannot overflow on any system. It needs Pillow (`pip install pillow`). The README picks the right theme with a `<picture>` element.

The social preview image is `assets/social-preview.png`, exported from `assets/social-preview.svg` at 1280 x 640. Set it under the repository's **Settings** > **Social preview**.

## Review cycle

When you verify the whole guide against current Google documentation, update the **Last reviewed** badge and note in the README and in `CHECKLIST.md`, and add an entry to [CHANGELOG.md](CHANGELOG.md).

## Automated checks

Every pull request runs:

- a link check across all Markdown files, which also runs monthly and opens an issue when links break
- a style check for em and en dashes
- a check that the SVGs in `assets/` match `scripts/build_visuals.py`

By contributing, you agree that your contributions are licensed under [CC BY-SA 4.0](LICENSE).
