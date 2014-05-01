"""
Genetic Car Algorithm

@author: Riley Chapman, Sophie Li, Josh Sapers, Paul Titchener

@teamName: Track Bot Driver (TBD)
"""
#import driveMatrixEvolution
import Model
import View
import Controller

import pygame, random, math, time
from pygame.locals import *
import math


#generage a genome
#genomeLength = 4
#gen = driveMatrixEvolution.Genome(genomeLength) 


pygame.init()
walls = []
size = (500, 500)
chromNum = 0

screen = pygame.display.set_mode(size)
model = Model.Platformer_Model(size)
view = View.PyGameWindowView(model,screen)
controller = Controller.PyGameController(model)



running = True
while running:
       

    while not model.duck.FAIL and running:
  
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

x        if model.drawTrack == False and model.drawMode == False and model.offsetMode == False:
            controller.Drive(chromNum)
        if model.duck.FAIL:
            try:
                pass#print "Current Best Chrom 1  ID", model.genome.bestChromosomes[0].identification
            except IndexError:
                pass
                #print "No best Chrom yet"
            model.genome.chromosomes[chromNum].strength = model.duck.Fitness
            model.Iteration +=1
            chromNum +=1
            if chromNum == 19:
                model.genome.evolve()
                chromNum = 0     
                model.Iteration =0
                
        view.draw1()
        time.sleep(0.001)

    #print 'Final Fitness',model.duck.Fitness
    model.new_individual()

    
    #changes to next chromosome
 
    
    
      
pygame.quit()






#gen.live() #insert chromosome, test chomosme, repeat


#gen.print_genome()



