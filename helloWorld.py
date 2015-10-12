
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



class CLSworld(object):
    
    def __init__(self):
        pygame.init()
        self.__STRfilename__ = "bg.png"
        self.__LSTobjects__ = []
        self.__TPLresolution__ = (800, 480)
        self.Screen = pygame.display.set_mode(self.__TPLresolution__, 0, 32)
        self.__IMGbgimage__ = pygame.image.load(self.__STRfilename__).convert_alpha()
        
    
    def process(self):
        if len(self.__LSTobjects__) > 0:        
            for OBJtmp in self.__LSTobjects__:
                OBJtmp.process()

    
    def render(self):
        self.Screen.blit(self.__IMGbgimage__,(0,0))
        if len(self.__LSTobjects__) > 0:        
            for OBJtmp in self.__LSTobjects__:
                OBJtmp.render()
        pygame.display.update()
        
    
    def AddObject(self, OBJobject):
        self.__LSTobjects__.append(OBJobject)



class bubble():
    
    def __init__(self, OBJworld, INTx, INTy):
        self.__STRfilenames__ = ['bubble1.png', 'bubble2.png', 'bubble3.png']
        self.__IMGimage__ = pygame.image.load(self.__STRfilenames__[random.randint(0,len(self.__STRfilenames__)-1)]).convert_alpha()
        self.__h__ = self.__IMGimage__.get_height()        
        self.__x__ = INTx
        self.__y__ = INTy
        self.__world__ = OBJworld
        OBJworld.AddObject(self)
        
        
    def process(self):        
        
        if self.__y__ > -self.__h__:
            INTxmovement = -1 + random.randint(0,2)
            INTymovement = random.randint(1,4)
            self.__x__ += INTxmovement
            self.__y__ -= INTymovement
        
    
    def render(self):
        self.__world__.Screen.blit(self.__IMGimage__, (self.__x__, self.__y__))
            
            

class fish():
    
    def __init__(self, OBJworld, INTx, INTy):
        self.__STRfilename__ = "fish.png"
        self.__IMGimage__ = pygame.image.load(self.__STRfilename__).convert_alpha()
        self.__h__ = self.__IMGimage__.get_height()        
        self.__x__ = INTx
        self.__y__ = INTy
        self.__world__ = OBJworld
        OBJworld.AddObject(self)
        
        
    def process(self):
        self.__x__, self.__y__ = pygame.mouse.get_pos()
        self.__x__ -= self.__IMGimage__.get_width() / 2
        self.__y__ -= self.__IMGimage__.get_height() / 2
        
        
        
    def render(self):
        self.__world__.Screen.blit(self.__IMGimage__, (self.__x__, self.__y__))



#pygame.display.set_caption("Hallo Oscar")
#BOOfullscreen = False
Game = CLSworld()
Pointer = fish(Game, 0, 0)

clock = pygame.time.Clock()

while True:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:            
            exit()

#        elif event.type == KEYDOWN:
#            if event.key == K_f:
#                BOOfullscreen = not BOOfullscreen
#                if BOOfullscreen:
#                    screen=pygame.display.set_mode((640, 480), FULLSCREEN, 32)
#                else:
#                    screen=pygame.display.set_mode((640, 480), 0, 32)

        elif event.type == MOUSEBUTTONDOWN:
            INTx, INTy = pygame.mouse.get_pos()
            b = bubble(Game,INTx, INTy)
            #print "%s:%s -> %s" % (INTx,INTy,screen.get_at((INTx, INTy)))
            #px=None
        
    Game.process()
    Game.render()    
 
