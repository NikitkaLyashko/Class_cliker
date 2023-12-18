import random

import pygame
class Round():
    def __init__(self,start_a,x,y,main_round=None):
        self.main_round=main_round
        self.x=x
        self.y=y
        self.radius=start_a
        self.speed_round_x = random.randint(-5, 5)
        self.speed_round_y = random.randint(-5, 5)
        self.color1 = random.randint(0, 255)
        self.color2 = random.randint(0, 255)
        self.color3 = random.randint(0, 255)
    def plus_10(self):
        self.radius+=10
    def plus_a(self,nomer):
        self.radius+=nomer

    def drow_round(self,place):

        pygame.draw.circle(place, [self.color1,self.color2,self.color3], [self.x,self.y], self.radius, 8)
        if self.main_round!=None:
            pygame.draw.line(place, [self.color1,self.color2,self.color3],[self.x,self.y],[self.main_round.x,self.main_round.y],3)

    def ride_round(self):
        self.x += self.speed_round_x
        self.y += self.speed_round_y
        if self.y+self.radius>=700:
            self.speed_round_y=-abs(self.speed_round_y)
        if self.y-self.radius<=0:
            self.speed_round_y=abs(self.speed_round_y)
        if self.x+self.radius>=1500:
            self.speed_round_x=-abs(self.speed_round_x)
        if self.x-self.radius<=0:
            self.speed_round_x=abs(self.speed_round_x)

        self.radius+=1
        if self.radius>100:
            self.radius=5

# or self.x>=1500 or self.x<=0 or self.y<=0