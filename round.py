import random

import pygame
class Round():
    def __init__(self,start_a,x,y):
        self.x=x
        self.y=y
        self.a=start_a
        self.speed_round_x = random.randint(-5, 5)
        self.speed_round_y = random.randint(-5, 5)
    def plus_10(self):
        self.a+=10
    def plus_a(self,nomer):
        self.a+=nomer

    def drow_round(self,place):
        pygame.draw.circle(place,[0,0,200],[self.x,self.y],self.a,3)

    def ride_round(self):
        self.x += self.speed_round_x
        self.y += self.speed_round_y