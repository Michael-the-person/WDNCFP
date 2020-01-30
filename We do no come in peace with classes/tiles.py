from defined_modules import touch
import pygame
class tile:
    def __init__(self,pos,tiletype,screen):
        self.pos = pos
        self.type = tiletype
        self.screen = screen
    def updatefloor(self,floortiles,tilestats,playerpos,Width,Height,size):
        if self.type in floortiles:
            pos = self.pos
            img = tilestats[self.type]
            self.screen.blit(img,
                             [pos[0]+Width/2-playerpos[0]-size[0]/2,
                              pos[1]+Height/2-playerpos[1]-size[1]/2])
            pygame.draw.circle(self.screen,(0,0,255),
                                    [round(self.pos[0]+Width/2-playerpos[0]),
                                     round(self.pos[1]+Height/2-playerpos[1])],3)
    def updatewallside(self,tilestats,wallimg,playerpos,Width,Height,size):
        if self.type == 5:
            pos = self.pos
            img = wallimg[0]
            self.screen.blit(img,
                             [pos[0]+Width/2-playerpos[0]-size[0]/2,
                              pos[1]+Height/2-playerpos[1]])
            #self.screen.blit(img,blockwidth/2

    def updatewalltop(self,tilestats,wallimg,playerpos,Width,Height,size):
        if self.type == 5:
            pos = self.pos
            img = wallimg[1]
            self.screen.blit(img,
                             [pos[0]+Width/2-playerpos[0]-size[0]/2,
                              pos[1]+Height/2-playerpos[1]-size[1]])
            #self.screen.blit(img,blockwidth/2
    def touching(self,pos,size):
        return touch(pos,size,self.pos,[42,42])
    def gettype(self):
        return self.type
