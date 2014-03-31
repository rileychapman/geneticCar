"""
Facilitates Genetic Matrix evolution

@author: Riley Chapman

@teamName: Track Bot Driver (TBD)
"""

import matrixEvolution

class Chromosome:
	def __init__(self,length = 20):
		genes = []
		for i in range(length):
			genes.append(matrixEvolution.formMatrix(2,2))
		self.genes = genes
	
	def evolve(self):
		""" Takes in the best genes and creates a new chromosome for the next generation
			fittest: the best genes from the previous generation
		"""
		#mixMatrix
		#mutate



if __name__ == '__main__':
	chrom = Chromosome(2)
	print chrom.genes
