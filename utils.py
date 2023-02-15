import pygame


def intersect_point(rect: pygame.Rect, x, y):
    if x >= rect.x and x <= (rect.x+rect.w) and y >= rect.y and y <= (rect.y+rect.h):
        return True
    else:
        return False


def intersect_rect(rect: pygame.Rect, rect1: pygame.Rect):
    x1 = rect.x
    x11 = rect1.x
    x2 = rect.x + rect.w
    x21 = rect1.x + rect1.w
    
    y1 = rect.y
    y2 = rect.y + rect.h
    y11 = rect1.y
    y21 = rect1.y + rect1.h
    if (((x1>x11 and x1 < x21)  or  (x2>x11 and x2 < x21))    and    ((y1>y11 and y1<y21)  or  (y2>y11 and y2<y21))):
        return True
    else:
        return False