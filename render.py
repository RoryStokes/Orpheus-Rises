# RENDER
import world
import pygame
tileset = pygame.image.load('img/tile_colours.png')

class Render():
    
    def __init__(self,event,world,window):
        self.world = world
        self.event = event
        self.window = window
        event.register("update", self.update)
        self.i = 0
        
    def update(self,dt):
        
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
        # Read ground type
        type = self.world.get_cell(y-x,x)
        
        # Calculate image locations
        dest = pygame.Rect((self.world.height-y-1)*32 + x*64, 16*y, 64,32)
        mask = pygame.Rect( (type%4)*64, (type/4)*32, 64,32)

        # Blit background image
        self.window.blit( tileset, dest, mask )
