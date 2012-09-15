# SETTINGS
from pygame.locals import *
from tile import Tile
from sprite import Sprite

# Key bindings
key_up = [K_UP,K_w]
key_down = [K_DOWN,K_s]
key_left = [K_LEFT,K_a]
key_right = [K_RIGHT,K_d]

# Entities
sprites =[]
 # 0: Orpheus
sprites.append( Sprite("player", "img/player.png", (15,42),(29,46) ) )
 # 1: Eurydice
sprites.append( Sprite("eurydice", "img/spirit.png",(32,64),(64,64)) )
 # 2: dead_tree
sprites.append( Sprite("dead_tree", "img/dead_tree.png", (70,86),(96,96)) )

# Tiles
tiles = []
 # 0: spawn
tiles.append( Tile( 1, 0,-1) )
 # 1: low ground
tiles.append( Tile( 1,-1,-1) )
 # 2: high ground
tiles.append( Tile( 1.5,-1,-1) )
 # 3: void
tiles.append( Tile( 0,-1,-1) )
 # 4: lava a
tiles.append( Tile(-1,-1, 5) )
 # 5: lava b
tiles.append( Tile( 0,-1, 6) )
 # 6: lava c
tiles.append( Tile( 0,-1, 7) )
 # 7: lava d
tiles.append( Tile( 0,-1, 4) )
 # 8: snakes a
tiles.append( Tile( 1, 1, 9) )
 # 9: snakes b
tiles.append( Tile( 1, 1, 8) )
 # 10: blue
tiles.append( Tile( 1,-1,-1) )
 # 11: pink
tiles.append( Tile( 1,-1,-1) )
 # 12: water_right a
tiles.append( Tile( 0,-1, 13) )
 # 13: water_right b
tiles.append( Tile( 0,-1, 14) )
 # 14: water_right c
tiles.append( Tile( 0,-1, 15) )
 # 15: water_right d
tiles.append( Tile( 0,-1, 12) )
 # 16: water_down a
tiles.append( Tile( 0,-1, 17) )
 # 17: water_down b
tiles.append( Tile( 0,-1, 18) )
 # 18: water_down c
tiles.append( Tile( 0,-1, 19) )
 # 19: water_down d
tiles.append( Tile( 0,-1, 16) )
 # 20: water_foam a
tiles.append( Tile( 1,-1, 21) )
 # 21: water_foam b
tiles.append( Tile( 1,-1, 20) )
 # 22: cliff_corner_down
tiles.append( Tile( 2,-1, -1) )
 # 23: a cliff end
tiles.append( Tile( 2,-1, -1) )
 # 24: another cliff end
tiles.append( Tile( 2,-1, -1) )
 # 25: another cliff end
tiles.append( Tile( 2,-1, -1) )
 # 26: another cliff end
tiles.append( Tile( 2,-1, -1) )
 # 27: another cliff end
tiles.append( Tile( 2,-1, -1) )
 # 28: another cliff end
tiles.append( Tile( 2,-1, -1) )
 # 29: another cliff end
tiles.append( Tile( 2,-1, -1) )
 # 30: last cliff end
tiles.append( Tile( 2,-1, -1) )
 # 31: cliff_corner_up
tiles.append( Tile( 2,-1, -1) )
 # 32: cliff_corner_right
tiles.append( Tile( 2,-1, -1) )
 # 33: cliff_corner_left
tiles.append( Tile( 2,-1, -1) )
 # 34: cliff_down
tiles.append( Tile( 2,-1, -1) )
 # 35: cliff_left
tiles.append( Tile( 2,-1, -1) )
 # 36: cliff_up
tiles.append( Tile( 2,-1, -1) )
 # 37: cliff_right
tiles.append( Tile( 2,-1, -1) )
