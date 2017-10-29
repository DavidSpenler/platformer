import pyglet

import global_vars

class base_object():

    def __init__(self,x,y,image,level,group,height_mod=0,width_mod=0):

        level.append(self)
        self.level = level
        self.image = pyglet.resource.image(image)
        self.sprite = pyglet.sprite.Sprite(self.image,batch=global_vars.batch)

        if group == 'f':
            self.sprite.group = global_vars.foreground
        else:
            self.sprite.group = global_vars.background

        self.sprite.image.anchor_x = self.image.width/2
        self.sprite.image.anchor_y = self.sprite.image.height/2
        self.sprite.x = x
        self.sprite.y = y

        self.width_mod = width_mod
        self.height_mod = height_mod

        self.update_dimensions(self.image.height,self.image.width)
        self.update_hitbox()

    def update_hitbox(self):
        self.hitbox = [
            self.sprite.x-self.width/2-self.width_mod,
            self.sprite.y-self.height/2-self.height_mod,
            self.sprite.x+self.width/2+self.width_mod,
            self.sprite.y+self.height/2+self.height_mod
            ]

    def update_dimensions(self,h,w):
        self.height = h
        self.width = w
