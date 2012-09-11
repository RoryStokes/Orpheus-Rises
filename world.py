# WORLD
import json


class World:
    
    def __init__(self,event,mapname):
        
        f = open(mapname)
        data = json.load(f)

        self.map = data["layers"][0]["data"]
        self.width = data["layers"][0]["width"]
        self.height = data["layers"][0]["height"]

    def get_cell(self,x,y):
        if x<self.width and y<self.height:
            return self.map[x + self.height*y] - 1
        else:
            print "ERROR: Invalid cell ("+x+","+y+")"
