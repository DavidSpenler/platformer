import pyglet

from base_object import base_object

import global_vars

class button(base_object):

    def __init__(self,x,y,image,gate,level):
        base_object.__init__(self,x,y,image,level,"f")
        self.col = image[7]
        self.pressed = False
        self.gate = gate

    def press(self):
        if self.pressed == False:
            self.pressed = True
            self.gate.open()
            self.x = self.sprite.x
            self.y = self.sprite.y
            self.sprite.image = pyglet.resource.image('button2'+self.col+'.png')
            self.sprite.image.anchor_x = self.image.width/2
            self.sprite.image.anchor_y = self.sprite.image.height/2
            self.sprite.x = self.x
            self.sprite.y = self.y-2
            self.updatehitbox()
