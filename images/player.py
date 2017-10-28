import pyglet

from collisions import collision

from base_object import base_object

import global_vars

class player(base_object):

    def __init__(self,x,y,image,level):
        base_object.__init__(self,x,y,image,level,"f")
        self.mousex = 0
        self.mousey = 0
        self.left = False
        self.right = False
        self.up = False
        self.space = False
        self.jump = False
        self.dir = 'r'
        self.speedx = 0
        self.maxspeedx = 5
        self.bufferx = 1
        self.carryx = 0
        self.plat = None
        self.speedy = 0
        self.maxspeedy = 15
        self.buffery = 1
        self.accely = 1
        self.terminalv = -30
        self.walkc = 0
        self.bufferw = 3
        self.walkp = 3
        self.tele = 0
        self.buffert = 1
        self.imagen = ('player'+self.dir+'1.png')
        self.Objects = level

    def updatehitbox(self):
        
        self.hitbox = [
            self.sprite.x-12/2,
            self.sprite.y-self.sprite.image.height/2,
            self.sprite.x+12/2,
            self.sprite.y+self.sprite.image.height/2
            ]

    def run(self):
        print(self.speedx)
        self.carryx = 0
        #self.updatehitbox()
        if self.left == True and self.speedx != -self.maxspeedx:
            self.speedx-=1
        if self.right == True and self.speedx != self.maxspeedx:
            self.speedx+=1
        if self.right == False and self.left == False and self.speedx != 0:
            if self.speedx > 0:
                self.speedx-=1
            else:
                self.speedx+=1
        if self.plat != None:
            self.carryx = self.plat.speedx
        self.plat = None
        for object in [object for object in self.Objects if object != self]:
            cl,cr,cu,cd = collision(self,object,self.speedx+self.carryx,0)
            if cl or cr:
                #print('I: ',self.speedx,self.carryx)
                self.carryx = 0
                if type(object).__name__=='enemy' and not object.dead:
                    self.sprite.x+=self.speedx
                    object.sprite.x+=self.speedx
                    batch.draw()
                    self.die()
                if cl:
                    if self.speedx < 0:
                        self.speedx = 0
                    self.sprite.x = object.hitbox[2]+6
                    #print('cl: relocated')
                elif cr:
                    if self.speedx > 0:
                        self.speedx = 0
                    self.sprite.x = object.hitbox[0]-6
                    #print('cr: relocated')
                #print('F: ',cl,cr,self.speedx,self.carryx)
                self.updatehitbox()
                cl,cr,cu,cd = collision(self,object,0,0)
                #print('new collision: ',cl,cr,cu,cd)
        self.updatehitbox()
            
    
    def jumping(self):
        if self.up == True and not self.jump and self.speedy == 0:
            self.jump = True
            self.speedy = self.maxspeedy
            self.buffery = 1
        if self.speedy > self.terminalv:
            if self.buffery == self.accely:
                self.speedy-=0.9
                self.buffery = 1
            else:
                self.buffery+=1
        self.updatehitbox()
        for object in [object for object in self.Objects if object != self]:
            cl,cr,cu,cd = collision(self,object,0,self.speedy)
            if cd or cu:
                #print(cl,cr,cu,cd)
                self.speedy = 0
                if cd:
                    if type(object).__name__ == 'button':
                        object.press()
                    elif type(object).__name__ == 'enemy' and not object.dead:
                        object.die()
                        if self.up:
                            self.speedy+=15
                        else:
                            self.speedy+=5
                    elif type(object).__name__=='platform':
                        self.plat = object
                    self.sprite.y = object.hitbox[3]+self.sprite.image.height/2
                    self.jump = False
                elif cu:
                    self.sprite.y = object.hitbox[1]-self.sprite.image.height/2
                    self.speedy = -1
                self.updatehitbox()
                    
    def teleport(self):
        if self.space == True and self.tele == 0:
            self.tele = 1
        elif self.tele != 0 and self.buffert == 2:
            self.tele+=1
            self.buffert = 1
            if self.tele > 5:
                self.tele = 0
            elif self.tele == 3:
                self.sprite.x = self.mousex
                self.sprite.y = self.mousey
        elif self.tele != 0:
            self.buffert+=1
            
    def animate(self):
        if (self.jump or self.speedy != 0) and self.tele == 0:
            self.image = pyglet.resource.image('player'+self.dir+'2.png')
        elif self.left == True or self.right == True and self.tele == 0:  
            if self.bufferw == 3:
                if self.walkc == 0:
                    self.image = pyglet.resource.image('player'+self.dir+'2.png')
                    self.walkc = 1
                else:
                    self.image = pyglet.resource.image('player'+self.dir+'1.png')
                    self.walkc = 0
                self.bufferw = 1
            else:
                self.bufferw+=1
        elif self.tele != 0:
               self.image = pyglet.resource.image('player'+self.dir+'t'+str(self.tele)+'.png') 
        else:
            self.image = pyglet.resource.image('player'+self.dir+'1.png')
            self.bufferw = 3
        if self.left and not self.right and not self.jump:
            self.dir = 'l'
        elif self.right and not self.left and not self.jump:
            self.dir = 'r'
        self.sprite.image = self.image
        self.sprite.image.anchor_x = self.sprite.image.width/2
        self.sprite.image.anchor_y = self.sprite.image.height/2

    def die(self):
        print('dead')
        sys.exit()
        
    def move(self):
        self.teleport()
        self.animate()
        self.run()
        self.jumping()
        self.sprite.x+=self.speedx
        self.sprite.x+=self.carryx
        self.sprite.y+=self.speedy
        self.updatehitbox()
        #print('tick')
