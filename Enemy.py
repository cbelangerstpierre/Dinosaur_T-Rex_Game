import Entity


class Enemy(Entity.Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.enemies = []
        self.x = x
        self.y = y
