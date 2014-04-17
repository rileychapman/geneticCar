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

    def print_chrom(self):
        print "   chromosome: " + str(self.genes) + '   strength: ' + str(self.strength)

class Genome:
    def __init__(self,population = 20,mutationRate = .05, mutationRange = .2):
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
        print 'Generation: ' + str(self.generation)
        for chrom in self.chromosomes:
            chrom.print_chrom()
    
    def random_live(self):
        """ Randomly assigns fittnes to each chromosome of the genome 
        """
        #random assignment of fittnes 
        for chrom in self.chromosomes:
            chrom.strength = random.random()
        self.chromosomes.sort(key=lambda chromosomes: chromosomes.strength, reverse = True)

        self.bestChromosomes = self.chromosomes[0:2]


    def evolve(self):
            """ Takes the best genes and creates a new genome for the next generation
            """
            bestChrom1=self.chromosomes[0]
            bestChrom2=self.chromosomes[1]
            for chrom in self.chromosomes:
                if chrom.strength > bestChrom1.strength:
                    bestChrom1=chrom
                elif chrom.strength > bestChrom2.strength:
                    bestChrom2=chrom
            self.bestChromosomes=[bestChrom1,bestChrom2]
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
            for i in range(len(nextGenChromosomesA)):
                chrom = Chromosome()
                chrom.genes = matrixEvolution.mixMatrix(nextGenChromosomesA[i].genes,nextGenChromosomesB[i].genes)
                nextGenChromos.append(chrom)
    
            self.chromosomes = nextGenChromos
            self.generation += 1
