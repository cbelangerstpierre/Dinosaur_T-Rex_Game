import pygame


class MainWindow:
    CAPTION = "T-Rex Game"
    WIDTH = 720
    HEIGHT = 200
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
