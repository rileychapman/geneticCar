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
        self.rect = pygame.Rect(32, 32, 16, 16)
        
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
#        distance = math.sqrt((x-xp)**2 + (y-yp)**2)
#        dx = (x-xp)/distance * 2
#        dy = (y-yp)/distance * 2

#        while distance >= 2:
#            xp += dx
#            yp += dy
#            distance -= 2
        wallx = []
        wally = []
        
        for wall in self.model.level1:
            wallx.append(xp - wall.posx)
            wally.append(yp - wall.posy)
#            if wall.rect.collidepoint(xp,yp):
#                portalclick = pygame.Rect.copy(wall.rect)
#                if event.button == 1:
#                    self.model.portal_update_orange(portalclick)
#                if event.button == 3:
#                    self.model.portal_update_blue(portalclick)
#                return
        print min(wallx)
        print min(wally)


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
#    car = Duck()
#    pygame.draw.rect(screen, (255, 200, 0), car.rect)

    running = True

    while running:
           
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                controller.handle_pygame_event(event)
        
#        model.update()
        view.draw()
        view.distance_calculate()
        time.sleep(0.001)

    pygame.quit()