
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
