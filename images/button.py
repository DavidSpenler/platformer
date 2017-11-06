import pyglet

from base_object import base_object

import global_vars

class button(base_object):

    def __init__(self,x,y,image,gate,level):
        base_object.__init__(self,x,y,image,level,"f")
        self.col = image[7]
        self.pressed = False
        self.gate = gate

        self.stats = {
            'can-kill-enemies':False,
            'weight':3
        }	
        self.weight = self.stats['weight']

    def press(self):
        if self.pressed == False:
            #print("pressed")
            self.pressed = True
            self.gate.open()
            self.x = self.sprite.x
            self.y = self.sprite.y
            self.image = pyglet.resource.image('button2'+self.col+'.png')
            self.sprite.image = self.image
            self.sprite.image.anchor_x = self.image.width/2
            self.sprite.image.anchor_y = self.sprite.image.height/2
            self.sprite.x = self.x
            self.sprite.y = self.y-2
            self.update_dimensions(self.image.height,self.image.width)
            self.update_hitbox()

    def update_hitbox(self):
        self.hitbox = [
            self.sprite.x-self.sprite.image.width/2,
            self.sprite.y-self.sprite.image.height/2-10,
            self.sprite.x+self.sprite.image.width/2,
            self.sprite.y+self.sprite.image.height/2
            ]
