import pygame
import pygame as pg
import numpy as np
import random
class Frog(pygame.sprite.Sprite):
    #_________________________________________________inicializador
    def __init__(self, x, y, width, height,ui):
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
        #Sonidos
        self.sound1 = pygame.mixer.Sound ( 'sounds/croack1.mp3')
        self.sound2 = pygame.mixer.Sound ( 'sounds/croack2.mp3')
        self.sound1.set_volume(0.2)
        self.sound2.set_volume(0.2)
        #imagen
        img = pygame.image.load(ui)
        self.image = pg.transform.scale(img, (self.width, self.height))
        self.decraced = 1.0
    #_________________________________________________Ajustar tamaño de rana
    def update_size(self, width, height):
        self.width = width
        self.height = height 
        img = pg.transform.scale(self.image, (self.width, self.height))
        self.image = img
    #_________________________________________________Reducir tamaño
    def decreace(self,val):
        self.decraced = val
        self.width = self.width-self.decraced
        self.height = self.height-self.decraced
        img = pg.transform.scale(self.image, (self.width, self.height))
        self.image = img
        self.decraced = val
        #_________________________________________________Reducir tamaño
    def undecreace(self):
        self.width = self.width+self.decraced
        self.height = self.height+self.decraced
        img = pg.transform.scale(self.image, (self.width, self.height))
        self.image = img
        self.decraced = None
    #_________________________________________________Ajustar posicion
    def update_pos(self, x, y):
        self.x = x
        self.y = y
    #_________________________________________________Dibujar Rana
    def draw(self,buff):
        buff.blit(self.image, (self.x, self.y))
    #_________________________________________________Verificar si el mouse esta encima
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
    #_________________________________________________Reproducir sonido
    """Sigue habiendo problema de delay"""
    def Croak(self):
        n = random.randrange(0,180)
        if n==1:
            self.sound1.play()
        if n==2:
            self.sound2.play()
    #_________________________________________________Funcion de control de mouse recicldo del boton
    def status(self,screen):
        mouse_pos = pygame.mouse.get_pos()
        self.draw(screen)
        click = pygame.mouse.get_pressed()
        if True==self.isOver(mouse_pos):
            #Efecto agrandar boton
            if self.mouseOver==False:
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
                self.mouseOver=False
    #_________________________________________________Funcion para cambiar de escena manualmente
    def jump(self,screen,x,y):
        self.update_pos(x,y-30)
