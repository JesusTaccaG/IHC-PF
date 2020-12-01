import pygame
import sys
import math
import numpy as np
from pygame.locals import *
from escenario import *
from boton import *

WIDTH=640
HEIGHT=480

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sapo come palabras")
    escenario01 = Escenario(0, 0, WIDTH, HEIGHT)
    escenario01.update_image("Images/Fondos/swamp_01.jpg")

    boton01 = Boton(270,190,100,100)
    boton01.update_image("Images/Botones/0.png")
    pygame.key.set_repeat(1, 80)
    clock = pygame.time.Clock()

    while True:
        tick = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(escenario01.image2, (escenario01.x, escenario01.y))
        screen.blit(boton01.image2, (boton01.x, boton01.y))
        pygame.display.flip()


if __name__ == "__main__":
    main()