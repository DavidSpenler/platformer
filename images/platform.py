import pyglet

from base_object import base_object

from collisions import collision

import global_vars

class platform(base_object):

    def __init__(self,x,y,image,dist,maxdist,level):
        base_object.__init__(self,x,y,image,level,"f")
        self.dist = dist
        self.maxdist = maxdist
        self.speedx = 2
        
    def move(self):
        if self.dist >= self.maxdist or self.dist <= 0:
            self.speedx*=-1
        self.sprite.x+=self.speedx
        self.dist+=self.speedx
        self.updatehitbox()
        for object in self.level:
            if object != self and 'move' in dir(object):
                cl,cr,cu,cd = collision(self,object,0,0)
                if cl:
                    object.sprite.x = self.hitbox[0]-6
                elif cr:
                    object.sprite.x = self.hitbox[2]+6

