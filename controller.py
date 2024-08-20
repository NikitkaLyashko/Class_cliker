import pygame

import model,text


free_type = pygame.event.custom_type()

pygame.time.set_timer(free_type, 1000, 0)

def cotroller():
    events=pygame.event.get()
    model.put_2.controller(events)

    model.worker2.controller_worker(events)
    model.worker3.controller_worker(events)

    for event in events:

        if event.type == free_type:
            model.doxod_v_secundy()

        if event.type==pygame.QUIT:
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            model.chet_monet()