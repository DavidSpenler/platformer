import pyglet

import global_vars

class base_object():

    def __init__(self,x,y,image,level,group):
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
        self.updatehitbox()

    def updatehitbox(self):
        self.hitbox = [
            self.sprite.x-self.sprite.width/2+2,
            self.sprite.y-self.sprite.height/2,
            self.sprite.x+self.sprite.width/2-2,
            self.sprite.y+self.sprite.height/2
            ]
