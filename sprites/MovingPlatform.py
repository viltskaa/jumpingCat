from pygame import sprite, image, Rect

from sprites.Platform import Platform


class MovingPlatform(Platform):
    def __init__(self, *groups: sprite.AbstractGroup, x, y, speed_x=2, shift_x=128):
        super().__init__(*groups, x=x, y=y)
        self.speed_x = speed_x
        self.shift_x = shift_x
        self.start_x = x

        self.image = image.load('assets/platform.png')
        self.rect = Rect(x, y, 128, 16)

    def update(self, *args, **kwargs):
        if self.rect.x + self.rect.w > self.start_x + self.rect.w + self.shift_x:
            self.speed_x = -self.speed_x

        if self.rect.x < self.start_x - self.shift_x:
            self.speed_x = -self.speed_x

        self.rect.x += self.speed_x
