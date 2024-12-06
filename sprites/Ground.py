from pygame import sprite, Surface

from sprites.Platform import Platform


class Ground(Platform):
    def __init__(self, *groups: sprite.AbstractGroup):
        super().__init__(*groups, x=0, y=4990, width=5000, height=10)
        self.image = Surface((5000, 10))
        self.image.fill((165, 227, 136))
