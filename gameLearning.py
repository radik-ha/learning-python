import pygame
pygame.init()

X = 600
Y = 600

scrn = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Car Game')
imp = pygame.image.load("./car.png").convert()
imp = pygame.transform.scale(imp,(40,60))

status = True
cx=X//2
cy=Y//2
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                cx+=10
            elif i.key == pygame.K_LEFT:
                cx-=10
            elif i.key == pygame.K_UP:
                cy-=10
            elif i.key == pygame.K_DOWN:
                cy+=10
    scrn.fill((0,0,0))
    scrn.blit(imp, (cx, cy))
    pygame.display.flip()
pygame.quit()
