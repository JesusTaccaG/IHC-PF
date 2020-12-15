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
from esc_mod_02 import *
import random

lst1=[['pro','ba','ble','men','te'],["Pa","ci","fi","ca","dor"],["Te","le","fo","ne","ma "],["Res","pi","ra","de","ro "],["Pa","ra","bó","li","ca "],["Com","pu","ta","do","ra"],["Bi","blio","gra","fí","a "],["Pa","ra","güe","rí","a "],["dis","tan","cia","mien","to "],["Ar","chi","va","do","ra"],["Tran","sa","tlán","ti","co"],["Tro","que","la","do","ra"],["Re","cep","cio","nis","ta"],["Se","cre","ta","ria","do"],["No","ti","fi","ca","ción"],["Cul","tu","ri","za","ción"],["Pro","tec","cion","is","ta "],["Re","ver","be","ra","ción "],["No","men","cla","tu","ra"],["A","sig","na","tu","ra"],["Li","cen","cia","tu","ra"],["Ba","chi","lle","ra","to"],["U","ni","ver","si","dad"],["Es","pe","cia","li","dad"],["Tri","go","no","me","tría"],["Ma","te","má","ti","cas"],["As","tro","no","mí","a"],["Te","ra","péu","ti","co"],["Qui","mio","te","ra","pia"],["Re","la","ti","vi","dad"],["Dis","co","grá","fi","co"],["Te","le","vi","so","ra"],["Pe","rio","dís","ti","co"],["Te","le","vi","si","vo"],["In","qui","si","ti","vo"],["Cir","cun","fe","ren","cia "],["In","te","li","gen","cia "]]

WIDTH=640
HEIGHT=480
#inicio donde comienza el juego
def inicio():
    init = Escenario(0 ,0, WIDTH, HEIGHT)
    init.update_image('Images/Fondos/swamp_01.jpg')
    boton_play = Boton(280,200,80,80)
    boton_play.update_image('Images/Botones/0.png')
    boton_play.dirige_a([1,0]) #pantalla rpincipal -> modos de juego
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
    boton_modo_01 = Boton(30,100,180,300)
    boton_modo_01.update_image("Images/Recursos/pizarra1.png")
    boton_modo_02 = Boton(225,100,180,300)
    boton_modo_02.update_image("Images/Recursos/pizarra2.png")
    boton_modo_03 = Boton(420,100,180,300)
    boton_modo_03.update_image("Images/Recursos/pizarra3.png")
    #[numeor del escenario, tipo de escenario]
    boton_modo_01.dirige_a([2,0])
    boton_modo_02.dirige_a([3,0])
    boton_modo_03.dirige_a([4,0])
    init.agregar_boton(boton_atras)
    init.agregar_boton(boton_modo_01)
    init.agregar_boton(boton_modo_02)
    init.agregar_boton(boton_modo_03)
    return init
#---------------------------------------------------------------------Pantallas de niveles por modo de juego
def Niveles_Mod01():
    init =Escenario(0, 0, WIDTH, HEIGHT)
    init.update_image('Images/Fondos/swamp_01.jpg')
    boton_atras = Boton(20,20,50,50)
    boton_atras.update_image('Images/Botones/8.png')
    boton_atras.dirige_a([1,0])
    for i in range(15):
        a = np.floor(i/5)
        b = i%5
        nivel = Boton(80+(b*95),80+(a*120),100,100)
        nivel.update_image("Images/Recursos/nivelbloqueado.png")
        if i==0:
            nivel.dirige_a([0,1])
            nivel.update_image("Images/Recursos/nivel0estrellas.png")
        init.agregar_boton(nivel)
    init.agregar_boton(boton_atras)
    return init

def Niveles_Mod02():
    init =Escenario(0, 0, WIDTH, HEIGHT)
    init.update_image('Images/Fondos/swamp_01.jpg')
    boton_atras = Boton(20,20,50,50)
    boton_atras.update_image('Images/Botones/8.png')
    boton_atras.dirige_a([1,0])
    for i in range(15):
        a = np.floor(i/5)
        b = i%5
        nivel = Boton(80+(b*95),80+(a*120),100,100)
        nivel.update_image("Images/Recursos/nivelbloqueado.png")
        if i==0:
            nivel.dirige_a([0,2])
            nivel.update_image("Images/Recursos/nivel0estrellas.png")
        init.agregar_boton(nivel)
    init.agregar_boton(boton_atras)
    return init
def Niveles_Mod03():
    init =Escenario(0, 0, WIDTH, HEIGHT)
    init.update_image('Images/Fondos/swamp_01.jpg')
    boton_atras = Boton(20,20,50,50)
    boton_atras.update_image('Images/Botones/8.png')
    boton_atras.dirige_a([1,0])
    for i in range(15):
        a = np.floor(i/5)
        b = i%5
        nivel = Boton(80+(b*95),80+(a*120),100,100)
        nivel.update_image("Images/Recursos/nivelbloqueado.png")
        if i==0:
            nivel.dirige_a([0,3])
            nivel.update_image("Images/Recursos/nivel0estrellas.png")
        init.agregar_boton(nivel)
    init.agregar_boton(boton_atras)
    return init
