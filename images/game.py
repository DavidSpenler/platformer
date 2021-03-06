import pyglet
from pyglet.window import key
from pyglet.window import mouse
import sys

window = pyglet.window.Window(800,500,caption='Game')

#batch = pyglet.graphics.Batch()
#background = pyglet.graphics.OrderedGroup(0)
#foreground = pyglet.graphics.OrderedGroup(1)

from sky import sky
from ground import ground
from platform import platform
from gate import gate
from button import button
from enemy import enemy
from player import player
from box import box
from collisions import collision

import global_vars

global_vars.init()

global_vars.batch = pyglet.graphics.Batch()
global_vars.background = pyglet.graphics.OrderedGroup(0)
global_vars.foreground = pyglet.graphics.OrderedGroup(1)

Objects = []

Player = player(400,250,'playerr1.png',Objects)

Platform1 = platform(80,280,'platform.png',30,260,Objects)
Platform2 = platform(110,260,'platform.png',60,260,Objects)
Platform3 = platform(140,240,'platform.png',90,260,Objects)
Platform4 = platform(170,220,'platform.png',120,260,Objects)
Platform5 = platform(200,200,'platform.png',150,360,Objects)

Box = box(450,400,'box.png',Objects)
Box = box(470,400,'box.png',Objects)
Box = box(490,400,'box.png',Objects)
Box = box(510,400,'box.png',Objects)
Box = box(530,400,'box.png',Objects)
Box = box(550,400,'box.png',Objects)
Box = box(570,400,'box.png',Objects)
Box = box(590,400,'box.png',Objects)
Box = box(450,440,'box.png',Objects)
Box = box(470,440,'box.png',Objects)
Box = box(490,440,'box.png',Objects)
Box = box(510,440,'box.png',Objects)
Box = box(530,440,'box.png',Objects)
Box = box(550,440,'box.png',Objects)
Box = box(570,440,'box.png',Objects)
Box = box(590,440,'box.png',Objects)
Box = box(480,420,'box.png',Objects)
Box = box(560,420,'box.png',Objects)
Box = box(580,420,'box.png',Objects)
Box = box(600,420,'box.png',Objects)
Box = box(530,480,'box.png',Objects)
Box = box(550,480,'box.png',Objects)
Box = box(570,480,'box.png',Objects)
Box = box(590,480,'box.png',Objects)
Box = box(550,550,'box.png',Objects)
Box = box(570,550,'box.png',Objects)
Box = box(590,550,'box.png',Objects)
Box = box(480,550,'box.png',Objects)
Box = box(560,550,'box.png',Objects)
Box = box(580,550,'box.png',Objects)
Box = box(600,550,'box.png',Objects)
Box = box(530,550,'box.png',Objects)
Box = box(550,550,'box.png',Objects)
Box = box(570,550,'box.png',Objects)
Box = box(590,550,'box.png',Objects)

Platform5 = platform(200,250,'platform.png',150,360,Objects)

#Player = player(400,250,'playerr1.png',Objects)

Ground1 = ground(150,110,'ground.png',Objects)
Ground2 = ground(500,220,'ground.png',Objects)
Ground3 = ground(500,70,'ground.png',Objects)
Ground4 = ground(650,110,'ground.png',Objects)
Gate1 = gate(560,164,'gater.png',Objects)
Gate2 = gate(590,164,'gateb.png',Objects)
Gate3 = gate(620,164,'gatey.png',Objects)
Button1 = button(400,95,'button1r.png',Gate1,Objects)
Button2 = button(170,135,'button1b.png',Gate2,Objects)
Button3 = button(230,135,'button1y.png',Gate3,Objects)
#Enemy1 = enemy(450,400,'enemy1.png',Objects)
#Enemy2 = enemy(470,310,'enemy1.png',Objects)
Enemy3 = enemy(450,100,'enemy1.png',Objects)
Enemy4 = enemy(470,130,'enemy1.png',Objects)
Enemy5 = enemy(60,192,'enemy1.png',Objects)
Sky = sky('sky.png',window.width,window.height)


@window.event
def on_draw():
    global_vars.batch.draw()

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
    #Player.move()
    for object in Objects:
        if 'move' in dir(object):
            object.move()
    window.clear()
    #print("tick")
   
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/30)
    pyglet.app.run()
