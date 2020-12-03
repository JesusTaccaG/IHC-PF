import pygame
import pygame as pg
from pygame.locals import *
class Game(pygame.sprite.Sprite):
    Escenarios = []
    Escenario_Actual = None
    screen = None
    def __init__(self, scr):
        self.screen = scr
    def Cambiar_Escenario(self, esc):
        self.Escenario_Actual = self.Escenarios[esc]
        print("lo logro")
    def Mostrar_Escenario(self):
        self.screen.blit(self.Escenario_Actual.image2, (self.Escenario_Actual.x, self.Escenario_Actual.y))
        for i in self.Escenario_Actual.Botones:
            self.screen.blit(i.image2, (i.x, i.y))
    def Agregar_Escenario(self, esc):
        self.Escenarios.append(esc)
        print(len(self.Escenarios))