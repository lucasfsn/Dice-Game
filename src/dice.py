import random
import pygame
from src.settings import DISPLAY


def displayDice(num):
    DISPLAY.blit(
        pygame.image.load(
            f'images/dice/dice-{num}.png'), (610, 300))
    assert num >= 0 and num <= 6, "No dice image found"


def rollDice():
    return random.randint(1, 6)
