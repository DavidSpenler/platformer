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
        self.update_hitbox()
        '''
        for object in self.level:
            if object != self and 'move' in dir(object):
                cl,cr,cu,cd = collision(self,object,0,0)
                if cl:
                    if object.__class__.__name__ == 'player':
                        object.movex += self.hitbox[0]-(object.sprite.x+6)
                        object.scroll()
                    else:
                        object.sprite.x = self.hitbox[0]-6
                elif cr:
                    if object.__class__.__name__ == 'player':
                        object.movex += self.hitbox[2]-(object.sprite.x-6)
                        object.scroll()
                    else:
                        object.sprite.x = self.hitbox[2]+6
        '''
