import pygame

pygame.init()

#Начальные параметры, загрузка материалов
width = 1366
height = 768
fps = 60
game_name = "Игра"
WHITE = "#FFFFFF"


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(game_name)
pac = pygame.image.load('pac-man.png')
pac_rect = pac.get_rect()


clock = pygame.time.Clock()

speedx = 10
speedy = 10



run = True
while run:
#Запуск экрана в выводом изображение
    clock.tick(fps)
    screen.fill(WHITE)
    screen.blit(pac, pac_rect)
#Колизия
    if pac_rect.bottom > height:
        pac_rect.x == 0
        pac_rect.y == 0
    if pac_rect.top < 0:
        speedy = -speedy
    if pac_rect.left < 0:
        speedx = -speedx
    if pac_rect.right > width:
        speedx = -speedx

#Управление
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and pac_rect.left > 0:
        if key[pygame.K_LEFT]:
            pac_rect.x -= 10
    if key[pygame.K_RIGHT] and pac_rect.right < width:
        if key[pygame.K_RIGHT]:
            pac_rect.x += 10
    if pac_rect.colliderect(pac_rect):
        speedy = -speedy
    if key[pygame.K_UP] and pac_rect.left > 0:
        if key[pygame.K_UP]:
            pac_rect.y -= 10
    if key[pygame.K_DOWN] and pac_rect.right < width:
        if key[pygame.K_DOWN]:
            pac_rect.y += 10
    if pac_rect.colliderect(pac_rect):
        speedy = -speedy
    pygame.display.update()
pygame.quit()
