import pygame
import ImageLoader
import Window


class RedrawWindow:
    @staticmethod
    def redraw_window():

        bg_x_position = 0
        bg_y_position = 0

        floor_x_position = 0
        floor_y_position = Window.Window.HEIGHT - ImageLoader.ImageLoader.FLOOR.get_height() - 10

        dino_jumping_x_position = int(Window.Window.WIDTH / 15)
        dino_jumping_y_position = int(
            Window.Window.HEIGHT -
            ImageLoader.ImageLoader.DINO_JUMPING.get_height() -
            ImageLoader.ImageLoader.FLOOR.get_height() / 3)

        Window.Window.WIN.blit(
            ImageLoader.ImageLoader.BG,
            (bg_x_position, bg_y_position))

        Window.Window.WIN.blit(
            ImageLoader.ImageLoader.FLOOR,
            (floor_x_position, floor_y_position))

        Window.Window.WIN.blit(
            ImageLoader.ImageLoader.DINO_JUMPING,
            (dino_jumping_x_position, dino_jumping_y_position))

        pygame.display.update()
