import pygame, sys
from pygame.locals import *

import world
import entity
import render
import event


window = pygame.display.set_mode((1024,600),pygame.RESIZABLE)
fpsClock = pygame.time.Clock()
event_manager = event.Event()
world = world.World(event_manager,"maps/test")
renderer = render.Render(event_manager,world,window)
pygame.display.update();
running = True
def close():
    global running
    running = False
event_manager.register("quit", close)

while running:
    fpsClock.tick(30)
    event_manager.notify("update", fpsClock.get_time()/1000.0)
    event_manager.update()

    eventlist = pygame.event.get()
    for e in eventlist:
        if e.type == QUIT:
            print "quit"
            event_manager.notify("quit")
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                event_manager.notify("quit")
                
