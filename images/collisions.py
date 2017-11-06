
def collision(sprite1,sprite2,xmod,ymod):
    cl,cr,cu,cd = False,False,False,False
    if sprite1.hitbox[0]+xmod < sprite2.hitbox[2] and sprite1.hitbox[2]+xmod > sprite2.hitbox[2] and sprite1.hitbox[1]+ymod < sprite2.hitbox[3] and sprite1.hitbox[3]+ymod > sprite2.hitbox[1]:
        cl = True
    if sprite1.hitbox[2]+xmod > sprite2.hitbox[0] and sprite1.hitbox[0]+xmod < sprite2.hitbox[0] and sprite1.hitbox[1]+ymod < sprite2.hitbox[3] and sprite1.hitbox[3]+ymod > sprite2.hitbox[1]:
        cr = True
    if (sprite1.hitbox[1]+ymod < sprite2.hitbox[3] and sprite1.hitbox[3]+ymod > sprite2.hitbox[3] and sprite1.hitbox[0]+xmod < sprite2.hitbox[2] and sprite1.hitbox[2]+xmod > sprite2.hitbox[0]) or (sprite1.hitbox[0]+xmod == sprite2.hitbox[0] and sprite1.hitbox[2]+xmod == sprite2.hitbox[2] and sprite1.hitbox[1]+ymod < sprite2.hitbox[3] and sprite1.hitbox[3]+ymod > sprite2.hitbox[3]):
        cd = True
    if (sprite1.hitbox[3]+ymod > sprite2.hitbox[1] and sprite1.hitbox[1]+ymod < sprite2.hitbox[1] and sprite1.hitbox[0]+xmod < sprite2.hitbox[2] and sprite1.hitbox[2]+xmod > sprite2.hitbox[0]) or (sprite1.hitbox[0] == sprite2.hitbox[0] and sprite1.hitbox[2] == sprite2.hitbox[2] and sprite1.hitbox[3] > sprite2.hitbox[1] and sprite1.hitbox[1]+ymod < sprite2.hitbox[1]):
        cu = True

    if sprite1.sprite.y < sprite2.hitbox[3] and sprite1.sprite.y > sprite2.hitbox[1] and sprite1.sprite.x > sprite2.hitbox[0] and sprite1.sprite.x < sprite2.hitbox[2]:
        if abs(sprite1.sprite.y-sprite2.hitbox[1]) < (sprite1.sprite.y-sprite2.hitbox[3]):
            cu = True
        else:
            cd = True
    return cl,cr,cu,cd

def clipped(sprite1,sprite2,xmod,ymod):
    #print('start')
    cl_m,cr_m,cu_m,cd_m = collision(sprite1,sprite2,xmod,ymod)
    cl,cr,cu,cd = collision(sprite1,sprite2,0,0)
    if cu_m and (cd or sprite1.sprite.y > sprite2.sprite.y):
        cd = True
        print('downward clipping')
    else:
        cd = False
    if cd_m and (cu or sprite1.sprite.y < sprite2.sprite.y):
        cu = True
        print('upward clipping')
    else:
        cu = False
    #print('done')
    return cd,cu
