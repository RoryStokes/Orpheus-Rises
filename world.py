# WORLD
import json
import settings
import tile

class World:
    
    def __init__(self,event):
        self.event = event
        self.map = "no map"
        self.width = 0
        self.height = 0
        event.register("load_map",self.load)
        event.register("update",self.update)

    def load(self, name):
        
        f = open(name)
        data = json.load(f)

        self.map = []
        for i in data["layers"][0]["data"]:
            self.map.append(i-1)
        self.width = data["layers"][0]["width"]
        self.height = data["layers"][0]["height"]

    def update(self,dt):
        for i in range(0,len(self.map)-1):
            cell = self.map[i]
            if cell < len(settings.tiles):
                decay = settings.tiles[cell].decay
                if decay != -1:
                    self.map[i] = decay
       
    def get_cell(self,x,y):
        if self.map == "no map":
            print "ERROR: No map loaded"
        else:
            if x<self.width and y<self.height:
                return self.map[x + self.height*y]
            else:
                print "ERROR: Invalid cell ("+x+","+y+")"
