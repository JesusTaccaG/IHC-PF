from random import uniform, random, choice, sample
from esc_mod_02 import lengua
import pygame
import pygame as pg
import numpy as np
from pygame.locals import *
import pygame.freetype

class Cartel_resultado(pygame.sprite.Sprite):
    #_________________________________________________inicializador
    def __init__(self, x, y, width, height,name,name_ayuda,tiempo_tablero):
        self.Botones = []
        #tamaño
        self.x = x
        self.y = y
        self.termino=False
        #posicion
        self.width = width
        self.height = height
        self.fuente = pygame.font.Font(None, 30)
        self.fuente2 = pygame.font.Font(None, 40)
        self.titulo=self.fuente.render("RESULTADOS",0,(0,0,0))
        self.tiempo_sobrante=self.fuente2.render("+{} segundos".format(tiempo_tablero),0,(0,0,0))
        self.estrellas=[]
    def agregar_boton(self, b):
        self.Botones.append(b)
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
        for i in self.Botones:
            i.draw(buff)
        for i in range(len(self.estrellas)):
            self.estrellas[i].draw(buff)
        buff.blit(self.titulo,(250,135))
        buff.blit(self.tiempo_sobrante,(280, 185))

class Cartel_ayuda(pygame.sprite.Sprite):
    #_________________________________________________inicializador
    def __init__(self, x, y, width, height,name,name_ayuda):
        self.Botones = []
        #tamaño
        self.x = x
        self.y = y
        self.termino=False
        #posicion
        self.width = width
        self.height = height
        self.fuente = pygame.font.Font(None, 30)
        self.fuente2 = pygame.font.Font(None, 25)
        self.titulo=self.fuente.render("Zona de ayuda",0,(0,0,0))
        self.info_animal=self.fuente2.render(name_ayuda,0,(0,0,0))
    def agregar_boton(self, b):
        self.Botones.append(b)
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
        for i in self.Botones:
            i.draw(buff)
        buff.blit(self.titulo,(250,135))
        buff.blit(self.info_animal,(200,260))

