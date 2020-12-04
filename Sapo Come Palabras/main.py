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

    boton01 = Boton(270,190,100,100)
    boton01.update_image("Images/Botones/0.png")
    escenario01.agregar_boton(boton01)

    botonRight = Boton(470,190,100,100)
    botonRight.update_image("Images/Botones/7.png")
    escenario01.agregar_boton(botonRight)

    botonLeft = Boton(70,190,100,100)
    botonLeft.update_image("Images/Botones/8.png")
    escenario01.agregar_boton(botonLeft)

    botonExit = Boton(540,20,70,70)
    botonExit.update_image("Images/Botones/33.png")
    escenario01.agregar_boton(botonExit)
    
    juego = config_game()
    juego.Agregar_Escenario(escenario01)

    #botonExit.set_scenario(0, 0, 560, 400,"Images/Recursos/ventana_emergente.png")
    #fin declaracion botones

    pygame.key.set_repeat(1, 80)
    clock = pygame.time.Clock()

    MoMu = Monita_Musical(50,50,100,100)
    MoMu.update_image('Images/Personajes/mensajero.png')
    MoMu.update_audio('sounds/Palabras/palabra_01.mp3')
    juego.Escenario_Actual.agregar_boton(MoMu)

    nenu = Nenufar(250,250,100,100)
    nenu.update_image('Images/Recursos/nenufar.png','Images/Recursos/nenufar_celeste.png','Images/Recursos/letrero_individual.png')
    juego.Escenario_Actual.agregar_boton(nenu)

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

    rana = Frog(270,190,150,150,"Images/Personajes/ranita.png")


    while True:
        tick = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        juego.Mostrar_Escenario(juego.screen)
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
            GP=escenario01.Botones[3].Pause(juego.screen)
            escenario01.Botones[3].draw(juego.screen)
            hilo_1 = threading.Thread(target=MoMu.si_clickea())
            hilo_1.start()
            hilo_2 = threading.Thread(target= nenu.nenufar_click())
            hilo_2.start()
            #rana en pantalla
            xn = random.randrange(0,600)
            yn = random.randrange(0,440)
            rana.Croak()
            rana.jump(juego.screen,xn,yn)
        pygame.display.flip()


if __name__ == "__main__":
    main()
