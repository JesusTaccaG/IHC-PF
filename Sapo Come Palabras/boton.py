import pygame
import pygame as pg
import numpy as np
from escenario import *
class Boton(pygame.sprite.Sprite):
    dirige = None
    def __init__(self, x, y, width, height):
        #tamaño
        self.x = x
        self.y = y
        #posicion
        self.width = width
        self.height = height
        #sistema de click solo boton
        self.mouseOver = False
        self.mouseClick = False
        self.disableClick = False
        #Sub ventana
        self.IsActiveVent = False
        self.ventana = None
        #Sonidos
        self.sound = pygame.mixer.Sound ( 'sounds/button.mp3')
        self.sound.set_volume(0.2)
        self.esc_camb = None
        self.tipo = None
        self.objetivo=""
    #_________________________________________________ORDEN
    def orden(self, objetivo):
        self.objetivo=objetivo
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
    #_________________________________________________Verificar si el mouse esta encima
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
    #_________________________________________________Reproducir sonido
    def sound_p(self):
        self.sound.play()
    def agregar_direccion(self, temp):
        self.dirige = temp
    #_________________________________________________Funcion para manejar todo  el funciona miento de boton
    def exit(self,screen):
        if True == self.status(screen):
            sys.exit()
    def dirige_a(self, dir):
        self.esc_camb = dir
    def camb(self,juego):
        if self.esc_camb != None:
            juego.Cambiar_Escenario(self.esc_camb[0],self.esc_camb[1])
    def func(self,juego):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if True==self.isOver(mouse_pos):
            #Efecto agrandar boton
            if self.mouseOver==False:
                self.sound_p()
                self.update_size(self.width+5, self.height+5)
                self.mouseOver=True
            #Habilitar el click si no esta siendo presonado
            if False==click[0] and self.disableClick==True:
                self.disableClick=False
            #Comprobar si se hace click dentro del boton
            if True==click[0] and self.disableClick==False:
                self.mouseClick=True
            #Comprobar si se suelta el click mientras esta dentro del boton [[[[ Accionl boton ]]]]
            if False==click[0] and self.mouseClick==True and self.disableClick==False:
                self.mouseClick=False
                if self.tipo == 'pause':
                    juego.Escenario_Actual.pauso = True
                elif self.tipo == 'ayuda':
                    juego.Escenario_Actual.ayuda = True 
                elif self.tipo == 'check':
                    juego.Escenario_Actual.pauso = False
                elif self.tipo == 'exit':
                    juego.Escenario_Actual.pauso = False
                else:
                    juego.Escenario_Actual.pauso = False
                    self.camb(juego)
                return True
            
        else:
            #Cambiar la condicion de presionado si se sale del boton sin hacer click
            if self.mouseClick==True:
                self.mouseClick=False
            #Desabilitar el mouse si se hace click afuera del boton
            if True==click[0] and self.disableClick==False:
                self.disableClick=True
            #Habilitar el mouse si se suelta el click afuera del boton
            if False==click[0] and self.disableClick==True:
                self.disableClick=False
            #Efecto desagrandar boton
            if self.mouseOver==True:
                self.update_size(self.width-5, self.height-5)
                self.mouseOver=False
        return False