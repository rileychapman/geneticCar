# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 14:43:31 2014

@author: sophie
"""
import pygame, random, math, time
from pygame.locals import *
import math
import time
import os


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Duck_sprite(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, pos):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image, self.rect = load_image("car1.jpg", -1)
       screen = pygame.display.get_surface()
       self.area = screen.get_rect()
       self.rect.x = pos[0]
       self.rect.y = pos[1]

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
#       self.rect = self.image.get_rect()
       
#def main():
#    """this function is called when the program starts.
#       it initializes everything it needs, then runs in
#       a loop until the function returns."""
##Initialize Everything
#    pygame.init()
#    screen = pygame.display.set_mode((500, 500))
#    pygame.display.set_caption('Monkey Fever')
#    pygame.mouse.set_visible(1)
#
##Create The Backgound
#    background = pygame.Surface(screen.get_size())
#    background = background.convert()
#    background.fill((250, 250, 250))
#
##Put Text On The Background, Centered
##    if pygame.font:
##        font = pygame.font.Font(None, 36)
##        text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
##        textpos = text.get_rect(centerx=background.get_width()/2)
##        background.blit(text, textpos)
#
##Display The Background
#    screen.blit(background, (0, 0))
#    pygame.display.flip()
#
##Prepare Game Objects
##    clock = pygame.time.Clock()
##    whiff_sound = load_sound('whiff.wav')
##    punch_sound = load_sound('punch.wav')
##    chimp = Chimp()
##    fist = Fist()
#    block = Duck_sprite([400,200])
#    allsprites = pygame.sprite.RenderPlain(block)
#
##Main Loop
#    while 1:
#
#    #Handle Input Events
#        for event in pygame.event.get():
#            if event.type == QUIT:
#                return
#            elif event.type == KEYDOWN and event.key == K_ESCAPE:
#                return
##            elif event.type == MOUSEBUTTONDOWN:
##                if fist.punch(chimp):
##                    punch_sound.play() #punch
##                    chimp.punched()
##                else:
##                    whiff_sound.play() #miss
##            elif event.type is MOUSEBUTTONUP:
##                fist.unpunch()
#
#        allsprites.update()
#
#    #Draw Everything
#        screen.blit(background, (0, 0))
#        allsprites.draw(screen)
#        pygame.display.flip()
#
##Game Over
#
#main()