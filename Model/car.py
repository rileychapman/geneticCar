# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 13:45:16 2014

@author: josh
"""
import pygame, random, math, time
from pygame.locals import *
import math
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

        self.read_sensors()
     
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
                
#        sensor_data = collide  #tuple(map(math.mean, zip(collide)))
#        return sensor_data        
#        
#    def check_sensor(self, theta, xp, yp):
#        x = 500*math.sin(theta)
#        y = 500*math.cos(theta)
#        
#        pygame.display.update()
#        
##        collide = []
#        m = (y-yp)/(x-xp)
#        b = y - m*x
#        
##        distance = math.sqrt((x-xp)**2 + (y-yp)**2)
##        dx = (x-xp)/distance
##        dy = (y-yp)/distance
##        pygame.draw.line(self.screen,(255,0,0),(xp,yp),(x,y))
##        distance = 0
#
#        x0 = xp #points that we're checking
#        y0 = yp
#        distance1 = 0
#        while (x0 < x) and (y0 < y):
##            y = mx + b
#            xp += 1
#            yp = m*xp + b
#            try:
#                if self.model.ArrayTrack[int(xp)][int(yp)] == 1:
#                    distance1 = math.hypot(xp - x0, yp - y0)
##                collide.append((xp,yp))
#                else:
#                    pass
#    
#            except IndexError:
#                distance1 = 'null'
#
#        return distance1                
##        sensor_data = collide  #tuple(map(math.mean, zip(collide)))
##        return sensor_data        
        
        
    def read_sensors(self):
        self.model.sensorPoints = []
        xp = int(self.model.duck.rect.x)
        yp = int(self.model.duck.rect.y)

        print "Current car location", xp, yp
        theta = float(self.model.duck.theta)
        theta_back = theta + (math.pi/2)
        print "Current car orientation", theta
        
        sensor1 = self.check_sensor(theta, xp, yp)
        sensor2 = self.check_sensor(theta_back, xp, yp)
        sensor3 = self.check_sensor(-theta_back, xp, yp)
        
        print "Closest forward block", sensor1
        print "Closest left block", sensor2
        print "Closest right block", sensor3

        return [sensor1, sensor2, sensor3]
        
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

