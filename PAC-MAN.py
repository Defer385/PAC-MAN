import pygame
import pac_man_object
import brick_object
import point_object
import utils
import random


pygame.init()

#Начальные параметры, загрузка материалов
width = 1366
height = 768
fps = 60
score = 0
game_name = "Игра"
BLACK = "#000000"
WHITE = "#HHHHHH"


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(game_name)
pac_man = pac_man_object.Pacman()

clock = pygame.time.Clock()

point_list = []
brick_list = []

for i in range(5):
    point = point_object.point(random.randint(0,width), random.randint(0,height))
    point_list.append(point)
for i in range(5):
    brick = brick_object.brick(random.randint(0,width), random.randint(0,height))
    brick_list.append(brick)


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

#Колизия экрана
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
        pac_man.pixel_for_animation = 0     #<<<--- Лево

    if pac_man.sprite_frame_sides == 3:
       pac_man.pixel_for_animation = 128    #<<<--- Вверх

    if pac_man.sprite_frame_sides == 4:
       pac_man.pixel_for_animation = 192    #<<<--- Вниз


    screen.fill(BLACK)

#Создание точек и их колизия
    for i in range(5):
        point = point_list[i]
        if utils.intersect_point(pac_man.rect, point.rect.x, point.rect.y):
            point.is_eaten = True
        if point.is_eaten == False:
            screen.blit(point.image, point.rect)

#Создание кипичей
    for i in range(5):
        brick = brick_list[i]
        screen.blit(brick.image, brick.rect)

#Колизия пак-мана и кирпича
    for i in range(5):
        brick = brick_list[i]
        if utils.intersect_cube(pac_man.rect, brick.rect) and key[pygame.K_RIGHT]:
           pac_man.rect.x -= pac_man.speed
        if utils.intersect_cube(pac_man.rect, brick.rect) and key[pygame.K_LEFT]:
            pac_man.rect.x += pac_man.speed
        if utils.intersect_cube(pac_man.rect, brick.rect) and key[pygame.K_UP]:
            pac_man.rect.y += pac_man.speed
        if utils.intersect_cube(pac_man.rect, brick.rect) and key[pygame.K_DOWN]:
            pac_man.rect.y -= pac_man.speed




    screen.blit(pac_man.image, pac_man.rect, pygame.Rect(64*pac_man.sprite_frame,pac_man.pixel_for_animation,64,64))


    pac_man.update()
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
