"""
@author: Sophie Li and Paul Titchener
"""

import pygame, random, math, time
from pygame.locals import *
import math

class PyGameWindowView:
    """ Draws our game in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
                   
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.rect(self.screen, pygame.Color(0,255,0), self.model.duck.rect)
        for wall in walls:
            pygame.draw.rect(self.screen, pygame.Color(255, 255, 255), wall.rect)          
        pygame.display.update()

    def draw1(self):
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.rect(self.screen, pygame.Color(0,255,0), self.model.duck.rect)
        if self.model.drawMode == True:
            for trackblock in self.model.Track:
                pygame.draw.rect(self.screen,pygame.Color(255,255,255),trackblock.rect)
        else:
            for trackblock in self.model.Track3[1]:
                pygame.draw.rect(self.screen,pygame.Color(255,255,255),trackblock.rect)
            for trackblock in self.model.Track3[0]: #model.FinalTrack[1]:
                pygame.draw.rect(self.screen,pygame.Color(255,0,0),trackblock.rect)
        pygame.display.update()

    def draw2(self):
        drawListInner  = []
        drawListOuter = []
        self.screen.fill(pygame.Color(0,0,0))

        pygame.draw.rect(self.screen, pygame.Color(0,255,0), model.duck.rect)
        if self.model.drawMode == True:
            for trackblock in model.Track:
                intRect = trackblock.rect.inflate(50,50)
                pygame.draw.rect(self.screen,pygame.Color(255,255,255),intRect)
        else:
            drawInd = 0
            for trackblock in model.Track3[1]:
                drawListInner.append((trackblock.pos[0],trackblock.pos[1]))
            for trackblock in model.Track3[0]: #model.FinalTrack[1]:
                drawListOuter.append((trackblock.pos[0],trackblock.pos[1]))
            pygame.draw.lines(self.screen,(255,255,255),True,drawListInner,3)
            pygame.draw.lines(self.screen,(255,255,255),True,drawListOuter,3)   

        pygame.display.update()

    def draw3(self):
        drawListInner  = []
        drawListOuter = []
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.lines(self.screen,(255,255,255),False,self.model.duck.pointlist)

        pygame.draw.rect(self.screen, pygame.Color(0,255,0), self.model.duck.rect)
        if self.model.drawMode == True:
            for trackblock in self.model.Track:
                intRect = trackblock.rect.inflate(50,50)
                pygame.draw.rect(self.screen,pygame.Color(255,255,255),intRect)
        else:

            pygame.draw.lines(self.screen,(255,255,255),True,self.model.drawListInner)
            pygame.draw.lines(self.screen,(255,255,255),True,self.model.drawListOuter)   

        pygame.display.update()

    def draw4(self):
        self.screen.fill(pygame.Color(0,0,0))
        xInd = 0
        thing = pygame.Rect(20,20,5,5)
        pygame.draw.rect(self.screen,pygame.Color(255,255,255),thing)
        if self.model.drawMode:
            for trackblock in self.model.Track:
                intRect = trackblock.rect.inflate(50,50)
                pygame.draw.rect(self.screen,pygame.Color(255,255,255),intRect)
        else:
            for a in self.model.ArrayTrack:
                yInd = 0
                for b in a:
                    if b ==1:
                        c = pygame.Rect(xInd,yInd,5,5)
                        pygame.draw.rect(self.screen,pygame.Color(255,255,255),c)
                    yInd +=1
                xInd +=1
            listInnerInt = self.model.drawListInner[0:-1]
            listOuterInt = self.model.drawListOuter[0:-1]
            pygame.draw.lines(self.screen,(255,255,255),True,listInnerInt)
            pygame.draw.lines(self.screen,(255,255,255),True,listOuterInt)   


        pygame.display.update()