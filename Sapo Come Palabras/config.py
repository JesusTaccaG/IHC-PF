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
from esc_mod_00 import *
import random
from imagess import *

lst1=[['pro','ba','ble','men','te'],["pa","ci","fi","ca","dor"],["te","le","fo","ne","ma"],["res","pi","ra","de","ro"],["pa","ra","bó","li","ca"],["com","pu","ta","do","ra"],["bi","blio","gra","fí","a"],["pa","ra","güe","rí","a"],["dis","tan","cia","mien","to"],["ar","chi","va","do","ra"],["tran","sa","tlán","ti","co"],["tro","que","la","do","ra"],["re","cep","cio","nis","ta"],["se","cre","ta","ria","do"],["no","ti","fi","ca","ción"],["cul","tu","ri","za","ción"],["pro","tec","cion","is","ta"],["re","ver","be","ra","ción"],["no","men","cla","tu","ra"],["a","sig","na","tu","ra"],["li","cen","cia","tu","ra"],["ba","chi","lle","ra","to"],["u","ni","ver","si","dad"],["es","pe","cia","li","dad"],["tri","go","no","me","tría"],["ma","te","má","ti","cas"],["as","tro","no","mí","a"],["te","ra","péu","ti","co"],["qui","mio","te","ra","pia"],["re","la","ti","vi","dad"],["dis","co","grá","fi","co"],["te","le","vi","so","ra"],["pe","rio","dís","ti","co"],["te","le","vi","si","vo"],["in","qui","si","ti","vo"],["cir","cun","fe","ren","cia"],["in","te","li","gen","cia"]]

WIDTH=640
HEIGHT=480

def unsort(l):
    return random.sample(l, len(l))

#inicio donde comienza el juego
def inicio():
    init = Escenario(0 ,0, WIDTH, HEIGHT)
    ##Imagen inicial de pantalla
    init.update_image('Images/Fondos/swamp_01.jpg')
    #Imagenes de rana y mosca
    img1 = Imagess(280,200,100,100)
    img1.update_image("Images/Personajes/ranita.png",'Images/Personajes/ranita.png',"Images/Recursos/mosca.png")
    #Imagen de letrero
    letrero = Boton(220,-100,200,200)
    letrero.update_image('Images/Recursos/cartel_c.png')
    #Mosca cartel xD
    mosca_cartel = Boton(230,105,170,170)
    mosca_cartel.update_image('Images/Recursos/mosca_letrero.png')
    #flecha de opciones
    flecha_opciones = Boton(590,350,50,50)
    flecha_opciones.update_image('Images/Recursos/flecha.png')
    flecha_opciones.dirige_a([5,0])
    #Boton de play
    boton_play = Boton(285,200,65,65)
    boton_play.update_image('Images/Botones/0.png')
    boton_play.dirige_a([1,0]) #pantalla principal -> modos de juego
    #Dibujar en la pantalla
    init.agregar_boton(letrero)
    init.agregar_boton(img1)
    init.agregar_boton(mosca_cartel)
    init.agregar_boton(boton_play)
    init.agregar_boton(flecha_opciones)
    return init
def inicio2():
    init = Escenario(0 ,0, WIDTH, HEIGHT)
    ##Imagen inicial de pantalla
    init.update_image('Images/Fondos/swamp_01.jpg')
    #Imagenes de rana y mosca
    img1 = Imagess(280,200,100,100)
    img1.update_image("Images/Personajes/ranita.png",'Images/Personajes/ranita.png',"Images/Recursos/mosca.png")
    #Imagen de letrero
    letrero = Boton(220,-100,200,200)
    letrero.update_image('Images/Recursos/cartel_c.png')
    #Mosca cartel xD
    mosca_cartel = Boton(230,105,170,170)
    mosca_cartel.update_image('Images/Recursos/mosca_letrero.png')
    #flecha de opciones
    flecha_opciones = Boton(379,350,55,55)
    flecha_opciones.update_image('Images/Recursos/flecha.png')
    flecha_opciones.dirige_a([0,0])
    #Opcion Logros
    Logros = Boton(445,355,40,40)
    Logros.update_image('Images/Recursos/logros.png')
    Logros.dirige_a([7,0])
    #Opcion Configuracion
    Configuracion = Boton(500,348,55,55)
    Configuracion.update_image('Images/Recursos/configuracion.png')
    Configuracion.dirige_a([9,0])
    #Opcion Tienda
    Tienda = Boton(560,340,70,70)
    Tienda.update_image('Images/Recursos/tienda.png')
    Tienda.dirige_a([6,0])
    #Panel de opciones
    panel_opciones = Boton(430,350,200,50)
    panel_opciones.update_image('Images/Recursos/franja_verde.png')
    #Boton de play
    boton_play = Boton(285,200,65,65)
    boton_play.update_image('Images/Botones/0.png')
    boton_play.dirige_a([1,0]) #pantalla principal -> modos de juego
    #Dibujar en la pantalla
    init.agregar_boton(letrero)
    init.agregar_boton(img1)
    init.agregar_boton(mosca_cartel)
    init.agregar_boton(boton_play)
    init.agregar_boton(flecha_opciones)
    init.agregar_boton(panel_opciones)
    init.agregar_boton(Logros)
    init.agregar_boton(Configuracion)
    init.agregar_boton(Tienda)
    return init
