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
from frog import *
from nenufar import *
import threading
import glob
from Cartel import *
WIDTH=640
HEIGHT=480
def armar_modo_02():
    mon_mus = Monita_Musical(50,50,100,100)
    mon_mus.update_image('Images/Personajes/mensajero.png')
    mon_mus.update_audio('sounds/Palabras/palabra_01.mp3')
    sap = Frog(270,190,50,50,"Images/Personajes/ranita.png")
    fuente = pygame.font.Font(None, 25)
    numero_de_fotogramas = 0
    tasa_fotogramas = 60
    tiempo_segundos = 90
    cartel = Cartel(WIDTH-250,HEIGHT-150,250,150,fuente,numero_de_fotogramas,tasa_fotogramas,tiempo_segundos)
    cartel.update_image("Images/Recursos/cartel.png")
    Mod = Modalidad_01(0,0,WIDTH,HEIGHT,sap,mon_mus, cartel)
    Mod.update_image('Images/Fondos/lake_02.png')
    A = ['pro','ba','ble','men','te']
    posx=0
    for i in A:
        fe = np.random.rand(2)
        posy=180+120*fe[1]
        nenu = Nenufar(int(posx),int(posy),100,100)
        nenu.update_image('Images/Recursos/nenufar.png','Images/Recursos/nenufar_celeste.png','Images/Recursos/letrero_individual.png')
        nenu.cambiar_palabra(i)
        Mod.agregar_nenufar(nenu)
        posx+=100
    boton01 = Boton(550,20,75,75)
    boton01.update_image("Images/Botones/6.png")
    Mod.agregar_boton(boton01)
    return Mod
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
    juego.Agregar_M_02(armar_modo_02())
    juego.Cambiar_Escenario(0,3)
    return juego