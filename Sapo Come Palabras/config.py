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
import threading
import glob
WIDTH=640
HEIGHT=480
def armar_escenario_01():
    Escenario = 4
    return 
def config_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    juego = Game(screen)
    Esc1 = glob.glob("Images/Fondos/*.jpg")
    Esc2 = glob.glob("Images/Fondos/*.png")
    for i in Esc1:
        escenary = Escenario(0,0,WIDTH,HEIGHT)
        escenary.update_image(i)
        juego.Agregar_Escenario(escenary)
    for i in Esc2:
        escenary = Escenario(0,0,WIDTH,HEIGHT)
        escenary.update_image(i)
        juego.Agregar_Escenario(escenary)
    juego.Cambiar_Escenario(2,0)
    return juego