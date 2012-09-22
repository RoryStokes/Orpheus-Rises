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
         #   self.event.register("lose",self.player_lose)
        elif self.type == "eurydice":
            self.event.register("move_eurydice",self.move_eurydice)
          #  self.event.register("lose",self.eurydice_lose)

    def move_player(self,dir):
        sight_range = 5
        if dir == "up":

            self.state = 1
            self.event.notify("move_eurydice",self.x, self.y-1)

            if self.world.move(self.type,(self.x,self.y),( self.x, self.y-1)):
                self.y -= 1

            lose = False
            for i in range(max(self.y-sight_range,0),self.y):
                for entity in self.world.get_objects(self.x,i):
                    if entity.type == "eurydice":
                        lose = True
                        break

            if lose:
                self.event.notify("lose")
            
        elif dir == "down":
            self.state = 2
            self.event.notify("move_eurydice",self.x, self.y+1)
            if self.world.move(self.type,(self.x,self.y),( self.x, self.y+1)):
                self.y += 1

            

            lose = False
            for i in range(self.y,min(self.y+sight_range,self.world.height)):
                for entity in self.world.get_objects(self.x,i):
                    if entity.type == "eurydice":
                        lose = True
                        break

            if lose:
                self.event.notify("lose")

        elif dir == "left":
            self.state = 0
            self.event.notify("move_eurydice",self.x-1, self.y)
            if self.world.move(self.type,(self.x,self.y),( self.x-1, self.y)):
                self.x -= 1

            lose = False
            for i in range(max(self.x-sight_range,0),self.x):
                for entity in self.world.get_objects(i,self.y):
                    if entity.type == "eurydice":
                        lose = True
                        break

            if lose:
                self.event.notify("lose")

        elif dir == "right":
            self.state = 3
            self.event.notify("move_eurydice",self.x+1, self.y)
            if self.world.move(self.type,(self.x,self.y),( self.x+1, self.y)):
                self.x += 1

            lose = False
            for i in range(self.x,min(self.x+sight_range,self.world.width)):
                for entity in self.world.get_objects(i,self.y):
                    if entity.type == "eurydice":
                        lose = True
                        break

            if lose:
                self.event.notify("lose")
                
        self.event.notify("focus",self.x,self.y)
            
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
                    
                    if x_dir>0:
                        self.state = 3
                    elif x_dir<0:
                        self.state = 0

                elif self.world.move(self.type,(self.x,self.y),(self.x, self.y+y_dir)):
                    self.y += y_dir
                    
                    if y_dir>0:
                        self.state = 2
                    elif y_dir<0:
                        self.state = 1
                    
            else:
                if self.world.move(self.type,(self.x,self.y),(self.x, self.y+y_dir)):
                    self.y += y_dir
                    
                    if y_dir>0:
                        self.state = 2
                    elif y_dir<0:
                        self.state = 1
                elif self.world.move(self.type,(self.x,self.y),(self.x+x_dir, self.y)):
                    self.x += x_dir
                    
                    if x_dir>0:
                        self.state = 3
                    elif x_dir<0:
                        self.state = 0

    def player_lose():
        self.event.deregister("move_player",self.move_eurydice)

    def eurydice_lose():
        self.event.deregister("move_eurydice",self.move_eurydice)
