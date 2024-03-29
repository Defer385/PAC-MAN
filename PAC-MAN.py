import pygame
import pac_man_object
import brick_object
import bonus_object
import point_object
import utils
import random


pygame.init()

#Начальные параметры, загрузка материалов
width = 1366
height = 768
fps = 60
score = 0
white = [50,50,50]
game_name = "Пак-Ман"
BLACK = "#000000"
WHITE = "#HHHHHH"


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(game_name)
pac_man = pac_man_object.Pacman()

clock = pygame.time.Clock()

point_list = []
brick_list = []
bonus_list = []

#Создание точек(Как объект, без вывода)
for i in range(5):
    point = point_object.point(random.randint(0,width), random.randint(0,height))
    point_list.append(point)
#Создание кирпичей(Как объект, без вывода)
for i in range(5):
    brick = brick_object.brick(random.randint(0,width), random.randint(0,height))
    brick_list.append(brick)
#Создание бонуса(Как объект, без вывода)
for i in range(2):
    bonus = bonus_object.bonus(random.randint(0,width), random.randint(0,height))
    bonus_list.append(bonus)



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

#Создание кирпичей и вывод на экран
    for i in range(5):
        brick = brick_list[i]
        screen.blit(brick.image, brick.rect)

#Колизия точек и вывод на экран
    for i in range(5):
        point = point_list[i]
        if utils.intersect_point(pac_man.rect, point.rect.x, point.rect.y):
            point.is_eaten = True
            score += 10
        if point.is_eaten == False:
            screen.blit(point.image, point.rect)

#Колизия бонусов и вывод на экран
    for i in range(2):
        bonus = bonus_list[i]
        if utils.intersect_rect(pac_man.rect, bonus.rect):
            bonus.is_eaten = True
            score += 50
        if bonus.is_eaten == False:
            screen.blit(bonus.image, bonus.rect)

#Вывод очков (Тестовый вариант)
        font = pygame.font.Font(None, 25)
        text = font.render("Score: "+str(score),True,white)
        screen.blit(text, [300,300])

#Колизия пак-мана и кирпича
    for i in range(5):
        brick = brick_list[i]
        if utils.intersect_rect(pac_man.rect, brick.rect) and key[pygame.K_RIGHT]:
           pac_man.rect.x -= pac_man.speed
        if utils.intersect_rect(pac_man.rect, brick.rect) and key[pygame.K_LEFT]:
            pac_man.rect.x += pac_man.speed
        if utils.intersect_rect(pac_man.rect, brick.rect) and key[pygame.K_UP]:
            pac_man.rect.y += pac_man.speed
        if utils.intersect_rect(pac_man.rect, brick.rect) and key[pygame.K_DOWN]:
            pac_man.rect.y -= pac_man.speed


    screen.blit(pac_man.image, pac_man.rect, pygame.Rect(64*pac_man.sprite_frame,pac_man.pixel_for_animation,64,64))

    pac_man.update()
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