class Cartel_00(pygame.sprite.Sprite):
    #_________________________________________________inicializador
    def __init__(self, x, y, width, height):
        self.letra=""
        self.Botones = []
        #tamaño
        self.x = x
        self.y = y
        #tiempo
        self.minutos=0
        self.segundos=0
        self.segundos_totales=0
        self.termino=False
        #posicion
        self.width = width
        self.height = height
        self.fuente = pygame.font.Font(None, 25)
        self.numero_de_fotogramas = 0
        self.tasa_fotogramas = 60
        self.instante_de_partida=0
        pygame.font.init()
        temp = pygame.font.Font(None,45)
        self.texto = temp.render(self.letra,0,(0,0,0))
    def agregar_boton(self, b):
        self.Botones.append(b)
    def establecer_tiempo(self,tiempo):
        self.instante_de_partida = tiempo
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
        buff.blit(self.texto,(self.x+50,self.y+50))
        for i in self.Botones:
            i.draw(buff)
    def iniciar_contador(self,screen):
        self.segundos_totales = self.instante_de_partida - (self.numero_de_fotogramas // self.tasa_fotogramas)
        if self.segundos_totales < 0:
            self.segundos_totales = 0
        self.minutos = self.segundos_totales // 60
        self.segundos = self.segundos_totales % 60
        texto_de_salida = "Tiempo: {0:02}:{1:02}".format(self.minutos, self.segundos)
        texto = self.fuente.render(texto_de_salida, True, (0, 0, 0))
        screen.blit(texto, [self.x+60, self.y+20])
        self.numero_de_fotogramas += 1
        if(self.minutos == 0 and self.segundos<=0):
            self.termino=True
    def aumentar_palabra(self,temp):
        self.letra+=temp
        pygame.font.init()
        temp = pygame.font.Font(None,30)
        self.texto = temp.render(self.letra,0,(0,0,0))

class Animal_00:
    def __init__(self, x, y, w, h,name):
        self.palabra = name
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        img = pygame.image.load('Images\m_animales/'+self.palabra+'.png')
        self.image1 = img
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
    def __str__(self):
        return 'Hola desde animales 00'
    def update_size(self, w, h):
        self.width = w
        self.height = h 
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
    
    def draw(self,buff):
        buff.blit(self.image2, (self.x, self.y))

class lengua_00(pygame.sprite.Sprite):
    def __init__(self,x,y,s):
        #puntos iniciales
        self.pix = x
        self.piy = y
        #puntos finales
        self.pfx = x
        self.pfy = y
        #grosor de la linea
        self.size = s
        self.line=None
        #largo de la linea
        self.est = 200
    def is_collided_with(self, mosca):
        # self.pfy <= mosca.y and self.pfy <= mosca.y+mosca.height and
        if(self.pfy >= mosca.y + (mosca.height-10) and self.pfy <= mosca.y+mosca.height and self.pfx >= mosca.x and self.pfx <= mosca.x+mosca.width):
            print('{} {} --- {} {}'.format(self.pfy,mosca.y+mosca.height,self.pfx,self.pfx<mosca.x+mosca.width))
            return True
        return False
    def draw(self, buffer):
        #creacion
        self.line = pygame.draw.line(buffer, (255, 0, 0), 
                    [self.pix, self.piy], [self.pfx, self.pfy], self.size)

class sapo_00(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.sec = 10
        hoj1 = pygame.image.load('Images/Recursos/hoja.png')
        self.hoja_o = hoj1
        hoj2 = pg.transform.scale(hoj1, (int(w/10), int(h/7)))
        self.hoja_m = hoj2
        self.pos_h_x = self.x+45
        self.pos_h_y = self.y-5
        self.angle = np.pi
        self.res = np.pi/180
        leng = lengua_00(self.x+50,self.y+25,5)
        self.lengua = leng
        self.presiono = False
        img = pygame.image.load('Images/Personajes/ranita.png')
        self.image1 = img
        self.temp = 1
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
        self.nenufar1 = pygame.image.load('Images/Recursos/nenufar.png')
        self.nenufar2 = pg.transform.scale(self.nenufar1, (int(w*1.3), int(h*1.3)))
    def __str__(self):
        return 'Hola desde sapo 00'

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
class Mosca_00(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,fuente,vel_x,vel_y):
        self.x = x
        self.y = y
        self.palabra = ""
        self.fuente = fuente
        self.width = w
        self.height = h
        self.velocidad_x = vel_x
        self.velocidad_y = vel_y
        img1 = pygame.image.load('Images/Recursos/mosca.png')
        img2 = pygame.image.load('Images/Recursos/cartel_c.png')
        self.image1 = img1
        self.image2 = img2
        img3 = pg.transform.scale(self.image1, (self.width, self.height))
        img4 = pg.transform.scale(self.image2, (self.width, self.height))
        self.image3 = img3
        self.image4 = img4
    def move(self):
        self.x+=self.velocidad_x
        self.y+=self.velocidad_y
        if self.x >500:
            self.velocidad_x = -1
        if self.x < 50:
            self.velocidad_x= 1
        if self.y >200:
            self.velocidad_y= -1
        if self.y < 50:
            self.velocidad_y= 1
    def update_size(self, width, height):
        self.width = width
        self.height = height 
        img3 = pg.transform.scale(self.image1, (self.width, self.height))
        img4 = pg.transform.scale(self.image2, (self.width, self.height))
        self.image3 = img3
        self.image4 = img4
    def draw(self, buffer):
        self.texto = self.fuente.render(self.palabra,0,(0,0,0))
        
        buffer.blit(self.image4, (self.x+5, self.y+25))
        buffer.blit(self.image3, (self.x, self.y))
        buffer.blit(self.texto, [self.x+20, self.y+55])

class Modalidad_00(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,n=0):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.sapo = sapo_00(270,360,100,100)
        self.moscas = []
        self.nivel = n
        self.Cartel = []
        self.Botones = []
        self.Animales = []
        self.ID = "mod1"
        self.esc_help = None
        self.esc_pause = None
        self.scr_pause = None
        self.ayuda = False
        self.scr_ayuda = None
        self.src_resultado = None
        self.pauso = False
        self.pauso_ayuda =False
        self.termino = False
        #Final :(
        opac = pygame.image.load('Images/Recursos/opacador.png')
        self.opacacion = pg.transform.scale(opac, (self.width, self.height))
        v_e = pygame.image.load('Images/Recursos/ventana_emergente.png')
        self.vent_emer = pg.transform.scale(v_e, (250, 250))
        self.vent_emer02 = pg.transform.scale(v_e, (400,400))

    def __str__(self):
        return 'Hola desde modalidad 00'
    def agregar_mos(self, m):
        self.moscas.append(m)
    def agregar_cart(self, c):
        self.Cartel.append(c)
    def agregar_boton(self, b):
        self.Botones.append(b)
    def agregar_animales(self, b):
        self.Animales.append(b)
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
        for i in self.Cartel:
            i.draw(buffer)
        for i in self.Animales:
            i.draw(buffer)
        for i in self.moscas:
            i.draw(buffer)
        if self.ayuda:
            self.scr_ayuda.draw(buffer)
        elif self.pauso:
            self.scr_pause.draw(buffer)
        elif self.termino:
            self.src_resultado.draw(buffer)
