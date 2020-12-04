import pygame
import pygame as pg
from pygame.locals import *
class Game(pygame.sprite.Sprite):
    Escenarios = []
    M_00 = []
    M_01 = []
    M_02 = []
    tipo = 0
    Escenario_Actual = None
    screen = None
    def __init__(self, scr):
        self.screen = scr
    def Cambiar_Escenario(self, esc, tipo):
        if tipo ==0:
            self.Escenario_Actual = self.Escenarios[esc]
            self.tipo = 0
        elif tipo==1:
            self.Escenario_Actual = self.M_00[esc]
            self.tipo = 1
        elif tipo==2:
            self.Escenario_Actual = self.M_01[esc]
            self.tipo = 2
        else:
            self.Escenario_Actual = self.M_02[esc]
            self.tipo = 3
             
    def Mostrar_Escenario(self):
        if self.tipo==0: 
            self.screen.blit(self.Escenario_Actual.image2, (self.Escenario_Actual.x, self.Escenario_Actual.y))
            for i in self.Escenario_Actual.Botones:
                i.draw(self.screen)
        elif self.tipo==3:
            self.Escenario_Actual.draw(self.screen)
    def Agregar_M_00(self, esc):
        self.M_00.append(esc)
    def Agregar_M_01(self, esc):
        self.M_01.append(esc)
    def Agregar_M_02(self, esc):
        self.M_02.append(esc)
    def Agregar_Escenario(self, esc):
        self.Escenarios.append(esc)