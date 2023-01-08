import pygame

class brick:
    image = None
    rect = None
    collision = False
    def __init__(self, x, y):
        self.image = pygame.image.load('Brick.png')
        self.rect = pygame.Rect(x, y, 64, 64)
