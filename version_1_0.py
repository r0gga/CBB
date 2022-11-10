# Benötigte Module
import pygame
import os
import random
from random import *

# Aussehen des Fenster
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oskar ist doof")
coordinates = []
#Farben
GREENISH = (144, 238, 144)

# Aktualisierungsrate
FPS = 60

# Surfaces
COFFEE_BIKE_IMAGE = pygame.image.load(
    os.path.join('Assets', 'CB.png'))

BES_IMAGE = pygame.image.load(
    os.path.join('Assets', 'bes.png'))

def new_spawn_bes():
    for p in range(100):
            x = randint(0, 849)
            y = randint(0, 449)
            z = x, y
            coordinates.append(z)

def new_spawn():
    x = randint(0, 849)
    y = randint(0, 449)
    z = x, y
    return z

# Gibt random Spawnpunkt
SPAWN = new_spawn()

def draw_bes():
    for i in range(100):
        WIN.blit(BES_IMAGE, (coordinates[i]))

# Sorgt für das Visuelle im Frame
def draw_window():
    WIN.fill(GREENISH)
    draw_bes()
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
        new_spawn_bes()
        new_spawn()
        draw_window()

    pygame.quit()

if __name__ == '__main__':
    main()

