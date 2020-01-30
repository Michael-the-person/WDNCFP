import pygame, random, time, math
pygame.init()
#Damage, accuracy, range, bullet speed, energy cost
Width = 500
Height = 500
radiantodegreenum=57.2957795
screen = pygame.display.set_mode((Width,Height),0, 32)
pygame.display.set_caption('We do not come in peace')
icon = pygame.image.load('icon.png')
def loadstudent(names):
    parts = []
    for name in names:
        parts.append(pygame.image.load('assets/sprites/studentimg/'+name+'.png').convert_alpha())
    return parts
student = loadstudent(['heads/heads1','pants/pants2','bodies/bodies3','mouths/mouths3','eyes/eyes4'])
print(student)

grassimg = pygame.image.load('assets/tiles/grass.png').convert()
roadimg = pygame.image.load('assets/tiles/road.png').convert()
treeimg = pygame.image.load('assets/tiles/tree.png').convert()
waterimg = pygame.image.load('assets/tiles/water.png').convert()
bushimg = pygame.image.load('assets/tiles/bush.png').convert()
swordimg = pygame.image.load('assets/sprites/knight/sword.png').convert_alpha()
barrierimg = pygame.image.load('assets/tiles/barrier.png').convert()
barriersideimg = pygame.image.load('assets/tiles/wallblock.png').convert()
gap = pygame.image.load('assets/tiles/gap.png').convert()
marble = pygame.image.load('assets/tiles/marble ground.png').convert()

alientrooperimg = pygame.image.load('assets/sprites/enemy/alientrooper.png').convert_alpha()

laserimg = pygame.image.load('assets/sprites/bullets/bullet.png').convert_alpha()
duckgunimg = pygame.image.load('duck gun.png').convert_alpha()
keys = [False,False,False,False,False,False]
blockimg = [grassimg,roadimg,treeimg,waterimg,bushimg,barrierimg,marble]
aliensimg = [alientrooperimg]
#gun: img,range,width,height,speed,damage,gunimg,accuracy
gunrecord = ((laserimg,500,27,27,5,10,duckgunimg,180),())
print(gunrecord)
bulletsspeed = [1]
playerdir = 1
playerspeed = 3
playerpos = [60,60]
Fullscreen = False
timer = pygame.time.Clock()
play = True
shoot = False
knightwalk = 11
blockwidth = barrierimg.get_width()
blockheight = barrierimg.get_height()
ground =[
    [5,5,5,5,5,0,0,5],
    [5,6,6,6,6,0,0,5],
    [5,6,6,6,5,0,0,5],
    [5,5,5,5,5,0,0,0]
]
#Alienstats: posx,posy,movex,movey,eventory,item
#aliens=[[60,60,0,[0],0],[10,10,0,[0],0],[-100,-100,0,[0],0],[-10,-100,0,[0],0]]
aliens = []
bullets=[]
pygame.display.set_icon(icon)
step = 0

playermove = False
#======================================================================================
studentheight = 26
studentwidth = 19
studentmiddle = 18
#======================================================================================
alienheight = 26
alienwidth = 19
alienmiddle = 18
#======================================================================================
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

def degtodir(flyspeed,bulletdir):
    y = flyspeed * math.sin(bulletdir/180*math.pi)
    x = flyspeed * math.cos(bulletdir/180*math.pi)
    return x,y

def dirtodeg(x,y):
    #deg = math.atan(y/x)*180/math.pi
    deg = math.atan2(x,y)
    deg = 360-deg*57.29+90
    return deg

def locatedir(x1,y1,x2,y2,speed):
    distancex=x2-x1
    distancey=y2-y1
    distance=math.sqrt(distancex**2+distancey**2)
    distancex = distancex/distance*speed
    distancey = distancey/distance*speed
    return distancex,distancey

def blit(things, aliens, bullets):
    global playerpos, blockwidth, blockheight, barriersideimg, \
           barrierimg, Height, Width,gunrecord,student,playerdir, step, playermove, studentmiddle, studentheight, \
           studentwidth, alienheight, alienmiddle, alienwidth
    for thing in things:
        if thing[2]!=5:
            blockx=thing[0]-playerpos[0]+Width/2
            blocky=thing[1]-playerpos[1]+Height/2
            if touch(blockx,blocky,blockwidth,blockheight,0,0,Width,Height)==True:
                screen.blit(blockimg[thing[2]],[blockx-blockwidth/2,blocky-blockheight/2])
    
    for thing in things:
        if thing[2]==5:
            blockx=thing[0]-playerpos[0]+Width/2
            blocky=thing[1]-playerpos[1]+Height/2
            if touch(blockx,blocky,blockwidth,blockheight,0,0,Width,Height)==True:
                screen.blit(barriersideimg,[blockx-blockwidth/2,blocky])
    
    #screen.blit(allknights[knightmode][knightdir-1],[Width/2,Height/2+knightwalk-22])
    #screen.blit(objectimg,[objectpos[0]-knightpos[0]+Width/2,objectpos[1]-knightpos[1]+Height/2+knightwalk-10])
    for part in student:
        if playerdir == 0:
            part = pygame.transform.flip(part,True,False)
        if playermove == False:
            newstep = 0
        else:
            newstep = step
        #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 20)
        screen.blit(part,[Width/2-studentwidth/2,Height/2-studentheight+studentmiddle/2-newstep])
    for alien in aliens:
        screen.blit(aliensimg[alien[4]],[alien[0]+Width/2-playerpos[0]-alienwidth/2,
                                         alien[1]+Height/2-playerpos[1]-alienheight+alienmiddle/2])
    #pos,direction,owner,btype,rangecount
    for bullet in bullets:
        bulletimg=gunrecord[bullet[3]][0]
        pos = bullet[0]
        gun = gunrecord[bullet[3]]
        screen.blit(bulletimg,[pos[0]+Width/2-playerpos[0]-gun[2]/2,pos[1]+Height/2-playerpos[1]-gun[3]/2])

    for thing in things:
        if thing[2]==5:
            blockx=thing[0]-playerpos[0]+Width/2
            blocky=thing[1]-playerpos[1]+Height/2
            if touch(blockx,blocky,blockwidth,blockheight,0,0,Width,Height)==True:
                screen.blit(barrierimg,[blockx-blockwidth/2,blocky-blockheight])

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

