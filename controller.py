import pygame

import model


def cotroller():
    events=pygame.event.get()

    for event in events:
        if event.type==pygame.QUIT:
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            model.money1+=2
            button_pos=model.rect_green_button.collidepoint(event.pos)
            if button_pos==True:
                model.levl+=1
                print(model.levl)





