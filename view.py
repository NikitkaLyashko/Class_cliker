import pygame

import model
pygame.init()
text=pygame.font.SysFont("Arial",50)
wind=pygame.display.set_mode([1500,700])
city = pygame.image.load("sprites/place/place1.jpg")
worker=pygame.image.load("sprites/worker/worker1.png")


city_big=pygame.transform.scale(city, [1500, 700])
worker_small=pygame.transform.scale(worker,[160,160])
def view():
    wind.blit(city_big,[0,0])
    wind.blit(worker_small,[150,500])
    text_money = "У вас " + str(model.money1) + " монет"
    text_mpney=text.render(text_money,True,[250,0,0])
    wind.blit(text_mpney,[0,70])



    pygame.display.flip()
