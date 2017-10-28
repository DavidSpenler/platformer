import pyglet

import global_vars

class ground():

    def __init__(self,x,y,image,level):
        level.append(self)
        self.image = pyglet.resource.image(image)
        self.sprite = pyglet.sprite.Sprite(self.image,batch=global_vars.batch,group=global_vars.foreground)
        self.sprite.image.anchor_x = self.image.width/2
        self.sprite.image.anchor_y = self.sprite.image.height/2
        self.sprite.x = x
        self.sprite.y = y
        self.updatehitbox()
        
    def updatehitbox(self):
        self.hitbox = [
            self.sprite.x-self.sprite.image.width/2,
            self.sprite.y-self.sprite.image.height/2,
            self.sprite.x+self.sprite.image.width/2,
            self.sprite.y+self.sprite.image.height/2
            ]
