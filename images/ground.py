import pyglet

from base_object import base_object

import global_vars

class ground(base_object):

    def __init__(self,x,y,image,level):
        base_object.__init__(self,x,y,image,level,"f")

        '''
        level.append(self)
        self.image = pyglet.resource.image(image)
        self.sprite = pyglet.sprite.Sprite(self.image,batch=global_vars.batch,group=global_vars.foreground)
        self.sprite.image.anchor_x = self.image.width/2
        self.sprite.image.anchor_y = self.sprite.image.height/2
        self.sprite.x = x
        self.sprite.y = y
        self.update_hitbox()
        

    def update_hitbox(self):
        self.hitbox = [
            self.sprite.x-self.sprite.image.width/2,
            self.sprite.y-self.sprite.image.height/2,
            self.sprite.x+self.sprite.image.width/2,
            self.sprite.y+self.sprite.image.height/2
            ]
        '''
