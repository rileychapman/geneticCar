# -*- coding: utf-8 -*-
"""
@author: sophiali
"""

import pygame, random, math, time
from pygame.locals import *

walls = []

class Wall(object):
    def __init__(self, posx, posy):
#        walls.append(self)
        self.rect = pygame.Rect(posx, posy, 20, 20)
        self.posx = posx
        self.posy = posy
        
#class Inner_wall(object):
#    def __init__(self, pos):
#        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)
        
def hold_levels():
    """Normal function that holds our levels as lists. Any other way is too hard"""
    level = [[
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                 W",
        "W  WWWWWWWWWWWWWWWWWWWWWWWWWWWWW  W",
        "W  W                           W  W",
        "W  W                           W  W",
        "W  W  IIIIIIIIIIIIIIIIIIIIIII  W  W",
        "W  W  I                     I  W  W",
        "W  W  I                     I  W  W",
        "W  W  I                     I  W  W",
        "W  W  I                     I  W  W",
        "W  W  I                     I  W  W",
        "W  W  I                     I  W  W",
        "W  W  I                     I  W  W",
        "W  W  I                     I  W  W",
        "W  W  I                     I  W  W",
        "W  W  I                     I  W  W",
        "W  W  I                     I  W  W",
        "W  W  I                     I  W  W",
        "W  W  I                     I  W  W",
        "W  W  IIIIIIIIIIIIIIIIIIIIIII  W  W",
        "W  W                           W  W",
        "W  W                           W  W",
        "W  WWWWWWWWWWWWWWWWWWWWWWWWWWWWW  W",
        "W                                 W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                                            ]]
    print level
    return level

def change_to_list(num):
#    walls = []
    level = hold_levels()       
    for platform in level[num]:
        x = y = 0
        for row in level[num]:
            for col in row:
                if col == "W":
                    walls.append(Wall(x, y))
#                if col == "I":
#                    walls.append(Inner_wall(x,y))
                x += 20
            y += 20
            x = 0
    return walls
    
blocks = change_to_list(0)
        
class Platformer_Model:
    """ Encodes the game state """
    """TO-DO: Clean up these level lists"""
    def __init__(self):
        self.level1 = change_to_list(0)
        self.duck = Duck()
        
    def update(self):
        self.duck.update(vx, vy)

class Duck:
    """Code for moving car"""
    def __init__(self):
        self.rect = pygame.Rect(80, 80, 20, 20)
        
    def update(self, vx, vy):
        if vx != 0:
            self.collision_test(vx, 0)
        if vy != 0:
            self.collision_test(0, vy)
        
    def collision_test(self, vx, vy):
        # Move the rect
        self.rect.x += vx
        self.rect.y += vy
    
        # If you collide with a wall, move out based on velocity
        for wall in blocks:
            if self.rect.colliderect(wall.rect):
                if vx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if vx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if vy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if vy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    
    

        
class Platform:
    """ Encodes the state of a singular rectangular platform in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

class PyGameWindowView:
    """ Draws our game in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
                   
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.rect(screen, pygame.Color(0,255,0), model.duck.rect)
        for wall in walls:
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), wall.rect)          
        pygame.display.update()
    
    def distance_calculate(self):
        xp = float(self.model.duck.rect.x)
        yp = float(self.model.duck.rect.y)
        print "Current car location", xp, yp
        calcu = []
        xdistance = []
        ydistance = []
        
        for wall in self.model.level1:

            wallx = float(wall.posx-xp)
            wally = float(wall.posy-yp)
            calcu.append((wallx, wally))
#        print calcu
        for walltuple in calcu:
            if walltuple[0] == xp:
#                print ydistance, "stuff"
                ydistance.append((walltuple[1]))
            #                xblocks.append(walltuple[0])
            if walltuple[1] == yp:
#                print xdistance, "stuff"
#                yblocks.append(walltuple[1])
                xdistance.append((walltuple[0]))
        if len(ydistance) == 0:
            raise Exception("No length on y")
        print "TOP", abs(min(x for x in ydistance if (x is not 0 and x < 0)))
        print "BOTTOM", min(x for x in ydistance if (x is not 0 and x > 0))
        print "RIGHT", min(x for x in xdistance if (x is not 0 and x > 0))
        print "LEFT", abs(min(x for x in xdistance if (x is not 0 and x < 0)))
        print " "
        
class PyGameKeyboardController:
    """ Manipulate game state based on keyboard input """
    def __init__(self, model):
        self.model = model
    
    def handle_pygame_event(self, event):
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            self.model.duck.update(-10, 0)
        if event.key == pygame.K_RIGHT:
            self.model.duck.update(10,0)
        if event.key == pygame.K_UP:
            self.model.duck.update(0,-10)
        if event.key == pygame.K_DOWN:
            self.model.duck.update(0,10)
    



if __name__ == '__main__':
#    walls = []
    pygame.init()
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    model = Platformer_Model()
    view = PyGameWindowView(model,screen)
    controller = PyGameKeyboardController(model)
    distance = [[0,0], [0,0]]
#    car = Duck()
#    pygame.draw.rect(screen, (255, 200, 0), car.rect)

    running = True

    while running:
           
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                controller.handle_pygame_event(event)
                view.distance_calculate()
        
#        model.update()
        view.draw()
#        distancenew = view.distance_calculate()
#        distance.append(distancenew)
#        if distance[-1][0] != distance[-2][0]:
#            print distance
#        if distance[-1][1] != distance[-2][1]:
#            print distance
#            
        time.sleep(0.001)

    pygame.quit()