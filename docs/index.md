# crp

_Tools for cropping images._

[![PyPI](https://img.shields.io/pypi/v/crp?color=success)](https://pypi.org/project/crp/)
[![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen?logo=pytest&logoColor=white)](https://coverage.readthedocs.io/en/latest/)
[![ci](https://github.com/br3ndonland/crp/workflows/ci/badge.svg)](https://github.com/br3ndonland/crp/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Description

Images often need to be cropped to specific aspect ratios and dimensions for upload to sites like [TheMovieDB](https://www.themoviedb.org/) (TMDB). [TheMovieDB's image upload guidelines](https://www.themoviedb.org/bible/image) explain that backdrops should be in a 16:9 aspect ratio (width x height) and posters should be in a 2:3 aspect ratio. Some sites have auto-cropping features that will offer to crop images to the required dimensions during upload, but this is often not adequate. Images often need further editing beyond just brute-force auto-cropping. It's therefore helpful to have dimensions to use as a guideline when editing images.

This project provides a command-line interface (CLI) that suggests dimensions to use for cropping.

## Installation

- [pip](https://pip.pypa.io/en/stable/cli/pip_install/)
    - Install with `python -m pip install crp` from within a virtual environment
    - Invoke with `crp` or `python -m crp`
- [pipx](https://pipx.pypa.io/stable/getting-started/)
    - Install CLI with `pipx install crp` and invoke with `crp`
    - Run without installing CLI with `pipx run crp`
- [uv](https://docs.astral.sh/uv/guides/tools/)
    - Install CLI with `uv tool install crp` and invoke with `crp`
    - Run without installing CLI with `uvx crp`

## Usage

```sh
crp suggest --width=3940 --height 2160 backdrop # Crop to 3840 x 2160 (16:9).
crp suggest --width 1652 --height 2214 poster # Crop to 1476 x 2214 (2:3).
```

To see the help text, run `crp --help`/`crp -h`.

## Related

- GitHub topics:
  [crop-image](https://github.com/topics/crop-image),
  [crop](https://github.com/topics/crop),
  [cropping](https://github.com/topics/cropping),
  [image-manipulation](https://github.com/topics/image-manipulation),
  [image-processing](https://github.com/topics/image-processing),
  [tmdb](https://github.com/topics/tmdb)
- [`react-easy-crop`](https://github.com/ValentinH/react-easy-crop)/[`svelte-easy-crop`](https://github.com/ValentinH/svelte-easy-crop)
- [`react-image-crop`](https://github.com/DominicTobias/react-image-crop)
- [`smartcrop.js`](https://github.com/jwagner/smartcrop.js)
- [`smartcrop.py`](https://github.com/smartcrop/smartcrop.py)
- [TMDB Trello: Add support for image cropping](https://trello.com/c/9nVLokdG/237-add-support-for-image-cropping)
