# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 13:45:16 2014

@author: josh
"""
import pygame, random, math, time
from pygame.locals import *
import math
import time
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
        self.last_fail_time = time.time()
        self.fitness = 0
        self.Fitness = 0
        self.RecentMovement = []
        self.TotalMovement = []
        self.S = [50,50,50]
        self.SensorList = []
#        self.screen = screen

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
            self.collision_test(self.dx, 0)
        if self.dy != 0:
            self.collision_test(0, self.dy)

        self.RecentMovement.append((self.dx,self.dy))
        if abs(distance(self.RecentMovement)[0]) >30 or abs(distance(self.RecentMovement)[0]) >30:
            self.TotalMovement.append(distance(self.RecentMovement))
            self.RecentMovement = []
            #print self.TotalMovement
            self.Fitness = distance(self.TotalMovement,True)
            print 'Fitness',self.Fitness

        self.S=self.read_sensors()
        self.time_limit()
#        self.success_check()
    
    
    def time_limit(self):
#        print "in time limit"
        xp = self.rect.x
        yp = self.rect.y
        
        if (math.hypot(100-xp, 100-yp) < 50) and ((time.time() - self.last_fail_time) > 15):
            print "Time expired"
            self.FAIL = True
    
    def success_check(self):
        xp = self.rect.x
        yp = self.rect.y
        
        if (yp == 100) and (50 <= xp <= 200) and self.Fitness<50:
            print "SUCCESS!"
            time_taken=time.time() - self.last_fail_time
            print "Time to complete", time_taken
            self.Fitness = 10000-time_taken
            self.FAIL = True

            
    
     
    def check_sensor(self, theta, xp, yp):
        x = 500*math.sin(theta)
        y = 500*math.cos(theta)
        
        pygame.display.update()
        
#        collide = []
        
        distance = math.sqrt((x-xp)**2 + (y-yp)**2)
        dx = (x-xp)/distance
        dy = (y-yp)/distance
#        pygame.draw.line(self.screen,(255,0,0),(xp,yp),(x,y))
        distance = 0
        
        while distance <= 600:
            xp += dx
            yp += dy
            
            distance += 1
            
            if self.model.ArrayTrack[int(xp)][int(yp)] == 1:
#                collide.append((xp,yp))
                return distance

        return 0
                
    def read_sensors(self):
        self.SensorList = []

        self.model.sensorPoints = []
        xp = int(self.rect.x)
        yp = int(self.rect.y)

        #print "Current car location", xp, yp
        theta = float(self.theta)
        #print "Current car orientation", theta
        
        sensor1 = self.check_sensor2(theta, xp, yp)
        sensor2 = self.check_sensor2(theta+math.pi/2, xp, yp)
        sensor3 = self.check_sensor2(theta-math.pi/2, xp, yp)
        
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
                self.FAIL = True                
#                print "FAIL"
        for wall in self.model.Track3[0]:
            if self.rect.colliderect(wall.rect):
                self.last_fail_time = time.time()
#                print self.last_fail_time
                self.FAIL = True
                #print "FAIL"


    def check_sensor1(self, theta, xp, yp):
        self.SensorList = []
        x = 500*math.sin(theta+math.pi/2)
        y = 500*math.cos(theta+math.pi/2)
        

        #calculating slopeb
        if abs(x) >= abs(y):
            functionOf  = 'X'
            if x != 0:
                slope = y/float(x)
            else:
                slope = 9999
        else:
            functionOf = 'Y'
            if y != 0:
                slope = x/float(y)
            else:
                slope = 9999

        #calculating direction of travel along the slope

        if functionOf == 'X':
            dirTravel = x/abs(x)
        else:
            dirTravel = y/abs(y)

        #iterating through that slope

        for i in range(500):
            if functionOf == 'X':
                xInd = i + xp
                yInd = i*slope + yp
            else:
                yInd = i + yp
                xInd = i*slope + xp

            self.SensorList.append((xInd,yInd))

            try:
                if self.model.ArrayTrack[int(xInd)][int(yInd)] == 1:
                    dist = math.hypot(xp-xInd,yp-yInd)
                    return dist 
            except IndexError:
                return 500

    def check_sensor2(self, theta, xp, yp):
        x = 500*math.sin(theta)
        y = 500*math.cos(theta)
    
        for i in range(20000):
            i2 = i/40.0
            xInd = xp + i2*math.cos(theta)
            yInd = yp + i2*math.sin(theta)
            self.SensorList.append((xInd,yInd))

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
        return (x,y)#math.sqrt(float(x)**2 + float(y)**2)
    else:
        x = 0
        y = 0
        for element in L:
            x += abs(element[0])
            y += abs(element[1])
        return math.sqrt(float(x)**2 + float(y)**2)

