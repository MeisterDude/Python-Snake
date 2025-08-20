
import pygame as pg

#from square import Square
from constants import SIZE_SQUARE
from board import board_to_screen


class Apple(pg.sprite.Sprite):
    def __init__(self, pos, size, color):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.pos = pos
        self.size = size
        self.color = color

    def draw(self, screen):
        x, y = board_to_screen(self.pos, self.size)
        #x += (SIZE_SQUARE - self.size) / 2
        #y += (SIZE_SQUARE - self.size) / 2
        pg.draw.rect(screen, self.color, (x, y, self.size, self.size))