def Tienda():
    init = Escenario(0 ,0, WIDTH, HEIGHT)
    ##Imagen inicial de pantalla
    init.update_image('Images/Fondos/tiendita.png')
    #boton cerrar
    boton_cerrar = Boton(545,30,65,65)
    boton_cerrar.update_image('Images/Recursos/cerrar.png')
    boton_cerrar.dirige_a([0,0]) #pantalla principal
    ##Estanteria
    Estanteria = Boton(20,20,450,450)
    Estanteria.update_image('Images/Recursos/estante.png')
    ##Rana Compradora
    Rana_compra = Boton(300,125,350,350)
    Rana_compra.update_image('Images/Recursos/ranacompra.png')
    ## Item rana roja
    Rana_roja = Boton(100,90,80,80)
    Rana_roja.update_image('Images/Recursos/ranaroja.png')
    ## Item rana amarilla
    Rana_amarilla = Boton(100,240,80,80)
    Rana_amarilla.update_image('Images/Recursos/ranamarialla.png')
    ## Item rana azul
    Rana_azul = Boton(230,90,80,80)
    Rana_azul.update_image('Images/Recursos/ranazul.png')
    ## Item rana camaleon
    Camaleon = Boton(230,240,80,80)
    Camaleon.update_image('Images/Recursos/camaleon.png')
    #Dibujar en la pantalla
    init.agregar_boton(boton_cerrar)
    init.agregar_boton(Estanteria)
    init.agregar_boton(Rana_compra)
    init.agregar_boton(Rana_roja)
    init.agregar_boton(Rana_amarilla)
    init.agregar_boton(Rana_azul)
    init.agregar_boton(Camaleon)
    return init
def Logros():
    init = Escenario(0 ,0, WIDTH, HEIGHT)
    ##Imagen inicial de pantalla
    init.update_image('Images/Fondos/fondo_inicial.png')
    cuadro_texto = Boton(70,-20,500,500)
    cuadro_texto.update_image('Images/Recursos/ventana_emergente.png')
    #Titulo de los logros
    texto_normal = Boton(240,20,150,60)
    texto_normal.update_image('Images/Recursos/titulo_logros.png')
    #boton cerrar
    boton_cerrar = Boton(545,30,65,65)
    boton_cerrar.update_image('Images/Recursos/cerrar.png')
    boton_cerrar.dirige_a([0,0]) #pantalla principal
    #Logro 1
    logro_1 = Boton(185,140,60,60)
    logro_1.update_image('Images/Recursos/logro1.png')
    #Logro 2
    logro_2 = Boton(185,220,60,60)
    logro_2.update_image('Images/Recursos/logro2.png')
    #Logro 3
    logro_3 = Boton(185,300,60,60)
    logro_3.update_image('Images/Recursos/logro3.png')
    #Logro 1 texto
    logro_1texto = Boton(265,140,200,60)
    logro_1texto.update_image('Images/Recursos/logro1texto.png')
    #Logro 2 texto
    logro_2texto = Boton(265,220,200,60)
    logro_2texto.update_image('Images/Recursos/logro2texto.png')
    #Logro 3 texto
    logro_3texto = Boton(265,300,200,60)
    logro_3texto.update_image('Images/Recursos/logro3texto.png')
    #Flecha Atras
    Flecha_Atras = Boton(125,170,40,180)
    Flecha_Atras.update_image('Images/Recursos/flecha2.png')
    Flecha_Atras.dirige_a([8,0])
    #Flecha Adelante
    Flecha_Adelante = Boton(480,170,40,180)
    Flecha_Adelante.update_image('Images/Recursos/flecha1.png')
    Flecha_Adelante.dirige_a([8,0])
    init.agregar_boton(boton_cerrar)
    init.agregar_boton(cuadro_texto)
    init.agregar_boton(texto_normal)
    init.agregar_boton(logro_1)
    init.agregar_boton(logro_2)
    init.agregar_boton(logro_3)
    init.agregar_boton(logro_1texto)
    init.agregar_boton(logro_2texto)
    init.agregar_boton(logro_3texto)
    init.agregar_boton(Flecha_Atras)
    init.agregar_boton(Flecha_Adelante)
    return init
