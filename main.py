import pygame
from MainVar import MainVar
from RedrawWindow import RedrawWindow
from Dino import Dino
from Events import Events
from Floor import Floor
from Enemy import Enemy


pygame.font.init()


def Main():

    dino = Dino()
    floor1 = Floor()
    floor2 = Floor()
    floor2.setX(floor1.img.get_width())
    floors = [floor1, floor2]

    while MainVar.run:
        MainVar.clock.tick(MainVar.fps)
        events = pygame.event.get()
        Events.dino_jump(events, dino, MainVar.fps)
        dino.sprinting()
        Events.quit_game(events)
        for floor in floors:
            floor.move()
        floor1.moveAFloor(floors)
        RedrawWindow.redraw_window(dino, floors)


if __name__ == "__main__":
    Main()
