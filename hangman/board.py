import pygame, os
from .constants import *
from .button import Button

pygame.init()
pygame.font.init()


class Board:
    def __init__(self):
        self.images = [pygame.image.load(os.path.normpath(f"{IMAGE_PATH}\{index}.png")) for index in range(8)]
        self.status = 0
        self.buttons = list()
        self.createButton()
        self.yn = list()
        self.yesno()
        self.FONT = pygame.font.SysFont("Sans", 30)
        self.WORD = pygame.font.SysFont("Sans", 50)

    def draw(self, win, display, score):
        win.fill(WHITE)
        win.blit(self.images[self.status], (80, 80))

        for btn in self.buttons:
            btn.draw(win)
            text = self.FONT.render(btn.letter, True, BLACK)
            win.blit(text, (btn.x - text.get_width()/2, btn.y - text.get_height()/2))

        word = self.WORD.render(display, 1, BLACK)
        win.blit(word, (300, 200))

        scr = self.FONT.render(f"Score: {score}", True, BLACK)
        win.blit(scr, (620 - scr.get_width()/2, 30 - scr.get_height()/2))

        pygame.display.update()

    def createButton(self):
        A = 65
        for index in range(26):

            x = STARTX + ((PADDING + 2 * RADIUS) * (index % 13))
            y = STARTY + GAP * (index // 13) * 3
            btn = Button(x, y, chr(A))
            self.buttons.append(btn)
            A += 1

    def outro(self, win, message, score):
        win.fill(WHITE)
        if "Lost" in message: color = RED
        else: color = GREEN
        
        text = self.WORD.render(message, 1, color)
        again = self.WORD.render("Do you want to play again?", True, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height() * 3))
        win.blit(again, (WIDTH/2 - again.get_width()/2, HEIGHT/2 - again.get_height()))

        for btn in self.yn:
            btn.draw(win)
            text = self.FONT.render(btn.letter, True, BLACK)
            win.blit(text, (btn.x - text.get_width()/2, btn.y - text.get_height()/2))
        
        scr = self.FONT.render(f"Score: {score}", True, BLACK)
        win.blit(scr, (620 - scr.get_width()/2, 30 - scr.get_height()/2))

        pygame.display.update()

    def yesno(self):
        yes = Button(300, 350, "Yes", 30)
        no = Button(400, 350, "No", 30)
        self.yn.append(yes)
        self.yn.append(no)


