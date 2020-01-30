import pygame
import math
from defined_modules import *
import random

class alien:
    def __init__(self,alientype,pos,screen,alienstats):
        self.type = alientype
        self.pos = pos
        self.dir = [0,0]
        self.screen = screen
        self.size = alienstats[self.type][1]

    def determinedir(self,alienstats,playerpos):
        if random.randint(0,100) == 1 or circletouch(playerpos,0,self.pos,150) != True:
            self.pointatplayer(alienstats,playerpos)
            #print(self.dir)
            self.dir[0] = self.dir[0]*random.randint(80,120)/100
            self.dir[1] = self.dir[1]*random.randint(80,120)/100
        
    def pointatplayer(self,alienstats,playerpos):
        speed = alienstats[self.type][2]
        self.dir = locatedir(playerpos,self.pos,speed)

    def move(self,tiles):
        self.pos[0]+=self.dir[0]
        self.pos[1]+=self.dir[1]
        newsize = [self.size[0],self.size[2]]
        if 5 in stufftouchedtiles(self.pos,newsize,tiles):
            self.pos[0]-=self.dir[0]
            if 5 in stufftouchedtiles(self.pos,newsize,tiles):
                self.pos[0]+=self.dir[0]
                self.pos[1]-=self.dir[1]
                if 5 in stufftouchedtiles(self.pos,newsize,tiles):
                    self.pos[0]-=self.dir[0]

    def updategraphic(self,alienstats,playerpos,step,Width,Height):
        alienstat = alienstats[self.type]
        size = alienstat[1]
        pos = self.pos
        alienimg = alienstat[0]
        #print(size)
        #print(alienimg)
        newalienimg = alienimg
        if self.dir[0] < 0:
            newalienimg = pygame.transform.flip(alienimg,True,False)
        if self.dir == [0,0]:
            newstep = 0
        else:
            newstep = step
        self.screen.blit(newalienimg,
                    [pos[0]+Width/2-playerpos[0]-size[0]/2,
                     pos[1]+Height/2-playerpos[1]-size[1]+size[2]/2-newstep])
        pygame.draw.circle(self.screen,(0,0,255),
                                [round(self.pos[0]+Width/2-playerpos[0]),
                                 round(self.pos[1]+Height/2-playerpos[1])],3)
