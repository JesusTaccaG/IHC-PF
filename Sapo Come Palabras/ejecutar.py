import pygame
import pygame as pg
import numpy as np
from config import *

def run_escenarios(juego, escenario):
    
    if escenario.ID=="mod3":
    
        if not escenario.pauso:
            escenario.Monita_Musical.si_clickea()
            for i in escenario.Nenufares:
                if i.nenufar_click():
                    xn=i.x+10
                    yn=i.y+30
                    escenario.Sapo.jump(juego.screen,xn,yn)
                    escenario.Cartel.aumentar_palabra(i.palabra)
            escenario.Cartel.iniciar_contador(juego.screen)
            escenario.Sapo.Croak()
            for i in escenario.Botones:
                i.func(juego)
        else:
            for i in escenario.scr_pause.Botones[1:]:
                if True==i.func(juego):
                    if i.objetivo=="reiniciar":
                        escenario=armar_modo_02()
                        #escenario.pauso=False
    elif escenario.ID=="esc":
        for i in escenario.Botones:
            i.func(juego) 