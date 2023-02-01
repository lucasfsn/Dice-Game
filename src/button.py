import pygame
from src.settings import BLUE, WHITE, DISPLAY, WIDTH


def clickedBtn(coords, y, x=WIDTH/2, width=150):
    return True if coords[0] > x - (width/2) and coords[0] < x + (width/2) and coords[1] > y and coords[1] < y + 35 else False


def displayBtn(fontSize, btnType, posY, color=BLUE, width=150, height=35, posX=WIDTH/2):
    pygame.draw.rect(DISPLAY, color, pygame.Rect(
        posX-width/2, posY, width,  height))

    assert width < 1280 and height < 720, "The button cannot be larger than the width and height of the game"
    assert posX <= (1280-width) and posY < (720 -
                                            height), "The button must be placed in the game region"

    buttonText = fontSize.render(btnType, True, WHITE)

    DISPLAY.blit(buttonText, (posX - buttonText.get_width()/2,
                 posY + (height/2 - buttonText.get_height()/2)))
