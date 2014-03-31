"""
Facilitates Genetic Matrix evolution

@author: Riley Chapman

@teamName: Track Bot Driver (TBD)
"""

import matrixEvolution

def createChromosome(l):
	""" Builds a chromosome out of matrices
		l: length of chromosome
		returns: list of matrices representing a chromosome
	"""
	chromosome = []
	for i in range(l):
		chromosome.append(matrixEvolution.formMatrix(2,2))
	return chromosome
	
def evolve(fittest):
	""" Takes in the best genes and creates a new chromosome for the next generation
		fittest: the best genes from the previous generation
	"""
	mixMatrix
	mutate



if __name__ == '__main__':
	chrom = createChromosome(2)
	print chrom
