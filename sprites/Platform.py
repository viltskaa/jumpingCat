from pygame import *


class Platform(sprite.Sprite):
    def __init__(self,
                 *groups: sprite.AbstractGroup,
                 x: int, y: int,
                 width: int = 128,
                 height: int = 16):
        super().__init__(*groups)

        self.image = image.load('assets/platform.png')
        self.rect = Rect(x, y, width, height)
