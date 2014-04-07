"""
Genetic Car Algorithm

@author: Riley Chapman, Sophie Li, Josh Sapers, Paul Titchener

@teamName: Track Bot Driver (TBD)
"""
import driveMatrixEvolution
import modelViewController
import pygame, random, math, time
from pygame.locals import *
import math

if __name__ == '__main__':
	#drawTrack
	pygame.init()
	walls = []
	size = (1200, 900)

	screen = pygame.display.set_mode(size)
	model = modelViewController.Platformer_Model(size)
	view = modelViewController.PyGameWindowView(model,screen)
	controller = modelViewController.PyGameController(model)

	running = True

	while running:
	       
	    for event in pygame.event.get():
	        if event.type == QUIT:
	            running = False
	        if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
	            controller.handle_pygame_event(event)
	            
	        if model.drawTrack == True and model.drawMode == True:
	            controller.draw_track()
	        if model.drawTrack == False and model.drawMode ==False and model.offsetMode == True:
	            controller.offset_track(50)
	            model.offsetMode = False

	    view.draw3()
	    time.sleep(0.001)

	pygame.quit()



	genomeLength = 4
	gen = driveMatrixEvolution.Genome(genomeLength) 


	gen.live() #insert chromosome, test chomosme, repeat


	gen.print_genome()






