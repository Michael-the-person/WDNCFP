import pygame, time, math
pygame.init()

Width = 500
Height = 500
screen = pygame.display.set_mode((Width,Height),0, 32)
pygame.display.set_caption('Harrow Invaders Demo')
icon = pygame.image.load('icon.png')
kf = pygame.image.load('assets/sprites/knight/knightfront.png').convert_alpha()
kfr = pygame.image.load('assets/sprites/knight/knightfrontright.png').convert_alpha()
kr = pygame.image.load('assets/sprites/knight/knightright.png').convert_alpha()
krb = pygame.image.load('assets/sprites/knight/knightrightback.png').convert_alpha()
kb = pygame.image.load('assets/sprites/knight/knightback.png').convert_alpha()
kbl = pygame.image.load('assets/sprites/knight/knightbackleft.png').convert_alpha()
kl = pygame.image.load('assets/sprites/knight/knightleft.png').convert_alpha()
klf = pygame.image.load('assets/sprites/knight/knightleftfront.png').convert_alpha()
kfw = pygame.image.load('assets/sprites/knight/knightfrontwater.png').convert_alpha()
kfrw = pygame.image.load('assets/sprites/knight/knightfrontrightwater.png').convert_alpha()
krw = pygame.image.load('assets/sprites/knight/knightrightwater.png').convert_alpha()
krbw = pygame.image.load('assets/sprites/knight/knightrightbackwater.png').convert_alpha()
kbw = pygame.image.load('assets/sprites/knight/knightbackwater.png').convert_alpha()
kblw = pygame.image.load('assets/sprites/knight/knightbackleftwater.png').convert_alpha()
klw = pygame.image.load('assets/sprites/knight/knightleftwater.png').convert_alpha()
klfw = pygame.image.load('assets/sprites/knight/knightleftfrontwater.png').convert_alpha()

grassimg = pygame.image.load('assets/tiles/grass.png').convert()
roadimg = pygame.image.load('assets/tiles/road.png').convert()
treeimg = pygame.image.load('assets/tiles/tree.png').convert()
waterimg = pygame.image.load('assets/tiles/water.png').convert()
bushimg = pygame.image.load('assets/tiles/bush.png').convert()
swordimg = pygame.image.load('assets/sprites/knight/sword.png').convert_alpha()
barrierimg = pygame.image.load('assets/tiles/barrier.png').convert()
wallimg = pygame.image.load('assets/tiles/wallblock.png').convert()
cornerimg = pygame.image.load('assets/tiles/cornerblock.png').convert()
gap = pygame.image.load('assets/tiles/gap.png').convert()

alientrooperimg = pygame.image.load('assets/sprites/enemy/alientrooper.png').convert_alpha()

laserimg = pygame.image.load('assets/sprites/bullets/bullet.png').convert_alpha()

pygame.mixer.music.load('assets/sounds/Elecrystal Sound Team - Forests.mp3')

