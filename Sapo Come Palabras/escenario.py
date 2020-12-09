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
    def draw(self, buffer):
        buffer.blit(self.image2, (self.x, self.y))
        for i in self.Botones:
            i.draw(buffer)
    def func(self, juego):
        for i in self.Botones:
            i.func(juego)
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
    def agregar_boton(self, bot):
        self.Botones.append(bot)
    def func(self,juego):
        if not self.pauso:
            self.Monita_Musical.si_clickea()
            for i in self.Nenufares:
                if i.nenufar_click():
                    xn=i.x+10
                    yn=i.y+30
                    self.Sapo.jump(juego.screen,xn,yn)
                    self.Cartel.aumentar_palabra(i.palabra)
            self.Cartel.iniciar_contador(juego.screen)
            self.Sapo.Croak()
            for i in self.Botones:
                i.func(juego)
        else:
            for i in self.scr_pause.Botones[1:]:
                i.func(juego)