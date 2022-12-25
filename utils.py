import pygame
import math

def intersect(rect: pygame.Rect, x, y):
    if x >= rect.x and x <= (rect.x+rect.w) and y >= rect.y and y <= (rect.y+rect.h):
        return True
    else:
        return False

#def aa(a,b):
    #c = a*a - 2*a*b + b*b
    #c = a*a + b*b
    #g = math.sqrt(c)
    #return g
