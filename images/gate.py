import pyglet

from base_object import base_object

import global_vars

class gate(base_object):
    
    def __init__(self,x,y,image,level):
        base_object.__init__(self,x,y,image,level,"f")  

    def open(self):
        self.level.remove(self)
        self.sprite.batch = None
