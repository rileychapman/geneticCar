# -*- coding: utf-8 -*-
"""
@author: sophiali
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
"""
def hold_levels():
    Normal function that holds our levels as lists. Any other way is too hard
    level = [[
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                 W",
        "W         WWWWWW                  W",
        "W   WWWW       W                  W",
        "W   W        WWWW                 W",
        "W WWW  WWWW                       W",
        "W   W     W W                     W",
        "W   W     W   WWW                WW",
        "W   WWW WWW   W W                 W",
        "W     W   W   W W                 W",
        "WWW   W   WWWWW W                 W",
        "W W      WW                       W",
        "W W   WWWW   WWW                  W",
        "W     W    W   W                  W",
        "W                                 W",
        "W                                 W",
        "W                                 W",
        "W                                 W",
        "W                                 W",
        "W                                 W",
        "WWWWWWWWWWWWW   WWWWWWWWWWWWWWWWW W",
        "W                                 W",
        "W                                 W",
        "WW                                W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                              ]]
    print level
    return level

def change_to_list(num):
    level = hold_levels()       
    for platform in level[num]:
        x = y = 0
        for row in level[num]:
            for col in row:
                if col == "W":
                    walls.append(Wall((x, y)))
#                    if col == "E":
#                        end_rect = pygame.Rect(x, y, 16, 16)
                x += 20
            y += 20
            x = 0
    return walls
    
blocks = change_to_list(0)
"""        
class Platformer_Model:
    """ Encodes the game state """
    """TO-DO: Clean up these level lists"""
    def __init__(self):
        #self.level1 = change_to_list(0)
        self.duck = Duck(self,(100,100))
        self.drawTrack = False
        self.drawMode = True
        self.Track = []
        self.offsetMode = True
        self.trackPopped = []
        self.innerTrack = []
        self.Track1 = [[],[]]
        self.Track2 = [[],[]]
        self.Track3 = [[],[]]
        
    def update(self):
        self.duck.update(vx, vy)

class Duck:
    """Code for moving car"""

    def __init__(self,model,pos):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        self.model = model

    def update(self, vx, vy):
        if vx != 0:
            self.collision_test(vx, 0)
        if vy != 0:
            self.collision_test(0, vy)
        
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
        pygame.draw.rect(screen, pygame.Color(0,255,0), model.duck.rect)
        for wall in walls:
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), wall.rect)          
        pygame.display.update()

    def draw1(self):
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.rect(screen, pygame.Color(0,255,0), model.duck.rect)
        if self.model.drawMode == True:
            for trackblock in model.Track:
                pygame.draw.rect(screen,pygame.Color(255,255,255),trackblock.rect)
        else:
            for trackblock in model.Track3[1]:
                pygame.draw.rect(screen,pygame.Color(255,255,255),trackblock.rect)
            for trackblock in model.Track3[0]: #model.FinalTrack[1]:
                pygame.draw.rect(screen,pygame.Color(255,0,255),trackblock.rect)
        pygame.display.update()

    def draw2(self):
        drawListInner  = []
        drawListOuter = []
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.rect(screen, pygame.Color(0,255,0), model.duck.rect)
        if self.model.drawMode == True:
            for trackblock in model.Track:
                intRect = trackblock.rect.inflate(50,50)
                pygame.draw.rect(screen,pygame.Color(255,255,255),intRect)
        else:
            drawInd = 0
            for trackblock in model.Track3[1]:
                drawListInner.append((trackblock.pos[0],trackblock.pos[1]))
            for trackblock in model.Track3[0]: #model.FinalTrack[1]:
                drawListOuter.append((trackblock.pos[0],trackblock.pos[1]))
            pygame.draw.lines(screen,(255,255,255),True,drawListInner)
            pygame.draw.lines(screen,(255,255,255),True,drawListOuter)   

        pygame.display.update()



class PyGameController:
    """ Manipulate game state based on keyboard input """
    def __init__(self, model):
        self.model = model
    
    def handle_pygame_event(self, event):
        if event.type == KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.model.duck.update(-10, 0)
            if event.key == pygame.K_RIGHT:
                self.model.duck.update(10,0)
            if event.key == pygame.K_UP:
                self.model.duck.update(0,-10)
            if event.key == pygame.K_DOWN:
                self.model.duck.update(0,10)
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
            print 'index',innerInd,'length', len(self.model.Track1[0])
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

        print 'number of popped elements',numPopped

def dist_walls(wall1,wall2):
    return math.sqrt((wall1.pos[0]-wall2.pos[0])**2 + (wall1.pos[1]-wall2.pos[1])**2)

if __name__ == '__main__':
#    walls = []
    pygame.init()
    walls = []
    size = (1200, 900)

    screen = pygame.display.set_mode(size)
    model = Platformer_Model()
    view = PyGameWindowView(model,screen)
    controller = PyGameController(model)


    running = True

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
    

        
#        model.update()
        view.draw1()
        time.sleep(0.001)

    pygame.quit()