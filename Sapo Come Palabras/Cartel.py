import pygame
import pygame as pg
import numpy as np
from pygame.locals import *
from escenario import *

class Cartel(pygame.sprite.Sprite):
    #_________________________________________________inicializador
    def __init__(self, x, y, width, height,fuente,numero_de_fotogramas,tasa_fotogramas,instante_de_partida):
        self.letra=""
        #tamaño
        self.x = x
        self.y = y
        #posicion
        self.width = width
        self.height = height
        self.fuente = fuente
        self.numero_de_fotogramas = numero_de_fotogramas
        self.tasa_fotogramas = tasa_fotogramas
        self.instante_de_partida = instante_de_partida
        pygame.font.init()
        temp = pygame.font.Font(None,45)
        self.texto = temp.render(self.letra,0,(0,0,0))
    #_________________________________________________Cambiar iamgen de boton
    def update_image(self, ui):
        img = pygame.image.load(ui)
        self.image1 = img
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
    #_________________________________________________Ajustar tamaño de boton
    def update_size(self, width, height):
        self.width = width
        self.height = height 
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
    #_________________________________________________Dibujar Boton
    def draw(self,buff):
        buff.blit(self.image2, (self.x, self.y))
        buff.blit(self.texto,(self.x+50,self.y+50))

    
    def iniciar_contador(self,screen):
        segundos_totales = self.instante_de_partida - (self.numero_de_fotogramas // self.tasa_fotogramas)
        if segundos_totales < 0:
            segundos_totales = 0
        minutos = segundos_totales // 60
        segundos = segundos_totales % 60
        texto_de_salida = "Tiempo: {0:02}:{1:02}".format(minutos, segundos)
        texto = self.fuente.render(texto_de_salida, True, (0, 0, 0))
        screen.blit(texto, [self.x+60, self.y+20])
        self.numero_de_fotogramas += 1
    def aumentar_palabra(self,temp):
        self.letra+=temp
        pygame.font.init()
        temp = pygame.font.Font(None,30)
        self.texto = temp.render(self.letra,0,(0,0,0))