import pygame
import sys

WIDTH = 1280
HEIGHT = 720
BLACK = (0, 0, 0)
GREY = (105, 105, 105)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

FPS = 60
CLOCK = pygame.time.Clock()
DISPLAY = pygame.display.set_mode([WIDTH, HEIGHT])


def terminate():
    pygame.quit()
    sys.exit()
