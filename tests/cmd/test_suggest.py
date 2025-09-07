import pytest
from click.testing import CliRunner

from crp.main import cli


@pytest.mark.parametrize(
    ("width", "height", "expected_width", "expected_height"),
    (
        (1920, 1080, 1920, 1080),
        (2000, 1101, 1957, 1101),
        (3840, 2160, 3840, 2160),
        (3940, 2160, 3840, 2160),
        (4000, 2260, 4000, 2250),
        # TODO: enforce minimum and maximum dimensions
        # https://www.themoviedb.org/bible/image
        # (4000, 2260, 3840, 2160),
    ),
)
def test_suggest_dimensions_for_backdrop(
    width: int, height: int, expected_width: int, expected_height: int
) -> None:
    """Test suggested crop values for backdrops with given width and height."""
    runner_args = [
        "suggest",
        "--width",
        str(width),
        "--height",
        str(height),
        "backdrop",
    ]
    runner = CliRunner()
    result = runner.invoke(cli, runner_args)
    assert f"Crop to {expected_width}x{expected_height}" in result.output


@pytest.mark.parametrize(
    ("width", "height", "expected_width", "expected_height"),
    (
        (1000, 1500, 1000, 1500),
        (1300, 2100, 1300, 1950),
        (1652, 2214, 1476, 2214),
        (2000, 3000, 2000, 3000),
        (2100, 3005, 2003, 3005),
        # TODO: enforce minimum and maximum dimensions
        # https://www.themoviedb.org/bible/image
        # (2100, 3005, 2000, 3000),
    ),
)
def test_suggest_dimensions_for_poster(
    width: int, height: int, expected_width: int, expected_height: int
) -> None:
    """Test suggested crop values for posters with given width and height."""
    runner_args = [
        "suggest",
        "--width",
        str(width),
        "--height",
        str(height),
        "poster",
    ]
    runner = CliRunner()
    result = runner.invoke(cli, runner_args)
    assert f"Crop to {expected_width}x{expected_height}" in result.output
