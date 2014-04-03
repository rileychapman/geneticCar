"""
Car Driver Class

@author: Paul Titchener

@teamName: Track Bot Driver (TBD)
"""

class Car(object):
	"""Drives a car based on a matrix that defines the relationship between sensor values and power outputs"""
	def __init__(self,M):
		"""Initialization Function"""
		self.M = M #parameter matrix
		self.w1 = 0 #wheel 1 velocity
		self.w2 = 0 #wheel 2 velocity
		self.x = 0
		self.y = 0
		self.dx = 0
		self.dy = 0


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

	def Position(self):
		pass

if __name__ == '__main__':
	car = Car([[1,1],[1,1],[1,1]])
	car.Drive([1,1,1])
	print car.w1 , car.w2
