
import pygame as pg


class Square(pg.sprite.Sprite):
    def __init__(self, x, y, color, size):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        
    def update(self, dt):
        # Update logic for the square can be added here
        pass

    def draw(self, surface):
        pass