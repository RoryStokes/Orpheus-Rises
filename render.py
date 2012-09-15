# RENDER

import world
import pygame
import tile
import settings

class Render():
    
    def __init__(self,event,world,window):
        self.world = world
        self.event = event
        self.window = window
        event.register("draw", self.draw)
        event.register("load_tileset", self.load)
        event.register("focus", self.pan)
        self.camera_x = 0
        self.camera_y = 0
        
    def load(self):
        # Load data from world
        self.data = self.world.map
        self.tileset = pygame.image.load(self.world.tileset)
        self.tile_w = self.world.tile_w
        self.tile_h = self.world.tile_h
        
    def draw(self):
        w = self.world.width
        h = self.world.height

        # Clear screen
        self.window.fill(pygame.Color(0,0,0,255))
        
        # Iterate through each 'row'
        y = 0

        while y<(w+h):

            # Calculate minimum x
            if(y<h):
                x = 0
            else:
                x = y-h+1
            
            # Calculate maximum x
            x_max = min(y+1,h,w-x) + x
            
            # Iterate along the row
            while x<x_max:
                self.draw_cell(x,y)
                x += 1

            y += 1

                    
    def draw_cell(self,x,y):
        (x_pos,y_pos) = self.from_grid(x,y)
        # Read ground type
        type = self.world.get_cell(x,y-x)
        
        # Calculate image locations
        dest = pygame.Rect(x_pos-32, y_pos-16, 64,32)
        mask = pygame.Rect( (type%4)*64, (type/4)*32, 64,32)

        # Blit background image
        self.window.blit( self.tileset, dest, mask )

        # Draw objects
        for i in self.world.get_objects(x,y-x):
            mask = pygame.Rect(i.state*i.w,0,i.w,i.h)
            dest = pygame.Rect(x_pos  - i.anchor_x, y_pos - i.anchor_y, 64,32)
            self.window.blit( i.image, dest, mask )
            
    def pan(self,x,y):
        self.camera_x = x
        self.camera_y = y

    def from_grid(self,x,y):
        new_x = (self.world.height-y)*32 + (x)*64
        new_y = 16*(y + 1)
        return(new_x,new_y)
        
