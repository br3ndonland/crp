import click

from crp import __version__
from crp.cmd.suggest import suggest


@click.group(context_settings=dict(help_option_names=("-h", "--help")))
@click.version_option(prog_name=__package__, version=__version__)
def cli() -> None:
    """Tools for cropping images."""
    pass


cli.add_command(suggest)
