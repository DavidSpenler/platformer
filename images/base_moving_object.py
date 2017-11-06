from collisions import collision
from collisions import clipped

class base_moving_object():

    def __init__(self):
        self.speedx = 0
        self.carryx = 0
        self.movex = 0

        self.movey = 0
        self.speedy = 0

        self.terminalv = -30
        self.accely = -1       	

        self.plat = None
        self.pusher = None

    def get_pusher_weight(self):
        if self.pusher == None:
            return self.weight
        else:
            return self.pusher.get_pusher_weight()

    def move_in_x(self):
        self.carryx = 0
        self.pusher = None
        if self.plat != None:
            self.carryx = self.plat.speedx
        self.plat = None
        self.update_hitbox()
        for object in [object for object in self.level if object != self]:
            cl,cr,cu,cd = collision(self,object,self.carryx+self.movex,0)
            if cl and object.get_pusher_weight() > self.get_pusher_weight():
                self.carryx = 0 
                self.sprite.x = object.hitbox[2]+self.sprite.image.height/2
                self.pusher = object
            if cr and object.get_pusher_weight() > self.get_pusher_weight():
                self.carryx = 0 
                self.sprite.x = object.hitbox[0]-self.sprite.image.height/2
                self.pusher = object
            self.update_hitbox()
            #print(self.weight)
        for object in self.level:
            if object != self:
                cl,cr,cu,cd = collision(self,object,self.carryx+self.movex,0)
                if cl or cr:
                    if object.get_pusher_weight() < self.get_pusher_weight():
                        #print("calling object's move function")
                        object.move()
                        #print('dead')
                    elif not self in self.level:
                        #self.level.remove(self)
                        #self.sprite.batch = None
                        #print('dead')
                        pass
                self.update_hitbox()
        self.update_hitbox()

    def move_in_y(self):
        if self.speedy > self.terminalv:
            self.speedy-=0.9
            self.update_hitbox()
        done = False
        count = 0
        while (done == False and count < 2):
            count+=1
            done = True
            for object in self.level:
                if object != self:
                    cl,cr,cu,cd = collision(self,object,self.movex+self.carryx,self.speedy+self.movey)
                    cld,clu = False,False#clipped(self,object,self.movex+self.carryx,self.speedy+self.movey)
                    if cd or cld:
                        done = False
                        #print("collision")
                        self.speedy = 0
                        if type(object).__name__ == "button":
                            object.press()
                        elif type(object).__name__ == "enemy":
                            object.die()
                        elif type(object).__name__ == "platform":
                            self.plat = object
                            print("platform")
                        self.sprite.y = object.hitbox[3]+self.sprite.image.height/2
                    if cu or clu:
                        done = False
                        self.sprite.y = object.hitbox[1]-self.sprite.image.height/2
                        self.speedy = 0
                    self.update_hitbox()
             
