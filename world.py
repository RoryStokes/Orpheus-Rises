# WORLD
import json
import settings
import tile
import entity

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
                self.objects[y].append([])
                if i < len(settings.tiles):
                    spawn_id = settings.tiles[i-1].spawn
                    if spawn_id >= 0 and spawn_id < len(settings.entities):
                        self.objects[y][x].append( entity.Entity( self.event, self, (x,y), settings.entities[spawn_id], (32,54) ) )
                        
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
    
    def get_objects(self,x,y):
        return self.objects[y][x]

    def move(self,type,(x_i,y_i),(x_f,y_f)):
        if 0 <= x_f < self.width and 0 <= y_f < self.height:
            source = settings.tiles[self.map[y_i][x_i]].walkable
            target = settings.tiles[self.map[y_f][x_f]].walkable
            if entity.can_cross(type,source,target):
            
                new_objects = []
                for i in self.objects[y_i][x_i]:
                    if i.type != type:
                        new_objects.append(i)
                    else:
                        self.objects[y_f][x_f].append(i)
                        
                        self.objects[y_i][x_i] = new_objects

                self.event.notify("focus",x_f,y_f)
                return True 

        return False
