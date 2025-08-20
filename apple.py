
import pygame as pg

from square import Square


class Apple(Square):
    def __init__(self, x, y, size):
        super().__init__(x, y, (255, 0, 0), size)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))