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
        self.car_images = []
        self.car_images_unScaled = []
        self.ymax=400
        self.xstep=20
        i = 0
        while i < 20:
            fileName = 'car' + str(i) + '.png'
            self.car_image = pygame.image.load(fileName)
            self.car_images_unScaled.append(self.car_image)
            self.car_image = pygame.transform.scale(self.car_image, (30, 17))
            self.car_images.append(self.car_image)
            i += 1
        self.car_colors = [pygame.Color(240,163,10),pygame.Color(27,161,226),pygame.Color(0,80,239),pygame.Color(162,0,37),pygame.Color(130,90,44),pygame.Color(216,0,115),pygame.Color(164,196,0),pygame.Color(106,0,255),pygame.Color(96,169,23),pygame.Color(0,138,0),pygame.Color(118,96,138),pygame.Color(109,135,100),pygame.Color(250,104,0),pygame.Color(244,114,208),pygame.Color(0,171,169),pygame.Color(122,59,63),pygame.Color(229,20,0),pygame.Color(170,0,255),pygame.Color(216,193,0),pygame.Color(255,255,255)]
        self.dead_car_image = pygame.transform.scale(pygame.image.load('dead_car.png'), (25,10))
        self.pos1 = pygame.Rect(int(100),int(100 ),160,80)
        self.pos2 = pygame.Rect(int(500),int(100 ),160,80)
                   
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
            Gen_pos = print_Gen.get_rect(bottomleft = (600, 10))
            self.screen.blit(print_Gen,Gen_pos) 
            
            Gen_time = str(int(time.time() - self.model.last_generation_time))
            Time_text = 'Generation runtime: '+Gen_time
            print_time = font.render(Time_text, 1, (255, 255, 255))
            Time_pos = print_time.get_rect(bottomleft = (600,35))
            self.screen.blit(print_time,Time_pos) 

            Iter_str = str(self.model.Iteration)
            Iter_text = 'Iteration: '+Iter_str
            print_Iter = font.render(Iter_text, 1, (255, 255, 255))
            Iter_pos = print_Iter.get_rect(bottomleft = (0, 425))
            self.screen.blit(print_Iter,Iter_pos)   
            
            
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




    def draw_sophie(self):
        #print 'drew frame'

        self.screen.fill(pygame.Color(60,60,60))

        
        i = 14
        for element in self.model.ducks:
            #pygame.draw.rect(self.screen, self.model.ducks[i].color, element.rect)
            rotatedImage = pygame.transform.rotate(self.car_images[i],self.model.ducks[i].theta * -57.2957)
            self.screen.blit(rotatedImage, self.model.ducks[i].rect)
            #pygame.draw.rect(self.screen,pygame.Color(255,255,255), element.rect)
            
            i-=1
            for b in element.SensorList:
                try:
                    c = [b[0],b[-1]]
                except:
                    pass    
                 


        if self.model.drawMode == True:
            for trackblock in self.model.Track:
                pygame.draw.rect(self.screen,pygame.Color(255,255,255),trackblock.rect)
                
        else:
            for trackblock in self.model.Track3[1]:
                pygame.draw.rect(self.screen,pygame.Color(255,255,255),trackblock.rect)
            for trackblock in self.model.Track3[0]: 

                pygame.draw.rect(self.screen,pygame.Color(255,200,0),trackblock.rect)
                
        colors = [100,200,255]        


        pygame.draw.lines(self.screen,(255,255,255),False,self.model.duck.pointlist)
        pygame.draw.line(self.screen,(255,255,255), (500,0), (500,500))
        font = pygame.font.Font(None, 20)

        Gen_str = str(self.model.genome.generation)
        Gen_text = 'Generation: '+Gen_str
        print_Gen = font.render(Gen_text, 1, (255, 255, 255))
        Gen_pos = print_Gen.get_rect(bottomleft = (525,25))
        self.screen.blit(print_Gen,Gen_pos) 
        
        Gen_time = str(int(time.time() - self.model.last_generation_time))
        Time_text = 'Generation runtime: '+Gen_time
        print_time = font.render(Time_text, 1, (255, 255, 255))
        Time_pos = print_time.get_rect(bottomleft = (525,50))
        self.screen.blit(print_time,Time_pos)
        
        Iter_text = 'Car'
        print_Iter = font.render(Iter_text, 1, (255, 255, 255))
        Iter_pos = print_Iter.get_rect(bottomleft = (525, 100))
        self.screen.blit(print_Iter,Iter_pos)               
        
        Fit_text = 'Fitness'
        print_Fit = font.render(Fit_text, 1, (255, 255, 255))
        Fit_pos = print_Fit.get_rect(bottomleft = (625, 100))
        self.screen.blit(print_Fit,Fit_pos)
        
        Fit_text = 'Status'
        print_Fit = font.render(Fit_text, 1, (255, 255, 255))
        Fit_pos = print_Fit.get_rect(bottomleft = (725, 100))
        self.screen.blit(print_Fit,Fit_pos)
        
        totalfitness = []
        
        for i in range(len(self.model.ducks)):
                                     
            Iter_text = str(i+1)
            print_Iter = font.render(Iter_text, 1, self.car_colors[i])
            Iter_pos = print_Iter.get_rect(bottomleft = (525, 125 + 15*i))
            self.screen.blit(print_Iter,Iter_pos)               
            
            totalfitness.append(self.model.ducks[i].Fitness)
            Fit_text = str(self.model.ducks[i].Fitness)
            print_Fit = font.render(Fit_text, 1, self.car_colors[i])
            Fit_pos = print_Fit.get_rect(bottomleft = (625, 125 + 15*i))
            self.screen.blit(print_Fit,Fit_pos)

            if self.model.ducks[i].FAIL:
                Fit_text = "dead )x"
                color = (184, 184, 184)
            elif self.model.ducks[i].FAIL == False:
                Fit_text = "still alive!"
                color = self.car_colors[i]           
            print_Fit = font.render(Fit_text, 1, color)
            Fit_pos = print_Fit.get_rect(bottomleft = (725, 125 + 15*i))
            self.screen.blit(print_Fit,Fit_pos)
                        
