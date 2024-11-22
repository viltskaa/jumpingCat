import pygame.image
from pygame import *
from sprites.MovingPlatform import MovingPlatform


class Cat(sprite.Sprite):
    MOVE_SPEED = 10
    WIDTH = 64
    HEIGHT = 64
    COLOR = "#FFFFFF"
    JUMP_POWER = 13
    GRAVITY = 0.65

    def __init__(self, x: int, y: int, *groups: sprite.AbstractGroup):
        super().__init__(*groups)

        self.images = {
            "jump_left": image.load("assets/cat/jump_left.png"),
            "jump_right": transform.flip(image.load("assets/cat/jump_left.png"), True, False),
            "fall_left": image.load("assets/cat/fall_left.png"),
            "fall_right": transform.flip(image.load("assets/cat/fall_left.png"), True, False),
            "walk_left": image.load("assets/cat/walk_left.png"),
            "walk_right": transform.flip(image.load("assets/cat/walk_left.png"), True, False),
            "falling_left": image.load("assets/cat/falling.png"),
            "falling_right": transform.flip(image.load("assets/cat/falling.png"), True, False),
            "stay": image.load("assets/cat/normal.png"),
        }

        # for key, value in self.images.items():
        #     self.images.update({key: pygame.transform.chop(value, Rect(0, 32, 64, 32))})

        self.velocity = Vector2(0, 0)

        self.image = self.images["stay"]
        self.rect = Rect(x, y, Cat.WIDTH, Cat.HEIGHT)

        self.onGround = False
        self.onMovingPlatform = False
        self.onShift = False
        self.state: int = 0

    def update(self,
               left: bool,
               right: bool,
               up: bool,
               shift: bool,
               platforms: list):
        self.onShift = shift

        if up and self.onGround:
            self.velocity.y = -Cat.JUMP_POWER
            # self.state = 1
            self.onGround = False
            self.onMovingPlatform = False
        if left:
            self.velocity.x = -Cat.MOVE_SPEED
            self.state = 2
            if up:
                self.state = 5
        if right:
            self.velocity.x = Cat.MOVE_SPEED
            self.state = 3
            if up:
                self.state = 6

        if not (left or right):
            if not self.onMovingPlatform:
                self.velocity.x = 0
            if not up and self.state != 0:
                self.state = 0

        if not self.onGround:
            self.velocity.y += Cat.GRAVITY
            if self.velocity.y > 0.65:
                self.state = 4

        self.onGround = False
        self.onMovingPlatform = False
        self.rect.y += self.velocity.y
        self.collide(0, self.velocity.y, platforms)

        if 0 < self.rect.x + self.velocity.x < 5000:
            self.rect.x += self.velocity.x
            self.collide(self.velocity.x, 0, platforms)

        self.switch_image_by_state()

    def switch_image_by_state(self):
        match self.state:
            case 0:
                self.image = self.images["stay"]
            case 1:
                self.image = self.images["falling_right"]
            case 2:
                self.image = self.images["walk_left"]
            case 3:
                self.image = self.images["walk_right"]
            case 4:
                self.image = self.images["falling_left"]
            case 5:
                self.image = self.images["jump_left"]
            case 6:
                self.image = self.images["jump_right"]

    def collide(self, xvel, yvel, platforms):
        if platforms is None:
            return

        for platform in platforms:
            if sprite.collide_rect(self, platform):
                if yvel > 0:
                    self.rect.bottom = platform.rect.top
                    self.onGround = True
                    self.velocity.y = 0
                    if isinstance(platform, MovingPlatform):
                        self.velocity.x = platform.speed_x
                        self.onMovingPlatform = True
                if yvel < 0:
                    self.rect.top = platform.rect.bottom
                    self.velocity.y = 0

                if xvel > 0:
                    self.rect.right = platform.rect.left
                if xvel < 0:
                    self.rect.left = platform.rect.right



