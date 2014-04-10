"""
@author: Sophie Li and Paul Titchener
"""

import pygame, random, math, time
from pygame.locals import *
import math

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
        while xInd in range(screen_size[0]):
            yInd = 0

            self.ArrayTrack.append([])
            while yInd in range(screen_size[1]):
                self.ArrayTrack[xInd].append(0)
                yInd +=1
            xInd +=1


        
    def update(self):
        self.duck.update(vx, vy)

    def new_individual(self):
        if self.duck.FAIL:
            self.duck = Duck(self,(100,100))

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
        self.FAIL = False
        self.fitness = 0
        self.RecentMovement = []
        self.TotalMovement = []

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

        self.RecentMovement.append((self.dx,self.dy))
        if abs(distance(self.RecentMovement)[0]) >30 or abs(distance(self.RecentMovement)[0]) >30:
            self.TotalMovement.append(distance(self.RecentMovement))
            self.RecentMovement = []
            print self.TotalMovement
            self.Fitness = distance(self.TotalMovement,True)
            print 'Fitness',self.Fitness

        self.read_sensor()

    def read_sensor(self):
        x = self.model.duck.x
        y = self.model.duck.y
        theta = self.model.duck.theta

        #sensor 1 is on the front, sensor 2 is on left, sensor 3 is on right

        #sensor 1 code:
        slope1 = math.tan(theta)

        hit1 = False
        if slope1 > .5:
            #y dominates
            yAdd = 0
            while not hit1:
                yInd = int(y+yAdd)
                xInd = int(x + yAdd*1.0/slope1)
                try:
                    hit1 = self.model.ArrayTrack[xInd][yInd] == 1
                except IndexError:
                    hit1 = True
                yAdd +=1
        else:
            # x dominates
            xAdd = 0
            while not hit1:
                xInd = int(x+xAdd)
                yInd = int(y + xAdd*slope1)
                try:
                    hit1 = self.model.ArrayTrack[xInd][yInd] == 1
                except IndexError:
                    hit1 = True
                xAdd +=1

        sensor1 = math.sqrt((x-xInd)**2 + (y-yInd)**2)
        print 'sensor val',sensor1
        return sensor1


        
    def collision_test(self, vx, vy):
        # Move the rect
        self.rect.x += vx
        self.rect.y += vy
    
        # If you collide with a wall, move out based on velocity
        for wall in self.model.Track3[1]:
            if self.rect.colliderect(wall.rect):
                self.FAIL = True
                print "FAIL"
        for wall in self.model.Track3[0]:
            if self.rect.colliderect(wall.rect):
                self.FAIL = True
                print "FAIL"

def distance(L,Absolute=False):
    """returns the sum of the distances between the elements of a lists
    Input: list
    Output: sum of the distances bewtwen the elements of the list
    """
    if not Absolute:
        x = 0
        y = 0
        for element in L:
            x += element[0]
            y += element[1]
        return (x,y)#math.sqrt(float(x)**2 + float(y)**2)
    else:
        x = 0
        y = 0
        for element in L:
            x += abs(element[0])
            y += abs(element[1])
        return (x,y)#math.sqrt(float(x)**2 + float(y)**2)
