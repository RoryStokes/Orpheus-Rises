# Sprite
import pygame

class Sprite:
    def __init__(self,name,path,(x,y),(w,h)):
        self.image =  pygame.image.load(path)
        self.name = name
        self.anchor_x = x
        self.anchor_y = y
        self.w = w
        self.h = h
