import pygame

import model,text


def cotroller():
    events=pygame.event.get()
    model.button_2.controller(events)
    model.put_2.controller(events)



    for event in events:
        if event.type==pygame.QUIT:
            exit()

        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            model.object_3.color="красный"

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            model.object_3.color = "синий"

        if event.type==pygame.MOUSEBUTTONDOWN:
            model.chet_monet()
            # model.object_3.color="синий



