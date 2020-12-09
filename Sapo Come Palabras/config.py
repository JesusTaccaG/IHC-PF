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
from boton import *
WIDTH=640
HEIGHT=480
#inicio donde comienza el juego
def inicio():
    init = Escenario(0 ,0, WIDTH, HEIGHT)
    init.update_image('Images/Fondos/swamp_01.jpg')
    boton_play = Boton(280,200,80,80)
    boton_play.update_image('Images/Botones/0.png')
    boton_play.dirige_a([1,0])
    init.agregar_boton(boton_play)
    return init
#escenario para los modos
#0 == Escenarios
#1 == Modalidad 1
#2 == Modalidad 2
#3 == Modalidad 3
def pant_modos():
    init = Escenario(0 ,0, WIDTH, HEIGHT)
    init.update_image('Images/Fondos/swamp_01.jpg')
    boton_atras = Boton(20,20,50,50)
    boton_atras.update_image('Images/Botones/8.png')
    boton_atras.dirige_a([0,0])
    boton_modo_01 = Boton(50,100,150,280)
    boton_modo_01.update_image("Images/Recursos/opacador.png")
    boton_modo_02 = Boton(245,100,150,280)
    boton_modo_02.update_image("Images/Recursos/opacador.png")
    boton_modo_03 = Boton(440,100,150,280)
    boton_modo_03.update_image("Images/Recursos/opacador.png")
    #[numeor del escenario, tipo de escenario]
    boton_modo_03.dirige_a([2,0])
    init.agregar_boton(boton_atras)
    init.agregar_boton(boton_modo_01)
    init.agregar_boton(boton_modo_02)
    init.agregar_boton(boton_modo_03)
    return init
#escenario de los niveles
def Niveles_Mod01():
    init =Escenario(0, 0, WIDTH, HEIGHT)
    init.update_image('Images/Fondos/swamp_01.jpg')
    boton_atras = Boton(20,20,50,50)
    boton_atras.update_image('Images/Botones/8.png')
    boton_atras.dirige_a([1,0])
    for i in range(15):
        a = np.floor(i/5)
        b = i%5
        nivel = Boton(80+(b*95),80+(a*120),80,100)
        nivel.update_image("Images/Recursos/opacador.png")
        if i==0:
            nivel.dirige_a([0,3])
        init.agregar_boton(nivel)
    init.agregar_boton(boton_atras)
    return init
#pausa de los escenarios
def inter_pausa():
    init = Escenario(0,0,WIDTH,HEIGHT)
    init.update_image("Images/Recursos/opacador.png")
    Ven_Emer = Boton(140,100,360,280)
    Ven_Emer.update_image("Images/Recursos/ventana_emergente.png")
    boton_Configuracion = Boton(200, 170, 50, 50)
    boton_Configuracion.update_image('Images/Botones/32.png')
    boton_Reintentar = Boton(200, 230, 50, 50)
    boton_Reintentar.update_image('Images/Botones/36.png')
    boton_Niveles = Boton(200, 290, 50, 50)
    boton_Niveles.update_image('Images/Botones/15.png')
    boton_Niveles.dirige_a([2,0])
    boton_exit = Boton(450,125,50,50)
    boton_exit.update_image('Images/Botones/33_r.png')
    boton_exit.tipo = 'exit'
    init.agregar_boton(Ven_Emer)
    init.agregar_boton(boton_Configuracion)
    init.agregar_boton(boton_Reintentar)
    init.agregar_boton(boton_Niveles)
    init.agregar_boton(boton_exit)
    return init

def armar_modo_02():
    mon_mus = Monita_Musical(50,50,100,100)
    mon_mus.update_image('Images/Personajes/mensajero.png')
    mon_mus.update_audio('sounds/Palabras/palabra_01.mp3')
    sap = Frog(170,370,80,80,"Images/Personajes/ranita.png")
    nenu_sapo = Boton(145,340,150,150)
    nenu_sapo.update_image("Images/Recursos/nenufar.png")
    fuente = pygame.font.Font(None, 25)
    numero_de_fotogramas = 0
    tasa_fotogramas = 60
    tiempo_segundos = 90
    cartel = Cartel(WIDTH-250,HEIGHT-150,250,150,fuente,numero_de_fotogramas,tasa_fotogramas,tiempo_segundos)
    cartel.update_image("Images/Recursos/cartel.png")
    Mod = Modalidad_01(0,0,WIDTH,HEIGHT,sap,mon_mus, cartel,[nenu_sapo])
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
    boton01.tipo = "pause"
    Mod.agregar_boton(boton01)
    Mod.scr_pause=inter_pausa()
    return Mod


def config_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    juego = Game(screen)
    juego.Agregar_Escenario(inicio())
    juego.Agregar_Escenario(pant_modos())
    juego.Agregar_Escenario(Niveles_Mod01())
    juego.Agregar_M_02(armar_modo_02())
    juego.Cambiar_Escenario(0,0)

    return juego