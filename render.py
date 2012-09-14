# RENDER

import world
import pygame
import tile
import settings

tileset = pygame.image.load('img/tile_colours.png')
player = pygame.image.load('img/player.png')

class Render():
    
    def __init__(self,event,world,window):
        self.world = world
        self.event = event
        self.window = window
        event.register("draw", self.draw)
        self.i = 0
        self.px = 0
        self.py = 0
        
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
        #self.window.blit( player, (self.px,self.py) )
            
    def draw_cell(self,x,y):
        # Read ground type
        type = self.world.get_cell(x,y-x)
        
        # Calculate image locations
        dest = pygame.Rect((self.world.height-y-1)*32 + x*64, 16*y, 64,32)
        mask = pygame.Rect( (type%4)*64, (type/4)*32, 64,32)

        # Blit background image
        self.window.blit( tileset, dest, mask )

        # Draw objects
        for i in self.world.get_objects(x,y-x):
            dest = pygame.Rect( (self.world.height-y)*32 + x*64 - i.anchor_x, 16*(y+1) - i.anchor_y, 64,32)
            self.window.blit( i.image, dest )
            