def stufftouchedtiles(tiles,pos,height,width):
    global blockheight,blockwidth
    touchedtiles = []
    for tile in tiles:
        if touch(tile[0]-blockwidth/2,tile[1]-blockheight/2,blockheight,blockwidth,pos[0]-height/2,pos[1]-width/2,\
                 width,height):
            touchedtiles.append(tile[2])
    #print(touchedtiles)
    return touchedtiles

def playertouchedtiles(tiles,playerpos):
    global studentwidth, studentmiddle
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 20)
    return stufftouchedtiles(tiles,playerpos,studentwidth,studentmiddle)

def makebullet(pos,direction,owner,btype):
    global bullets
    bullets.append([pos,direction,owner,btype,0])

def autofirebullet(pos,targetpos,owner,btype):
    global gunrecord
    gun = gunrecord[btype]
    if pos != targetpos:
        #img,range,width,height,speed,damage,gunimg,accuracy
        #dirtodeg(pos[0]-targetpos[0],pos[1]-targetpos[1])
        randomthing = random.randint(-gun[7],gun[7])
        makebullet(pos,dirtodeg(targetpos[0]-pos[0],targetpos[1]-pos[1])+randomthing,owner,btype)

def handlebullets():
    global gunrecord
    #pos,direction,owner,btype,rangecount
    #gun: img,range,width,height,speed
    for bullet in bullets:
        gun = gunrecord[bullet[3]]
        pos = bullet[0]
        direction = bullet[1]
        move = degtodir(gun[4],bullet[1])
        bulletouched=stufftouchedtiles(tiles,pos,gun[2],gun[3])
        pos[0]+=move[0]
        pos[1]+=move[1]
        bullet[4]+=gun[4]
        if 5 in bulletouched:
            bullets.remove(bullet)
        elif bullet[4]>gun[1]:
            bullets.remove(bullet)

def circletouch(pos1,rad1,pos2,rad2):
    x = abs(pos1[0]-pos2[0])
    y = abs(pos1[1]-pos2[1])
    if math.sqrt(x**2 + y**2) < rad1+rad2:
        return True

def studentcheck(pos,rad,studentpos):
    global studentmiddle, studentwidth
    radius = (studentmiddle+studentheight)/4
    return circletouch(pos,rad,studentpos)
    

def handlealiens():
    global aliens
    for alien in aliens:
        print()

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
#=========================================================================================================
    previousplayerpos = [playerpos[0],playerpos[1]]
    for i in range(len(aliens)):
        aliens[i][3]=aliens[i][1]
        aliens[i][4]=aliens[i][2]
    playermove = True
    if keys[0] and keys[1]:
        playerpos[0] += playerspeed
        playerpos[1] += playerspeed
    elif keys[1] and keys[2]:
        playerpos[0] += playerspeed
        playerpos[1] -= playerspeed
    elif keys[2] and keys[3]:
        playerpos[0] -= playerspeed
        playerpos[1] -= playerspeed
    elif keys[3] and keys[0]:
        playerpos[0] -= playerspeed
        playerpos[1] += playerspeed
    elif keys[0]:
        playerpos[1] += playerspeed
    elif keys[1]:
        playerpos[0] += playerspeed
    elif keys[2]:
        playerpos[1] -= playerspeed
    elif keys[3]:
        playerpos[0] -= playerspeed
    else:
        playermove = False
#######################################################################################
    if keys[3]:
        playerdir = 0
    elif keys[1]:
        playerdir = 1

    touched = playertouchedtiles(tiles,playerpos)
    if 5 in touched:
        #print("touched")
        playerpos = previousplayerpos

    for alien in aliens:
        if shoot:
            if playerpos[0] != alien[0]:
                if playerpos[1] != alien[1]:
                    #pos,direction,owner,btype,rangecount
                    autofirebullet([alien[0],alien[1]],playerpos,0,0)
    shoot = False
    handlebullets()
    if object == 'sword':
        objectimg = swordimg
    step += 0.2
    if step > 5:
        step = 0
    screen.fill((0,0,0))
    blit(tiles,aliens, bullets)
    pygame.display.flip()
    timer.tick(50)
