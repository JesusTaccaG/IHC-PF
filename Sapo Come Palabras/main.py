import pygame
import sys
import math
from os import system
import numpy as np
from pygame.locals import *
from escenario import *
from boton import *

WIDTH=640
HEIGHT=480

def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sapo come palabras")
    escenario01 = Escenario(0, 0, WIDTH, HEIGHT)
    escenario01.update_image("Images/Fondos/swamp_01.jpg")

    #botones

    boton01 = Boton(270,190,100,100)
    boton01.update_image("Images/Botones/0.png")

    botonRight = Boton(470,190,100,100)
    botonRight.update_image("Images/Botones/7.png")

    botonLeft = Boton(70,190,100,100)
    botonLeft.update_image("Images/Botones/8.png")

    botonExit = Boton(540,20,70,70)
    botonExit.update_image("Images/Botones/33.png")
    """Error con la UI"""
    botonExit.set_scenario(0, 0, 560, 400,"Images/Recursos/ventana_emergente.png")
    #fin declaracion botones

    pygame.key.set_repeat(1, 80)
    clock = pygame.time.Clock()

    scenarios_lst=["Images/Fondos/swamp_01.jpg","Images/Fondos/river_01.jpg","Images/Fondos/river_02.jpg","Images/Fondos/lake_01.jpg"]
    scene_pos = 0
    
    while True:
        tick = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(escenario01.image2, (escenario01.x, escenario01.y))
        #__________________________________________BOTON
        # Toda la parte de control del boton esta en una funcion
        # solo en caso de hcer un click botara un True de esta 
        # manera se le puede dar diferentes funcionalidades al 
        # boton con un solo if
        
        #----cambiar a escena cualquiera
        #boton01.change_scene_on_click(screen,escenario01,"Images/Fondos/lake_01.jpg")
        #----cambiar a escenas con lista de derecha a izquierda
        #scene_pos = botonRight.change_scene_lst_to_right(screen,escenario01,scene_pos,scenarios_lst)
        #scene_pos = botonLeft.change_scene_lst_to_left(screen,escenario01,scene_pos,scenarios_lst)
        #----Salir del juego
        #botonExit.exit(screen)

        """funcion con ventana emergente con errores"""
        """botonExit.show_vent(screen)"""

        if True == boton01.status(screen):
            print("po lo que quieres que haga el boton aqui")
            #aqui va lo que quieres que haga el boton
        #__________________________________________BOTON____________FIN
        pygame.display.flip()


if __name__ == "__main__":
    main()