#---------------------------------------------------------------------pausa de los escenarios
def inter_pausa(retorno,niv):
    init = Escenario(0,0,WIDTH,HEIGHT)
    init.update_image("Images/Recursos/opacador.png")
    Ven_Emer = Boton(140,100,360,280)
    Ven_Emer.update_image("Images/Recursos/ventana_emergente.png")
    boton_Configuracion = Boton(200, 170, 50, 50)
    boton_Configuracion.update_image('Images/Botones/32.png')
    boton_Reintentar = Boton(200, 230, 50, 50)
    boton_Reintentar.update_image('Images/Botones/36.png')
    boton_Reintentar.orden("reiniciar")
    boton_Reintentar.dirige_a(niv)
    boton_Niveles = Boton(200, 290, 50, 50)
    boton_Niveles.update_image('Images/Botones/15.png')
    boton_Niveles.dirige_a(retorno)
    boton_Niveles.orden("salir")
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
    cartel = Cartel(WIDTH-250,HEIGHT-110,250,130,fuente,numero_de_fotogramas,tasa_fotogramas,tiempo_segundos)
    cartel.update_image("Images/Recursos/cartel.png")
    Mod = Modalidad_01(0,0,WIDTH,HEIGHT,sap,mon_mus, cartel,[nenu_sapo])
    Mod.update_image('Images/Fondos/lake_02.png')
    xrand=random.randrange(0,100)%37
    A = lst1[xrand]
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
    Mod.scr_pause=inter_pausa([4,0],[0,3])
    return Mod

def armar_modo_01():
    init = Modalidad_02(0,0,WIDTH,HEIGHT,1)
    init.update_image('Images/Fondos/lake_01.jpg')
    list_m = ['c','s','z']
    list_p = [('conducir','condu','ir'), ('aducir','adu','ir'), 
                ('traducir','tradu','ir'), ('esparcir','espar','ir'), 
                ('producir','produ','ir')]
    for a,b in enumerate(list_m):
        mos = Mosca(150+a*100,150,50,50)
        mos.palabra=b
        init.agregar_mos(mos)
    for a,b in enumerate(list_p):
        cart = Cartel_01(490,330,150,150)
        cart.palabra = b
        init.agregar_cart(cart)
    boton_help  = Boton(20,20,50,50)
    boton_help.update_image('Images/Botones/23.png')
    boton_pause = Boton(570,20,50,50)
    boton_pause.update_image('Images/Botones/6.png')
    init.agregar_boton(boton_help)
    init.agregar_boton(boton_pause)
    return init
    

def config_game():  
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    juego = Game(screen)                                #se a creado el buffer del juego y se asigno al GAME
    juego.Agregar_Escenario(inicio())                   
    juego.Agregar_Escenario(pant_modos())
    juego.Agregar_Escenario(Niveles_Mod01())
    juego.Agregar_Escenario(Niveles_Mod02())
    juego.Agregar_Escenario(Niveles_Mod03())
    juego.Agregar_M_02(armar_modo_02())
    juego.Agregar_M_01(armar_modo_01())
    juego.Cambiar_Escenario(0,0)                        #el juego no tiene una ventana predefinida asi que se
                                                        #asigna la de la funcion inicio()
    return juego

#Aca se hace las funcionalidades
def run_escenarios(juego):
    #mod sapo come moscas con palabras
    if juego.Escenario_Actual.ID=='mod2':
        for i in juego.Escenario_Actual.Botones:
            i.func(juego)
        juego.Escenario_Actual.sapo.func(juego)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() #salir del juego
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    juego.Escenario_Actual.sapo.presiono=True

    #el sapo que salta
    elif juego.Escenario_Actual.ID=="mod3":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() #salir del juego
        if not juego.Escenario_Actual.pauso:
            juego.Escenario_Actual.Monita_Musical.si_clickea()
            for i in juego.Escenario_Actual.Nenufares:
                if i.nenufar_click():
                    xn=i.x+10
                    yn=i.y+30
                    juego.Escenario_Actual.Sapo.jump(juego.screen,xn,yn)
                    juego.Escenario_Actual.Cartel.aumentar_palabra(i.palabra)
            juego.Escenario_Actual.Cartel.iniciar_contador(juego.screen)
            juego.Escenario_Actual.Sapo.Croak()
            for i in juego.Escenario_Actual.Botones:
                i.func(juego)
        else:
            for i in juego.Escenario_Actual.scr_pause.Botones[1:]:
                if True==i.func(juego):
                    if i.objetivo=="reiniciar":
                        juego.Quitar_M_02()
                        juego.Agregar_M_02(armar_modo_02())
                        juego.Escenario_Actual.pauso=False
                    if i.objetivo=="salir":
                        juego.Quitar_M_02()
                        juego.Agregar_M_02(armar_modo_02())
    elif juego.Escenario_Actual.ID=="esc":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() #salir del juego
        for i in juego.Escenario_Actual.Botones:
            i.func(juego) 
    