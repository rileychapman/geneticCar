# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 13:48:15 2014

@author: josh
"""
from math import *
class motion:
    def __init__(self,x,y,w1,w2,m1,m2,mt,l,theta):
        self.x = x        
        self.y = y
        self.vx = 0        
        self.vy = 0
        self.theta=theta #angle
        self.w1=w1 #wheel1
        self.w2=w2 #wheel2
        self.m1=m1 #wheel motion 1?
        self.m2=m2 #wheel motion 2?
        self.mt=mt #motion turn?
        self.l=l
        self.w=0
    def turn(self):
        t=self.w1-self.w2
        I = l * (self.m1+self.m2)*(self.m1+self.m2)/12.0
        self.w = t/I
    def move(self):
        self.theta+=self.w #updates angle
        f = self.w1+self.w2 #force on the car
        self.vx+=f/self.mt*cos(theta) #updates velocity
        self.vy+=f/self.mt*sin(theta) 
        self.x+=self.vx#updates position    
        self.y+=self.vy
        
        
        
        
        