def Logros_bloqueados():
    init = Escenario(0 ,0, WIDTH, HEIGHT)
    ##Imagen inicial de pantalla
    init.update_image('Images/Fondos/fondo_inicial.png')
    cuadro_texto = Boton(70,-20,500,500)
    cuadro_texto.update_image('Images/Recursos/ventana_emergente.png')
    #Titulo de los logros
    texto_normal = Boton(240,20,150,60)
    texto_normal.update_image('Images/Recursos/titulo_logros.png')
    #boton cerrar
    boton_cerrar = Boton(545,30,65,65)
    boton_cerrar.update_image('Images/Recursos/cerrar.png')
    boton_cerrar.dirige_a([0,0]) #pantalla principal
    #Logro 1
    logro_1 = Boton(185,140,60,60)
    logro_1.update_image('Images/Recursos/logro1bc.png')
    #Logro 2
    logro_2 = Boton(185,220,60,60)
    logro_2.update_image('Images/Recursos/logro2bc.png')
    #Logro 3
    logro_3 = Boton(185,300,60,60)
    logro_3.update_image('Images/Recursos/logro3bc.png')
    #Logro 1 texto
    logro_1texto = Boton(265,140,200,60)
    logro_1texto.update_image('Images/Recursos/logro1bctexto.png')
    #Logro 2 texto
    logro_2texto = Boton(265,220,200,60)
    logro_2texto.update_image('Images/Recursos/logro2bctexto.png')
    #Logro 3 texto
    logro_3texto = Boton(265,300,200,60)
    logro_3texto.update_image('Images/Recursos/logro3bctexto.png')
    #Flecha Atras
    Flecha_Atras = Boton(125,170,40,180)
    Flecha_Atras.update_image('Images/Recursos/flecha2.png')
    Flecha_Atras.dirige_a([7,0])
    #Flecha Adelante
    Flecha_Adelante = Boton(480,170,40,180)
    Flecha_Adelante.update_image('Images/Recursos/flecha1.png')
    Flecha_Adelante.dirige_a([7,0])
    init.agregar_boton(boton_cerrar)
    init.agregar_boton(cuadro_texto)
    init.agregar_boton(texto_normal)
    init.agregar_boton(logro_1)
    init.agregar_boton(logro_2)
    init.agregar_boton(logro_3)
    init.agregar_boton(logro_1texto)
    init.agregar_boton(logro_2texto)
    init.agregar_boton(logro_3texto)
    init.agregar_boton(Flecha_Atras)
    init.agregar_boton(Flecha_Adelante)
    return init
def Configuracion():
    init = Escenario(0 ,0, WIDTH, HEIGHT)
    ##Imagen inicial de pantalla
    init.update_image('Images/Fondos/fondo_inicial.png')
    #Titulo de los Configuracion
    texto_normal = Boton(220,20,190,60)
    texto_normal.update_image('Images/Recursos/titulo_configuracion.png')
    #Ventana basura
    cuadro_texto = Boton(70,-20,500,500)
    cuadro_texto.update_image('Images/Recursos/ventana_emergente.png')
    #boton cerrar
    boton_cerrar = Boton(545,30,65,65)
    boton_cerrar.update_image('Images/Recursos/cerrar.png')
    boton_cerrar.dirige_a([0,0]) #pantalla principal
    init.agregar_boton(boton_cerrar)
    init.agregar_boton(cuadro_texto)
    init.agregar_boton(texto_normal)
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
            nivel.niv=str(i+1)
            nivel.update_image("Images/Recursos/nivel0estrellas.png")
        nivel.objetivo=str(i+1)
        init.agregar_boton(nivel)
    init.agregar_boton(boton_atras)
    init.esc_niv=True
    return init
#---------------------------------------------------------------------pausa de los escenarios
def inter_pausa(retorno,niv):
    init = Escenario(0,0,WIDTH,HEIGHT)
    init.update_image("Images/Recursos/opacador.png")
    Ven_Emer = Boton(140,100,360,280)
    Ven_Emer.update_image("Images/Recursos/ventana_emergente.png")
    boton_Configuracion = Boton(230, 170, 162, 50)
    boton_Configuracion.update_image('Images/Botones/32_.png')
    boton_Reintentar = Boton(230, 230, 162, 50)
    boton_Reintentar.update_image('Images/Botones/36_.png')
    boton_Reintentar.orden("reiniciar")
    boton_Reintentar.dirige_a(niv)
    boton_Niveles = Boton(230, 290, 162, 50)
    boton_Niveles.update_image('Images/Botones/15_.png')
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
#---------------------------------------------------------------------final mensaje
def fin_juego(retorno,niv):
    init = Escenario(0,0,WIDTH,HEIGHT)
    init.update_image("Images/Recursos/opacador2.png")

    Ven_Emer = Boton(140,100,360,280)
    Ven_Emer.update_image("Images/Recursos/ventana_emergente.png")

    boton_Continuar = Boton(205, 270, 70, 70)
    boton_Continuar.update_image('Images/Botones/7.png')
    boton_Continuar.orden("continuar")
    boton_Continuar.dirige_a(retorno)

    boton_Reintentar = Boton(285, 270, 70, 70)
    boton_Reintentar.update_image('Images/Botones/36.png')
    boton_Reintentar.orden("reiniciar")
    boton_Reintentar.dirige_a(niv)

    boton_Niveles = Boton(365, 270, 70, 70)
    boton_Niveles.update_image('Images/Botones/15.png')
    boton_Niveles.dirige_a(retorno)
    boton_Niveles.orden("salir")

    estrella1 = Boton(210, 190, 70, 70)
    estrella1.update_image('Images/Recursos/estrella2.png')
    estrella1.noButton=True

    estrella2 = Boton(290, 160, 70, 70)
    estrella2.update_image('Images/Recursos/estrella2.png')
    estrella2.noButton=True

    estrella3 = Boton(370, 190, 70, 70)
    estrella3.update_image('Images/Recursos/estrella2.png')
    estrella3.noButton=True

    init.agregar_boton(Ven_Emer)
    init.agregar_boton(boton_Continuar)
    init.agregar_boton(boton_Reintentar)
    init.agregar_boton(boton_Niveles)
    init.agregar_boton(estrella1)
    init.agregar_boton(estrella2)
    init.agregar_boton(estrella3)

    return init

