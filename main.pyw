import pygame
import math
import random
from hangman.constants import *
from hangman.board import Board


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")
clock = pygame.time.Clock()
SCORE = 0


def main():
    global SCORE
    WORD = get_word()
    GUESS = list()
    board = Board()


    run = True
    
    buttons = board.buttons

    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                return "break"


            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                for btn in buttons:
                    if math.sqrt((btn.x - x) ** 2 + (btn.y - y) ** 2) <= RADIUS:
                        buttons.remove(btn)
                        GUESS.append(btn.letter)

                        if btn.letter not in WORD:
                            board.status += 1

        display = ""
        for letter in WORD:
            if letter in GUESS:
                display += f"{letter} "
            else:
                display += "_ "


        board.draw(WIN, display, SCORE)

        if "_" not in display:
            message = f"You Won. It was {WORD}"
            run = False
            SCORE += 1
            pygame.time.delay(int(0.5 * SECOND))
            again(message)

        elif board.status == 7:
            message = f"You Lost. It was {WORD}"
            run = False
            SCORE -= 1
            pygame.time.delay(int(0.5 * SECOND))
            again(message)
            
def get_word():
    with open(f"{DOC_PATH}\words.txt") as f:
        file = f.read()
        word = random.choice(file.split("\n"))
        return f"{word.upper()}"

def again(message):
    global SCORE
    run = True 
    board = Board()
    buttons = board.yn

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                return "break"

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for btn in buttons:
                    if math.sqrt((btn.x - x) ** 2 + (btn.y - y) ** 2) <= RADIUS:
                        if btn.letter == "Yes":
                            run = False
                            main()
                            return "break"
                        else:
                            run = False
                            pygame.quit()
                            return "break"

        board.outro(WIN, message, SCORE)

if __name__ == "__main__":
    main()
