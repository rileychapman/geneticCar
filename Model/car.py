# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 13:45:16 2014

@author: josh
"""
from math import *
class car(object):
    def __init__(self,x,y,width,theta):
        self.x = x
        self.y = y
        self.width = width
        self.v = 0
        self.theta = theta
    def update(self,v):
        self.v=v
        self.x += v*cos(theta)
        self.y += v*sin(theta)