def inter_ayuda(nombre_animal,ayuda_animal):
    init = Cartel_ayuda(0,0,WIDTH,HEIGHT,nombre_animal,ayuda_animal)
    init.update_image("Images/Recursos/opacador.png")
    Ven_Emer = Boton(140,100,360,280)
    Ven_Emer.update_image("Images/Recursos/ventana_emergente.png")
    btn_animal = Boton(270,165,80,80)
    btn_animal.update_image('Images\m_animales/'+nombre_animal+'.png')
    boton_check = Boton(430,320,50,50)
    boton_check.update_image('Images/Botones/34.png')
    boton_check.tipo = 'check'
    boton_check.orden("aceptar")

    init.agregar_boton(Ven_Emer)
    init.agregar_boton(btn_animal)
    init.agregar_boton(boton_check)
    return init

def inter_resultado(nombre_animal,animal_tablero,tiempo_tablero):
    init = Cartel_resultado(0,0,WIDTH,HEIGHT,nombre_animal,animal_tablero,tiempo_tablero)
    init.update_image("Images/Recursos/opacador.png")
    Ven_Emer = Boton(140,100,360,280)
    Ven_Emer.update_image("Images/Recursos/ventana_emergente.png")
    
    boton_reloj = Boton(230, 175, 40, 40)
    boton_reloj.update_image('Images/Recursos/circulo_tiempo.png')

    boton_Configuracion = Boton(230, 280, 50, 50)
    boton_Configuracion.update_image('Images/Botones/32.png')
    boton_Reintentar = Boton(290, 280, 50, 50)
    boton_Reintentar.update_image('Images/Botones/36.png')
    boton_Reintentar.objetivo ="adios"
    boton_Reintentar.dirige_a([0,1])
    
    boton_siguiente = Boton(350, 280, 50, 50)
    boton_siguiente.update_image('Images/Botones/0.png')
    boton_siguiente.orden("reiniciar2")
    boton_siguiente.dirige_a([0,1])
    
    
    if len(nombre_animal)==len(animal_tablero):
        if nombre_animal==animal_tablero:
                for i in range(3):
                    est_b = Boton(230+i*60,220,50,50)
                    est_b.update_image('Images/Recursos/estrella_brillante.png')
                    init.estrellas.append(est_b)
        else:
            est_b1 = Boton(230,220,50,50)
            est_b1.update_image('Images/Recursos/estrella_brillante.png')
            est_b2 = Boton(290,220,50,50)
            est_b2.update_image('Images/Recursos/estrella_opaca.png')
            est_b3 = Boton(350,220,50,50)
            est_b3.update_image('Images/Recursos/estrella_opaca.png')
            init.estrellas.append(est_b1)
            init.estrellas.append(est_b2)
            init.estrellas.append(est_b3)
    elif nombre_animal[0:2]==animal_tablero[0:2]:
        est_b1 = Boton(230,220,50,50)
        est_b1.update_image('Images/Recursos/estrella_brillante.png')
        est_b2 = Boton(290,220,50,50)
        est_b2.update_image('Images/Recursos/estrella_brillante.png')
        est_b3 = Boton(350,220,50,50)
        est_b3.update_image('Images/Recursos/estrella_opaca.png')
        init.estrellas.append(est_b1)
        init.estrellas.append(est_b2)
        init.estrellas.append(est_b3)
    else:
        est_b1 = Boton(230,220,50,50)
        est_b1.update_image('Images/Recursos/estrella_opaca.png')
        est_b2 = Boton(290,220,50,50)
        est_b2.update_image('Images/Recursos/estrella_opaca.png')
        est_b3 = Boton(350,220,50,50)
        est_b3.update_image('Images/Recursos/estrella_opaca.png')
        init.estrellas.append(est_b1)
        init.estrellas.append(est_b2)
        init.estrellas.append(est_b3)
    init.agregar_boton(Ven_Emer)
    init.agregar_boton(boton_reloj)
    init.agregar_boton(boton_Configuracion)
    init.agregar_boton(boton_Reintentar)
    init.agregar_boton(boton_siguiente)
    
    return init

