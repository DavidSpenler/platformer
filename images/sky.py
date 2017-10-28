import pyglet

import global_vars

class sky():

    def __init__(self,image,width,height):
        self.image = pyglet.resource.image(image)
        self.sprite = pyglet.sprite.Sprite(self.image,batch=global_vars.batch,group=global_vars.background)
        self.sprite.image.height=height
        self.sprite.image.width=width
        self.sprite.image.anchor_x = self.image.width/2
        self.sprite.image.anchor_y = self.sprite.image.height/2
        self.sprite.x = width/2
        self.sprite.y = height/2
