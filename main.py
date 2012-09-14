import pygame, sys
from pygame.locals import *

import world
import entity
import render
import event
import settings

# Initialise Pygame
window = pygame.display.set_mode((1024,600),pygame.RESIZABLE)
fpsClock = pygame.time.Clock()

# Set up objects
event_manager = event.Event()
world = world.World(event_manager)
renderer = render.Render(event_manager,world,window)
event_manager.notify("load_map", "maps/test")

# Set up basic running code
running = True
def close():
    global running
    running = False
event_manager.register("quit", close)

time = 0
# Main game loop
while running:
    # Set up frame rate
    fpsClock.tick(60)

    time += fpsClock.get_time()/1000.0
    # Trigger update events
    if(time >= 0.2):
        event_manager.notify("update", time)
        event_manager.notify("draw")
        pygame.display.update()
        time = 0

    # React to pygame events
    eventlist = pygame.event.get()
    for e in eventlist:
        if e.type == QUIT:
            print "quit"
            event_manager.notify("quit")
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                event_manager.notify("quit")
            elif e.key in settings.key_up:
                event_manager.notify("move","up")
            elif e.key in settings.key_down:
                event_manager.notify("move","down")
            elif e.key in settings.key_left:
                event_manager.notify("move","left")
            elif e.key in settings.key_right:
                event_manager.notify("move","right")
    if len(eventlist)>0:
        event_manager.notify("draw")
        pygame.display.update()
                

    event_manager.update()
