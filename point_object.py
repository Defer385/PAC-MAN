import pygame

class point:
    image = None
    rect = None
    is_eaten = False
    def __init__(self, x, y):
        self.image = pygame.image.load('point.png')
        self.rect = pygame.Rect(x, y, 8, 8)
