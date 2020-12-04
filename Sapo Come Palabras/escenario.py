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
class Modalidad_01(pygame.sprite.Sprite):
    Monita_Musical = None
    Sapo = None
    Nenufares = []
    Cartel = None
    def __init__(self, x, y, width, height, sap, mon_mus, cart):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.Sapo = sap
        self.Cartel = cart
        self.Monita_Musical = mon_mus
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