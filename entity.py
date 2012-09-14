# ENTITY
import pygame

def can_cross(type,source,target):
    return source == target

class Entity:
    
    def __init__(self,event,world,(x_loc,y_loc),type,(x_anch,y_anch)):
        print type
        self.image = pygame.image.load('img/'+type+'.png')
        self.type = type
        self.anchor_x = x_anch
        self.anchor_y = y_anch
        self.x = x_loc
        self.y = y_loc
        self.world = world
        self.event = event
        if self.type == "player":
            self.event.register("move",self.move)
            self.event.notify("focus",self.x,self.y)

    def move(self,dir):
        if dir == "up":
            if self.world.move(self.type,(self.x,self.y),( self.x, self.y-1)):
                self.y -= 1
        elif dir == "down":
            if self.world.move(self.type,(self.x,self.y),( self.x, self.y+1)):
                self.y += 1
        elif dir == "left":
            if self.world.move(self.type,(self.x,self.y),( self.x-1, self.y)):
                self.x -= 1
        elif dir == "right":
            if self.world.move(self.type,(self.x,self.y),( self.x+1, self.y)):
                self.x += 1
            
