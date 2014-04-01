"""
Facilitates Genetic Matrix evolution

@author: Riley Chapman

@teamName: Track Bot Driver (TBD)
"""

import matrixEvolution
import random

class Chromosome:
	def __init__(self):
		self.genes = matrixEvolution.formMatrix(3,2)
		self.strength = 0.0 

class Genome:
	def __init__(self,population = 20,mutationRate = .5, mutationRange = .2):
		chrom = []
		for i in range(population):
			chrom.append(Chromosome())
		self.population = population
		self.chromosomes = chrom
		self.bestChromosomes = []
		self.generation = 1
		self.mutationRate = mutationRate
		self.mutationRange = mutationRange

	def print_genome(self):
		print 'Generation: ' + str(gen.generation)
		for chrom in self.chromosomes:
			print chrom.genes
			print chrom.strength
	
	def live(self):
		""" Test generation and determines the 2 most fit chromosomes
			Sets the bestChromosomes as determined by another function
		"""
		#random assignment of fittnes for now
		for chrom in self.chromosomes:
			chrom.strength = random.random()
		self.chromosomes.sort(key=lambda chromosomes: chromosomes.strength, reverse = True)

		self.bestChromosomes = self.chromosomes[0:2]


	def evolve(self):
		""" Takes the best genes and creates a new genome for the next generation
		"""
		# Create 20 mutations of each of the 2 best chromosomes
		i = self.population-1
		nextGenChromosomesA = []
		nextGenChromosomesB = []
		while i >= 0:
			AChrom = Chromosome()
			BChrom = Chromosome()
			AChrom.genes = matrixEvolution.mutateMatrix(self.bestChromosomes[0].genes,self.mutationRate,self.mutationRange)
			BChrom.genes = matrixEvolution.mutateMatrix(self.bestChromosomes[1].genes,self.mutationRate,self.mutationRange)
			nextGenChromosomesA.append(AChrom)
			nextGenChromosomesB.append(BChrom)
			i -= 1
		#combine the two groups to form the next generation genome
		nextGenChromos = []
		for chromA in nextGenChromosomesA:
			for chromB in nextGenChromosomesB:
				chrom = Chromosome()
				chrom.genes = matrixEvolution.mixMatrix(chromA.genes,chromB.genes)
				nextGenChromos.append(chrom)


		self.chromosomes = nextGenChromos
		self.generation += 1



if __name__ == '__main__':
	gen = Genome(3)
	gen.live()
	gen.print_genome()

	gen.evolve()
	gen.print_genome()




