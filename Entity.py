class Entity:
    def __init__(self):
        self.y = None
        self.x = None
        self.velocity = 4
        self.img = None
        
    def move(self):
        self.x -= self.velocity
        
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
