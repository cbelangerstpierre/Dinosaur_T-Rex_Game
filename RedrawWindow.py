import pygame
import ImageLoader
import MainWindow


class RedrawWindow:
    @staticmethod
    def redraw_window(dino):

        bg_x_position = 0
        bg_y_position = 0

        floor_x_position = 0
        floor_y_position = MainWindow.MainWindow.HEIGHT - ImageLoader.ImageLoader.FLOOR.get_height() - 10

        MainWindow.MainWindow.WIN.blit(
            ImageLoader.ImageLoader.BG,
            (bg_x_position, bg_y_position))

        MainWindow.MainWindow.WIN.blit(
            ImageLoader.ImageLoader.FLOOR,
            (floor_x_position, floor_y_position))

        dino.draw(MainWindow.MainWindow.WIN)

        pygame.display.update()
