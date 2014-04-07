"""
Genetic Car Algorithm

@author: Riley Chapman, Sophie Li, Josh Sapers, Paul Titchener

@teamName: Track Bot Driver (TBD)
"""
import driveMatrixEvolution
import modelViewController

if __name__ == '__main__':
	#drawTrack
	gen = driveMatrixEvolution.Genome(4)
	gen.live() #simulation
	gen.print_genome()

	gen.evolve()
	gen.live()
	gen.print_genome()

	gen.evolve()
	gen.live()
	gen.print_genome()





