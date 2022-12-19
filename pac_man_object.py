import pygame

class Pacman:
    rect = None
    sprite_frame_time = 0
    sprite_frame = 0
    speed = 10
    sprite_frame_sides = 0
    pixel_for_animation = 0
    image = None
    def __init__ (self):
        self.x = 10
        self.y = 10
        self.image = pygame.image.load('pac-man.png')
        self.rect = pygame.Rect(0, 0, 64, 64)

    def update (self):
        #Анимация
        if self.sprite_frame_time > 5:  #Условия для изменение спрайта
            self.sprite_frame += 1
            self.sprite_frame_time = 0
        if self.sprite_frame == 4:       #Для цикличности анимации
            self.sprite_frame = 0
