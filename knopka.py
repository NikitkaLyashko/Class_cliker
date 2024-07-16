import pygame

import picture

pygame.init()

class Knopka():

    def __init__(self,x,y,size,picture1,action):
        self.x=x
        self.y=y
        self.size=size
        self.def_action=action


        self.object_for_draw=picture.Picture(picture1, self.size, self.x, self.y)




    def draw(self, place: pygame.Surface):
        self.object_for_draw.draw(place)

    def controller(self,events:list):


        for event in events:

            rect_for_picture=pygame.rect.Rect(self.x,self.y,self.size[0],self.size[1])

            if event.type == pygame.MOUSEBUTTONDOWN and rect_for_picture.collidepoint(event.pos):
                self.def_action()


                events.remove(event)











