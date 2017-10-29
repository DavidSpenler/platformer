import pyglet

from collisions import collision

from base_object import base_object

import global_vars

class enemy(base_object):

    def __init__(self,x,y,image,level):
        base_object.__init__(self,x,y,image,level,"f",0,-2)	
        self.Objects = level
        self.speedx = 0
        self.speedy = 0
        self.terminalv = -30
        self.buffery = 0
        self.accely = 2
        self.speed = 4
        self.bufferw = 2
        self.walkc = 1
        self.dir = -1
        self.landed = False
        self.walkc = 1
        self.bufferw = 1
        self.dead = False
        self.bufferd = 1
        #self.update_hitbox()

    def fall(self):
        if self.speedy > self.terminalv:
            if self.buffery == self.accely:
                self.speedy-=2
                self.buffery = 1
            else:
                self.buffery+=1
        self.update_hitbox()

        for object in self.Objects:
            cl,cr,cu,cd = collision(self,object,0,self.speedy)
            if cd and object != self:
                self.speedy = 0
                self.sprite.y = object.hitbox[3]+self.sprite.image.height/2
                self.update_hitbox()

    def walk(self):
        self.speedx = self.dir
        for object in self.Objects:
            cl,cr,cu,cd = collision(self,object,self.speedx,0)
            if cl and object != self or cr and object != self:
                self.dir*=(-1)
                self.speedx = self.dir
                if type(object).__name__=='enemy':
                    object.dir*=-1
            c1,c2,c3,cdp = collision(self,object,self.speedx,-1)
            cl2,cr2,cu2,cd2 = collision(self,object,(self.sprite.image.width*self.dir)+self.speedx,-1)
            if not cd2 and cdp and object != self and type(object).__name__=='ground':
                self.dir*=(-1)
                self.speedx = self.dir
        if self.dead == True:
            self.speedx = 0
        self.update_hitbox()

    def animate(self):
        if self.bufferw == 10:
            self.bufferw = 1
            if self.walkc == 1:
                self.walkc = 2
            else:
                self.walkc = 1
        else:
            self.bufferw+=1
        if self.dead == False:
            self.sprite.image = pyglet.resource.image('enemy'+str(self.walkc)+'.png')
            self.sprite.image.anchor_x = self.image.width/2
            self.sprite.image.anchor_y = self.image.height/2

    def die(self):
        self.image = pyglet.resource.image('enemy3.png')
        self.sprite.image = self.image
        self.update_dimensions(self.image.height,self.image.width)
        self.sprite.image.anchor_x = self.sprite.image.width/2
        self.sprite.image.anchor_y = self.sprite.image.height/2
        self.update_hitbox()
        self.dead = True
        if self.bufferd == 30:
            self.Objects.remove(self)
            self.sprite.batch = None
        else:
            self.bufferd+=1
            
    def move(self):
        self.update_hitbox()
        if self.dead:
            self.die()
        self.fall()
        self.walk()
        self.animate()
        self.sprite.x+=self.speedx
        self.sprite.y+=self.speedy
        self.update_hitbox()
