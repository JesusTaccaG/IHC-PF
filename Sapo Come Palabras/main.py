import pygame
import sys
import math
from os import system
import numpy as np
from pygame.locals import *
from Game import *
from config import *
#from ejecutar import *
import threading

WIDTH=640
HEIGHT=480

def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init()
    pygame.init()
    pygame.display.set_caption("Sapo come palabras")
    juego = config_game() #configuracion inicial del juego- escenarios, botones, etc ( mejor miralo por ti mismo )
    pygame.key.set_repeat(1, 80)
    clock = pygame.time.Clock()
    while True:
        tick = clock.tick(60)
        juego.Mostrar_Escenario()           # muestra TODO 
        run_escenarios(juego)  # hace funcionar TODO
        pygame.display.flip()

if __name__ == "__main__":
    main()
