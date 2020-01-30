import pygame
from defined_modules import *
import math

class player:
    def __init__(self,pos,speed,look,screen,size):
        self.speed = speed
        self.look = look
        self.dir = None
        self.pos = pos
        self.screen = screen
        self.size = size
        self.side = 0
    def pointatmouse(self,Width,Height):
        mousepos = pygame.mouse.get_pos()
        if circletouch(mousepos,20,[Width/2,Height/2],0):
            #print("stopped")
            self.dir = [0,0]
        else:
            #print("following")
            #print(len([mousepos[0],mousepos[1],self.pos[0],self.pos[1],self.speed]))
            self.dir = locatedir(mousepos,[Width/2,Height/2],self.speed)
            #self.dir = self.locatedir(mousepos[1],self.pos[0],self.pos[1],self.speed)
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
    def updategraphic(self,parts,step,Width,Height):
        #self.screen.blit()
        for part in parts:
            if self.dir[0] < 0:
                part = pygame.transform.flip(part,True,False)
            if self.dir == [0,0]:
                newstep = 0
            else:
                newstep = step
            pygame.draw.circle(self.screen, (0, 0, 255),
                                    (round(Width/2), round(Height/2)), 3)
            size = self.size
            self.screen.blit(part,
                             [Width/2-size[0]/2,Height/2-size[1]+size[2]/2-newstep])
    def returnpos(self):
        return self.pos
