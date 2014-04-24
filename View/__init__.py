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
        colors = [100,200,255]        
        for b in self.model.duck.SensorList:

            block = pygame.Rect(b[0],b[1],2,2)
            pygame.draw.rect(self.screen,pygame.Color(255,0,255),block)

        pygame.draw.lines(self.screen,(255,255,255),False,self.model.duck.pointlist)
        if pygame.font:
            font = pygame.font.Font(None, 20)

            Gen_str = str(self.model.genome.generation)
            Gen_text = 'Generation: '+Gen_str
            print_Gen = font.render(Gen_text, 1, (255, 255, 255))
            Gen_pos = print_Gen.get_rect(bottomleft = (0, 400))
            self.screen.blit(print_Gen,Gen_pos) 

            Iter_str = str(self.model.Iteration)
            Iter_text = 'Iteration: '+Iter_str
            print_Iter = font.render(Iter_text, 1, (255, 255, 255))
            Iter_pos = print_Iter.get_rect(bottomleft = (0, 425))
            self.screen.blit(print_Iter,Iter_pos)   
            
            Gen_time = str(int(time.time() - self.model.duck.last_fail_time))
            Time_text = 'Iteration runtime: '+Gen_time
            print_time = font.render(Time_text, 1, (255, 255, 255))
            Time_pos = print_time.get_rect(bottomleft = (0,450))
            self.screen.blit(print_time,Time_pos) 
            
            Fit_str = str(self.model.duck.Fitness)
            Fit_text = 'Fitness: '+Fit_str
            print_Fit = font.render(Fit_text, 1, (255, 255, 255))
            Fit_pos = print_Fit.get_rect(bottomleft = (0, 475))
            self.screen.blit(print_Fit,Fit_pos) 
            
            Id_str = str(self.model.genome.chromosomes[self.model.Iteration].identification)
            Fit_text = 'Id: '+Id_str
            print_Id = font.render(Fit_text, 1, (255, 255, 255))
            Id_pos = print_Id.get_rect(bottomleft = (0, 500))
            self.screen.blit(print_Id,Id_pos) 
        

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

        if pygame.font:
            font = pygame.font.Font(None, 20)


            Iter_str = str(self.model.Iteration)
            Iter_text = 'Iteration:'+Iter_str
            print_Iter = font.render(Iter_text, 1, (255, 255, 255))
            Iter_pos = print_Iter.get_rect(topright = (500,25))
            self.screen.blit(print_Iter,Iter_pos)   

            Gen_str = str(self.model.genome.generation)
            Gen_text = 'Generation:'+Gen_str
            print_Gen = font.render(Gen_text, 1, (255, 255, 255))
            Gen_pos = print_Gen.get_rect(topright = (500,0))
            self.screen.blit(print_Gen,Gen_pos) 
            
            Gen_time = str(int(time.time() - self.model.duck.last_fail_time))
            Time_text = 'Current iteration runtime:'+Gen_time
            print_time = font.render(Time_text, 1, (255, 255, 255))
            Time_pos = print_time.get_rect(topright = (500, 50))
            self.screen.blit(print_time,Time_pos) 
            
            Iter_Fit = str(self.model.duck.Fitness)
            Fit_text = 'Fitness'+Iter_Fit
            print_Fit = font.render(Fit_text, 1, (255, 255, 255))
            Fit_pos = print_Fit.get_rect(topright = (500, 75))
            self.screen.blit(print_Fit,Fit_pos) 
            

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

        for b in self.model.sensorPoints:
            block = pygame.Rect(b[1],b[2],20,20)
            pygame.draw.rect(self.screen,pygame.Color(255,255,255),b)


    def draw5(self):
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
        colors = [100,200,255]        
        for b in self.model.duck.SensorList:

            block = pygame.Rect(b[0],b[1],2,2)
            pygame.draw.rect(self.screen,pygame.Color(255,0,255),block)

        pygame.draw.lines(self.screen,(255,255,255),False,self.model.duck.pointlist)
        
        if pygame.font:
            font = pygame.font.Font(None, 20)

            Gen_str = str(self.model.genome.generation)
            Gen_text = 'Generation: '+Gen_str
            print_Gen = font.render(Gen_text, 1, (255, 255, 255))
            Gen_pos = print_Gen.get_rect(bottomleft = (0, 400))
            self.screen.blit(print_Gen,Gen_pos) 

            Iter_str = str(self.model.Iteration)
            Iter_text = 'Iteration: '+Iter_str
            print_Iter = font.render(Iter_text, 1, (255, 255, 255))
            Iter_pos = print_Iter.get_rect(bottomleft = (0, 425))
            self.screen.blit(print_Iter,Iter_pos)   
            
            Gen_time = str(int(time.time() - self.model.duck.last_fail_time))
            Time_text = 'Iteration runtime: '+Gen_time
            print_time = font.render(Time_text, 1, (255, 255, 255))
            Time_pos = print_time.get_rect(bottomleft = (0,450))
            self.screen.blit(print_time,Time_pos) 
            
            Fit_str = str(self.model.duck.Fitness)
            Fit_text = 'Fitness: '+Fit_str
            print_Fit = font.render(Fit_text, 1, (255, 255, 255))
            Fit_pos = print_Fit.get_rect(bottomleft = (0, 475))
            self.screen.blit(print_Fit,Fit_pos) 
            
            Id_str = str(self.model.genome.chromosomes[self.model.Iteration].identification)
            Fit_text = 'Id: '+Id_str
            print_Id = font.render(Fit_text, 1, (255, 255, 255))
            Id_pos = print_Id.get_rect(bottomleft = (0, 500))
            self.screen.blit(print_Id,Id_pos) 
        


        pygame.display.flip()