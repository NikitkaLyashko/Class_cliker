import random

import pygame.display,round,text

money1=0
levl=1

chislo_monet=text.Text(0, 70, money1)

rect_green_button=pygame.Rect(70,70,70,70)
rect_green_button.center=[1450,50]

# print(rect_green_button)




list_krug=[]
#
# object_2=round.Round(1,100,500)
# object_2.plus_10()
# object_2.plus_10()
#
# object_3=round.Round(50,350,700)
# object_3.plus_a(3)

for krug in range(40):
    object_2 = round.Round(random.randint(5,100), random.randint(0,1000), random.randint(0,1000),list_krug)
    object_2.plus_10()


    list_krug.append(object_2)






def model_ride_round():
    for ride_krug in list_krug:
        ride_krug.ride_round()

