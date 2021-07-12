import pygame
import os
import Window


class ImageLoader:
    DIR_ASSETS = "assets"
    DIR_IMAGES = "images"

    BG = pygame.transform.scale(
        pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "white.jpg")),
        (Window.Window.WIDTH, Window.Window.HEIGHT)
    )
    FLOOR = pygame.transform.scale(
        pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "terrain.png")),
        (Window.Window.WIDTH * 5, int(Window.Window.HEIGHT / 5))
    )
    DINO_SPRINTING = [
        pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "dino-3.png")),
        pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "dino-4.png"))
    ]
    DINO_JUMPING = pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "dino-1.png"))
