import pygame

import knopka
import picture
import text

pygame.init()

class Worker():
    def __init__(self,put,x,y,size,price_abgrade,bank):
        self.x=x
        self.y=y
        self.size=size
        self.put=put
        self.bank=bank
        self.a=1.05


        self.kopka=knopka.Knopka(x+100,y-50,[50,50],"sprites/controls/up_yellow.png",self.for_worker)

        self.yroven=text.Text(x+50,y-50,0,"уровень","",20)

        self.ctoimost_levl = text.Text(x + 50, y - 30, price_abgrade, "", "",20)




        self.worker_2_2 = picture.Picture(put,size,x,y)

    def draw_worker(self,place:pygame.Surface):
        self.worker_2_2.draw(place)
        self.kopka.draw(place)
        self.yroven.draw_text(place)
        self.ctoimost_levl.draw_text(place)


    def for_worker(self):
        print(self.kopka.x)

        if self.bank.chislo>=self.ctoimost_levl.chislo:
            self.yroven.chislo += 1
            self.bank.chislo-=self.ctoimost_levl.chislo
            self.ctoimost_levl.chislo*=self.a
            self.a=self.a+0.02283

        # if chislo_monet.chislo >= stoimost_yellow_button.chislo:

        # chislo_monet.chislo -= stoimost_yellow_button.chislo


        # chislo_monet.chislo -= stoimost_yellow_button.chislo
        # stoimost_yellow_button.chislo*=a
        # a=a+0.02283
        # level_3.chislo+=1



        pass



    def controller_worker(self,events):

        self.kopka.controller(events)

