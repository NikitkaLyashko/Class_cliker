import random

import pygame.display,round,text


chislo_monet=text.Text(0, 70, 0,"У вас ","монет ")
object_levl=text.Text(0,120,1,"Уровень ","")
upgrade=text.Text(0,20,10,"Для улучшения надо столько: ","")
ceichas_mony=text.Text(0,170,2,"За клик столько:","")
uvel_mony=text.Text(0,220,1,"ЗА апгрейд столько:","")
level_2=text.Text(350,380,0,"Уровеь:","",25)


rect_green_button=pygame.Rect(70,70,70,70)
rect_green_button.center=[1450,50]

def chet_monet():

    chislo_monet.chislo+=ceichas_mony.chislo





def chet_yrovn(collide):
    button_pos = rect_green_button.collidepoint(collide)
    if button_pos == True and chislo_monet.chislo >=upgrade.chislo:

        chislo_monet.chislo -= upgrade.chislo
        upgrade.chislo *=1.05
        object_levl.chislo+=1

        ceichas_mony.chislo+=uvel_mony.chislo
        uvel_mony.chislo += 1





# list_krug=[]
# #
# # object_2=round.Round(1,100,500)
# # object_2.plus_10()
# # object_2.plus_10()
# #
# object_3=round.Round(50,350,700)
# object_3.plus_a(3)
#
# for krug in range(40):
#     object_2 = round.Round(random.randint(5,100), random.randint(0,1000), random.randint(0,1000),list_krug)
#     object_2.plus_10()
#
#
#     list_krug.append(object_2)




#
#
# def model_ride_round():
#     for ride_krug in list_krug:
#         ride_krug.ride_round()

