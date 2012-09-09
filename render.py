# RENDER
import world
import pygame
tileset = pygame.image.load('img/tile_colours.png')

class Render():
    
    def __init__(self,event,world,window):
        self.world = world
        self.event = event
        self.window = window
        window.fill(pygame.Color(0,0,0,255))
        w = world.width
        h = world.height
        data = world.map
        
        if(w>h):
            max = w
            min = h
        else:
            max = h
            min = w
        diff = w-h
            
        i = 0
        
        while i<min:
            j=0
            while j<=i:
                self.draw_cell(j,i,world.get_cell(j,i-j)),
                j += 1
            print
            i += 1
        i = 1
        while i<min:
            j=0
            while j<=min-i-1:
                self.draw_cell(j+i,min+i-1,world.get_cell(i+j,min-1-j))
                j += 1
            print
            i += 1

        
    #pygame.display.update()

            
    def draw_cell(self,x,y,type):
        type_id = type-1
        dest = pygame.Rect((self.world.height-y-1)*32 + x*64, 16*y, 64,32)
        mask = pygame.Rect( (type_id%4)*64, (type_id/4)*32, 64,32)
        self.window.blit( tileset, dest, mask )
        print str(x)+','+str(y)+': '+str(type)
