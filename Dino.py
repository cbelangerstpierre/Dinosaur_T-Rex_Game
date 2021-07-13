import pygame
import MainWindow
import ImageLoader


class Dino:
    def __init__(self):
        self.x = int(MainWindow.MainWindow.WIDTH / 15)
        self.y = int(
            MainWindow.MainWindow.HEIGHT -
            ImageLoader.ImageLoader.DINO_JUMPING.get_height() -
            ImageLoader.ImageLoader.FLOOR.get_height() / 3)
        self.true_y = 0
        self.speed = 8
        self.initial_speed = 8
        self.gravity = -15
        self.dino_img = ImageLoader.ImageLoader.DINO_JUMPING
        self.current_sprint_img = 0
        self.mask = pygame.mask.from_surface(self.dino_img)

    def getY(self):
        return self.y

    def setY(self, new_y):
        self.y = new_y

    def getTrueY(self):
        return self.true_y

    def setTrueY(self, new_true_y):
        self.true_y = new_true_y

    def getX(self):
        return self.x

    def getSpeed(self):
        return self.speed

    def setSpeed(self, new_speed):
        self.speed = new_speed

    def getInitialSpeed(self):
        return self.initial_speed

    def getGravity(self):
        return self.gravity

    def getDinoImg(self):
        return self.dino_img

    def setDinoImg(self, new_dino_img):
        self.dino_img = new_dino_img

    def draw(self, window):
        window.blit(self.getDinoImg(), (self.getX(), self.getY()))

    def onSurface(self):
        return self.true_y == 0

    def jump(self):
        new_true_y = self.getTrueY() - self.getSpeed()
        self.setTrueY(new_true_y)
        new_y = self.getY() - self.getSpeed()
        self.setY(new_y)
        self.setDinoImg(ImageLoader.ImageLoader.DINO_JUMPING)

    def finish_jump(self, fps):
        new_speed = self.getSpeed() + self.getGravity() * (1 / fps)
        self.setSpeed(new_speed)
        new_y = self.getY() - self.getSpeed()
        self.setY(new_y)
        new_true_y = self.getTrueY() - self.getSpeed()
        self.setTrueY(new_true_y)
        self.setDinoImg(ImageLoader.ImageLoader.DINO_JUMPING)

    def sprinting(self):
        if self.onSurface():
            if self.current_sprint_img < 5:
                self.setDinoImg(ImageLoader.ImageLoader.DINO_SPRINTING[1])
                self.current_sprint_img += 1
            elif self.current_sprint_img < 10:
                self.setDinoImg(ImageLoader.ImageLoader.DINO_SPRINTING[0])
                self.current_sprint_img += 1

            else:
                self.current_sprint_img = 0

