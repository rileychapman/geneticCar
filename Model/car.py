# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 13:45:16 2014

@author: josh
"""
import pygame, random, math, time
from pygame.locals import *
import math
import time
from geneticModel import *

class Duck:
    """Code for moving car"""

    def __init__(self,model,pos):
        self.rect = pygame.Rect(pos[0], pos[1], 30, 15)
        self.x = pos[0]       #x position
        self.y = pos[1]        #y position
        self.dx = 0        
        self.dy = 0
        self.theta=0 #angle from the reference frame of the car is at angle zero if it pointed in the positive x direction. 
        self.radius = 5 #wheel radius
        self.pointlist = [pos,pos]
        self.model= model
        self.FAIL = False
        self.last_fail_time = time.time()
        self.Fitness = 0
        self.RecentMovement = []
        self.TotalMovement = []
        self.S = [50,50,50]
        self.SensorList = [[],[],[]]
        self.color = color
        self.assign_color()
        self.Fitness2 = 0
        self.FitnessNew = 0


#        self.screen = screen


    def assign_color(self):
#        print "assigning color"
        color1 = random.randint(50,255)
        color2 = random.randint(50,255)
        color3 = random.randint(50,255)

        self.color = pygame.Color(color1, color2, color3)
            
    def update(self, w1, w2):
        time2 = time.time()
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

        self.S=self.read_sensors()

        t=(w2-w1)*self.radius #distance around the turning circle that the wheels have traveled against each other
        w = math.atan(float(t)/self.rect.width)

        dist = float(w1+w2)/2 #calculates the forward distance by which the car travels

        self.theta+= w #updates angle\
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
            self.collision_test(self.dx,0)
        if self.dy != 0:
            self.collision_test(0, self.dy)

        self.RecentMovement.append((self.dx,self.dy))
        if abs(distance(self.RecentMovement)) >30 or abs(distance(self.RecentMovement)) >30:
            self.TotalMovement.append(distance(self.RecentMovement))
            self.RecentMovement = []
            #print self.TotalMovement
            self.Fitness = distance(self.TotalMovement,True)
            #print 'Fitness',self.Fitness

        #print 'total time', time.time()-time2

        self.time_limit()

        self.movement_limit()

        
        if True:
            distances = [math.hypot((self.x-element.pos[0]) , (self.y-element.pos[1])) for element in self.model.Track3[0]]
            distInt = 500
            for i in range(len(distances)):
                if distances[i] < distInt :
                    distInt = distances[i]
                    self.Fitnessnew = i
            diff = self.Fitnessnew - self.Fitness
            if diff >500:
                self.Fitness = -(len(self.model.Track3[0]) - self.Fitnessnew)
            else:
                self.Fitness = self.Fitnessnew

        if self.Fitness < -100:
            self.FAIL = True

        self.success_check()

    def time_limit(self):
#        print "in time limit"
        xp = self.rect.x
        yp = self.rect.y
        

        if (math.hypot(100-xp, 100-yp) < 50) and ((time.time() - self.last_fail_time) > 45) and self.Fitness < 50:
            print "Time expired"

            self.FAIL = True

    def movement_limit(self):

        positions = self.pointlist
        try:
            point1 = self.pointlist[-50]
            point2 = self.pointlist[-1]
            xDist = point1[0]-point2[0]
            yDist = point1[1]-point2[1]

            if math.hypot(xDist,yDist) < 5:

                self.color = pygame.Color(255, 0, 0)
                self.FAIL = True
                print "Too Slow"
        except IndexError:
            pass

    def success_check(self):
        xp = self.rect.x
        yp = self.rect.y
            
        if (math.hypot(100-xp, 100-yp) < 50) and self.Fitness >600:
            print "SUCCESS!"
            time_taken=time.time() - self.last_fail_time
            #print "Time to complete", time_taken
            self.Fitness = int(10000-time_taken)
            self.FAIL = True




                
    def read_sensors(self):
        self.SensorList = [[],[],[]]

        self.model.sensorPoints = []
        xp = int(self.rect.x)
        yp = int(self.rect.y)

        #print "Current car location", xp, yp
        theta = float(self.theta)
        #print "Current car orientation", theta
        
        sensor1 = self.check_sensor2(theta, xp, yp,0)
        sensor2 = self.check_sensor2(theta+math.pi/2, xp, yp,1)
        sensor3 = self.check_sensor2(theta-math.pi/2, xp, yp,2)
        
        #print "Closest forward block", sensor1
        #print "Closest left block", sensor2
        #print "Closest right block", sensor3

        return [sensor1, sensor2, sensor3]
        
    def collision_test(self, vx, vy):
        # Move the rect
        self.rect.x += vx
        self.rect.y += vy
    
        # If you collide with a wall, move out based on velocity
        for wall in self.model.Track3[1]:
            if self.rect.colliderect(wall.rect):
                self.last_fail_time = time.time()
#                print self.last_fail_time
                self.color = pygame.Color(255, 0, 0)
                self.FAIL = True                
#                print "FAIL"
        for wall in self.model.Track3[0]:
            if self.rect.colliderect(wall.rect):
                self.last_fail_time = time.time()
                self.color = pygame.Color(255, 0, 0)
#                print self.last_fail_time
                self.FAIL = True
                #print "FAIL"




    def check_sensor2(self, theta, xp, yp,iteration):
        x = 500*math.sin(theta)
        y = 500*math.cos(theta)
    
        for i in range(3*500):
            i2 = i/3
            xInd = xp + i2*math.cos(theta)
            yInd = yp + i2*math.sin(theta)
            self.SensorList[iteration].append((xInd,yInd))

            try:
                if self.model.ArrayTrack[int(xInd)][int(yInd)] == 1:
                    return math.hypot(xp-xInd,yp-yInd)
            except IndexError:
                return 500
        
        return 500



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
        return math.hypot(x,y)
    else:
        distance = 0
        for element in L:
            distance += element

        return distance

if __name__ == '__main__':
    print abs(distance([(1,1),(2,2)]))