#            if i == len(self.model.ducks):
#                totalfitness = []
        
        res = sorted(range(len(totalfitness)), key=lambda i: totalfitness[i])[-2:]
        mostfit = [totalfitness[res[0]], totalfitness[res[1]]]
        best_text = "Two most fit  " +str(mostfit)

        print_best = font.render(best_text, 1, (255,255,255))
        best_pos = print_best.get_rect(bottomleft = (600, 75))
        self.screen.blit(print_best,best_pos)
        

        
        pygame.draw.line(self.screen, (255,255,255), (500,340),(800,340)) 
        
        if not self.model.genome.bestFitness == [] and self.model.genome.bestFitness[-1]>1600:
            self.ymax= 1600
        elif not self.model.genome.bestFitness == [] and self.model.genome.bestFitness[-1]>self.ymax:
            self.ymax=self.ymax*2
            
        for i in range(0,self.ymax/100+1,self.ymax/400):            
            y_str = str(i*100)
            print_y = font.render(y_str, 1, (255,255,255))
            y_pos = print_y.get_rect(bottomleft = (525, 480-30*400*i/self.ymax))
            self.screen.blit(print_y,y_pos) 
        
        
            
        x= 550
        yi = 475
        y=yi            
        
        for fit in self.model.genome.bestFitness:
            
            if fit>1600:
                fit = 3*(fit-10000)+1600
            
            xnew=x+self.xstep
            if xnew >=800:
                self.xstep=self.xstep/2
            ynew=yi-.3*400*fit/self.ymax
                           
            pygame.draw.line(self.screen, (255,255,255), (x,y),(xnew,ynew)) 
            #pygame.display.update()                
            
            y = ynew
            x=xnew

        pygame.display.update()




    def draw6(self):
        self.screen.fill(pygame.Color(0,0,0))
        
        i = 0
        for element in self.model.ducks:

            #print "drawing rect",i,element.rect.center
            if not self.model.ducks[i].FAIL:
                pygame.draw.rect(self.screen, pygame.Color(0,255,0), element.rect)
            else:
                pygame.draw.rect(self.screen, pygame.Color(255,0,0), element.rect)
            i+=1


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
      
        


        pygame.display.update()


    def evolution_animation(self,time):

        self.screen.fill(pygame.Color(60,60,60))

        font = pygame.font.Font(None, 30)
        Gen_text = 'When a daddy car and a mother car love each other very much...'
        print_Gen = font.render(Gen_text, 1, (255, 255, 255))
        Gen_pos = print_Gen.get_rect(center = (800/2.0,50))
        self.screen.blit(print_Gen,Gen_pos) 

        
        daddyCar = pygame.transform.scale(self.car_images_unScaled[0], (160,80))
        mommyCar = pygame.transform.scale(self.car_images_unScaled[1],(160,80))

        if time <.5:
            self.pos1 = pygame.Rect(int(100),int(100 ),160,80)
            self.pos2 = pygame.Rect(int(500),int(100 ),160,80)

        elif time <3:
            self.pos1 = pygame.Rect(int(100 + 80*(time-.5)),int(100 +10*(time-.5)),160,80)
            self.pos2 = pygame.Rect(int(500 - 80*(time-.5)),int(100 +10*(time-.5)),160,80)

        xpos_list = [50, 128, 206, 284, 362, 440, 518, 596, 674, 752, 50, 128, 206, 284, 362, 440, 518, 596, 674, 752]
        ypos_list = [300,300,300,300,   300, 300, 300, 300, 300, 300, 400, 400,400, 400, 400, 400, 400, 400, 400, 400]
        if time > 3:
            text_ev = 'Evolution!!'
            print_ev = font.render(text_ev, 1, (255, 255, 255))
            Gen_pos_ev = print_ev.get_rect(center = (800/2.0,250))
            self.screen.blit(print_ev,Gen_pos_ev) 

            i = 0
            for car in self.car_images_unScaled:
                pos = pygame.Rect(xpos_list[i]-30,ypos_list[i],160,80)
                self.screen.blit(pygame.transform.scale(car,(80,50)),pos)
                i += 1


        self.screen.blit(daddyCar, self.pos1)
        self.screen.blit(mommyCar,self.pos2)



        pygame.display.update()





