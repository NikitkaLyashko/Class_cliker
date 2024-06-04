import random

import pygame.display,round,text,knopka




def chet_monet():

    chislo_monet.chislo+=ceichas_mony.chislo


def work_button():
    if chislo_monet.chislo >= upgrade.chislo:
        chislo_monet.chislo -= upgrade.chislo
        upgrade.chislo *= 1.05

        object_levl.chislo += 1

        ceichas_mony.chislo += uvel_mony.chislo
        uvel_mony.chislo += 1

def for_worker_2():
    level_2.chislo+=1


chislo_monet=text.Text(0, 70, 0,"У вас ","монет ")
object_levl=text.Text(0,120,1,"Уровень ","")
upgrade=text.Text(0,20,10,"Для улучшения надо столько: ","")
ceichas_mony=text.Text(0,170,2,"За клик столько:","")
uvel_mony=text.Text(0,220,1,"ЗА апгрейд столько:","")
level_2=text.Text(350,380,0,"Уровеь:","",25)


button_2=knopka.Knopka(370,380,[100,100],"sprites/controls/up_yellow.png",for_worker_2)
put_2=knopka.Knopka(1400,0,[100,100],"sprites/controls/up_green.png",work_button)


