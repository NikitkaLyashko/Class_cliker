import pygame

import picture

pygame.init()

class Knopka():

    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size=size
        rect_work_2=pygame.Rect(30,30,30,30)
        rect_work_2.center=[370,380]
        self.pict_work_2=picture.Picture("sprites/controls/up_green.png",self.size,self.x,self.y)


    def draw(self, place: pygame.Surface):
        self.pict_work_2.draw(place)









