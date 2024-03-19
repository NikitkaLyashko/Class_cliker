import pygame

import picture

pygame.init()

class Knopka():

    def __init__(self,x,y):
        self.x=x
        self.y=y
        rect_work_2=pygame.Rect(30,30,30,30)
        rect_work_2.center=[370,380]
        self.pict_work_2=picture.Picture("sprites/controls/up_green.png",[160,180],250,380)


    def draw(self, place: pygame.Surface):
        self.pict_work_2.draw(place)









