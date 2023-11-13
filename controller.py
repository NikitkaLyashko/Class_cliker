import pygame

import model


def cotroller():
    events=pygame.event.get()

    for event in events:
        if event.type==pygame.QUIT:
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            model.money1+=2
