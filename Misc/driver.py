"""
Car Driver Class

@author: Paul Titchener

@teamName: Track Bot Driver (TBD)
"""
from math import *
class Car(object):
	"""Drives a car based on a matrix that defines the relationship between sensor values and power outputs"""
	def __init__(self,M,m1,m2,mt,l):
		"""Initialization Function"""
		self.M = M #parameter matrix
		self.w1 = 0 #wheel 1 velocity
		self.w2 = 0 #wheel 2 velocity
		self.x = 0
		self.y = 0
		self.dx = 0
		self.dy = 0
           self.vx = 0        
           self.vy = 0
           self.theta=0
           self.m1=m1
           self.m2=m2
           self.mt=mt
           self.l=l
           self.w=0
	def Drive(self,S):
		"""Creates w1 and w2 values for the car based on sensor values"""
		w1 = 0
		w2 = 0
		if len(self.M) != len(S):
			raise Exception("Number of Parameters does not Match Number of sensors")
		for i in range(len(self.M)):
			w1 += self.M[i][0]*S[i]
			w2 += self.M[i][1]*S[i]

		self.w1 = w1
		self.w2 = w2
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

if __name__ == '__main__':
	car = Car([[1,1],[1,1],[1,1]])
	car.Drive([1,1,1])
	print car.w1 , car.w2
