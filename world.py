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
        
        y = 0
        while y < self.height:
            self.map.append([])
            self.objects.append([])
            x = 0
            while x < self.width:
                i = data["layers"][0]["data"][x + y*self.width]
                self.map[y].append(i-1)
                if i < len(settings.tiles):
                    print settings.tiles[i-1].spawn
                else:
                    print "ERROR "+str(i)
                x += 1
            y += 1

    def update(self,dt):
        y = 0
        while y < self.height:
            x = 0
            while x < self.width:
                cell = self.map[y][x]
                if cell < len(settings.tiles):
                    decay = settings.tiles[cell].decay
                    if decay != -1:
                        self.map[y][x] = decay
                x += 1
            y += 1
       
    def get_cell(self,x,y):
        if self.map == "no map":
            print "ERROR: No map loaded"
        else:
            if x<self.width and y<self.height:
                return self.map[y][x]
            else:
                print "ERROR: Invalid cell ("+x+","+y+")"

 #   def move_player:
