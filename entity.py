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
        self.w = sprite.w
        self.h = sprite.h
        self.world = world
        self.event = event
        self.state = 0
        if self.type == "player":
            self.event.register("move_player",self.move_player)
            self.event.notify("focus",self.x,self.y)
        elif self.type == "eurydice":
            self.event.register("move_eurydice",self.move_eurydice)

    def move_player(self,dir):
        if dir == "up":
            self.state = 1
            self.event.notify("move_eurydice",self.x, self.y-1)
            if self.world.move(self.type,(self.x,self.y),( self.x, self.y-1)):
                self.y -= 1
        elif dir == "down":
            self.state = 2
            self.event.notify("move_eurydice",self.x, self.y+1)
            if self.world.move(self.type,(self.x,self.y),( self.x, self.y+1)):
                self.y += 1
        elif dir == "left":
            self.state = 0
            self.event.notify("move_eurydice",self.x-1, self.y)
            if self.world.move(self.type,(self.x,self.y),( self.x-1, self.y)):
                self.x -= 1
        elif dir == "right":
            self.state = 3
            self.event.notify("move_eurydice",self.x+1, self.y)
            if self.world.move(self.type,(self.x,self.y),( self.x+1, self.y)):
                self.x += 1
            
    def move_eurydice(self,x,y):
        x_dist = self.x-x
        y_dist = self.y-y
        x_dir = 0
        y_dir = 0

        dist = x_dist*x_dist + y_dist*y_dist
        
        if(dist > 8):

            if x_dist>0: x_dir = -1
            elif x_dist<0: x_dir = 1
            
            if y_dist>0: y_dir = -1
            elif y_dist<0: y_dir = 1
            
            
            if(abs(x_dist)>abs(y_dist)):
                
                if self.world.move(self.type,(self.x,self.y),(self.x+x_dir, self.y)):
                    self.x += x_dir
                elif self.world.move(self.type,(self.x,self.y),(self.x, self.y+y_dir)):
                    self.y += y_dir
                    
            else:
                if self.world.move(self.type,(self.x,self.y),(self.x, self.y+y_dir)):
                    self.y += y_dir
                elif self.world.move(self.type,(self.x,self.y),(self.x+x_dir, self.y)):
                    self.x += x_dir
