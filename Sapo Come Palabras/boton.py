import pygame
import pygame as pg
import numpy as np
from escenario import *
class Boton(pygame.sprite.Sprite):
    #_________________________________________________inicializador
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
        self.sound.set_volume(0.3)
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
    """Sigue habiendo problema de delay"""
    def sound_p(self):
        self.sound.play()
    #_________________________________________________Agregar ventana a boton
    """Error al definir la UI"""
    def set_scenario(self,x,y,width,height,ui):
        self.ventana = Escenario(x,y,width,height)
        self.ventana(ui)
    #_________________________________________________Funcion para manejar todo  el funciona miento de boton
    def status(self,screen):
        mouse_pos = pygame.mouse.get_pos()
        self.draw(screen)
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
    #_________________________________________________Funcion para cambiar de escena manualmente
    def change_scene_on_click(self,screen,scene,ui):
        if True == self.status(screen):
            scene.update_image(ui)
    #_________________________________________________Funcion para cambiar una lista de escenas a la derecha
    def change_scene_lst_to_right(self,screen,escenario,lst_pos,scenarios_lst):
        if True == self.status(screen):
            if lst_pos >= len(scenarios_lst):
                lst_pos=len(scenarios_lst)-1 
            if lst_pos+1 < len(scenarios_lst):
                lst_pos+=1
                print(scenarios_lst[lst_pos])
                escenario.update_image(scenarios_lst[lst_pos])
        return lst_pos
    #_________________________________________________Funcion para cambiar una lista de escenas a la izquierda
    def change_scene_lst_to_left(self,screen,escenario,lst_pos,scenarios_lst):
        if True == self.status(screen):
            if lst_pos < 0:
                lst_pos = 0
            if lst_pos-1 >= 0:
                lst_pos-=1
                print(scenarios_lst[lst_pos])
                escenario.update_image(scenarios_lst[lst_pos])
        return lst_pos
    #_________________________________________________Salir del juego
    def exit(self,screen):
        if True == self.status(screen):
            sys.exit()
    #_________________________________________________Salir del juego
    """Aun esta en beta, no se puede quitar la 
    ventana ni hacer que desaparesca lo que esta 
    por detras, ya que esto conlleva configurar 
    la clase de escenario y el main creo yo"""
    def show_vent(self,screen):
        if True == self.status(screen):
            self.IsActiveVent = True
        if self.IsActiveVent==True and self.ventana!=None:
            screen.blit(self.ventana.image2, (self.ventana.x, self.ventana.y))