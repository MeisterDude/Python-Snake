
import pygame as pg

from square import Square


class Snake(Square):
    def __init__(self, x, y, size):
        super().__init__(x, y, (0, 255, 0), size)
        self.length = 1
        #self.positions = [(100, 100)]  # Starting position of the snake
        self.direction = (0, -1)  # Initial direction (up)
        #self.color = (0, 255, 0)  # Green color for the snake
        #self.size = 20  # Size of each segment of the snake

    def update(self, dt):
        # Update the snake's position based on its direction
        #self.x += self.direction[0] * self.size
        #self.y += self.direction[1] * self.size
        pass

    def draw(self, screen):
        # Draw the snake as a rectangle
        pg.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        # Optionally, draw the snake's body segments if needed
        # for pos in self.positions:
        #     pg.draw.rect(surface, self.color, (pos[0], pos[1], self.size, self.size))