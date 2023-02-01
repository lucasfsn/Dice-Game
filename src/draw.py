from src.settings import *


def displayItem(item, height):
    assert height < 720, "The item must be placed on the game screen"

    return DISPLAY.blit(item, ((WIDTH/2-item.get_width()/2), height))


def renderFont(size):
    return pygame.font.Font('fonts/JetBrainsMono.ttf', size)


def backGround(name):
    return DISPLAY.blit(pygame.image.load(f'images/{name}.jpg'), (0, 0))


def displayStats(name, points, turnPoints, x):
    allPoints = renderFont(35).render(
        f'{name}: {points}', True, BLACK)
    DISPLAY.blit(allPoints, (x-(len(name)*7), 225))
    DISPLAY.blit(renderFont(20).render('CURRENT', True, BLACK), (x, 300))
    DISPLAY.blit(renderFont(20).render(
        f'{turnPoints}', True, BLACK), (x+35, 325))