#rana con imagenes
def armar_modo_00():
    fuente = pygame.font.Font(None, 25)
    init = Modalidad_00(0,0,WIDTH,HEIGHT,1)
    init.update_image('Images/Fondos/river_02.jpg')
    list_animales = ['ajolote','ameba','archaeopteryx','ciempiés','cotorra','kiwi','pinzón','rodaballo','escorpión','pingüino']
    list_animales_ayuda=[
        'El ajolote es un lagarto de dos patas',
        'La ameba es un pequeño animal',
        'Archaeopteryx vivió hace millones de años.',
        'Pequeño animal, parecido al gusano',
        'Un tipo de loro de larga cola.',
        'Ave de plumas lanudas',
        'Pájaro cantor europeo',
        'Pez grande',
        'Signo de los que nacen en octubre',
        'Es de la familia de aves'
        ]
    # list_animales = ['or']
    n_animal = random.randrange(len(list_animales))
    print(n_animal)
    animal = Animal_00(20,150,100,100,list_animales[n_animal])
    init.agregar_animales(animal)
    cartel = Cartel_00(WIDTH-250,HEIGHT-110,250,130)
    cartel.establecer_tiempo(60) #Establecer tiempo de juego
    cartel.update_image("Images/Recursos/cartel.png")
    init.agregar_cart(cartel)

    n=2
    chunks = [list_animales[n_animal][i:i+n] for i in range(0, len(list_animales[n_animal]), n)]
    for a,b in enumerate(chunks):
        ran = random.randrange(100,150)
        ran_x , ran_y = random.choice([-1, 1]), random.choice([-1, 1])
        mos = Mosca_00(50+a*100,ran,50,50,fuente,ran_x,ran_y)
        mos.palabra = b
        init.agregar_mos(mos)
    
    boton_help  = Boton(20,20,50,50)
    boton_help.update_image('Images/Botones/23.png')

    boton_pause = Boton(570,20,50,50)
    boton_pause.update_image('Images/Botones/6.png')

    boton_pause.tipo = "pause"
    init.scr_pause=inter_pausa([2,0],[0,1])
    boton_help.tipo = "ayuda"
    init.scr_ayuda=inter_ayuda(list_animales[n_animal],list_animales_ayuda[n_animal])
    init.agregar_boton(boton_pause)
    init.agregar_boton(boton_help)
    return init

#rana que salta
def armar_modo_02(seed=None):
    mon_mus = Monita_Musical(50,50,100,100)
    mon_mus.update_image('Images/Personajes/mensajero.png')
    
    sap = Frog(170,370,80,80,"Images/Personajes/ranita.png")
    nenu_sapo = Boton(145,340,150,150)
    nenu_sapo.update_image("Images/Recursos/nenufar.png")
    fuente = pygame.font.Font(None, 25)
    numero_de_fotogramas = 0
    tasa_fotogramas = 60
    tiempo_segundos = 90
    cartel = Cartel(WIDTH-250,HEIGHT-110,250,130,fuente,numero_de_fotogramas,tasa_fotogramas,tiempo_segundos)
    cartel.update_image("Images/Recursos/cartel.png")
    xrand=random.randrange(0,100)%37
    A = lst1[xrand]
    if seed!=None:
        A=seed
    aud="sounds/palabras/"+A[0]+A[1]+A[2]+A[3]+A[4]+".mp3"

    print("audio---------------------- ",aud)
    try:
        mon_mus.update_audio(aud)
    except:
        mon_mus.update_audio("sounds/palabras/except.mp3")
    cartel.textooriginal=A
    A=unsort(A)
    posx=0
    
    Mod = Modalidad_01(0,0,WIDTH,HEIGHT,sap,mon_mus, cartel,[nenu_sapo])
    Mod.update_image('Images/Fondos/lake_02.png')
    
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
    Mod.scr_final=fin_juego([4,0],[0,3])
    Mod.niv_num=0
    return Mod
