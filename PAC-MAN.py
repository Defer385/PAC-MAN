import pygame
import pac_man_object



pygame.init()

#Начальные параметры, загрузка материалов
width = 1366
height = 768
fps = 60
game_name = "Игра"
WHITE = "#FFFFFF"


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(game_name)
pac_man = pac_man_object.Pacman()

clock = pygame.time.Clock()



run = True
while run:
#Управление
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        pac_man.rect.x -= pac_man.speed
        pac_man.sprite_frame_time += 1 # <<<---- Таймер
        pac_man.sprite_frame_sides = 1
    if key[pygame.K_RIGHT]:
        pac_man.rect.x += pac_man.speed
        pac_man.sprite_frame_time += 1 # <<<---- Таймер
        pac_man.sprite_frame_sides = 2
    if key[pygame.K_UP]:
        pac_man.rect.y -= pac_man.speed
        pac_man.sprite_frame_time += 1 # <<<---- Таймер
        pac_man.sprite_frame_sides = 3
    if key [pygame.K_DOWN]:
        pac_man.rect.y += pac_man.speed
        pac_man.sprite_frame_time += 1 # <<<---- Таймер
        pac_man.sprite_frame_sides = 4

#Колизия
    if pac_man.rect.bottom > height:
        pac_man.rect.y = height - pac_man.rect.height
    if pac_man.rect.top < 0:
        pac_man.rect.y = 0
    if pac_man.rect.left < 0:
        pac_man.rect.x = 0
    if pac_man.rect.right > width:
        pac_man.rect.x = width - pac_man.rect.width

#Условия для работы анимации
    if pac_man.sprite_frame_sides == 1:
        pac_man.pixel_for_animation = 64    #<<<--- Право

    if pac_man.sprite_frame_sides == 2:
        pac_man.pixel_for_animation = 0     #<<<--- Леов

    if pac_man.sprite_frame_sides == 3:
       pac_man.pixel_for_animation = 128    #<<<--- Вверх

    if pac_man.sprite_frame_sides == 4:
       pac_man.pixel_for_animation = 192    #<<<--- Вниз
        


    screen.fill(WHITE)
    screen.blit(pac_man.image, pac_man.rect, pygame.Rect(64*pac_man.sprite_frame,pac_man.pixel_for_animation,64,64))

    pac_man.update()

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
