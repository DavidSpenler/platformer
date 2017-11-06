import pyglet

from collisions import collision
from collisions import clipped

from base_object import base_object

import global_vars

class player(base_object):

    def __init__(self,x,y,image,level):

        base_object.__init__(self,x,y,image,level,"f")

        self.images = {}
        self.images["r1"] = pyglet.resource.image('playerr1.png')
        self.images["r2"] = pyglet.resource.image('playerr2.png')
        self.images["l1"] = pyglet.resource.image('playerl1.png')
        self.images["l2"] = pyglet.resource.image('playerl2.png')
        self.images["lt1"] = pyglet.resource.image('playerlt1.png')
        self.images["lt2"] = pyglet.resource.image('playerlt2.png')
        self.images["lt3"] = pyglet.resource.image('playerlt3.png')
        self.images["lt4"] = pyglet.resource.image('playerlt4.png')
        self.images["lt5"] = pyglet.resource.image('playerlt5.png')
        self.images["rt1"] = pyglet.resource.image('playerrt1.png')
        self.images["rt2"] = pyglet.resource.image('playerrt2.png')
        self.images["rt3"] = pyglet.resource.image('playerrt3.png')
        self.images["rt4"] = pyglet.resource.image('playerrt4.png')
        self.images["rt5"] = pyglet.resource.image('playerrt5.png')

        self.mousex = 0
        self.mousey = 0

        self.left = False
        self.right = False
        self.up = False
        self.space = False
        self.jump = False

        self.dir = 'r'
       
        self.speedx = 0
        self.maxspeedx = 5
        self.carryx = 0
        self.movex = 0
        
        #Possibly unnecessary
        self.bufferx = 1
        
        self.plat = None
        
        self.speedy = 0
        self.maxspeedy = 15
        self.movey = 0
        self.accel_time = 10

        #Possibly unnecessary
        self.buffery = 1

        self.accely = 1
        self.terminalv = -30
        
        self.walkc = 0
        self.bufferw = 3
        self.walkp = 3
        
        self.tele = 0
        self.buffert = 1
        
        #Possibly unnecessary
        self.imagen = ('player'+self.dir+'1.png')
        
        self.level = level

        self.stats = {
            'can-kill-enemies':True,
            'weight':2
        }
        self.weight = 2
        self.pusher = None
    '''
    def update_hitbox(self):
        
        self.hitbox = [
            self.sprite.x-self.width/2,
            self.sprite.y-self.sprite.image.height/2,
            self.sprite.x+self.width/2,
            self.sprite.y+self.sprite.image.height/2
            ]
    '''
    def run(self):
        self.carryx = 0
        if self.left == True and self.speedx != -self.maxspeedx:
            self.speedx-=1
        if self.right == True and self.speedx != self.maxspeedx:
            self.speedx+=1
        if self.right == False and self.left == False and self.speedx != 0:
            if self.speedx > 0:
                self.speedx-=1
            else:
                self.speedx+=1
        if self.plat != None:
            self.carryx = self.plat.speedx
        self.plat = None
        for object in [object for object in self.level if object != self]:
            cl,cr,cu,cd = collision(self,object,self.speedx+self.carryx+self.movex,0)
            if cl or cr:
                self.carryx = 0
                if type(object).__name__=='enemy' and not object.dead:
                    self.sprite.x+=self.speedx
                    object.sprite.x+=self.speedx
                    batch.draw()
                    self.die()
                if cl and object.get_pusher_weight() > self.get_pusher_weight():
                    #print("left collision")
                    if self.speedx < 0:
                        self.speedx = 0
                    self.movex += (object.hitbox[2]+6)-self.sprite.x
                elif cr and object.get_pusher_weight() > self.get_pusher_weight():
                    if self.speedx > 0:
                        self.speedx = 0
                    self.movex += (object.hitbox[0]-6)-self.sprite.x
                self.update_hitbox()
        for object in [object for object in self.level if object != self]:
            cl,cr,cu,cd = collision(self,object,self.speedx+self.carryx+self.movex,0)
            if (cl or cr) and object.get_pusher_weight() > self.weight:
                self.die()
        self.update_hitbox()
            
    def jumping(self):
        if self.up == True and not self.jump and self.speedy == 0 :
            self.jump = True
            self.speedy = self.maxspeedy
            self.buffery = 1
        if self.speedy > self.terminalv:
            if self.buffery == self.accely:
                self.speedy-=0.9
                self.buffery = 1
                if not self.up and self.jump and self.speedy > 0:
                    self.speedy-=2
            else:
                self.buffery+=1
        self.update_hitbox()
        for object in [object for object in self.level if object != self]:
            cl,cr,cu,cd = collision(self,object,self.movex+self.carryx,self.speedy+self.movey)
            ccd,ccu = False,False#clipped(self,object,self.movex+self.carryx,self.speedy+self.movey)
            if cd or cu:
                self.speedy = 0
                if cd or ccd:
                    if type(object).__name__ == 'button':
                        object.press()
                    elif type(object).__name__ == 'enemy' and not object.dead:
                        object.die()
                        self.jump = True
                        if self.up:
                            self.speedy+=15
                        else:
                            self.speedy+=5
                    elif type(object).__name__=='platform':
                        self.plat = object
                    self.movey+=(object.hitbox[3]+self.sprite.image.height/2)-(self.sprite.y+self.movey)
                    #self.sprite.y = object.hitbox[3]+self.sprite.image.height/2
                    self.jump = False
                elif cu or ccu:
                    self.movey+=(object.hitbox[1]-self.sprite.image.height/2)-self.sprite.y
                    #self.sprite.y = object.hitbox[1]-self.sprite.image.height/2
                    self.speedy = 0
                self.update_hitbox()
                    
    def teleport(self):
        if self.space == True and self.tele == 0:
            self.tele = 1
        elif self.tele != 0 and self.buffert == 2:
            self.tele+=1
            self.buffert = 1
            if self.tele > 5:
                self.tele = 0
            elif self.tele == 3:
                self.movex += self.mousex-self.sprite.x
                self.movey += self.mousey-self.sprite.y
        elif self.tele != 0:
            self.buffert+=1
            
    def animate(self):
        if (self.jump or self.speedy != 0) and self.tele == 0:
            #self.image = pyglet.resource.image('player'+self.dir+'2.png')
            self.image = self.images[self.dir+'2'] 
        elif self.left == True or self.right == True and self.tele == 0:  
            if self.bufferw == 3:
                if self.walkc == 0:
                    #self.image = pyglet.resource.image('player'+self.dir+'2.png')
                    self.image = self.images[self.dir+'2']
                    self.walkc = 1
                else:
                    #self.image = pyglet.resource.image('player'+self.dir+'1.png')
                    self.image = self.images[self.dir+'1']
                    self.walkc = 0
                self.bufferw = 1
            else:
                self.bufferw+=1
        elif self.tele != 0:
               #self.image = pyglet.resource.image('player'+self.dir+'t'+str(self.tele)+'.png') 
               self.image = self.images[self.dir+'t'+str(self.tele)]
        else:
            #self.image = pyglet.resource.image('player'+self.dir+'1.png')
            self.image = self.images[self.dir+'1']
            self.bufferw = 3
        if self.left and not self.right and not self.jump:
            self.dir = 'l'
        elif self.right and not self.left and not self.jump:
            self.dir = 'r'
        self.sprite.image = self.image
        self.sprite.image.anchor_x = self.sprite.image.width/2
        self.sprite.image.anchor_y = self.sprite.image.height/2

    def die(self):
        print('dead')
        sys.exit()
        
    def move(self):
        self.teleport()
        self.animate()
        self.run()
        self.jumping()
        #self.sprite.x+=(self.speedx+self.carryx)
        #self.sprite.y+=self.speedy
        '''
        for object in self.level:
            if (object != self):
                object.sprite.x-=(self.speedx+self.carryx+self.movex)
                object.sprite.y-=(self.speedy+self.movey)
                object.update_hitbox()
        self.movex = 0
        self.movey = 0
        '''
        self.scroll()
        self.update_hitbox()

    def scroll(self):
        for object in self.level:
            if (object != self):
                object.sprite.x-=(self.speedx+self.carryx+self.movex)
                object.sprite.y-=(self.speedy+self.movey)
                object.update_hitbox()
        self.movex = 0
        self.movey = 0

    def get_pusher_weight(self):
        if self.pusher == None:
            return self.weight
        else:
            return self.pusher.get_pusher_weight()
