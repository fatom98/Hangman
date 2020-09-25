import pygame
import os

WIDTH, HEIGHT = 700, 500
FPS = 60
SECOND = 1000
# RGB
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

# PATH
CURRENT_PATH = os.path.dirname("main.py")
IMAGE_PATH = os.path.join(CURRENT_PATH, "images")
DOC_PATH = os.path.join(CURRENT_PATH, "docs")

# BUTTON
GAP = 20
PADDING = 10
RADIUS = 20
STARTX = GAP + RADIUS
STARTY = 400
