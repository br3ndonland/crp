import click

from crp.types import AspectRatio, ImageType


def suggest_aspect_ratio(
    image_type: ImageType, *, width: int, height: int
) -> AspectRatio:
    """Suggest a width and height to use for cropping the given image type."""
    if image_type is ImageType.BACKDROP:
        aspect_ratio = AspectRatio(16, 9)
        # TODO: enforce minimum and maximum dimensions
        # https://www.themoviedb.org/bible/image
        # maximum_size = AspectRatio(3840, 2160)
        # minimum_size = AspectRatio(1280, 720)
    elif image_type is ImageType.POSTER:
        aspect_ratio = AspectRatio(2, 3)
        # TODO: enforce minimum and maximum dimensions
        # https://www.themoviedb.org/bible/image
        # maximum_size = AspectRatio(2000, 3000)
        # minimum_size = AspectRatio(500, 750)
    scale = min(width / aspect_ratio.width, height / aspect_ratio.height)
    suggested_width = int(aspect_ratio.width * scale)
    suggested_height = int(aspect_ratio.height * scale)
    return AspectRatio(width=suggested_width, height=suggested_height)


@click.command()
@click.argument("image-type", type=click.Choice(ImageType, case_sensitive=False))
@click.option("--width", help="Width in pixels.", type=int)
@click.option("--height", help="Height in pixels.", type=int)
def suggest(image_type: ImageType, width: int, height: int) -> None:
    """Suggest dimensions for cropping images of the given image type.

    Images often need to be cropped to specific aspect ratios and dimensions for upload
    to sites like TheMovieDB (https://www.themoviedb.org/bible/image).

    \b
    Backdrops: 16:9 (minimum 1280x720 pixels, maximum 3840x2160 pixels)
    Posters: 2:3 (minimum 500x750 pixels, maximum 2000x3000 pixels)

    This command suggests dimensions to use for cropping. Examples:

    \b
    crp suggest --width=3940 --height 2160 backdrop -> Crop to 3840x2160
    crp suggest --width 1652 --height 2214 poster -> Crop to 1476x2214

    `-h` is not used as a short option for `--height` because it would conflict
    with the `-h` used for help (https://github.com/pallets/click/issues/2819).

    This command does not currently enforce minimum and maximum dimensions. Support for
    minimum and maximum dimensions is planned for a future release.
    """
    # TODO: enforce minimum and maximum dimensions
    aspect_ratio = suggest_aspect_ratio(image_type, width=width, height=height)
    click.secho(f"Crop to {aspect_ratio.width}x{aspect_ratio.height}", bold=True)
