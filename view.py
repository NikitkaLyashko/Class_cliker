import pygame,round

import model,text as text_mod
pygame.init()
text=pygame.font.SysFont("Arial",50)
wind=pygame.display.set_mode([1500,700])
city = pygame.image.load("sprites/place/place1.jpg")
worker=pygame.image.load("sprites/worker/worker1.png")
button_up=pygame.image.load("sprites/controls/up_green.png")


city_big=pygame.transform.scale(city, [1500, 700])
worker_small=pygame.transform.scale(worker,[160,160])
place_green_button=pygame.transform.scale(button_up,[70,70])

text_money = "У вас " + str(model.money1) + " монет"

def view():
    wind.blit(city_big,[0,0])
    wind.blit(worker_small,[150,500])
    wind.blit(place_green_button,model.rect_green_button)
    print(model.money1)

    # wind.blit(text_mpney,[0,70])
    model.chislo_monet.draw_text(wind)


    text_levl_pers="Уровень "+str(model.levl)
    text_c=text.render(text_levl_pers,True,[250,0,0])
    wind.blit(text_c,[0,120])
    pygame.draw.rect(wind,[0,0,225],model.rect_green_button,3)

    # for view_krug in model.list_krug:
    #     view_krug.drow_round(wind)



    pygame.display.flip()
