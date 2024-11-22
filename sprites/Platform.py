from pygame import *


class Platform(sprite.Sprite):
    def __init__(self,
                 *groups: sprite.AbstractGroup,
                 x: int, y: int,
                 width: int = 128,
                 height: int = 16,
                 color: str = "#00ff00"):
        super().__init__(*groups)

        self.image = Surface((width, height))
        self.image.fill(Color(color))
        self.rect = Rect(x, y, width, height)
