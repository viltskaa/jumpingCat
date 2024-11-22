from pygame import sprite

from sprites.Platform import Platform


class Ground(Platform):
    def __init__(self, *groups: sprite.AbstractGroup):
        super().__init__(*groups, x=0, y=4990, width=5000, height=10, color="#00ff00")
