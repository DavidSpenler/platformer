import pyglet
from pyglet.window import key
from pyglet.window import mouse
import sys

window = pyglet.window.Window(800,500,caption='Game')

batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
       
def collision(sprite1,sprite2,xmod,ymod):
    cl,cr,cu,cd = False,False,False,False
    if sprite1.hitbox[0]+xmod < sprite2.hitbox[2] and sprite1.hitbox[2]+xmod > sprite2.hitbox[2] and sprite1.hitbox[1]+ymod < sprite2.hitbox[3] and sprite1.hitbox[3]+ymod > sprite2.hitbox[1]:
        cl = True
    if sprite1.hitbox[2]+xmod > sprite2.hitbox[0] and sprite1.hitbox[0]+xmod < sprite2.hitbox[0] and sprite1.hitbox[1]+ymod < sprite2.hitbox[3] and sprite1.hitbox[3]+ymod > sprite2.hitbox[1]:
        cr = True
    if sprite1.hitbox[1]+ymod < sprite2.hitbox[3] and sprite1.hitbox[3]+ymod > sprite2.hitbox[3] and sprite1.hitbox[0]+xmod < sprite2.hitbox[2] and sprite1.hitbox[2]+xmod > sprite2.hitbox[0]:
        cd = True
    if sprite1.hitbox[3]+ymod > sprite2.hitbox[1] and sprite1.hitbox[1]+ymod < sprite2.hitbox[1] and sprite1.hitbox[0]+xmod < sprite2.hitbox[2] and sprite1.hitbox[2]+xmod > sprite2.hitbox[0]:
        cu = True
    return cl,cr,cu,cd


class ground():

    def __init__(self,x,y,image,level):
        level.append(self)
        self.image = pyglet.resource.image(image)
        self.sprite = pyglet.sprite.Sprite(self.image,batch=batch,group=foreground)
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


class platform():

    def __init__(self,x,y,image,dist,maxdist,level):
        level.append(self)
        self.image = pyglet.resource.image(image)
        self.sprite = pyglet.sprite.Sprite(self.image,batch=batch,group=foreground)
        self.sprite.image.anchor_x = self.image.width/2
        self.sprite.image.anchor_y = self.sprite.image.height/2
        self.sprite.x = x
        self.sprite.y = y
        self.dist = dist
        self.maxdist = maxdist
        self.speedx = 2
        self.updatehitbox()
        
    def updatehitbox(self):
        self.hitbox = [
            self.sprite.x-self.sprite.image.width/2,
            self.sprite.y-self.sprite.image.height/2,
            self.sprite.x+self.sprite.image.width/2,
            self.sprite.y+self.sprite.image.height/2
            ]
        
    def move(self):
        if self.dist >= self.maxdist or self.dist <= 0:
            self.speedx*=-1
        self.sprite.x+=self.speedx
        self.dist+=self.speedx
        self.updatehitbox()


class button():

    def __init__(self,x,y,image,gate,level):
        level.append(self)
        self.pressed = False
        self.gate = gate
        self.image = pyglet.resource.image(image)
        self.col = image[7]
        self.sprite = pyglet.sprite.Sprite(self.image,batch=batch,group=foreground)
        self.sprite.image.anchor_x = self.image.width/2
        self.sprite.image.anchor_y = self.sprite.image.height/2
        self.sprite.x = x
        self.sprite.y = y
        self.updatehitbox()

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

    def updatehitbox(self):   
        self.hitbox = [
            self.sprite.x-self.sprite.image.width/2,
            self.sprite.y-self.sprite.image.height/2-10,
            self.sprite.x+self.sprite.image.width/2,
            self.sprite.y+self.sprite.image.height/2
            ]


class gate():

    def __init__(self,x,y,image,level):
        level.append(self)
        self.level = level
        self.image = pyglet.resource.image(image)
        self.sprite = pyglet.sprite.Sprite(self.image,batch=batch,group=foreground)
        self.sprite.image.anchor_x = self.image.width/2
        self.sprite.image.anchor_y = self.sprite.image.height/2
        self.sprite.x = x
        self.sprite.y = y
        self.updatehitbox()
        
    def updatehitbox(self):   
        self.hitbox = [
            self.sprite.x-self.sprite.image.width/2,
            self.sprite.y-self.sprite.image.height/2-10,
            self.sprite.x+self.sprite.image.width/2,
            self.sprite.y+self.sprite.image.height/2+2
            ]

    def open(self):
        self.level.remove(self)
        self.sprite.batch = None
        

