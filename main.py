import os
import pygame
import random
from MainVar import MainVar
from Window import Window
from RedrawWindow import RedrawWindow

pygame.font.init()


def Main():

    while MainVar.run:
        MainVar.clock.tick(MainVar.fps)
        RedrawWindow.redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MainVar.run = False


if __name__ == "__main__":
    Main()
