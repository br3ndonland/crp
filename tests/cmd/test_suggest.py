import pytest
from click.testing import CliRunner

from crp.main import cli


def test_missing_width_and_height() -> None:
    """Test that omitting width and height raises an exception."""
    expected_output = "Neither width nor height supplied"
    runner_args = ["suggest", "backdrop"]
    runner = CliRunner()
    result = runner.invoke(cli, runner_args)
    assert result.exit_code > 0
    assert expected_output in result.output


@pytest.mark.parametrize(
    ("image_type", "height", "expected_width", "expected_height"),
    (
        ("backdrop", 2160, 3840, 2160),
        ("backdrop", 3000, 3840, 2160),
        ("poster", 1500, 1000, 1500),
        ("poster", 2100, 1400, 2100),
    ),
)
def test_missing_width(
    image_type: str, height: int, expected_width: int, expected_height: int
) -> None:
    """Test that omitting width sets the expected default height."""
    expected_output = f"Crop {image_type} to {expected_width} x {expected_height}"
    runner_args = ["suggest", "--height", str(height), image_type]
    runner = CliRunner()
    result = runner.invoke(cli, runner_args)
    assert result.exit_code == 0
    assert expected_output in result.output


@pytest.mark.parametrize(
    ("image_type", "width", "expected_width", "expected_height"),
    (
        ("backdrop", 3840, 3840, 2160),
        ("backdrop", 5000, 3840, 2160),
        ("poster", 1000, 1000, 1500),
        ("poster", 2200, 2000, 3000),
    ),
)
def test_missing_height(
    image_type: str, width: int, expected_width: int, expected_height: int
) -> None:
    """Test that omitting height sets the expected default width."""
    expected_output = f"Crop {image_type} to {expected_width} x {expected_height}"
    runner_args = ["suggest", "--width", str(width), image_type]
    runner = CliRunner()
    result = runner.invoke(cli, runner_args)
    assert result.exit_code == 0
    assert expected_output in result.output


@pytest.mark.parametrize(("width", "height"), ((640, 480), (1920, 600), (230, 100)))
def test_minimum_dimensions_for_backdrop(width: int, height: int) -> None:
    """Test that providing values below minimum width and height raises an exception."""
    expected_output = "smaller than the minimum dimensions required for upload to TMDB"
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
    assert result.exit_code > 0
    assert expected_output in result.output


@pytest.mark.parametrize(("width", "height"), ((400, 600), (490, 800), (600, 650)))
def test_minimum_dimensions_for_poster(width: int, height: int) -> None:
    """Test that providing values below minimum width and height raises an exception."""
    expected_output = "smaller than the minimum dimensions required for upload to TMDB"
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
    assert result.exit_code > 0
    assert expected_output in result.output


@pytest.mark.parametrize(
    ("width", "height", "expected_width", "expected_height"),
    (
        (1920, 1080, 1920, 1080),
        (2000, 1101, 1957, 1101),
        (3840, 2160, 3840, 2160),
        (3940, 2160, 3840, 2160),
        (4000, 2260, 3840, 2160),
    ),
)
def test_suggest_dimensions_for_backdrop(
    width: int, height: int, expected_width: int, expected_height: int
) -> None:
    """Test suggested crop values for backdrops with given width and height."""
    expected_output = f"Crop backdrop to {expected_width} x {expected_height} (16:9).\n"
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
    assert result.output == expected_output


@pytest.mark.parametrize(
    ("width", "height", "expected_width", "expected_height"),
    (
        (1000, 1500, 1000, 1500),
        (1300, 2100, 1300, 1950),
        (1652, 2214, 1476, 2214),
        (2000, 3000, 2000, 3000),
        (2100, 3005, 2000, 3000),
    ),
)
def test_suggest_dimensions_for_poster(
    width: int, height: int, expected_width: int, expected_height: int
) -> None:
    """Test suggested crop values for posters with given width and height."""
    expected_output = f"Crop poster to {expected_width} x {expected_height} (2:3).\n"
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
    assert result.output == expected_output
