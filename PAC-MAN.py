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
pac_rect = pygame.Rect(0, 0, 64, 64)


clock = pygame.time.Clock()

speed = 10
sprite_frame = 0
sprite_frame_time = 0

run = True
while run:
#Управление
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        pac_rect.x -= speed
    if key[pygame.K_RIGHT]:
        pac_rect.x += speed
    if key[pygame.K_UP]:
        pac_rect.y -= speed
    if key [pygame.K_DOWN]:
        pac_rect.y += speed

#Колизия
    if pac_rect.bottom > height:
        pac_rect.y = height - pac_rect.height
    if pac_rect.top < 0:
        pac_rect.y = 0
    if pac_rect.left < 0:
        pac_rect.x = 0
    if pac_rect.right > width:
        pac_rect.x = width - pac_rect.width

    screen.fill(WHITE)
    screen.blit(pac, pac_rect, pygame.Rect(64*sprite_frame,0,64,64))

#Анимация
    sprite_frame_time += 1      #Таймер
    if sprite_frame_time > 10:  #Условия для изменение спрайта
        sprite_frame += 1
        sprite_frame_time = 0
    if sprite_frame == 4:       #Для цикличности анимации
        sprite_frame = 0

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
