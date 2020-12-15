import pygame
import pygame as pg
import numpy as np

class Cartel_01(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        self.palabra = None
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        img = pygame.image.load('Images/Recursos/cartel.png')
        self.image1 = img
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2

    def update_size(self, w, h):
        self.width = w
        self.height = h 
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
    
    def draw(self,buff):
        buff.blit(self.image2, (self.x, self.y))

class lengua(pygame.sprite.Sprite):
    def __init__(self,x,y,s):
        self.pix = x
        self.piy = y
        self.pfx = x
        self.pfy = y
        self.size = s
        self.est = 0
    def draw(self, buffer):
        pygame.draw.line(buffer, (255, 0, 0), 
                    [self.pix, self.piy], [self.pfx, self.pfy], self.size)
class sapo_01(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.sec = 1
        hoj1 = pygame.image.load('Images/Recursos/hoja.png')
        self.hoja_o = hoj1
        hoj2 = pg.transform.scale(hoj1, (int(w/10), int(h/7)))
        self.hoja_m = hoj2
        self.pos_h_x = self.x+45
        self.pos_h_y = self.y-5
        self.angle = np.pi
        self.res = np.pi/180
        leng = lengua(self.x+50,self.y+25,5)
        self.lengua = leng
        self.presiono = False
        img = pygame.image.load('Images/Personajes/ranita.png')
        self.image1 = img
        self.temp = 1
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
        self.nenufar1 = pygame.image.load('Images/Recursos/nenufar.png')
        self.nenufar2 = pg.transform.scale(self.nenufar1, (int(w*1.3), int(h*1.3)))
    def update_size(self, width, height):
        self.width = width
        self.height = height 
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
    def draw(self, buffer):
        buffer.blit(self.nenufar2, (self.x-14, self.y-10))
        buffer.blit(self.image2, (self.x, self.y))
        buffer.blit(self.hoja_m, (self.pos_h_x, self.pos_h_y))
        if self.presiono:
            self.lengua.draw(buffer)
    def mov_hoja(self):
        self.pos_h_x=np.round(np.cos(self.angle)*50)+self.x+45
        self.pos_h_y=np.round(np.sin(self.angle)*50)+self.y+20
        self.angle= self.angle+self.res
        hoj = pygame.transform.rotate(self.hoja_o , self.temp)
        self.hoja_m = pg.transform.scale(hoj, (int(self.width/10), int(self.height/7)))
        self.temp+=1
        if self.angle+self.res>np.pi*2 or self.angle+self.res<np.pi:
            self.res=-self.res
    def lengua_l(self):
        self.lengua.pfx=self.lengua.pix+self.lengua.est*np.cos(self.angle)
        self.lengua.pfy=self.lengua.piy+self.lengua.est*np.sin(self.angle)
        self.lengua.est+=self.sec
        if self.lengua.est>250:
            self.sec=-self.sec
        elif self.lengua.est<0:
            self.lengua.est=0
            self.sec=-self.sec
            self.presiono=False
    def func(self, game):
        if self.presiono:
            self.lengua_l()
        else:
            self.mov_hoja()
class Mosca(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.palabra = ""
        img1 = pygame.image.load('Images/Recursos/mosca.png')
        img2 = pygame.image.load('Images/Recursos/cartel_c.png')
        self.image1 = img1
        self.image2 = img2
        img3 = pg.transform.scale(self.image1, (self.width, self.height))
        img4 = pg.transform.scale(self.image2, (self.width, self.height))
        self.image3 = img3
        self.image4 = img4
    def update_size(self, width, height):
        self.width = width
        self.height = height 
        img3 = pg.transform.scale(self.image1, (self.width, self.height))
        img4 = pg.transform.scale(self.image2, (self.width, self.height))
        self.image3 = img3
        self.image4 = img4
    def draw(self, buffer):
        buffer.blit(self.image4, (self.x+5, self.y+25))
        buffer.blit(self.image3, (self.x, self.y))
class Modalidad_02(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,n):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.sapo = sapo_01(270,360,100,100)
        self.moscas = []
        self.nivel = n
        self.cartel = []
        self.Botones = []
        self.ID = "mod2"
        self.esc_help = None
        self.esc_pause = None
        self.ayuda = False
        self.pauso = False
        self.termino = False
    def agregar_mos(self, m):
        self.moscas.append(m)
    def agregar_cart(self, c):
        self.cartel.append(c)
    def agregar_boton(self, b):
        self.Botones.append(b)
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
        self.sapo.draw(buffer)
        for i in self.Botones:
            i.draw(buffer)
        for i in self.cartel:
            i.draw(buffer)
        for i in self.moscas:
            i.draw(buffer)
        if self.ayuda:
            self.scr_ayuda.draw(buffer)
        elif self.pauso:
            self.scr_pause.draw(buffer)
        elif self.termino:
            self.scr_term.draw(buffer)