#modos completa la palabra
def armar_modo_01():
    init = Modalidad_02(0,0,WIDTH,HEIGHT,1)
    init.update_image('Images/Fondos/lake_01.jpg')
    list_m = ['c','s','z']
    list_p = [('conducir',['condu','ir']), ('aducir',['adu','ir']), 
                ('traducir',['tradu','ir']), ('esparcir',['espar','ir']), 
                ('producir',['produ','ir'])]
    for a,b in enumerate(list_m):
        mos = Mosca(150+a*100,150,50,50,b)
        init.agregar_mos(mos)
    for a,b in enumerate(list_p):
        cart = Cartel_01(440,330,200,150, b)
        if a==0:
            cart.activo=True
        init.agregar_cart(cart)
    boton_help  = Boton(20,20,50,50)
    boton_help.update_image('Images/Botones/23.png')
    boton_help.objetivo="ayuda"
    boton_pause = Boton(570,20,50,50)
    boton_pause.update_image('Images/Botones/6.png')
    boton_pause.objetivo="pausa"
    boton_niveles = Boton(250,270,40,40)
    boton_niveles.update_image('Images/Botones/15.png')
    boton_niveles.dirige_a([3,0])
    boton_reintentar = Boton(300,270,40,40)
    boton_reintentar.update_image('Images/Botones/31.png')
    boton_reintentar.dirige_a([0,2])
    boton_siguiente = Boton(350,270,40,40)
    boton_siguiente.update_image('Images/Botones/7.png')
    boton_lanza_1 = Boton(250,180,40,40)
    boton_lanza_1.update_image('Images/Recursos/circulo_1.png')
    boton_lanza_2 = Boton(300,180,40,40)
    boton_lanza_2.update_image('Images/Recursos/circulo_2.png')
    boton_tiempo = Boton(350,180,40,40)
    boton_tiempo.update_image('Images/Recursos/circulo_tiempo.png')
    for i in range(3):
        est_b = Boton(250+i*50,220,40,40)
        est_b.update_image('Images/Recursos/estrella_brillante.png')
        est_o = Boton(250+i*50,220,40,40)
        est_o.update_image('Images/Recursos/estrella_opaca.png')
        init.estrellas.append(est_b)
        init.estrellas.append(est_o)
    boton_cerrar = Boton(470,80,40,40)
    boton_cerrar.update_image('Images/Botones/33_r.png')
    boton_cerrar.objetivo='cerrar'
    temporal="REGLA DEL USO DE LA C \n Se usa la 'c' en las \n palabras terminadas en 'cir'"
    init.agregar_texto(temporal)
    boton_niveles02       = Boton(220,180,40,40)
    boton_niveles02.update_image('Images/Botones/15.png')
    boton_niveles02.dirige_a([3,0])
    boton_Configuracion02 = Boton(220,230,40,40)
    boton_Configuracion02.update_image('Images/Botones/32.png')
    #boton_Configuracion02.dirige_a([])
    boton_reintentar02    = Boton(220,280,40,40)
    boton_reintentar02.update_image('Images/Botones/31.png')
    boton_reintentar02.dirige_a([0,2])
    boton_exit02          = Boton(415,130,40,40)
    boton_exit02.update_image('Images/Botones/33_r.png')
    boton_exit02.objetivo='salir'
    init.agregar_boton(boton_help)
    init.agregar_boton(boton_pause)
    init.botones_01.append(boton_reintentar)
    init.botones_01.append(boton_siguiente)
    init.botones_01.append(boton_niveles)
    init.objetivos.append(boton_lanza_1)
    init.objetivos.append(boton_lanza_2)
    init.objetivos.append(boton_tiempo)
    init.botones_02.append(boton_cerrar)
    init.botones_03.append(boton_niveles02)
    init.botones_03.append(boton_Configuracion02)
    init.botones_03.append(boton_reintentar02)
    init.botones_03.append(boton_exit02)
    
    return init
    

def config_game():  
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    juego = Game(screen)                                #se a creado el buffer del juego y se asigno al GAME
    juego.Agregar_Escenario(inicio())                   
    juego.Agregar_Escenario(pant_modos())
    juego.Agregar_Escenario(Niveles_Mod01())
    juego.Agregar_Escenario(Niveles_Mod02())
    juego.Agregar_Escenario(Niveles_Mod03())
    
    juego.Agregar_Escenario(inicio2())
    juego.Agregar_Escenario(Tienda())
    juego.Agregar_Escenario(Logros())
    juego.Agregar_Escenario(Logros_bloqueados())
    juego.Agregar_Escenario(Configuracion())
    #Rana con imagenes
    juego.Agregar_M_00(armar_modo_00())
    #agregar modo rana que salta
    juego.Agregar_M_02(armar_modo_02())
    #agregar el modo completa la palabra
    juego.Agregar_M_01(armar_modo_01())
    juego.Cambiar_Escenario(0,0)                        #el juego no tiene una ventana predefinida asi que se
                                                        #asigna la de la funcion inicio()
    return juego

