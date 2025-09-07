import pytest
from click.testing import CliRunner

import crp
from crp.main import cli


@pytest.mark.parametrize("option", ("-h", "--help"))
def test_help_option(option: str) -> None:
    """Test that the --help option displays usage information."""
    runner = CliRunner()
    result = runner.invoke(cli, [option])
    assert result.exit_code == 0
    assert "Show this message and exit" in result.output


def test_no_option() -> None:
    """Test that running the main command with no options shows help text and exits with
    a non-zero exit code.
    """
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code > 0
    assert "Show this message and exit" in result.output


def test_no_option_with_runpy() -> None:
    """Test that `import crp.__main__` (equivalent to invoking with `python -m`)
    and no options exits with a non-zero exit code.

    https://docs.python.org/3/library/__main__.html#main-py-in-python-packages
    https://docs.python.org/3/library/runpy.html
    """
    with pytest.raises(SystemExit):
        import crp.__main__  # noqa: F401 # pyright: ignore[reportUnusedImport]


def test_version_option() -> None:
    """Test that the `--version` option displays the expected package name and version."""
    expected_output = f"{crp.__package__}, version {crp.__version__}\n"
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert result.output == expected_output
