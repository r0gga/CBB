import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

MENU_IMAGE = pygame.image.load(
    os.path.join('Assets', 'menu.png'))
MENU = pygame.transform.scale(MENU_IMAGE, (1, 1))

def menu():
    WIN.blit(MENU, (450, 250))
