import pygame
import pygame as pg
import numpy as np

class Monita_Musical(pygame.sprite.Sprite):
    def __init__(self, posx, posy, width, height):
        self.x = posx
        self.y = posy
        self.width = width
        self.height = height
        self.mouseOver = False
        self.mouseClick = False
        self.disableClick = False
    def update_image(self, ui):
        img = pygame.image.load(ui)
        self.image1 = img
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
    def update_audio(self, ua):
        self.audio = pygame.mixer.Sound(ua)
        self.audio.set_volume(1)
    def volumen(self, vol):
        self.audio.set_volume(vol)
    def update_size(self, width, height):
        self.width = width
        self.height = height 
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
    def sound_p(self):
        self.audio.play()
    def si_clickea(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.isOver(mouse_pos):
            if self.mouseOver==False:
                self.update_size(self.width+5, self.height+5)
                self.mouseOver=True
            if False==click[0] and self.disableClick==True:
                self.disableClick=False
            if True==click[0] and self.disableClick==False:
                self.sound_p()
                self.mouseClick=True
            if False==click[0] and self.mouseClick==True and self.disableClick==False:
                self.mouseClick=False
            
        else:
            if self.mouseClick==True:
                self.mouseClick=False
            if True==click[0] and self.disableClick==False:
                self.disableClick=True
            if False==click[0] and self.disableClick==True:
                self.disableClick=False
            if self.mouseOver==True:
                self.update_size(self.width-5, self.height-5)
                self.mouseOver=False
    def draw(self,screen):
        screen.blit(self.image2, (self.x, self.y))