import pygame

import knopka
import picture

pygame.init()

class Worker():
    def __init__(self,put,x,y,size):
        self.x=x
        self.y=y
        self.size=size
        self.put=put



        self.kopka=knopka.Knopka(x+100,y-50,[50,50],"sprites/controls/up_yellow.png",self.for_worker)


        self.worker_2_2 = picture.Picture(put,size,x,y)

    def draw_worker(self,place:pygame.Surface):
        self.worker_2_2.draw(place)
        self.kopka.draw(place)

    def for_worker(self):
        pass