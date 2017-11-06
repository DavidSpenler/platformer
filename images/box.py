import pyglet

from base_object import base_object

from base_moving_object import base_moving_object

from collisions import collision

import global_vars

class box(base_object,base_moving_object):
	
    def __init__(self,x,y,image,level):
        base_object.__init__(self,x,y,image,level,"f")
        base_moving_object.__init__(self)
	    
        self.movex = 0
        self.carryx = 0

        self.movey = 0
        self.speedy = 0
        self.terminalv = -30
        self.accely = -1       	

        self.plat = None

        self.stats = {
            'can-kill-enemies':True,
            'weight':1
        }
        self.weight = self.stats['weight']

    def move(self):
        self.move_in_x()
        self.move_in_y()
        self.sprite.y+=self.speedy
        self.sprite.x+=self.carryx
        self.update_hitbox()
