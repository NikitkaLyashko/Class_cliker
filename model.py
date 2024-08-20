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


chislo_monet=text.Text(0, 70, 10000000,"У вас ","монет ")
object_levl=text.Text(0,120,1,"Уровень ","")
upgrade=text.Text(0,20,10,"Для улучшения надо столько: ","")
ceichas_mony=text.Text(0,170,2,"За клик столько:","")
uvel_mony=text.Text(0,220,1,"ЗА апгрейд столько:","")
doxod=text.Text(700,50,0,"Доход:","",60)
put_2=knopka.Knopka(1400,0,[100,100],"sprites/controls/up_green.png",work_button)
worker3=worker.Worker("sprites/worker/worker3_inv.png",500,500,[160,180],50000,chislo_monet,doxod,5,"sprites/worker/worker3.png",None)
worker2=worker.Worker("sprites/worker/worker2_inv.png",350,500,[160,180],10000,chislo_monet,doxod,1,"sprites/worker/worker2.png",worker3)


