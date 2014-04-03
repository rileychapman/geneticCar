# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 13:48:15 2014

@author: josh
"""
from math import *
class motion:
    def __init__(self,x,y,t1,t2,m1,m2,mt,l,theta):
        self.x = x        
        self.y = y
        self.vx = 0        
        self.vy = 0
        self.theta=theta
        self.t1=t1
        self.t2=t2
        self.m1=m1
        self.m2=m2
        self.mt=mt
        self.l=l
        self.w=0
    def turn(self):
        t=self.t1-self.t2
        I = l * (self.m1+self.m2)*(self.m1+self.m2)/12.0
        self.w = t/I
    def move(self):
        self.theta+=self.w
        self.vx+=(self.t1+self.t2)/self.mt*cos(theta)
        self.vy+=(self.t1+self.t2)/self.mt*sin(theta)
        self.x+=self.vx
        self.y+=self.vy
        
        
        
        
        