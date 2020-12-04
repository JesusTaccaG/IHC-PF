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

    escenario01 = Escenario(0, 0, WIDTH, HEIGHT)
    escenario01.update_image("Images/Fondos/swamp_01.jpg")
    #botones

    boton01 = Boton(550,20,75,75)
    boton01.update_image("Images/Botones/6.png")
    escenario01.agregar_boton(boton01)

    juego = config_game()
    juego.Agregar_Escenario(escenario01)

    #botonExit.set_scenario(0, 0, 560, 400,"Images/Recursos/ventana_emergente.png")
    #fin declaracion botones

    pygame.key.set_repeat(1, 80)
    clock = pygame.time.Clock()

    GP=False
    SUBCW=560
    SUBCH=400
    opacador = Escenario(0, 0, WIDTH, HEIGHT)
    opacador.update_image("Images/Recursos/opacador.png")

    escenarioPaused = Escenario(WIDTH/2-(SUBCW/2), HEIGHT/2-(SUBCH/2), SUBCW, SUBCH)
    escenarioPaused.update_image("Images/Recursos/ventana_emergente.png")

    subBotones=4

    botonConfig = Boton((SUBCW/2)-SUBCW/4,160,60,60)
    botonConfig.update_image("Images/Botones/32.png")
    escenarioPaused.agregar_boton(botonConfig)

    botonRestart = Boton((SUBCW/2)-SUBCW/4,230,60,60)
    botonRestart.update_image("Images/Botones/36.png")
    escenarioPaused.agregar_boton(botonRestart)

    botonSalir = Boton((SUBCW/2)-SUBCW/4,300,60,60)
    botonSalir.update_image("Images/Botones/8.png")
    escenarioPaused.agregar_boton(botonSalir)

    botonExit_P = Boton(SUBCW,HEIGHT-SUBCH,60,60)
    botonExit_P.update_image("Images/Botones/33.png")
    escenarioPaused.agregar_boton(botonExit_P)


    while True:
        tick = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        juego.Mostrar_Escenario()
        if GP == True:
            #el juego esta pausado

            #opacador
            juego.screen.blit(opacador.image2, (opacador.x, opacador.y))
            #mostrar subventana
            juego.screen.blit(escenarioPaused.image2, (escenarioPaused.x, escenarioPaused.y))
            #subbotones sin funcion
            escenarioPaused.Botones[0].status(juego.screen)
            escenarioPaused.Botones[0].draw(juego.screen)
            escenarioPaused.Botones[1].status(juego.screen)
            escenarioPaused.Botones[1].draw(juego.screen)
            escenarioPaused.Botones[2].status(juego.screen)
            escenarioPaused.Botones[2].draw(juego.screen)
            escenarioPaused.Botones[3].draw(juego.screen)
            #subboton de salir de subventana
            if escenarioPaused.Botones[3].status(juego.screen):
                GP = False
        else:
            #el juego esta corriendo
            hilo_1 = threading.Thread(target = juego.Escenario_Actual.Monita_Musical.si_clickea())
            hilo_1.start()
            for i in juego.Escenario_Actual.Nenufares:
                if i.nenufar_click():
                    xn=i.x+10
                    yn=i.y+30
                    juego.Escenario_Actual.Sapo.jump(juego.screen,xn,yn)
                    juego.Escenario_Actual.Cartel.aumentar_palabra(i.palabra)

            for i in juego.Escenario_Actual.Botones:
                GP = i.Pause(juego.screen)
            hilo_3 = threading.Thread(target = juego.Escenario_Actual.Cartel.iniciar_contador(juego.screen))
            hilo_3.start()
            #rana en pantalla
            juego.Escenario_Actual.Sapo.Croak()
        pygame.display.flip()


if __name__ == "__main__":
    main()
