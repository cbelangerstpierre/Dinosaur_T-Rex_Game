import pygame
import os
import MainWindow


class ImageLoader:
    DIR_ASSETS = "assets"
    DIR_IMAGES = "images"

    # Background images
    BG = pygame.transform.scale(
        pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "white.jpg")),
        (MainWindow.MainWindow.WIDTH, MainWindow.MainWindow.HEIGHT)
    )
    FLOOR = pygame.transform.scale(
        pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "terrain.png")),
        (MainWindow.MainWindow.WIDTH * 5, int(MainWindow.MainWindow.HEIGHT / 5))
    )
    CLOUD = pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "cloud.png"))

    # Dino images
    DINO_SPRINTING = [
        pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "dino-3.png")),
        pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "dino-4.png"))
    ]
    DINO_JUMPING = pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "dino-1.png"))

    DINO_LOW = [
        pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "dino-low-1.png")),
        pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "dino-low-2.png"))
    ]

    # Enemies images
    CACTUS_1 = pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "cactus-1.png"))
    CACTUS_2 = pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "cactus-2.png"))
    CACTUS_3 = pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "cactus-3.png"))

    CACTUS_BIG_1 = pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "cactus-large-1.png"))
    CACTUS_BIG_2 = pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "cactus-large-2.png"))
    CACTUS_BIG_3 = pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "cactus-large-3.png"))

    BIRD_1 = pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "bird-1.png"))
    BIRD_2 = pygame.image.load(os.path.join(DIR_ASSETS, DIR_IMAGES, "bird-2.png"))
