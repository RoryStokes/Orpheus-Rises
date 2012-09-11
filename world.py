# WORLD
import json


class World:
    
    def __init__(self,event):
        self.event = event
        self.map = "no map"

    def load(self, name):
        
        f = open(mapname)
        data = json.load(f)

        self.map = data["layers"][0]["data"]
        self.width = data["layers"][0]["width"]
        self.height = data["layers"][0]["height"]
        
    
    def get_cell(self,x,y):
        if self.map == "no map":
            print "ERROR: No map loaded"
        else:
            if x<self.width and y<self.height:
                return self.map[x + self.height*y] - 1
            else:
                print "ERROR: Invalid cell ("+x+","+y+")"
