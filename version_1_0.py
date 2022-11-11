# Benötigte Module
import pygame
import os
from random import *
from Classes.button import Button
import Menu
import runpy


# Aussehen des Fenster
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation V.0.6") #Oskar ist doof
coordinates = []
#Farben
GREENISH = (144, 238, 144)

# Aktualisierungsrate
FPS = 60
BUTTON_WIDTH, BUTTON_HEIGHT = 55, 45

# Surfaces
COFFEE_BIKE_IMAGE = pygame.image.load(
    os.path.join('Assets', 'CB.png'))

BES_IMAGE = pygame.image.load(
    os.path.join('Assets', 'bes.png'))

PAUSE_IMAGE = pygame.image.load(
    os.path.join('Assets', 'pause.png'))
PAUSE = pygame.transform.scale(PAUSE_IMAGE, (555, 355))

MENU_IMAGE = pygame.image.load(
    os.path.join('Assets', 'menu.png'))
MENU = pygame.transform.scale(MENU_IMAGE, (4000, 2000))

paus_e = Button(5, 5, PAUSE)

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

# Gibt random Spawnpunkt CB
SPAWN = new_spawn()

def draw_bes():
    for i in range(100):
        WIN.blit(BES_IMAGE, (coordinates[i]))

# Sorgt für das Visuelle im Frame
def draw_window():
    WIN.fill(GREENISH)
    draw_bes()
    if paus_e.draw():
        WIN.blit(MENU, (350, 50))
    WIN.blit(COFFEE_BIKE_IMAGE, SPAWN)
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