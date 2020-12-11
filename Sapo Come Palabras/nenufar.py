import pygame
import pygame as pg
import numpy as np
from escenario import *
from main import *

class Nenufar(pygame.sprite.Sprite):
    #_________________________________________________inicializador
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.mouseOver = False
        self.mouseClick = False
        self.disableClick = False
        self.IsActiveVent = False
        self.ventana = None
        self.actual = None
        pygame.font.init()
        temp = pygame.font.Font(None,45)
        self.palabra = ''
        self.texto = temp.render(self.palabra,0,(200,60,80))
        self.presiono = False
    #_________________________________________________Cambiar imagen nenufar
    def update_image(self, ui,ui2,ui3):
        img = pygame.image.load(ui)
        img2 = pygame.image.load(ui2)
        img3 = pygame.image.load(ui3)
        self.image1 = img
        self.image2 = img2
        self.image3 = img3
        img4 = pg.transform.scale(self.image1, (self.width, self.height))
        img5 = pg.transform.scale(self.image2, (self.width, self.height))
        img6 = pg.transform.scale(self.image3, (self.width, self.height))
        self.image4 = img4
        self.image5 = img5
        self.image6 = img6
        self.actual = self.image4
        
    #_________________________________________________Ajustar tamaño de Nenufar
    def update_size(self, width, height):
        wp = width-self.width
        self.width = width
        self.height = height 
        img4 = pg.transform.scale(self.image1, (self.width, self.height))
        img5 = pg.transform.scale(self.image2, (self.width, self.height))
        img6 = pg.transform.scale(self.image3, (self.width, self.height))
        self.image4 = img4
        self.image5 = img5
        self.image6 = img6
        pygame.font.init()
        temp = pygame.font.Font(None,int(30+wp/4))
        self.texto = temp.render(self.palabra,0,(0,0,0))
    #_________________________________________________Dibujar Nenufar
    def draw(self,buff):
        buff.blit(self.actual, (self.x, self.y))
        buff.blit(self.image6, (self.x, self.y-20))
        buff.blit(self.texto,(self.x+30,self.y))
    #_________________________________________________Verificar si el mouse esta encima
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

    def nenufar_click(self):
        nenufar_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if True==self.isOver(nenufar_pos) and not self.presiono:
            #Efecto agrandar boton
            if self.mouseOver==False:
                #self.sound_p()
                self.update_size(self.width+5, self.height+5)
                self.actual=self.image5
                self.mouseOver=True
            #Habilitar el click si no esta siendo presonado
            if False==click[0] and self.disableClick==True:
                self.disableClick=False
            #Comprobar si se hace click dentro del boton
            if True==click[0] and self.disableClick==False:
                #self.actual=self.image5
                #nenufar.update_image('Images/Recursos/nenufar_celeste.png')
                self.mouseClick=True
                self.presiono = True
                return True
            #Comprobar si se suelta el click mientras esta dentro del boton [[[[ Accionl boton ]]]]
            if False==click[0] and self.mouseClick==True and self.disableClick==False:
                self.mouseClick=False
                
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
                self.actual=self.image4
                self.mouseOver=False
        return False
    def cambiar_palabra(self, pal):
        pygame.font.init()
        temp = pygame.font.Font(None,30)
        self.palabra = pal
        self.texto = temp.render(self.palabra,0,(0,0,0))