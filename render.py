# RENDER

import world
import pygame
import tile
import settings

tileset = pygame.image.load('img/tile_colours.png')
player = pygame.image.load('img/player.png')
dead_tree = pygame.image.load('img/dead_tree.png')

class Render():
    
    def __init__(self,event,world,window):
        self.world = world
        self.event = event
        self.window = window
        event.register("draw", self.draw)
        event.register("focus", self.pan)
        self.camera_x = 0
        self.camera_y = 0
        
    def draw(self):
        
        # Load data from world
        w = self.world.width
        h = self.world.height
        data = self.world.map

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
        self.window.blit( tileset, dest, mask )

        # Draw objects
        for i in self.world.get_objects(x,y-x):
            dest = pygame.Rect(x_pos  - i.anchor_x, y_pos - i.anchor_y, 64,32)
            self.window.blit( i.image, dest )
            
    def pan(self,x,y):
        self.camera_x = x
        self.camera_y = y

    def from_grid(self,x,y):
        new_x = (self.world.height-y)*32 + (x)*64
        new_y = 16*(y + 1)
        return(new_x,new_y)
        
