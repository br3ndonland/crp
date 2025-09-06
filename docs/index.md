# crp

_Tools for cropping images._

[![ci](https://github.com/br3ndonland/crp/workflows/ci/badge.svg)](https://github.com/br3ndonland/crp/actions/workflows/ci.yml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Description

Images often need to be cropped to specific aspect ratios and dimensions for upload to sites like [TheMovieDB](https://www.themoviedb.org/) (TMDB). [TheMovieDB's image upload guidelines](https://www.themoviedb.org/bible/image) explain that backdrops should be in a 16:9 aspect ratio (width x height) and posters should be in a 2:3 aspect ratio. This project provides a command-line interface (CLI) that suggests dimensions to use for cropping.

## Installation

- [pip](https://pip.pypa.io/en/stable/cli/pip_install/)
    - Install with `python -m pip install crp` from within a virtual environment
    - Invoke with `crp` or `python -m crp`
- [pipx](https://pipx.pypa.io/stable/getting-started/)
    - Install CLI with `pipx install crp` and invoke with `crp`
    - Run one-off commands with `pipx run crp`
- [uv](https://docs.astral.sh/uv/guides/tools/)
    - Install CLI with `uv tool install crp` and invoke with `crp`
    - Run one-off commands with `uvx crp`

## Usage

```sh
crp suggest --width=3940 --height 2160 backdrop # Crop to 3840x2160
crp suggest --width 1652 --height 2214 poster # Crop to 1476x2214
```

To see the help text, run `crp --help`/`crp -h`.

## Related

- [`react-image-crop`](https://github.com/DominicTobias/react-image-crop)
- [`smartcrop.js`](https://github.com/jwagner/smartcrop.js)
