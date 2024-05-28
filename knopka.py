import pygame

import picture

pygame.init()

class Knopka():

    def __init__(self,x,y,size,picture1):
        self.x=x
        self.y=y
        self.size=size

        rect_work_2=pygame.Rect(30,30,30,30)
        rect_work_2.center=[370,380]
        self.object_for_draw=picture.Picture(picture1, self.size, self.x, self.y)
        print(("11"))



    def draw(self, place: pygame.Surface):
        self.object_for_draw.draw(place)

    def controller(self,events):

        for event in events:

            rect_for_picture=pygame.rect.Rect(self.x,self.y,self.size[0],self.size[1])

            if event.type == pygame.MOUSEBUTTONDOWN and rect_for_picture.collidepoint(event.pos):


                print(self.x,self.y)








