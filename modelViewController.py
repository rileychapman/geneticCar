# -*- coding: utf-8 -*-
"""
@author: sophiali and Paul Titchener
"""

import pygame, random, math, time
from pygame.locals import *
import math

walls = []

class Wall(object):
    def __init__(self, pos):

        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 5, 5)
        self.pos = pos

class Platformer_Model:
    """ Encodes the game state """
    """TO-DO: Clean up these level lists"""
    def __init__(self,screen_size):
        #self.level1 = change_to_list(0)
        self.duck = Duck(self,(100,100))
        self.drawTrack = False
        self.drawMode = True
        self.Track = []
        self.offsetMode = True
        self.Track1 = [[],[]]
        self.Track2 = [[],[]]
        self.Track3 = [[],[]]
        self.ArrayTrack = []
        self.drawListInner = []
        self.drawListOuter = []
        #making the track be an array instead of pair of lists
        xInd = 0
        while xInd in range(size[0]):
            yInd = 0

            self.ArrayTrack.append([])
            while yInd in range(size[1]):
                self.ArrayTrack[xInd].append(0)
                yInd +=1
            xInd +=1


        
    def update(self):
        self.duck.update(vx, vy)

class Duck:
    """Code for moving car"""

    def __init__(self,model,pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        self.x = pos[0]       #x position
        self.y = pos[1]        #y position
        self.dx = 0        
        self.dy = 0
        self.theta=0 #angle from the reference frame of the car is at angle zero if it pointed in the positive x direction. 
        self.radius = 5 #wheel radius
        self.pointlist = [pos,pos]
        self.model= model

    def update(self, w1, w2):
        """ updates the position and angle of the car given the speed of rotation of the wheel. Angular veloctity of the wheel is use rather than a torque output becuase
        the only way to reasonable simuulate a torque output would be to calcualte the loading curve of the motor. At this point in the project it is 
        more reasonable to assume an ideal motor that does not respond to differenct loading conditions, or a motor with a well tuned PID loop and feedback
        Inputs:
        W1: angular velocity of wheel 1. This is the wheel on the left side of the car, looking from the back
        W2: angular velocity of wheel 2. This is the wheel on the right side of the car, looking from the back

        Outputs:
        Car angle, x and y updated
        Car angle is determined from the reference frame of the car
        """
        t=(w2-w1)*self.radius #distance around the turning circle that the wheels have traveled against each other
        w = math.atan(float(t)/self.rect.width)

        dist = float(w1+w2)/2 #calculates the forward distance by which the car travels

        self.theta+=w #updates angle\

        #updating the position of the car
        self.dx = dist*math.cos(self.theta)
        self.dy = dist*math.sin(self.theta)

        self.x += self.dx
        self.y += self.dy
        self.rect.center = (self.x,self.y)

        """
        print 'w',w,"theta",self.theta,'dist',dist
        print 'x',self.x,'dx',self.dx,'y',self.y,'dy',self.dy
        print "wheel1pos", (self.x-self.rect.width/2*math.sin(self.theta),self.y+self.rect.width/2*math.cos(self.theta) )
        #print "wheel2pos", (self.x+self.rect.width/2*math.sin(self.theta),self.y-self.rect.width/2*math.cos(self.theta) )

        print """
        self.pointlist.append((self.x,self.y))
    

        if self.dx != 0:
            self.collision_test(self.dx, 0)
        if self.dy != 0:
            self.collision_test(0, self.dy)
        
    def collision_test(self, vx, vy):
        # Move the rect
        self.rect.x += vx
        self.rect.y += vy
    
        # If you collide with a wall, move out based on velocity
        for wall in self.model.Track3[1]:
            if self.rect.colliderect(wall.rect):
                if vx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if vx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if vy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if vy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
        for wall in self.model.Track3[0]:
            if self.rect.colliderect(wall.rect):
                if vx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if vx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if vy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if vy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    
    

        
class Platform:
    """ Encodes the state of a singular rectangular platform in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

class PyGameWindowView:
    """ Draws our game in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
                   
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.rect(self.screen, pygame.Color(0,255,0), model.duck.rect)
        for wall in walls:
            pygame.draw.rect(self.screen, pygame.Color(255, 255, 255), wall.rect)          
        pygame.display.update()

    def draw1(self):
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.rect(self.screen, pygame.Color(0,255,0), model.duck.rect)
        if self.model.drawMode == True:
            for trackblock in model.Track:
                pygame.draw.rect(self.screen,pygame.Color(255,255,255),trackblock.rect)
        else:
            for trackblock in model.Track3[1]:
                pygame.draw.rect(self.screen,pygame.Color(255,255,255),trackblock.rect)
            for trackblock in model.Track3[0]: #model.FinalTrack[1]:
                pygame.draw.rect(self.screen,pygame.Color(255,0,255),trackblock.rect)
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
            pygame.draw.lines(self.screen,(255,255,255),True,drawListInner)
            pygame.draw.lines(self.screen,(255,255,255),True,drawListOuter)   

        pygame.display.update()

    def draw3(self):
        drawListInner  = []
        drawListOuter = []
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.lines(self.screen,(255,255,255),False,self.model.duck.pointlist)

        pygame.draw.rect(self.screen, pygame.Color(0,255,0), model.duck.rect)
        if self.model.drawMode == True:
            for trackblock in model.Track:
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
            for trackblock in model.Track:
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
            listInnerInt = self.model.drawListInner[0:]
            listOuterInt = self.model.drawListOuter[0:]
            pygame.draw.lines(self.screen,(255,255,255),True,listInnerInt)
            pygame.draw.lines(self.screen,(255,255,255),True,listOuterInt)   


        pygame.display.update()






class PyGameController:
    """ Manipulate game state based on keyboard input """
    def __init__(self, model):
        self.model = model
    
    def handle_pygame_event(self, event):
        if event.type == KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.model.duck.update(4,5)
            if event.key == pygame.K_RIGHT:
                self.model.duck.update(5,4)
            if event.key == pygame.K_UP:
                self.model.duck.update(5,5)
            if event.key == pygame.K_DOWN:
                self.model.duck.update(-5,-5)
        if event.type == MOUSEBUTTONDOWN:
            self.model.drawTrack = True
    
        elif event.type == MOUSEBUTTONUP:
            self.model.drawTrack=False
            self.model.drawMode =False
        else:
            return

    def draw_track(self):
        wallBlock = Wall(pygame.mouse.get_pos())
        model.Track.append(wallBlock)


    def offset_track(self,radius):
        i = 0
        for element in self.model.Track:
            xDiff = float((element.pos[0] - self.model.Track[i-1].pos[0]))
            yDiff = float((element.pos[1] - self.model.Track[i-1].pos[1]))

            if xDiff == 0 and yDiff ==0:
                pass
            elif xDiff != 0:
                xSign = xDiff/abs(xDiff)
                slope = yDiff/xDiff#float((element.pos[1] - self.model.Track[i-1].pos[1]))/(element.pos[0] - self.model.Track[i-1].pos[0])
                if slope != 0:
                    ySign = yDiff/abs(yDiff)
                    slopeSign = slope/abs(slope)

                    perpendicularSlope = -1.0/slope
                    angle = math.atan(perpendicularSlope)
                    innerPos = (element.pos[0] + abs(math.cos(angle))*radius*(xSign**2*ySign) , element.pos[1] + abs(math.sin(angle))*radius*-(xSign*ySign**2))
                    outerPos = (element.pos[0] - abs(math.cos(angle))*radius*(xSign**2*ySign) , element.pos[1] - abs(math.sin(angle))*radius*-(xSign*ySign**2))
                else:
                    innerPos = (element.pos[0] , element.pos[1] + radius*-xDiff/abs(xDiff))
                    outerPos = (element.pos[0] , element.pos[1] - radius*-xDiff/abs(xDiff))

            else:
                innerPos = (element.pos[0] +radius*yDiff/abs(yDiff), element.pos[1])
                outerPos = (element.pos[0] -radius*yDiff/abs(yDiff), element.pos[1])
            
            #print math.sqrt((innerPos[0]-outerPos[0])**2 + (innerPos[1]-outerPos[1])**2)


            innerBlock = Wall(innerPos)
            outerBlock = Wall(outerPos)
            self.model.Track1[0].append(innerBlock)
            self.model.Track1[1].append(outerBlock)

            i +=1

        #Check for outliers 
        innerInd = 1
        while innerInd in range(len(self.model.Track1[0])-2):
            innerPop = False
            if dist_walls(self.model.Track1[0][innerInd],self.model.Track1[0][innerInd+1]) > 20:
                innerPop = True
            if not innerPop:
                self.model.Track2[0].append(self.model.Track1[0][innerInd])
            innerInd +=1

        outerInd = 1
        while outerInd in range(len(self.model.Track1[1])-2):
            outerPop = False
            if dist_walls(self.model.Track1[1][outerInd],self.model.Track1[1][outerInd+1]) > 20 :
                outerPop = True
            if not outerPop:
                self.model.Track2[1].append(self.model.Track1[1][outerInd])
            outerInd +=1





        #Make sure that the tracks are the proper distance appart
        j = 0
        numPopped = 0
        sizePopped = len(self.model.Track2[0])
        for innerElement in self.model.Track2[0]:
            popped = False
            for outerElement in self.model.Track2[1]:
                if not popped:    
                    #if abs(innerElement.pos[0] - outerElement.pos[0]) < radius*2+5 and abs(innerElement.pos[1] - outerElement.pos[1]) < radius*2+5: #radius-20 > math.sqrt((innerElement.pos[0]-outerElement.pos[0])**2 + (innerElement.pos[1]-outerElement.pos[1])**2) :# If the distance is too snall between any two inner and outer elements, remove those elements
                    if  math.sqrt((innerElement.pos[0]-outerElement.pos[0])**2 + (innerElement.pos[1]-outerElement.pos[1])**2) <= float(radius*2-5) :
        
                        popped = True
                        numPopped +=1

            if not popped:
                self.model.Track3[0].append(innerElement)
            j+=1

        for element in self.model.Track2[1]:
            self.model.Track3[1].append(element)


        drawInd = 0
        for trackblock in self.model.Track3[1]:
            self.model.drawListInner.append((int(trackblock.pos[0]),int(trackblock.pos[1])))
        for trackblock in self.model.Track3[0]: 
            self.model.drawListOuter.append((int(trackblock.pos[0]),int(trackblock.pos[1])))

        innerInd = 0
        while innerInd in range(len(self.model.drawListInner)-1):
            p1 = self.model.drawListInner[innerInd] #first point
            p2 = self.model.drawListInner[innerInd+1] #second point
            xSign = p1[0] - p2[0]
            ySign = p1[1] - p2[1]

            if abs(p1[0]-p2[0]) > abs(p1[1]-p2[1]):
                xInd = 0
                slope = float(p1[1]-p2[1])/(p1[0]-p2[0])
                while xInd in range(abs(p1[0]-p2[0])):
                    yIndAppend = int(p1[1] + slope*xInd)
                    xIndAppend = int(p1[0] + xInd)
                    self.model.ArrayTrack[xIndAppend][yIndAppend] = 1 
                    xInd +=1
            else:# abs(p1[0]-p2[0]) <= abs(p1[1]-p2[1]) :
                yInd = 0
                if p1[1]-p2[1] !=0:
                    slope = float(p1[0]-p2[0])/(p1[1]-p2[1]) #note: different from the slope above. assumes a fucntion in y
                else:
                    slope = 50000
                while yInd in range(abs(p1[1]-p2[1])):
                    xIndAppend = int(p1[0] - slope*yInd)
                    yIndAppend = int(p1[1] - yInd)
                    self.model.ArrayTrack[xIndAppend][yIndAppend] = 1 
                    yInd +=1
            innerInd+=1

        outerInd = 0
        while outerInd in range(len(self.model.drawListOuter)-1):
            p1 = self.model.drawListOuter[outerInd] #first point
            p2 = self.model.drawListOuter[outerInd+1] #second point

            if abs(p1[0]-p2[0]) > abs(p1[1]-p2[1]):
                xInd = 0
                slope = float(p1[1]-p2[1])/(p1[0]-p2[0])
                while xInd in range(abs(p1[0]-p2[0])):
                    yIndAppend = int(p1[1] + slope*xInd)
                    xIndAppend = int(p1[0] + xInd)
                    self.model.ArrayTrack[xIndAppend][yIndAppend] = 1 
                    xInd +=1
            else:# abs(p1[0]-p2[0]) <= abs(p1[1]-p2[1]) :
                yInd = 0
                if p1[1]-p2[1] != 0:
                    slope = float(p1[0]-p2[0])/(p1[1]-p2[1]) #note: different from the slope above. assumes a fucntion in y
                else:
                    slope = 50000
                while yInd in range(abs(p1[1]-p2[1])):
                    xIndAppend = int(p1[0] - slope*yInd)
                    yIndAppend = int(p1[1] - yInd)
                    self.model.ArrayTrack[xIndAppend][yIndAppend] = 1 
                    yInd +=1
            outerInd+=1

 



def dist_walls(wall1,wall2):
    return math.sqrt((wall1.pos[0]-wall2.pos[0])**2 + (wall1.pos[1]-wall2.pos[1])**2)

if __name__ == '__main__':
#    walls = []
    pygame.init()
    walls = []
    size = (500, 500)

    screen = pygame.display.set_mode(size)
    model = Platformer_Model(size)
    view = PyGameWindowView(model,screen)
    controller = PyGameController(model)


    running = True
    running2= False
    while running:
           
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                controller.handle_pygame_event(event)
                
            if model.drawTrack == True and model.drawMode == True:
                controller.draw_track()
            if model.drawTrack == False and model.drawMode ==False and model.offsetMode == True:
                controller.offset_track(50)
                model.offsetMode = False
          
        view.draw4()
        time.sleep(0.001)

    pygame.quit()