import pygame
from .constants import *


class Button:

    def __init__(self, x, y, ltr, radius = RADIUS):
        self.x = x
        self.y = y
        self.letter = ltr
        self.radius = radius

    def draw(self, win):
        pygame.draw.circle(win, BLACK, (self.x, self.y), self.radius, 2)
