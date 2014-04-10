"""
@author: Paul Titchener
"""


import Model
import View
import Controller

import pygame, random, math, time
from pygame.locals import *
import math


pygame.init()
walls = []
size = (500, 500)

screen = pygame.display.set_mode(size)
model = Model.Platformer_Model(size)
view = View.PyGameWindowView(model,screen)
controller = Controller.PyGameController(model)


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
      
    view.draw1()
    time.sleep(0.001)

pygame.quit()
