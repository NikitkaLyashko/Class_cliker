import pygame

import knopka
import picture
import text

pygame.init()

class Worker():
    def __init__(self, obvodka, x, y, size, price_abgrade, bank, general_doxod, doxod_person_second, picture_2, next_worker):
        self.x=x
        self.y=y
        self.size=size
        self.bank=bank
        self.a=1.05
        self.general_doxod=general_doxod
        self.doxod_person_second=doxod_person_second
        self.picture_2=picture_2
        self.next_worker=next_worker
        self.levl_test=0
        self.visible=False

        self.kopka=knopka.Knopka(x+100,y-50,[50,50],"sprites/controls/up_yellow.png",self.for_worker)
        self.yroven=text.Text(x+50,y-50,0,"уровень","",20)
        self.ctoimost_levl = text.Text(x + 50, y - 30, price_abgrade, "", "",20)
        self.doxod_pers=text.Text(x+50,y-70,self.doxod_person_second, "Доход:+", "", 25)

        self.picture_2 = picture.Picture(self.picture_2, self.size, self.x, self.y)

        self.obvodaka_w = picture.Picture(obvodka, size, x, y)

    def draw_worker(self,place:pygame.Surface):
        self.kopka.draw(place)
        self.yroven.draw_text(place)
        self.ctoimost_levl.draw_text(place)
        self.doxod_pers.draw_text(place)

        if self.yroven.chislo>=1:
            self.picture_2.draw(place)
        else:
            self.obvodaka_w.draw(place)




    def for_worker(self):
        """
        деф for worker вызывается в классе кнопка, при нажатии на кнопку

        """
        print(self.kopka.x)

        if self.bank.chislo>=self.ctoimost_levl.chislo:
            self.yroven.chislo += 1
            if self.yroven.chislo>=10:
                self.next_worker.visible=True

            self.bank.chislo-=self.ctoimost_levl.chislo
            self.ctoimost_levl.chislo*=self.a
            self.a=self.a+0.02283


            self.general_doxod.chislo += self.doxod_pers.chislo
            self.doxod_pers.chislo += self.doxod_person_second
            self.levl_test+=1






        # self.wich_worker=picture.Picture("sprites/worker/worker2.png", [160, 180], 250, 380)
        pass



    def controller_worker(self,events):

        self.kopka.controller(events)

