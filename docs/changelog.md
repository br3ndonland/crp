# Changelog

## 0.0.4 - 2025-09-28

### Changes

**Handle missing dimensions in `suggest` subcommand**
(c1d297c4d5ee338e165cc4d41975eeda2a2bd9cc)

The [Click docs](https://click.palletsprojects.com/en/stable/arguments/)
on arguments explain:

> It is possible to make an argument required by setting
> `required=True`. It is not recommended since we think command line
> tools should gracefully degrade into becoming no ops. We think this
> because command line tools are often invoked with wildcard inputs and
> they should not error out if the wildcard is empty.

In the spirit of keeping arguments optional, the `width` and `height`
arguments to the `crp suggest` subcommand are both optional. However,
with the code as it is now, both of these arguments should be required.
Without either width or height, the command will raise the exception
`'<' not supported between instances of 'NoneType' and 'int'` which
originates from `if width < minimum_width or height < minimum_height` in
`crp.types.Image.__init__` (Click sets the missing value to `None`).

Missing dimensions will now be handled in the following manner:

- If neither width nor height are supplied, raise an exception.
- If only width or only height is supplied, set the missing dimension to
  a default value appropriate for the aspect ratio of the image type.

### Commits

- Bump version from 0.0.3 to 0.0.4 (c1d297c)
- Handle missing dimensions in `suggest` subcommand (8d5026e)
- Limit Click version constraint to minor version (6710c6f)
- Update to Hatch 1.14.2 (5a3fc35)
- Use Hatch commands consistently in testing docs (9c4b207)
- Revert "Move contributing symlink to `.github`" (9967d2a)
- Move contributing symlink to `.github` (258b924)
- Justify project in light of auto-cropping features (bf43eb0)
- Add TMDB auto-cropping Trello link to README (835b88a)
- Update `suggest` subcommand output format in docs (400982e)
- Switch type checking from mypy to BasedPyright (527b908)
- Add `[project.urls]` table to `pyproject.toml` (9af7e84)
- Add suggested VSCode settings and extensions (414a9b6)
- Don't use same deployment environment name twice (01fed9d)
- Update changelog for version 0.0.3 (#3) (cec5635)

Tagger: Brendon Smith <bws@bws.bio>

Date: 2025-09-28 17:37:08 -0400

```text
-----BEGIN SSH SIGNATURE-----
U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAgwLDNmire1DHY/g9GC1rGGr+mrE
kJ3FC96XsyoFKzm6IAAAADZ2l0AAAAAAAAAAZzaGE1MTIAAABTAAAAC3NzaC1lZDI1NTE5
AAAAQGtc0wlmm3wBiGrjMr2i8fHIupWDrOjsuPgTo/s2O7QNqYVqcUU7qoQx0THk1tqHGH
yvhy5SDFujxx2Ad1KC0gE=
-----END SSH SIGNATURE-----
```

## 0.0.3 - 2025-09-08

### Changes

**Drop support for Python 3.11**
(ade0b0e2ff6d611dc40ce8c224bec172f9dc68f8)

This release will drop support for Python 3.11 and set the minimum
required version to Python 3.12. This is needed due to the use of the
[`@typing.override`](https://docs.python.org/3/library/typing.html#typing.override)
decorator that was introduced in Python 3.12. It is also possible to
install the `typing_extensions` package as a runtime dependency if
support for older versions of Python is needed. This project is new and
does not need to support older versions of Python, so it is simpler to
just drop support for Python 3.11.

### Commits

- Bump version from 0.0.2 to 0.0.3 (b877c36)
- Drop support for Python 3.11 (ade0b0e)
- Update changelog for version 0.0.2 (#2) (0db3694)
- Add `workflow_dispatch` to changelog job (e8d926e)
- Fix ref in GitHub Actions changelog job (3ca374f)

Tagger: Brendon Smith <bws@bws.bio>

Date: 2025-09-08 04:16:42 -0400

```text
-----BEGIN SSH SIGNATURE-----
U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAgwLDNmire1DHY/g9GC1rGGr+mrE
kJ3FC96XsyoFKzm6IAAAADZ2l0AAAAAAAAAAZzaGE1MTIAAABTAAAAC3NzaC1lZDI1NTE5
AAAAQGrPPnzaE2fsO9Uv8aVew/JSESmvfEcwbPpSAmuqeEpIum/R4d8oadzPRcrbn77kZ5
QDz36QTatBXp/PVjvZjQg=
-----END SSH SIGNATURE-----
```

## 0.0.2 - 2025-09-08

### Changes

**Enforce minimum and maximum image dimensions**
(3c673c219869f3be2fb4a88dc533ebf93bb7a2fa)

This release will add enforcement of minimum and maximum image
dimensions to the `suggest` subcommand.

- Backdrops (16:9): minimum 1280x720 pixels, maximum 3840x2160 pixels
- Posters (2:3): minimum 500x750 pixels, maximum 2000x3000 pixels

This will be accomplished with a dataclass that checks image dimensions
as part of its `__init__` method. Tests will be added to verify that the
error messages and exit codes are propagated back to the user.

### Commits

- Bump version from 0.0.1 to 0.0.2 (7268885)
- Enforce minimum and maximum image dimensions (3c673c2)
- Add more related projects to README (f0aa320)
- Clarify installing vs. running CLI in README (4b15489)
- Add PyPI badge to README (958eff9)
- Add test coverage badge to README (3641bbf)
- Remove CodeQL GitHub Actions workflow (1a53bce)
- Format Git tag messages with Prettier (d7136fc)
- Update references to `develop` branch (755610f)
- Update changelog for version 0.0.1 (#1) (f320050)

Tagger: Brendon Smith <bws@bws.bio>

Date: 2025-09-08 01:45:12 -0400

```text
-----BEGIN SSH SIGNATURE-----
U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAgwLDNmire1DHY/g9GC1rGGr+mrE
kJ3FC96XsyoFKzm6IAAAADZ2l0AAAAAAAAAAZzaGE1MTIAAABTAAAAC3NzaC1lZDI1NTE5
AAAAQKKlG8jFW3Elsf0Jplxdp2e8sNULHMNhWL/Q9wJKFs7ACC6wy5MRvD6qQw0VQukT+a
UOec6ayxMQxrAQsgwc9wA=
-----END SSH SIGNATURE-----
```

## 0.0.1 - 2025-09-07

### Changes

**Implement `suggest` subcommand**
(08a18dd648caff3c1cf057c45d225c9bb0565f36,
a0d70725a95f01992cd616e2c0ee75ad31c381bc)

This release will provide a minimal working implementation of a
`suggest` subcommand. The purpose of the `suggest` subcommand is to
suggest dimensions for cropping images of the given image type.

Images often need to be cropped to specific aspect ratios and dimensions
for upload to sites like
[TheMovieDB](https://www.themoviedb.org/bible/image).

- Backdrops: 16:9 (minimum 1280x720 pixels, maximum 3840x2160 pixels)
- Posters: 2:3 (minimum 500x750 pixels, maximum 2000x3000 pixels)

This command suggests dimensions to use for cropping. Examples:

```sh
crp suggest --width=3940 --height 2160 backdrop -> Crop to 3840x2160
crp suggest --width 1652 --height 2214 poster -> Crop to 1476x2214
```

`-h` is not used as a short option for `--height` because it would
conflict with the `-h` used for help.

This command does not currently enforce minimum and maximum dimensions.
Support for minimum and maximum dimensions is planned for a future
release.

The implementation uses
[`enum.StrEnum`](https://docs.python.org/3/library/enum.html), which was
introduced in Python 3.11. This release will set the minimum Python
version to 3.11 accordingly.

### Commits

- Bump version to 0.0.1 (83e0e2d)
- Add subprocess test for invoking with `python -m` (a0d7072)
- Implement `suggest` subcommand (08a18dd)
- Fix Hatch env in GitHub Actions (091a880)
- Publish to PyPI with trusted publisher (5012782)
- Add a changelog (3d47f39)
- Use same contributing file for repo and docs (0a68946)
- Use same file for README and docs homepage (7bab3b3)
- Update project configuration (29ae4d4)
- Use `$HATCH_ENV_TYPE_VIRTUAL_PATH` (822d0d5)
- Format `pyproject.toml` with Tombi (6982e47)
- Format Git commit messages with Prettier (352c3da)
- Update `.gitignore` (36a434b)
- Remove example code (70c0b28)
- Initial commit (d1b3efa)

Tagger: Brendon Smith <bws@bws.bio>

Date: 2025-09-07 03:38:31 -0400

```text
-----BEGIN SSH SIGNATURE-----
U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAgwLDNmire1DHY/g9GC1rGGr+mrE
kJ3FC96XsyoFKzm6IAAAADZ2l0AAAAAAAAAAZzaGE1MTIAAABTAAAAC3NzaC1lZDI1NTE5
AAAAQJFoREsICt+w9C9qje4acnBmk52Rg/51fGsxQ6ZCEoMbIo2iq4gjFOgZFcTtKBPrwb
jQHsBgu8Eox6pNaUYY+Qw=
-----END SSH SIGNATURE-----
```
