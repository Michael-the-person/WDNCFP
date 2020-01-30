import pygame, random, time, math
from aliens import alien
from player_class import player
from tiles import tile
pygame.init()

#basic setup
Width = 800
Height = 500
screen = pygame.display.set_mode((Width,Height),0, 32)
pygame.display.set_caption('We do not come in peace')
timer = pygame.time.Clock()

#asset loading
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
tilestats = [grassimg,roadimg,treeimg,waterimg,bushimg,None,marble]
wallimg = [barriersideimg,barrierimg]

#variable setup
alienstats = ((alientrooperimg,(19,26,18),1),())
aliens = []
tilesize = (42,42)
def loadboard(board):
    global screen
    tiles = []
    for a in range(0,len(board)):
        b = 0
        for b in range(0,len(board[a])):
            #print(b*42,a*42,board[a][b])
            tiles.append(tile([b*42,a*42],board[a][b],screen))
    return tiles

#ground loading
ground =[[5,5,5,5,5,5,5,5],
         [5,6,6,6,5,0,0,5],
         [5,6,6,6,0,0,0,5],
         [5,6,6,6,5,0,0,5],
         [5,5,5,5,5,0,0,5],
         [5,0,0,0,0,0,0,5],
         [5,0,5,5,0,0,0,5],
         [5,0,5,0,0,5,5,5],
         [5,0,0,0,0,0,0,5],
         [5,5,5,5,5,0,0,5],
         [0,0,0,0,0,0,0,0],
         [5,5,5,5,5,0,5,5]]
tiles = loadboard(ground)

def loadstudent(names):
    parts = []
    for name in names:
        parts.append(\
            pygame.image.load('assets/sprites/studentimg/'+name+'.png').convert_alpha())
    return parts

studentparts = loadstudent(['heads/heads1','pants/pants2',\
                       'bodies/bodies3','mouths/mouths3','eyes/eyes4'])

aliens.append(alien(0,[-200,-200],screen,alienstats))

player = player([-100,-100],3,0,screen,(19,26,18))
print("hi")

#gaming options setup
playing = True
Fullscreen = False

#defined modules
def stufftouchedtiles(pos,size):
    touched = []
    for tile in tiles:
        if tile.touching(pos,size) == True:
            touched.append(tile.gettype())
    return touched

step = 0
while playing == True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((Width,Height), pygame.FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((Width,Height), 0, 32)

    player.pointatmouse(Width,Height)
    player.move(tiles)
    playerpos = player.pos
    
    for tile in tiles:
        tile.updatefloor([0,6],tilestats,playerpos,Width,Height,tilesize)
        tile.updatewallside(tilestats,wallimg,playerpos,Width,Height,tilesize)

    player.updategraphic(studentparts,step,Width,Height)
    
    for alien in aliens:
        alien.determinedir(alienstats,playerpos)
        alien.move(tiles)
        alien.updategraphic(alienstats,playerpos,step,Width,Height)

    for tile in tiles:
        tile.updatewalltop(tilestats,wallimg,playerpos,Width,Height,tilesize)
    
    pygame.display.flip()
    timer.tick(50)
    step += 0.2
    if step>4:
        step = 0
