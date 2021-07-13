import pygame
import ImageLoader
import MainWindow


class RedrawWindow:
    @staticmethod
    def redraw_window(dino, floors):

        bg_x_position = 0
        bg_y_position = 0

        MainWindow.MainWindow.WIN.blit(
            ImageLoader.ImageLoader.BG,
            (bg_x_position, bg_y_position))

        for floor in floors:
            floor.draw(MainWindow.MainWindow.WIN)

        dino.draw(MainWindow.MainWindow.WIN)

        pygame.display.update()
