import os
import pygame
import random
from MainVar import MainVar
from MainWindow import MainWindow
from RedrawWindow import RedrawWindow
from Dino import Dino
from Events import Events


pygame.font.init()


def Main():

    dino = Dino()

    while MainVar.run:
        MainVar.clock.tick(MainVar.fps)
        events = pygame.event.get()
        Events.dino_jump(events, dino, MainVar.fps)
        dino.sprinting()
        Events.quit_game(events)
        RedrawWindow.redraw_window(dino)


if __name__ == "__main__":
    Main()
