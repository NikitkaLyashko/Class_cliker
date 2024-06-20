import random

import pygame.display,round,text,knopka,picture




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
    global  worker_2_2
    chislo_monet.chislo -= stoimost_yellow_button.chislo
    level_2.chislo+=1
    worker_2_2 = picture.Picture("sprites/worker/worker2.png", [160, 180], 250, 380)



chislo_monet=text.Text(0, 70, 0,"У вас ","монет ")
object_levl=text.Text(0,120,1,"Уровень ","")
upgrade=text.Text(0,20,10,"Для улучшения надо столько: ","")
ceichas_mony=text.Text(0,170,2,"За клик столько:","")
uvel_mony=text.Text(0,220,1,"ЗА апгрейд столько:","")
level_2=text.Text(350,380,0,"Уровеь:","",25)
stoimost_yellow_button=text.Text(470,380,10,"","")


button_2=knopka.Knopka(370,380,[100,100],"sprites/controls/up_yellow.png",for_worker_2)
put_2=knopka.Knopka(1400,0,[100,100],"sprites/controls/up_green.png",work_button)

worker_2_2 = picture.Picture("sprites/worker/worker2_inv.png",[160,180],250,380)

