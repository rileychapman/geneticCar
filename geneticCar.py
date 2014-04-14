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
cheomNum = 0

screen = pygame.display.set_mode(size)
model = Model.Platformer_Model(size)
view = View.PyGameWindowView(model,screen)
controller = Controller.PyGameController(model)
genome = Controller.Genome()

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
<<<<<<< HEAD
    while not model.duck.FAIL:
        
            
        
      
      view.draw1()
      time.sleep(0.001)
    model.new_individual()
    
    genome.chromosomes[chromNum].stregnth = model.duck.fitness
    
    #changes to next chromosome
    chromNum =+1
    if chromnum == 20:
        genome.evolve()
        chromNum = 0      
    
    
      
pygame.quit()






#gen.live() #insert chromosome, test chomosme, repeat


#gen.print_genome()






=======

        if model.Testing == True:
            pass #make sure code builds before pushing
            #stick the matrix to the duck


    if model.duck.FAIL:
        model.duck.fitness #set this equal to the fitness for the chromosome that we were testing

        model.new_individual()
        
      
    view.draw1()
    time.sleep(0.001)

pygame.quit()
>>>>>>> upstream2/master
