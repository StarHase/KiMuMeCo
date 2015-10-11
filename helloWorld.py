
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:15:18 2015

@author: lars
"""

import pygame
from pygame.locals import *
from sys import exit
import random
import threading
import Queue
import time

class bubble(threading.Thread):
    
    def __init__(self, INTx, INTy, IMGbg, SCRscreen):
        threading.Thread.__init__(self)
        self.__STRfilenames__ = ['bubble1.png', 'bubble2.png', 'bubble3.png']
        self.__IMGbubble__ = pygame.image.load(self.__STRfilenames__[random.randint(0,len(self.__STRfilenames__)-1)]).convert_alpha()
        self.__h__ = self.__IMGbubble__.get_height()        
        self.__x__ = INTx
        self.__y__ = INTy
        self.__bg__ = IMGbg
        self.__screen__ = SCRscreen
        self.start()
    
    def run(self):
        while self.__y__ > self.__h__ * -1:
            #screen.blit(self.__bg__,(0,0))
            self.__screen__.blit(self.__IMGbubble__, (self.__x__, self.__y__))
            pygame.display.update()
            self.__y__ -= 1
            time.sleep(0.01)
            


class ScreenUpdater(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.BOOloop = True
        self.start()
        
    def run(self):
        while BOOloop:
            pygame.display.update()
            time.sleep(0.005)
        
        

STRbg = 'bg.png'
STRfish = 'fish.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Hallo Oscar")
IMGbg = pygame.image.load(STRbg).convert()
IMGfg = pygame.image.load(STRfish).convert_alpha()

BOOfullscreen = False

#SU = ScreenUpdater()
clock = pygame.time.Clock()
while True:
    #time.sleep(0.01)
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            #SU.BOOloop = False
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_f:
                BOOfullscreen = not BOOfullscreen
                if BOOfullscreen:
                    screen=pygame.display.set_mode((640, 480), FULLSCREEN, 32)
                else:
                    screen=pygame.display.set_mode((640, 480), 0, 32)
        elif event.type == MOUSEBUTTONDOWN:
            #px = pygame.PixelArray(screen)
            INTx, INTy = pygame.mouse.get_pos()
            b = bubble(INTx, INTy, IMGbg, screen)
            #print "%s:%s -> %s" % (INTx,INTy,screen.get_at((INTx, INTy)))
            #px=None
        
    screen.blit(IMGbg,(0,0))
    INTx, INTy = pygame.mouse.get_pos()
    INTx -= IMGfg.get_width() / 2
    INTy -= IMGfg.get_height() / 2
    screen.blit(IMGfg, (INTx, INTy))
    pygame.display.update()
 
