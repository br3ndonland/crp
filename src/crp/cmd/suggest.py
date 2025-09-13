import click

from crp.types import Image, ImageType


def suggest_dimensions(image: Image) -> Image:
    """Suggest dimensions to use for cropping the given image type."""
    scale = min(
        image.width / image.aspect_ratio.width, image.height / image.aspect_ratio.height
    )
    scaled_width = int(image.aspect_ratio.width * scale)
    scaled_height = int(image.aspect_ratio.height * scale)
    suggested_width = max(image.minimum_width, min(scaled_width, image.maximum_width))
    suggested_height = max(
        image.minimum_height, min(scaled_height, image.maximum_height)
    )
    return Image(image.image_type, width=suggested_width, height=suggested_height)


@click.command()
@click.argument("image-type", type=click.Choice(ImageType, case_sensitive=False))
@click.option("--width", help="Width in pixels.", type=int)
@click.option("--height", help="Height in pixels.", type=int)
def suggest(image_type: ImageType, width: int, height: int) -> None:
    """Suggest dimensions for cropping images of the given image type.

    Images often need to be cropped to specific aspect ratios and dimensions for upload
    to sites like TMDB. This command suggests dimensions to use for cropping. Dimensions
    conform to [TMDB guidelines](https://www.themoviedb.org/bible/image).

    \b
    Backdrops (16:9): minimum 1280 x 720 pixels, maximum 3840 x 2160 pixels
    Posters (2:3): minimum 500 x 750 pixels, maximum 2000 x 3000 pixels

    Examples:

    \b
    crp suggest --width=3940 --height 2160 backdrop ->  Crop to 3840 x 2160 (16:9).
    crp suggest --width 1652 --height 2214 poster ->  Crop to 1476 x 2214 (2:3).
    """
    # `-h` is not used as a short option for `--height` because it would conflict
    # with the `-h` used for help (https://github.com/pallets/click/issues/2819).
    try:
        input_image = Image(image_type, width=width, height=height)
        suggested_image = suggest_dimensions(input_image)
        message = (
            f"Crop {input_image.image_type} to {suggested_image.dimensions} "
            f"({suggested_image.aspect_ratio})."
        )
        click.secho(message, bold=True)
    except Exception as e:
        error_message = click.style(str(e), fg="red")
        raise click.UsageError(error_message) from e
