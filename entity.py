# ENTITY
import pygame
from sprite import Sprite

def can_cross(type,source,target):
    return abs(source - target) < 1

class Entity:
    
    def __init__(self,event,world,sprite,(x_loc,y_loc)):
        self.image =  sprite.image
        self.type = sprite.name
        self.anchor_x = sprite.anchor_x
        self.anchor_y = sprite.anchor_y
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
            
