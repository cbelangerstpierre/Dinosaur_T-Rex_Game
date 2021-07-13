import Entity
import MainWindow
import ImageLoader


class Floor(Entity.Entity):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = MainWindow.MainWindow.HEIGHT - ImageLoader.ImageLoader.FLOOR.get_height() - 10
        self.img = ImageLoader.ImageLoader.FLOOR
        self.current_floor = 0

    def getX(self):
        return self.x

    def setX(self, new_x):
        self.x = new_x

    def moveAFloor(self, floors):
        if floors[self.current_floor].getX() + self.img.get_width() < 0:
            if self.current_floor == 0:
                index = 1
            else:
                index = 0
            new_x = floors[index].getX() + floors[index].img.get_width()
            floors[self.current_floor].setX(new_x)
            self.current_floor = index
