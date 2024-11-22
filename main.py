import random

import pygame
import config

from sprites import Cat, Platform, Ground, Background, MovingPlatform
from CameraObject import Camera

pygame.init()

background = Background()

running = True
FRAMERATE = 60
screen = pygame.display.set_mode(
    (config.WIDTH,
     config.HEIGHT)
)
clock = pygame.time.Clock()

total_level_width = 5000  # Высчитываем фактическую ширину уровня
total_level_height = 5000  # высоту

camera = Camera(total_level_width, total_level_height)
entities = pygame.sprite.Group()

cat = Cat(2500, 4500, entities)
platforms: list[Platform] = [
    Ground(entities)
]

left, right, up, shift = False, False, False, False
need_spawn = False


def spawn_platform():
    cat_x, cat_y = cat.rect.center
    random_shift_x = random.randint(150, 328) * (-1 if random.random() > 0.5 else 0)
    random_shift_y = random.randint(78, 84)

    if not 0 < cat_x + random_shift_x < 5000:
        random_shift_x *= -1

    if random.random() > 0.5:
        platform = Platform(entities, x=cat_x + random_shift_x, y=cat_y - random_shift_y)
    else:
        platform = MovingPlatform(entities, x=cat_x + random_shift_x, y=cat_y - random_shift_y)

    platforms.append(platform)


def despawn_platform():
    if len(platforms) > 0:
        platforms.pop(-1)


if __name__ == '__main__':
    while running:
        clock.tick(FRAMERATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_SPACE:
                        up = True
                    case pygame.K_LEFT:
                        left = True
                    case pygame.K_RIGHT:
                        right = True
                    case pygame.K_SPACE:
                        space = True
                    case pygame.K_LSHIFT:
                        shift = True
            elif event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_SPACE:
                        up = False
                    case pygame.K_LEFT:
                        left = False
                    case pygame.K_RIGHT:
                        right = False
                    case pygame.K_SPACE:
                        space = False
                    case pygame.K_LSHIFT:
                        shift = False

        camera.update(cat)
        entities.update(left, right, up, shift, platforms)

        if cat.onGround and need_spawn:
            spawn_platform()
            need_spawn = False

        if not need_spawn:
            need_spawn = platforms[-1].rect.y == cat.rect.bottomleft[1]

        screen.fill((0, 0, 0))
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.flip()

    pygame.quit()