from ItemIds import ids
import pygame

pygame.init()


class Inventory:
    def __init__(self):
        self.tiles = [Tile(10, 20), Tile(75, 20), Tile(150, 20), Tile(215, 20), Tile(280, 20), Tile(345, 20)]
        self.open = False
        self.font = pygame.font.SysFont("calibri", 20)
        self.pickeditem = None
        self.pickedamount = None
        self.pressed = False
        self.selectednum = 0
        self.selectedslot = None
        self.selecteditem = None

    def draw(self, screen):
        if self.open:
            screen.fill((0, 0, 0))
            for slot in self.tiles:
                slot.draw(screen)
            screen.blit(self.font.render("hands", False, (255, 255, 255)), (55, 2))
            screen.blit(self.font.render("pockets", False, (255, 255, 255)), (250, 2))
            if self.pickeditem is not None:
                screen.blit(ids[self.pickeditem],
                            (pygame.mouse.get_pos()[0] - 32, pygame.mouse.get_pos()[1] - 32))
        else:
            # width of 420 height of 85
            pygame.draw.rect(screen, (0, 0, 0), (190, 415, 420, 85))
            for slot in self.tiles:
                slot.hotbar_draw(screen, (201 + self.tiles.index(slot) * 65, 426))
                if (slot.xpos, slot.ypos) == self.selectedslot:
                    pygame.draw.rect(screen, (0, 0, 0), (203 + self.tiles.index(slot) * 65, 428, 59, 59), 1)

    def update(self, screen, events):
        self.selectedslot = self.tiles[self.selectednum].xpos, self.tiles[self.selectednum].ypos
        for slot in self.tiles:
            if (slot.xpos, slot.ypos) == self.selectedslot:
                self.selecteditem = slot.item
        mouse = pygame.mouse.get_pressed()
        self.draw(screen)
        if self.open:
            mouse_slot = self.mouse_on_slot()
            if mouse[0]:
                if not self.pressed:
                    self.pressed = True
                    if self.pickeditem is not None:
                        self.placeitem(mouse_slot)
                    else:
                        self.pickitem(mouse_slot)
            if not mouse[0]:
                if self.pressed:
                    self.pressed = False
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6]:
                    self.selectednum = int(event.unicode) - 1
                elif event.key == pygame.K_e:
                    self.open = not self.open

    def mouse_on_slot(self):
        mouse = pygame.mouse.get_pos()
        for slot in self.tiles:
            if slot.rect.collidepoint(mouse[0], mouse[1]):
                return slot.xpos, slot.ypos

    def pickitem(self, slot):
        for tile in self.tiles:
            if (tile.xpos, tile.ypos) == slot:
                self.pickeditem, self.pickedamount = tile.item, tile.amount
                tile.item, tile.amount = None, None

    def placeitem(self, slot):
        for tile in self.tiles:
            if (tile.xpos, tile.ypos) == slot:
                if tile.item == self.pickeditem:
                    self.pickedamount -= 1
                    tile.amount += 1
                    if self.pickedamount == 0:
                        self.pickeditem = None
                elif tile.item is None:
                    tile.item, tile.amount = self.pickeditem, self.pickedamount
                    self.pickeditem, self.pickedamount = None, None
                elif tile.item != self.pickeditem:
                    item, amount = tile.item, tile.amount
                    tile.item, tile.amount = self.pickeditem, self.pickedamount
                    self.pickeditem, self.pickedamount = item, amount

    def additem(self, item, amount):
        for slot in self.tiles:
            if slot.item == item:
                slot.amount += amount
                item, amount = None, None
        for slot in self.tiles:
            if slot.item is None:
                slot.item, slot.amount = item, amount
                item, amount = None, None

    def space_for(self, item):
        for slot in self.tiles:
            if slot.item == item:
                return True
            if slot.item is None:
                return True
        return False

    def read_slot(self, slotnum):
        return self.tiles[slotnum].item, self.tiles[slotnum].amount


class Tile(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, item=None, amount=None):
        super().__init__()
        self.xpos = xpos
        self.ypos = ypos
        self.image = pygame.Surface((63, 63))
        self.image.fill((255, 255, 255))
        self.item = item
        self.amount = amount
        self.ids = ids
        self.font = pygame.font.SysFont("calibri", 10)
        self.rect = pygame.Rect(xpos, ypos, 65, 65)

    def add_item(self, item, amount):
        self.item = item
        self.amount = amount

    def draw(self, screen):
        screen.blit(self.image, (self.xpos + 1, self.ypos + 1))
        if self.item is not None:
            screen.blit((self.ids[self.item]), ((self.xpos + 3), (self.ypos + 3)))
            screen.blit(self.font.render(str(self.amount), False, (0, 0, 0)), (self.xpos + 5, self.ypos + 50))

    def hotbar_draw(self, screen, pos):
        xpos, ypos = pos
        screen.blit(self.image, pos)
        if self.item is not None:
            screen.blit((self.ids[self.item]), ((xpos + 3), (ypos + 3)))
            screen.blit(self.font.render(str(self.amount), False, (0, 0, 0)), (xpos + 5, ypos + 50))
