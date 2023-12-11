import random

import pygame
class Round():
    def __init__(self,start_a,x,y):
        self.x=x
        self.y=y
        self.a=start_a
        self.speed_round_x = random.randint(-5, 5)
        self.speed_round_y = random.randint(-5, 5)
        self.color1 = random.randint(0, 255)
        self.color2 = random.randint(0, 255)
        self.color3 = random.randint(0, 255)
    def plus_10(self):
        self.a+=10
    def plus_a(self,nomer):
        self.a+=nomer

    def drow_round(self,place):

        pygame.draw.circle(place,[self.color1,self.color2,self.color3],[self.x,self.y],self.a,8)

    def ride_round(self):
        self.x += self.speed_round_x
        self.y += self.speed_round_y
        if self.y+self.a>=700:
            self.speed_round_y=-abs(self.speed_round_y)
        if self.y-self.a<=0:
            self.speed_round_y=abs(self.speed_round_y)
        if self.x+self.a>=1500:
            self.speed_round_x=-abs(self.speed_round_x)
        if self.x-self.a<=0:
            self.speed_round_x=abs(self.speed_round_x)

        self.a+=1
        if self.a>100:
            self.a=5

# or self.x>=1500 or self.x<=0 or self.y<=0