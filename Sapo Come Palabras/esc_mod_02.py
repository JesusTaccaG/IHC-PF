import pygame
import pygame as pg
import numpy as np
import random


class Cartel_01(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, pal):
        self.cont=0
        self.fallo=False
        self.activo=False
        self.palabra = pal
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        img = pygame.image.load('Images/Recursos/cartel.png')
        self.image1 = img
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
        fuente = pygame.font.Font(None, 40) 
        temp=self.palabra[1][0]+'_'+self.palabra[1][1]
        print(temp)
        self.mensaje = fuente.render(temp, 1, (0, 0, 0))
        self.men_fall = fuente.render('FALLASTE', 1, (255, 0, 0))

    def update_size(self, w, h):
        self.width = w
        self.height = h 
        img2 = pg.transform.scale(self.image1, (self.width, self.height))
        self.image2 = img2
    def func(self):
        if self.fallo:
            if self.cont==50:
                self.fallo=False
                self.cont=0
            self.cont+=1

    def draw(self,buff):
        buff.blit(self.image2, (self.x, self.y))
        buff.blit(self.mensaje, (self.x+30, self.y+45))
        if self.fallo:
            buff.blit(self.men_fall, (self.x+30, self.y+85))
class lengua(pygame.sprite.Sprite):
    def __init__(self,x,y,s):
        #puntos iniciales
        self.pix = x
        self.piy = y
        #puntos finales
        self.pfx = x
        self.pfy = y
        #grosor de la linea
        self.size = s
        #largo de la linea
        self.est = 0
    def draw(self, buffer):
        #creacion
        pygame.draw.line(buffer, (197, 141, 140), 
                    [self.pix, self.piy], [self.pfx, self.pfy], self.size)
        pygame.draw.ellipse(buffer, (197, 141, 140), 
                    [self.pfx, self.pfy, 7, 7], 0)
class sapo_01(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        self.lenguetazo=0
        self.mosca_atrapada=None
        self.atrapo_mosca=False
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.sec = 5
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
        if self.lengua.est>350:
            self.sec=-self.sec
        elif self.lengua.est<0:
            self.lengua.est=0
            self.sec=-self.sec
            self.presiono=False
    def func(self, game):
        if self.presiono:
            if self.atrapo_mosca and self.mosca_atrapada==None:
                print("lo atrapo")
            self.lengua_l()
        else:
            self.mov_hoja()
class Mosca(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,palabra):
        self.palabra=palabra
        self.fue_atrapado=False
        self.vivo = True
        self.velocidad=1
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        img1 = pygame.image.load('Images/Recursos/mosca.png')
        img2 = pygame.image.load('Images/Recursos/cartel_c.png')
        self.image1 = img1
        self.image2 = img2
        img3 = pg.transform.scale(self.image1, (self.width, self.height))
        img4 = pg.transform.scale(self.image2, (self.width, self.height))
        self.image3 = img3
        self.image4 = img4
        fuente = pygame.font.Font(None, 40) 
        self.mensaje = fuente.render(palabra, 1, (0, 0, 0))
    def update_size(self, width, height):
        self.width = width
        self.height = height 
        img3 = pg.transform.scale(self.image1, (self.width, self.height))
        img4 = pg.transform.scale(self.image2, (self.width, self.height))
        self.image3 = img3
        self.image4 = img4
    def draw(self, buffer):
        if self.vivo:
            buffer.blit(self.image4, (self.x+5, self.y+25))
            buffer.blit(self.image3, (self.x, self.y))
            buffer.blit(self.mensaje, (self.x+25, self.y+45))
    def movimiento(self,game):
        if self.fue_atrapado:
            s=game.sapo
            self.x=self.x+s.sec*np.cos(s.angle)
            self.y=self.y+s.sec*np.sin(s.angle)
            if s.y-self.y<0:
                self.vivo=False
                t=game.cartel[0]
                t2=t.palabra[1][0]+self.palabra+t.palabra[1][1]
                if t.palabra[0]==t2:
                    game.termino=True
                else:
                    t.fallo=True
        else:
            self.x= self.x+self.velocidad
            if self.x+75>640 or self.x-75<0:
                self.velocidad=-self.velocidad
    def atrapado(self,x,y):
        temp1 = self.x+self.width/2
        temp2 = self.y+self.height/2
        rad = self.width/3
        if np.sqrt(pow(x-temp1,2)+pow(y-temp2,2))<rad:
            return True
        return False
class Modalidad_02(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,n):
        self.texto_ayuda=""
        self.fuente = pygame.font.Font(None, 30)
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
        self.ayuda = False
        self.pauso = False
        self.termino = False
        opac = pygame.image.load('Images/Recursos/opacador.png')
        self.opacacion = img2 = pg.transform.scale(opac, (self.width, self.height))
        v_e = pygame.image.load('Images/Recursos/ventana_emergente.png')
        self.vent_emer = pg.transform.scale(v_e, (250, 250))
        self.vent_emer02 = pg.transform.scale(v_e, (400,400))
        self.vent_emer03 = pg.transform.scale(v_e, (300,300))
        #Fin del jueo
        self.botones_01=[]
        #Ayuda
        self.botones_02=[]
        #Botones pausa
        self.botones_03=[]
        self.estrellas=[]
        self.objetivos=[]
        self.t_a=[]
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
    def agregar_texto(self,text):
        temp=text.split('\n')
        for i in temp:
            temp2=self.fuente.render(i, 1, (0, 0, 0))
            self.t_a.append(temp2)
    def reiniciar(self):
        for i in self.moscas:
            i.vivo=True
            i.fue_atrapado=False
            x=random.randrange(80,560)
            y=random.randrange(100,150)
            print(x,y)
            i.x=x
            i.y=y
        self.termino=False
        self.pauso=False
        self.ayuda=False
        self.sapo.mosca_atrapada=None
        self.sapo.atrapo_mosca=False
        self.sapo.lenguetazo=0
    def draw(self, buffer):
        buffer.blit(self.image2, (self.x, self.y))
        self.sapo.draw(buffer)
        for i in self.Botones:
            i.draw(buffer)
        for i in self.cartel:
            if i.activo:
                i.draw(buffer)
        for i in self.moscas:
            i.draw(buffer)
        if self.ayuda:
            buffer.blit(self.opacacion,(self.x, self.y))
            buffer.blit(self.vent_emer02, (self.x+120, self.y+40))
            for i in self.botones_02:
                i.draw(buffer)
            for a,i in enumerate(self.t_a):
                buffer.blit(i,(200,140+40*a))
        elif self.pauso:
            buffer.blit(self.opacacion,(self.x,self.y))
            buffer.blit(self.vent_emer03,(self.x+170,self.y+90))
            for i in self.botones_03:
                i.draw(buffer)
        elif self.termino:
            buffer.blit(self.opacacion, (self.x, self.y))
            buffer.blit(self.vent_emer, (self.x+195, self.y+115))
            for i in self.botones_01:
                i.draw(buffer)
            if self.sapo.lenguetazo==1:
                self.estrellas[0].draw(buffer)
            else:
                self.estrellas[1].draw(buffer)
            if self.sapo.lenguetazo<=2:
                self.estrellas[2].draw(buffer)
            else:
                self.estrellas[3].draw(buffer)
            self.estrellas[4].draw(buffer)
            """
            for i in range(int(len(self.estrellas)/2)):
                self.estrellas[i*2].draw(buffer)"""
            for i in self.objetivos:
                i.draw(buffer)