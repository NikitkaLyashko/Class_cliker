import pygame,time,model,view,controller

while True:

    time.sleep(1/60)
    view.view()
    controller.cotroller()
    model.model_ride_round()