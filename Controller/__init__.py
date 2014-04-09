"""
@author: Sophie Li and Paul Titchener
"""

import pygame, random, math, time
from pygame.locals import *
import math

#walls = []

class Wall(object):
    def __init__(self, pos):

        #walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 5, 5)
        self.pos = pos

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
        self.model.Track.append(wallBlock)


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

        self.model.drawListInner.append(self.model.drawListInner[0])
        self.model.drawListOuter.append(self.model.drawListOuter[0])

        innerInd = 0
        while innerInd in range(len(self.model.drawListInner)-1):
            p1 = self.model.drawListInner[innerInd] #first point
            p2 = self.model.drawListInner[innerInd+1] #second point

            if abs(p1[0]-p2[0]) > abs(p1[1]-p2[1]):
                xSign = (p1[0] - p2[0])/abs(p1[0]-p2[0])
                print xSign
                xInd = 0
                slope = float(p1[1]-p2[1])/(p1[0]-p2[0])
                while xInd in range(abs(p1[0]-p2[0])):
                    yIndAppend = int(p1[1] - xSign*slope*xInd)
                    xIndAppend = int(p1[0] - xSign*xInd)
                    self.model.ArrayTrack[xIndAppend][yIndAppend] = 1 
                    xInd +=1
            elif (p1[1]-p2[1]) != 0:# abs(p1[0]-p2[0]) <= abs(p1[1]-p2[1]) :
                ySign = (p1[1] - p2[1])/abs(p1[1]-p2[1])
                print ySign
                yInd = 0
                if p1[1]-p2[1] !=0:
                    slope = float(p1[0]-p2[0])/(p1[1]-p2[1]) #note: different from the slope above. assumes a fucntion in y
                else:
                    slope = 50000
                while yInd in range(abs(p1[1]-p2[1])):
                    xIndAppend = int(p1[0] - ySign*slope*yInd)
                    yIndAppend = int(p1[1] - ySign*yInd)
                    self.model.ArrayTrack[xIndAppend][yIndAppend] = 1 
                    yInd +=1
            innerInd+=1

        outerInd = 0
        while outerInd in range(len(self.model.drawListOuter)-1):
            p1 = self.model.drawListOuter[outerInd] #first point
            p2 = self.model.drawListOuter[outerInd+1] #second point

            if abs(p1[0]-p2[0]) > abs(p1[1]-p2[1]):
                xSign = (p1[0] - p2[0])/abs(p1[0]-p2[0])


                xInd = 0
                slope = float(p1[1]-p2[1])/(p1[0]-p2[0])
                while xInd in range(abs(p1[0]-p2[0])):
                    yIndAppend = int(p1[1] - xSign*slope*xInd)
                    xIndAppend = int(p1[0] - xSign*xInd)
                    self.model.ArrayTrack[xIndAppend][yIndAppend] = 1 
                    xInd +=1
            elif (p1[1]-p2[1]) != 0:# abs(p1[0]-p2[0]) <= abs(p1[1]-p2[1]) :
                ySign = (p1[1] - p2[1])/abs(p1[1]-p2[1])

                yInd = 0
                if p1[1]-p2[1] != 0:
                    slope = float(p1[0]-p2[0])/(p1[1]-p2[1]) #note: different from the slope above. assumes a fucntion in y
                else:
                    slope = 50000
                while yInd in range(abs(p1[1]-p2[1])):
                    xIndAppend = int(p1[0] - ySign*slope*yInd)
                    yIndAppend = int(p1[1] - ySign*yInd)
                    self.model.ArrayTrack[xIndAppend][yIndAppend] = 1 
                    yInd +=1
            outerInd+=1

 



def dist_walls(wall1,wall2):
    return math.sqrt((wall1.pos[0]-wall2.pos[0])**2 + (wall1.pos[1]-wall2.pos[1])**2)