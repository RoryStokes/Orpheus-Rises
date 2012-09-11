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
        
    def update(self,dt):

        self.window.fill(pygame.Color(0,0,0,255))
        w = self.world.width
        h = self.world.height
        data = self.world.map
           
        y = 0

        while y<(w+h):
                        
            if(y<h):
                x = 0
            else:
                x = y-h+1

            x_max = min(y+1,h,w-x) + x
            
            while x<x_max:
                self.draw_cell(x,y,self.world.get_cell(y-x,x))
                x += 1
            y+=1

            
    def draw_cell(self,x,y,type):
        type_id = type-1
        dest = pygame.Rect((self.world.height-y-1)*32 + x*64, 16*y, 64,32)
        mask = pygame.Rect( (type_id%4)*64, (type_id/4)*32, 64,32)
        self.window.blit( tileset, dest, mask )
