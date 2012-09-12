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
        self.objects = []
        self.width = data["layers"][0]["width"]
        self.height = data["layers"][0]["height"]
        
        i = 0
        while i < height:
            self.map.append([])
            data["layers"][0]["data"]:
            self.map.append(i-1)
            self.objects.append( settings.tiles[i-1].spawn )
            if(

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

    def move_player:
