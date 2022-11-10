# Benötigte Module
import pygame
import os
import random
from random import *

# Aussehen des Fenster
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oskar ist doof")

#Farben
GREENISH = (144, 238, 144)

# Aktualisierungsrate
FPS = 60

# Surfaces
COFFEE_BIKE_IMAGE = pygame.image.load(
    os.path.join('Assets', 'CB.png'))

# Random Spawn für das CB
def new_spawn():
    x = randint(0, 849)
    y = randint(0, 449)
    z = x, y
    return z

# Gibt random Spawnpunkt
SPAWN = new_spawn()

# Sorgt für das Visuelle im Frame
def draw_window():
    WIN.fill(GREENISH)
    WIN.blit(COFFEE_BIKE_IMAGE, (SPAWN))
    pygame.display.update()

# Mainloop
def main ():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        new_spawn()
        draw_window()

    pygame.quit()

if __name__ == '__main__':
    main()

