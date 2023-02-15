import pygame

class bonus:
    image = None
    rect = None
    is_eaten = False
    def __init__(self, x, y):
        self.image = pygame.image.load('Bonus.png')
        self.rect = pygame.Rect(x, y, 64, 64)