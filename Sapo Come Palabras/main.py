import pygame
import sys
import math
from os import system
import numpy as np
from pygame.locals import *
from escenario import *
from boton import *
from Game import *
from monita_musical import *
from config import *
from nenufar import *
from frog import *
import threading

WIDTH=640
HEIGHT=480

def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init()
    pygame.init()
    pygame.display.set_caption("Sapo come palabras")

    juego = config_game()

    pygame.key.set_repeat(1, 80)
    clock = pygame.time.Clock()

    while True:
        tick = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        juego.Mostrar_Escenario()
        juego.Escenario_Actual.func(juego)
        pygame.display.flip()
            


if __name__ == "__main__":
    main()
