import dataclasses
import enum


@dataclasses.dataclass
class AspectRatio:
    width: int
    height: int


class ImageType(enum.StrEnum):
    """Image type.

    This type is an enum because enums can be used for both type annotations and
    `click.Choice`. `Literal` cannot be used for `click.Choice`.

    https://click.palletsprojects.com/en/stable/parameter-types/#choice
    """

    BACKDROP = enum.auto()
    POSTER = enum.auto()
