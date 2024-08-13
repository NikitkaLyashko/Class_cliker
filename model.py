import random

import pygame.display,round,text,knopka,picture

import worker


def doxod_v_secundy():
    chislo_monet.chislo += doxod.chislo




def chet_monet():

    chislo_monet.chislo+=ceichas_mony.chislo


def work_button():
    if chislo_monet.chislo >= upgrade.chislo:
        chislo_monet.chislo -= upgrade.chislo
        upgrade.chislo *= 1.05

        object_levl.chislo += 1

        ceichas_mony.chislo += uvel_mony.chislo
        uvel_mony.chislo += 1


a=1.02
def for_worker_2():
    global  worker_2_2,a

    if chislo_monet.chislo>=stoimost_yellow_button.chislo:

        chislo_monet.chislo -= stoimost_yellow_button.chislo
        stoimost_yellow_button.chislo*=a
        a=a+0.02283
        level_2.chislo+=1
        doxod.chislo+=doxod_pers1.chislo

        # doxod_v_secundy()
        doxod_pers1.chislo += 1

    worker_2_2 = picture.Picture("sprites/worker/worker2.png", [160, 180], 250, 380)


def for_worker_3():
    global  worker_3_3,a

    if chislo_monet.chislo>=stoimost_yellow_button.chislo:

        chislo_monet.chislo -= stoimost_yellow_button.chislo
        stoimost_yellow_button.chislo*=a
        a=a+0.02283
        level_3.chislo+=1

    worker_3_3 = picture.Picture("sprites/worker/worker3.png", [160,180],500,500)


chislo_monet=text.Text(0, 70, 10000000,"У вас ","монет ")
object_levl=text.Text(0,120,1,"Уровень ","")
upgrade=text.Text(0,20,10,"Для улучшения надо столько: ","")
ceichas_mony=text.Text(0,170,2,"За клик столько:","")
uvel_mony=text.Text(0,220,1,"ЗА апгрейд столько:","")
level_2=text.Text(350,380,0,"Уровеь:","",25)
level_3=text.Text(580,550,0,"Уровеь:","",25)
doxod=text.Text(700,50,0,"Доход:","",60)
doxod_pers1=text.Text(350, 330, 1, "Доход:+", "", 25)


stoimost_yellow_button=text.Text(470,380,10000,"","")


button_2=knopka.Knopka(370,380,[100,100],"sprites/controls/up_yellow.png",for_worker_2)
put_2=knopka.Knopka(1400,0,[100,100],"sprites/controls/up_green.png",work_button)
put_3=knopka.Knopka(650,500,[100,100],"sprites/controls/up_yellow.png",for_worker_3)

worker_2_2 = picture.Picture("sprites/worker/worker2_inv.png",[160,180],250,380)
worker_3_3=picture.Picture("sprites/worker/worker3_inv.png",[160,180],500,500)


worker3=worker.Worker("sprites/worker/worker3_inv.png",500,180,[160,180],50000,chislo_monet,doxod,5,"sprites/worker/worker3.png",None)
worker2=worker.Worker("sprites/worker/worker2_inv.png",250,180,[160,180],10000,chislo_monet,doxod,1,"sprites/worker/worker2.png",worker3)


