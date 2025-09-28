import dataclasses
import enum
from typing import override


@dataclasses.dataclass
class AspectRatio:
    width: int
    height: int

    @override
    def __str__(self) -> str:
        """The aspect ratio of an image is expressed as `width:height`.

        https://en.wikipedia.org/wiki/Aspect_ratio_%28image%29
        """
        return f"{self.width}:{self.height}"


class ImageType(enum.StrEnum):
    """Image type.

    This type is an enum because enums can be used for both type annotations and
    `click.Choice`. `Literal` cannot be used for `click.Choice`.

    https://click.palletsprojects.com/en/stable/parameter-types/#choice
    """

    BACKDROP = enum.auto()
    POSTER = enum.auto()


@dataclasses.dataclass
class Image:
    image_type: ImageType
    width: int
    height: int
    minimum_width: int
    minimum_height: int
    maximum_width: int
    maximum_height: int

    def __init__(self, image_type: ImageType, *, width: int, height: int) -> None:
        self.image_type = image_type
        if not width and not height:
            raise ValueError("Neither width nor height supplied.")
        if not width:
            width = int(height * (self.aspect_ratio.width / self.aspect_ratio.height))
        if not height:
            height = int(width * (self.aspect_ratio.height / self.aspect_ratio.width))
        if image_type is ImageType.BACKDROP:
            minimum_width = 1280
            minimum_height = 720
            maximum_width = 3840
            maximum_height = 2160
        elif image_type is ImageType.POSTER:
            minimum_width = 500
            minimum_height = 750
            maximum_width = 2000
            maximum_height = 3000
        if width < minimum_width or height < minimum_height:
            error_message = (
                f"{image_type} dimensions ({width} x {height}) "
                "are smaller than the minimum dimensions required for upload to TMDB "
                f"({minimum_width} x {minimum_height})."
            )
            raise ValueError(error_message)
        self.width = width
        self.height = height
        self.minimum_width = minimum_width
        self.minimum_height = minimum_height
        self.maximum_width = maximum_width
        self.maximum_height = maximum_height

    @property
    def aspect_ratio(self) -> AspectRatio:
        return (
            AspectRatio(16, 9)
            if self.image_type == ImageType.BACKDROP
            else AspectRatio(2, 3)
        )

    @property
    def dimensions(self) -> str:
        return f"{self.width} x {self.height}"
