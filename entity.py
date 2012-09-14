# ENTITY
import pygame

class Entity:
    
    def __init__(self,image,(x,y)):
        self.image = pygame.image.load('img/character.png')
        self.anchor_x = x
        self.anchor_y = y