class enemy():

    def __init__(self,x,y,image,level):
        level.append(self)
        self.image = pyglet.resource.image(image)
        self.sprite = pyglet.sprite.Sprite(self.image,batch=batch,group=foreground)
        self.sprite.image.anchor_x = self.image.width/2
        self.sprite.image.anchor_y = self.sprite.image.height/2
        self.sprite.x = x
        self.sprite.y = y
        self.speedx = 0
        self.speedy = 0
        self.terminalv = -30
        self.buffery = 0
        self.accely = 2
        self.speed = 4
        self.bufferw = 2
        self.walkc = 1
        self.dir = -1
        self.landed = False
        self.walkc = 1
        self.bufferw = 1
        self.dead = False
        self.bufferd = 1
        self.updatehitbox()

    def updatehitbox(self):
        self.hitbox = [
            self.sprite.x-self.sprite.image.width/2+2,
            self.sprite.y-self.sprite.image.height/2,
            self.sprite.x+self.sprite.image.width/2-2,
            self.sprite.y+self.sprite.image.height/2
            ]

    def fall(self):
        if self.speedy > self.terminalv:
            if self.buffery == self.accely:
                self.speedy-=2
                self.buffery = 1
            else:
                self.buffery+=1
        self.updatehitbox()

        for object in Objects:
            cl,cr,cu,cd = collision(self,object,0,self.speedy)
            if cd and object != self:
                self.speedy = 0
                self.sprite.y = object.hitbox[3]+self.sprite.image.height/2
                self.updatehitbox()

    def walk(self):
        self.speedx = self.dir
        for object in Objects:
            cl,cr,cu,cd = collision(self,object,self.speedx,0)
            if cl and object != self or cr and object != self:
                self.dir*=(-1)
                self.speedx = self.dir
                if type(object).__name__=='enemy':
                    object.dir*=-1
            c1,c2,c3,cdp = collision(self,object,self.speedx,-1)
            cl2,cr2,cu2,cd2 = collision(self,object,(self.sprite.image.width*self.dir)+self.speedx,-1)
            if not cd2 and cdp and object != self and type(object).__name__=='ground':
                self.dir*=(-1)
                self.speedx = self.dir
        if self.dead == True:
            self.speedx = 0
        self.updatehitbox()

    def animate(self):
        if self.bufferw == 10:
            self.bufferw = 1
            if self.walkc == 1:
                self.walkc = 2
            else:
                self.walkc = 1
        else:
            self.bufferw+=1
        if self.dead == False:
            self.sprite.image = pyglet.resource.image('enemy'+str(self.walkc)+'.png')
            self.sprite.image.anchor_x = self.image.width/2
            self.sprite.image.anchor_y = self.image.height/2

    def die(self):
        self.sprite.image = pyglet.resource.image('enemy3.png')
        self.sprite.image.anchor_x = self.sprite.image.width/2
        self.sprite.image.anchor_y = self.sprite.image.height/2
        self.updatehitbox()
        self.dead = True
        if self.bufferd == 30:
            Objects.remove(self)
            self.sprite.batch = None
        else:
            self.bufferd+=1
            
    def move(self):
        self.updatehitbox()
        if self.dead:
            self.die()
        self.fall()
        self.walk()
        self.animate()
        self.sprite.x+=self.speedx
        self.sprite.y+=self.speedy
        self.updatehitbox()


class player():

    def __init__(self):
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
        self.image = pyglet.resource.image('player'+self.dir+'1.png')
        self.sprite = pyglet.sprite.Sprite(self.image,6,200,batch=batch,group=foreground)
        self.sprite.image.anchor_x = self.image.width/2
        self.sprite.image.anchor_y = self.image.height/2
        self.updatehitbox()

    def updatehitbox(self):
        
        self.hitbox = [
            self.sprite.x-12/2,
            self.sprite.y-self.sprite.image.height/2,
            self.sprite.x+12/2,
            self.sprite.y+self.sprite.image.height/2
            ]

    def run(self):
        self.carryx = 0
        self.updatehitbox()
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
        for object in Objects:
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
        for object in Objects:
            cl,cr,cu,cd = collision(self,object,self.carryx,self.speedy)
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


class sky():

    def __init__(self,image):
        self.image = pyglet.resource.image(image)
        self.sprite = pyglet.sprite.Sprite(self.image,batch=batch,group=background)
        self.sprite.image.height=window.height
        self.sprite.image.width=window.width
        self.sprite.image.anchor_x = self.image.width/2
        self.sprite.image.anchor_y = self.sprite.image.height/2
        self.sprite.x = window.width/2
        self.sprite.y = window.height/2

Objects = []
Ground1 = ground(150,110,'ground.png',Objects)
Ground2 = ground(500,220,'ground.png',Objects)
Ground3 = ground(500,70,'ground.png',Objects)
Ground4 = ground(650,110,'ground.png',Objects)
Platform1 = platform(80,280,'platform.png',30,260,Objects)
Platform2 = platform(110,260,'platform.png',60,260,Objects)
Platform3 = platform(140,240,'platform.png',90,260,Objects)
Platform4 = platform(170,220,'platform.png',120,260,Objects)
Platform5 = platform(200,200,'platform.png',150,360,Objects)
Gate1 = gate(560,164,'gater.png',Objects)
Gate2 = gate(590,164,'gateb.png',Objects)
Gate3 = gate(620,164,'gatey.png',Objects)
Button1 = button(400,95,'button1r.png',Gate1,Objects)
Button2 = button(500,245,'button1b.png',Gate2,Objects)
Button3 = button(230,135,'button1y.png',Gate3,Objects)
Enemy1 = enemy(450,400,'enemy1.png',Objects)
Enemy2 = enemy(470,310,'enemy1.png',Objects)
Enemy3 = enemy(450,100,'enemy1.png',Objects)
Enemy4 = enemy(470,130,'enemy1.png',Objects)
Enemy5 = enemy(60,192,'enemy1.png',Objects)
Sky = sky('sky.png')

Player = player()

@window.event
def on_draw():
    batch.draw()

@window.event
def on_mouse_motion(x,y,dx,dy):
    Player.mousex = x
    Player.mousey = y
    

@window.event
def on_key_press(symbol,modifier):
    if symbol == key.A:
        Player.left = True
    if symbol == key.D:
        Player.right = True
    if symbol == key.W:
        Player.up = True
    if symbol == key.SPACE:
        Player.space = True

@window.event
def on_key_release(symbol,modifier):
    if symbol == key.A:
        Player.left = False
    if symbol == key.D:
        Player.right = False
    if symbol == key.W:
        Player.up = False
    if symbol == key.SPACE:
        Player.space = False
        
def update(dt):
    Player.move()
    for object in Objects:
        if 'move' in dir(object):
            object.move()
   
    window.clear()
   
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/30)
    pyglet.app.run()
