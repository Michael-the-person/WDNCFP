import pygame

Width = 500
Height = 500
screen = pygame.display.set_mode((Width,Height),0, 32)

roadimg = pygame.image.load('assets/tiles/road.png').convert()
treeimg = pygame.image.load('assets/tiles/tree.png').convert()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    screen.blits(((roadimg,(0,0)),(treeimg,(0,0))))
    pygame.display.flip()

