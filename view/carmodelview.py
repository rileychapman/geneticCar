#! /usr/bin/env python

import os
from pygame.locals import *
import random
import pygame
#from world import *

class Platformer_Model:
    """encodes data of game into one model"""
    def __init__(self):
        self.car = Car(40,40)
        self.walls = []
        self.construct_environment(0)
        
    def construct_environment(self, number):
        """generates level states"""
        self.walls = []
        level = [
                "WWWWWWWWWWWWWWWWWWWW",
                "W                  W",
                "W WWWWWWWWWWWWWWWW W",
                "W W              W W",
                "W W              W W",
                "W W              W W",
                "W W              W W",
                "W W              W W",
                "W W              W W",
                "W W              W W",
                "W W              W W",
                "W W              W W",
                "W WWWWWWWWWWWWWWWW W",
                "W                  W",
                "WWWWWWWWWWWWWWWWWWWW",
                ]

        for platform in level:
            x = y = 0
            for row in level[num]:
                for col in row:
                    self.walls.append(Wall(x,y))
                    x += 20
                y += 20
                x = 0
                
    def update(self):
        self.paddle.update()
                
#    def move_single_axis(self, number):
#        """moves car box around world"""


class Platformer_View:
    def __init__(self):
        self.walls = []

# Class for the orange dude
class Car():
    
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def update(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.collision_test(dx, 0)
        if dy != 0:
            self.collision_test(0, dy)
    
    def collision_test(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    
class Controller:
    def __init__(self, model):
        self.model = model
    
    def handle_mouse_event(self, event):
            
    # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            car.update(-2, 0)
        if key[pygame.K_RIGHT]:
            car.update(2, 0)
        if key[pygame.K_UP]:
            car.update(0, -2)
        if key[pygame.K_DOWN]:
            car.update(0, 2)

# Nice class to hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)



if __name__ == '__main__':
    pygame.init()
    walls = []
    pygame.display.set_caption("Genetic Car goooooo")
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    model = Platformer_Model()
    view = Platformer_View(model,screen)
    controller = Controller(model)

    running = True

    while running:
           
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                controller.handle_pygame_mouse(event)
#        controller.handle_pygame_key()
        model.update()
        view.draw()
        time.sleep(0.001)

    pygame.quit()
#
#def main():
#    # Initialise pygame
#    os.environ["SDL_VIDEO_CENTERED"] = "1"
#    pygame.init()
#    
#    # Set up the display
#    pygame.display.set_caption("Get to the red square!")
#    screen = pygame.display.set_mode((320, 240))
#    
#    clock = pygame.time.Clock()
#    walls = [] # List to hold the walls
#    player = Car() # Create the player
#    Platformer_Model()
#    # Holds the level layout in a list of strings.
#    #
#    ## Parse the level string above. W = wall, E = exit
#    #x = y = 0
#    #for row in level:
#    #    for col in row:
#    #        if col == "W":
#    #            Wall((x, y))
#    ##        if col == "E":
#    ##            end_rect = pygame.Rect(x, y, 16, 16)
#    #        x += 16
#    #    y += 16
#    #    x = 0
#    
#    running = True
#    while running:
#        
#        clock.tick(60)
#        
#
#        
#        # Just added this to make it slightly fun ;)
#    #    if player.rect.colliderect(end_rect):
#    #        raise SystemExit, "You win!"
#    #    
#        # Draw the scene
#        screen.fill((0, 0, 0))
#        for wall in walls:
#            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
#    #    pygame.draw.rect(screen, (255, 0, 0), end_rect)
#        pygame.draw.rect(screen, (255, 200, 0), player.rect)
#        pygame.display.flip()