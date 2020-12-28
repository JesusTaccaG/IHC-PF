import pygame
import pygame as pg
import numpy as np

class Escenario(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.Botones = []
        self.ID="esc"
        self.esc_niv=False
    def update_image(self, ui):
        img = pygame.image.load(ui)
        self.image1 = img
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
    def update_size(self, width, height):
        self.width = width
        self.height = height 
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
    def agregar_boton(self, bot):
        self.Botones.append(bot)
    def draw(self, buffer):
        buffer.blit(self.image2, (self.x, self.y))
        for i in self.Botones:
            i.draw(buffer)
          #habilita todos los botones del escenario
class Modalidad_01(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, sap, mon_mus, cart,img_sueltas):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.Sapo = sap
        self.Cartel = cart
        self.Monita_Musical = mon_mus
        self.Nenufares = []
        self.Botones = []
        self.img_sueltas = img_sueltas
        self.Nivel = 1
        self.pauso = False
        self.scr_pause = None
        self.scr_final = None
        self.termino=False
        self.estrellas=0
        self.num_pals=5
        self.ID="mod3"
        self.niv_num=0
    def agregar_nenufar(self, nenu):
        self.Nenufares.append(nenu)
    def update_image(self, ui):
        img = pygame.image.load(ui)
        self.image1 = img
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
    def update_size(self, width, height):
        self.width = width
        self.height = height 
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
    def draw(self, buffer):
        buffer.blit(self.image2, (self.x, self.y))
        self.Monita_Musical.draw(buffer)
        for i in self.Nenufares:
            i.draw(buffer)
        for i in self.Botones:
            i.draw(buffer)
        for i in self.img_sueltas:
            i.draw(buffer)
        self.Cartel.draw(buffer)
        self.Sapo.draw(buffer)
        if self.pauso:
            self.scr_pause.draw(buffer)
        if self.termino:
            self.scr_final.draw(buffer)
    def agregar_boton(self, bot):
        self.Botones.append(bot)

