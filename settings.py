# SETTINGS
from pygame.locals import *
from tile import Tile
from entity import Entity

# Key bindings
key_up = [K_UP,K_w]
key_down = [K_DOWN,K_s]
key_left = [K_LEFT,K_a]
key_right = [K_RIGHT,K_d]


# Entities
entities = []
 # 0: player
entities.append(Entity('img/character.png'))


# Tiles
tiles = []
 # 0: spawn
tiles.append( Tile( 1, 0,-1) )
 # 1: low ground
tiles.append( Tile( 1,-1,-1) )
 # 2: high ground
tiles.append( Tile( 2,-1,-1) )
 # 3: void
tiles.append( Tile( 0,-1,-1) )
 # 4: snakes a
tiles.append( Tile(-1,-1, 8) )
 # 5: lava a
tiles.append( Tile( 0,-1, 6) )
 # 6: lava b
tiles.append( Tile( 0,-1, 7) )
 # 7: lava c
tiles.append( Tile( 0,-1, 5) )
 # 8: snakes b
tiles.append( Tile(-1,-1, 4) )
 