allknights = [[kf,kfr,kr,krb,kb,kbl,kl,klf],[kfw,kfrw,krw,krbw,kbw,kblw,klw,klfw]]
keys = [False,False,False,False,False,False]
blockimg = [grassimg,roadimg,treeimg,waterimg,bushimg,barrierimg,wallimg,cornerimg,gap,wallimg,cornerimg]
aliensimg = [alientrooperimg]
bulletsimg = [laserimg]
bulletsspeed = [1]
knightdir = 1
knightlandspeed = 1.5
knightwaterspeed = 1
knightbushspeed = 0.5
knightspeed = knightlandspeed
knightpos = [42,42]
objectpos = [42,42]
Fullscreen = False
jumping = False
timer = pygame.time.Clock()
play = True
shoot = False
knightwalk = 11
ground =[
    [7,6,6,6,6,6,6,6,6,7,8,8,8,8,8,8,8,8,8,7,6,6,6,6,6,6,6,6,7],
    [5,0,0,0,0,3,3,3,3,5,8,8,8,8,8,8,8,8,8,5,0,0,0,0,0,0,0,0,5],
    [5,1,3,3,3,3,3,3,3,5,8,8,8,8,8,8,8,8,8,5,0,0,0,0,0,0,0,0,5],
    [5,1,0,3,3,3,3,3,0,6,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,5],
    [5,0,1,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
    [5,0,0,1,1,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
    [5,2,2,0,0,1,0,4,4,10,9,9,9,9,9,9,9,9,9,10,0,0,0,0,0,0,0,0,5],
    [5,2,2,2,2,0,1,0,4,5,8,8,8,8,8,8,8,8,8,5,0,0,0,0,0,0,0,0,5],
    [5,2,2,2,2,2,0,1,1,5,8,8,8,8,8,8,8,8,8,5,0,0,0,0,0,0,0,0,5],
    [6,9,9,9,9,9,9,9,9,6,8,8,8,8,8,8,8,8,8,6,9,9,9,9,9,9,9,9,6],
]
aliens=[[0,42,42,0,0]]
bullets=[]
object = 'sword'
pygame.display.set_icon(icon)
def loadboard(board):
    tiles = []
    for a in range(0,len(board)):
        b = 0
        for b in range(0,len(board[a])):
            #print(b*42,a*42,board[a][b])
            tiles.append([b*42,a*42,board[a][b]])
    return tiles
tiles = loadboard(ground)
#print(tiles)
def blit(things, aliens, bullets):
    global knightpos
    for thing in things:
        blockx=thing[0]-knightpos[0]+Width/2-blockimg[thing[2]].get_width()+42
        blocky=thing[1]-knightpos[1]+Height/2-blockimg[thing[2]].get_height()+42
        if blockx+blockimg[thing[2]].get_height()>0 and blockx<Width and blocky+blockimg[thing[2]].get_height()>0 and blocky<Height and thing[2] != 9 and thing[2] != 10:
            screen.blit(blockimg[thing[2]],[blockx,blocky])
    for alien in aliens:
        screen.blit(aliensimg[alien[0]],[alien[1]+Width/2-knightpos[0],alien[2]+Height/2-knightpos[1]])
    for bullet in bullets:
        screen.blit(bulletsimg[bullet[0]],[bullet[1]+Width/2-knightpos[0],bullet[2]+Height/2-knightpos[1]])
    screen.blit(allknights[knightmode][knightdir-1],[Width/2,Height/2+knightwalk-22])
    screen.blit(objectimg,[objectpos[0]-knightpos[0]+Width/2,objectpos[1]-knightpos[1]+Height/2+knightwalk-10])
    for thing in things:
        blockx=thing[0]-knightpos[0]+Width/2-blockimg[thing[2]].get_width()+42
        blocky=thing[1]-knightpos[1]+Height/2-blockimg[thing[2]].get_height()+42
        if blockx+blockimg[thing[2]].get_height()>0 and blockx<Width and blocky+blockimg[thing[2]].get_height()>0 and blocky<Height and thing[2] == 9 or thing[2] == 10:
            screen.blit(blockimg[thing[2]],[blockx,blocky])
def touch(ox1,oy1,w1,h1,ox2,oy2,w2,h2):
    nx2 = ox1 + w1
    ny2 = oy1 + h1
    nx4 = ox2 + w2
    ny4 = oy2 + h2
    nx3 = ox2
    ny3 = oy2
    nx1 = ox1
    ny1 = oy1
    #print(nx1,ny1,nx2,ny2,nx3,ny3,nx4,ny4)
    if ny3 < ny2 and ny3 > ny1 or ny4 > ny1 and ny3 < ny2:
        if nx3 < nx2 and nx3 > nx1 or nx4 > nx1 and nx3 < nx2:
            return True

def knighttouchedtiles(tiles,knightpos,objectwidth,objectheight):
    touchedtiles = []
    for tile in tiles:
        if touch(tile[0],tile[1],42,42,knightpos[0],knightpos[1],objectwidth,objectheight):
            touchedtiles.append(tile[2])
    #print(touchedtiles)
    return touchedtiles

#pygame.mixer.music.play(-1,0)

while play == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((Width,Height), pygame.FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((Width,Height), 0, 32)

            if event.key == pygame.K_DOWN:
                keys[0] = True
            if event.key == pygame.K_RIGHT:
                keys[1] = True
            if event.key == pygame.K_UP:
                keys[2] = True
            if event.key == pygame.K_LEFT:
                keys[3] = True
            if event.key == pygame.K_SPACE:
                keys[4] = True
            if event.key == pygame.K_s:
                shoot = True
            if event.key == pygame.K_c:
                bullets=[]
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                keys[0] = False
            if event.key == pygame.K_RIGHT:
                keys[1] = False
            if event.key == pygame.K_UP:
                keys[2] = False
            if event.key == pygame.K_LEFT:
                keys[3] = False
            if event.key == pygame.K_SPACE:
                keys[4] = False
    previousknightpos = [knightpos[0],knightpos[1]]
    for i in range(len(aliens)):
        aliens[i][3]=aliens[i][1]
        aliens[i][4]=aliens[i][2]
    if keys[4]:
        if not jumping:
            beforespacetime=time.perf_counter()
            jumping=True
            knightmode=1
            knightspeed=3
    if jumping:
        knightwalk=7
    if jumping and round(10*time.perf_counter())/10-2==round(10*beforespacetime)/10:
        jumping=False
    if keys[0] and keys[1]:
        knightdir = 2
        knightpos[0] += knightspeed
        knightpos[1] += knightspeed
        objectpos = [knightpos[0]+15,knightpos[1]-6]
    elif keys[1] and keys[2]:
        knightdir = 4
        knightpos[0] += knightspeed
        knightpos[1] -= knightspeed
        objectpos = [knightpos[0]-3,knightpos[1]-6]
    elif keys[2] and keys[3]:
        knightdir = 6
        knightpos[0] -= knightspeed
        knightpos[1] -= knightspeed
        objectpos = [knightpos[0]-3,knightpos[1]-6]
    elif keys[3] and keys[0]:
        knightdir = 8
        knightpos[0] -= knightspeed
        knightpos[1] += knightspeed
        objectpos = [knightpos[0]+3,knightpos[1]-6]
    elif keys[0]:
        knightdir = 1
        knightpos[1] += knightspeed
        objectpos = [knightpos[0]+15,knightpos[1]-6]
    elif keys[1]:
        knightdir = 3
        knightpos[0] += knightspeed
        objectpos = [knightpos[0]+15,knightpos[1]-6]
    elif keys[2]:
        knightdir = 5
        knightpos[1] -= knightspeed
        objectpos = [knightpos[0]-3,knightpos[1]-6]
    elif keys[3]:
        knightdir = 7
        knightpos[0] -= knightspeed
        objectpos = [knightpos[0]-3,knightpos[1]-6]

    touched = knighttouchedtiles(tiles,knightpos,21,5)
    if 2 in touched:
        if not jumping:
            knightpos = previousknightpos
    if 5 in touched: knightpos = previousknightpos
    elif 6 in touched: knightpos = previousknightpos
    elif 7 in touched: knightpos = previousknightpos
    elif 9 in touched: knightpos = previousknightpos
    
    if touched in [[3],[3,3],[3,3,3],[3,3,3,3]]:
        if not jumping:
            knightwalk = 7
            knightmode = 1
            knightspeed = knightwaterspeed
    elif 4 in touched:
        if not jumping:
            knightwalk = 7
            knightspeed= knightbushspeed
    else:
        if not jumping: knightmode = 0
        if not jumping: knightspeed = knightlandspeed
        if keys[0] or keys[1] or keys[2] or keys[3]:
            if knightwalk > 6:
                knightwalkspeed = -1
            if knightwalk < 0:
                knightwalkspeed = 1
            knightwalk += knightwalkspeed
        else:
            knightwalk = 7
    for alien in aliens:
        if shoot:
            bullets.append([0,alien[1],alien[2],0,0,0])
            shoot=False
    for bullet in bullets:
        bulletouched=knighttouchedtiles(tiles,[bullet[1],bullet[2]],45,45)
        bulletx=bullet[1]
        bullety=bullet[2]
        distancex=-1*(bullet[1]-knightpos[0])
        distancey=-1*(bullet[2]-knightpos[1])
        distance_=math.sqrt(distancex**2+distancey**2)
        if not bullet[3]:
            bullet[4] = (bulletsspeed[bullet[0]]*distancex)/distance_
            bullet[5] = (bulletsspeed[bullet[0]]*distancey)/distance_
            bullet[3] = True
        bullet[1]=bulletx+bullet[4]
        bullet[2]=bullety+bullet[5]
        if 5 in bulletouched: bullets.remove(bullet)
        elif 6 in bulletouched: bullets.remove(bullet)
        elif 7 in bulletouched: bullets.remove(bullet)
        elif 9 in bulletouched: bullets.remove(bullet)
    if object == 'sword':
        objectimg = swordimg
    screen.fill((0,0,0))
    blit(tiles,aliens, bullets)
    pygame.display.flip()
    timer.tick(60)
