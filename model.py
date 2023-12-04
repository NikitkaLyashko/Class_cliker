import pygame.display,round

money1=0
levl=1

rect_green_button=pygame.Rect(70,70,70,70)
rect_green_button.center=[1450,50]

print(rect_green_button)

object_1=round.Round(70,300,400)
object_1.plus_10()

object_2=round.Round(1,100,500)
object_2.plus_10()
object_2.plus_10()

object_3=round.Round(50,350,700)
object_3.plus_a(3)

def model_ride_round():
    object_3.ride_round()
    object_2.ride_round()
    object_1.ride_round()
print(object_3.a)