#Aca se hace las funcionalidades
def run_escenarios(juego):
    estrellasNIVEL=0
    desbloquear=False
    nivelActual=0
    if juego.Escenario_Actual.ID=="mod1":
        if not juego.Escenario_Actual.pauso and not juego.Escenario_Actual.ayuda:
            for i in juego.Escenario_Actual.Botones:
                i.func(juego)
        juego.Escenario_Actual.sapo.func(juego)
        list_moscas = juego.Escenario_Actual.moscas

        bool_termino_tiempo = juego.Escenario_Actual.Cartel[0].termino
        animal_actual = juego.Escenario_Actual.Animales[0].palabra
        animal_tablero = juego.Escenario_Actual.Cartel[0].letra
        tiempo_tablero = juego.Escenario_Actual.Cartel[0].segundos_totales
        
        #si termina el tiempo o ya comio todas las moscas
        if (bool_termino_tiempo or len(list_moscas)==0) and juego.Escenario_Actual.termino==False:
            juego.Escenario_Actual.src_resultado = inter_resultado(animal_actual,animal_tablero,tiempo_tablero)
            juego.Escenario_Actual.termino=True

        else:
            juego.Escenario_Actual.Cartel[0].iniciar_contador(juego.screen)

        #movimiento de moscas
        for a,b in enumerate(list_moscas):
            b.move()  
        for a,b in enumerate(list_moscas):
            if juego.Escenario_Actual.sapo.lengua.is_collided_with(b):
                list_moscas.pop(a)
                juego.Escenario_Actual.Cartel[0].aumentar_palabra(b.palabra)
        #pausa
        if juego.Escenario_Actual.pauso:
            for i in juego.Escenario_Actual.scr_pause.Botones[1:]:
                if True==i.func(juego):
                    if i.objetivo=="reiniciar":
                        juego.Quitar_M_00()
                        juego.Agregar_M_00(armar_modo_00())
                        juego.Escenario_Actual.pauso=False
                    if i.objetivo=="salir":
                        juego.Quitar_M_00()
                        juego.Agregar_M_00(armar_modo_00())
        elif juego.Escenario_Actual.ayuda:
            for i in juego.Escenario_Actual.scr_ayuda.Botones[1:]:
                    if True==i.func(juego):
                        if i.objetivo=="aceptar":
                            juego.Escenario_Actual.ayuda = False
        elif juego.Escenario_Actual.termino:
            for i in juego.Escenario_Actual.src_resultado.Botones[2:]:
                    if True==i.func(juego):
                        if i.objetivo=="adios":
                            juego.Quitar_M_00()
                            juego.Agregar_M_00(armar_modo_00())
                            juego.Escenario_Actual.termino=False
                        if i.objetivo=="reiniciar2":
                            juego.Quitar_M_00()
                            juego.Agregar_M_00(armar_modo_00())
                            juego.Escenario_Actual.termino=False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() #salir del juego
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    juego.Escenario_Actual.sapo.presiono=True

    #mod sapo come moscas con palabras
    if juego.Escenario_Actual.ID=='mod2':
        frog=juego.Escenario_Actual.sapo
        if not juego.Escenario_Actual.ayuda and not juego.Escenario_Actual.termino:
            for i in juego.Escenario_Actual.Botones:
                if i.func(juego):
                    if i.objetivo=='ayuda':
                        juego.Escenario_Actual.ayuda=True
                    if i.objetivo=='pausa':
                        juego.Escenario_Actual.pauso=True
        juego.Escenario_Actual.sapo.func(juego)

        for i in juego.Escenario_Actual.moscas:
            if i.vivo:
                i.movimiento(juego.Escenario_Actual)
                if not frog.atrapo_mosca and i.atrapado(frog.lengua.pfx,frog.lengua.pfy) and frog.sec>0:
                    #frog.atrapo_mosca=True
                    #frog.mosca_atrapada=i
                    frog.sec=-frog.sec
                    i.fue_atrapado=True
        for i in juego.Escenario_Actual.cartel:
            if i.activo:
                i.func()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() #salir del juego
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    if not juego.Escenario_Actual.sapo.presiono:
                        juego.Escenario_Actual.sapo.lenguetazo+=1
                    juego.Escenario_Actual.sapo.presiono=True
                    print(juego.Escenario_Actual.sapo.lenguetazo)
        if juego.Escenario_Actual.termino:
            for i in juego.Escenario_Actual.botones_01:
                temp=juego.Escenario_Actual
                if i.func(juego):
                    temp.reiniciar()
        elif juego.Escenario_Actual.ayuda:
            for i in juego.Escenario_Actual.botones_02:
                if i.func(juego):
                    if i.objetivo=='cerrar':
                        juego.Escenario_Actual.ayuda=False
        elif juego.Escenario_Actual.pauso:
            for i in juego.Escenario_Actual.botones_03:
                temp=juego.Escenario_Actual
                if i.func(juego):
                    if i.objetivo=='salir':
                        juego.Escenario_Actual.pauso=False
                    else:
                        temp.reiniciar()

    #el sapo que salta
    elif juego.Escenario_Actual.ID=="mod3":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() #salir del juego
        if juego.Escenario_Actual.termino==True:
            
            if juego.Escenario_Actual.estrellas==1:
                juego.Escenario_Actual.scr_final.Botones[4].update_image('Images/Recursos/estrella1.png')
                
            if juego.Escenario_Actual.estrellas==2:
                juego.Escenario_Actual.scr_final.Botones[4].update_image('Images/Recursos/estrella1.png')
                juego.Escenario_Actual.scr_final.Botones[5].update_image('Images/Recursos/estrella1.png')
                
            if juego.Escenario_Actual.estrellas==3:
                juego.Escenario_Actual.scr_final.Botones[4].update_image('Images/Recursos/estrella1.png')
                juego.Escenario_Actual.scr_final.Botones[5].update_image('Images/Recursos/estrella1.png')
                juego.Escenario_Actual.scr_final.Botones[6].update_image('Images/Recursos/estrella1.png')
            juego.estrellasNIVEL=juego.Escenario_Actual.estrellas
            
            for i in juego.Escenario_Actual.scr_final.Botones[1:]:

                if True==i.func(juego):
                    if i.objetivo=="reiniciar":
                        juego.Quitar_M_02()
                        juego.Agregar_M_02(armar_modo_02())
                        juego.Escenario_Actual.pauso=False
                    if i.objetivo=="salir":
                        estrellasNIVEL=juego.estrellasNIVEL
                        nivelActual=juego.nivelActual
                        print(estrellasNIVEL)
                        juego.Quitar_M_02()
                        juego.Agregar_M_02(armar_modo_02())
                    if i.objetivo=="continuar":
                        estrellasNIVEL=juego.estrellasNIVEL
                        nivelActual=juego.nivelActual
                        juego.Quitar_M_02()
                        juego.Agregar_M_02(armar_modo_02())
                        desbloquear=True
                        
        elif not juego.Escenario_Actual.pauso and juego.Escenario_Actual.termino==False:
            
            juego.Escenario_Actual.Monita_Musical.si_clickea()
            for i in juego.Escenario_Actual.Nenufares:
                if i.nenufar_click():
                    xn=i.x+10
                    yn=i.y+30
                    juego.Escenario_Actual.Sapo.jump(juego.screen,xn,yn)
                    juego.Escenario_Actual.Cartel.aumentar_palabra(i.palabra)
                    
                    juego.Escenario_Actual.num_pals=juego.Escenario_Actual.num_pals-1
            juego.Escenario_Actual.Cartel.iniciar_contador(juego.screen)
            juego.Escenario_Actual.Sapo.Croak()
            
            for i in juego.Escenario_Actual.Botones:
                i.func(juego)
            if juego.Escenario_Actual.num_pals==0:
                txttmp=juego.Escenario_Actual.Cartel.textooriginal[0]+juego.Escenario_Actual.Cartel.textooriginal[1]+juego.Escenario_Actual.Cartel.textooriginal[2]+juego.Escenario_Actual.Cartel.textooriginal[3]+juego.Escenario_Actual.Cartel.textooriginal[4]
                print(txttmp,"-----",juego.Escenario_Actual.Cartel.letra)
                if juego.Escenario_Actual.Cartel.letra!=txttmp:
                    juego.penalizacion+=1200
                    juego.Cambiar_Escenario(0,3)
                    juego.Quitar_M_02()
                    juego.Agregar_M_02(armar_modo_02(juego.Escenario_Actual.Cartel.textooriginal))
                    juego.Escenario_Actual.Cartel.numero_de_fotogramas=juego.Escenario_Actual.Cartel.numero_de_fotogramas+juego.penalizacion
                else:
                    if juego.Escenario_Actual.Cartel.numero_de_fotogramas<1500:
                        juego.Escenario_Actual.estrellas=3
                    if juego.Escenario_Actual.Cartel.numero_de_fotogramas<3000 and juego.Escenario_Actual.Cartel.numero_de_fotogramas >= 1500:
                        juego.Escenario_Actual.estrellas=2
                    if juego.Escenario_Actual.Cartel.numero_de_fotogramas<4499 and juego.Escenario_Actual.Cartel.numero_de_fotogramas >=3000:
                        juego.Escenario_Actual.estrellas=1
                    juego.penalizacion=0
                    juego.Escenario_Actual.termino=True
        elif juego.Escenario_Actual.termino==False:
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
            try:
                if i.niv!=0:
                    juego.nivelActual=i.niv
            except:
                print("no se puede")
    if estrellasNIVEL!=0 and juego.Escenario_Actual.esc_niv==True:
        for i in range (len(juego.Escenario_Actual.Botones)):
            if juego.Escenario_Actual.Botones[i].objetivo==nivelActual:
                juego.Escenario_Actual.Botones[i].update_image("Images/Recursos/nivel"+str(estrellasNIVEL)+"estrellas.png")
                if desbloquear==True:
                    juego.Escenario_Actual.Botones[i+1].dirige_a([0,3])
                    juego.Escenario_Actual.Botones[i+1].niv=str(i+1)
                    juego.Escenario_Actual.Botones[i+1].update_image("Images/Recursos/nivel0estrellas.png")
                    desbloquear=False
