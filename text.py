import pygame

import text

pygame.init()

class Text():


    def __init__(self,x,y,number,stroka,next_stroka,size=50):
        self.def_x=x
        self.def_y=y
        self.new_num=number
        self.def_stroks=stroka
        self.def_next_str=next_stroka
        self.font = pygame.font.SysFont("Arial", size)
        self.object=self.font.render(self.def_stroks+str(self.new_num)+self.def_next_str, True, [250, 0, 0])
        print(self.new_num)

    def draw_text(self,place:pygame.Surface):
        place.blit(self.object,[self.def_x,self.def_y])
    #
    # def obnovi_chislo(self,number):
    #     self.new_num=number
    #     self.object = self.font.render(self.def_stroks+str(int(self.new_num))+self.def_next_str, True, [250, 0, 0])

    @property
    def chislo(self):
        return  self.new_num

    @chislo.setter
    def chislo(self,new_number):
        self.new_num=new_number
        self.object=self.font.render(self.def_stroks+str(int(self.new_num))+self.def_next_str, True, [250, 0, 0])








