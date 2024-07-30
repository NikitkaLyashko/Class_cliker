import pygame

import model,text


free_type = pygame.event.custom_type()

pygame.time.set_timer(free_type, 1000, 0)

def cotroller():
    events=pygame.event.get()
    model.button_2.controller(events)
    model.put_2.controller(events)
    model.put_3.controller(events)

    model.worker2.controller_worker(events)
    model.worker3.controller_worker(events)

    for event in events:

        if event.type == free_type:
            model.doxod_v_secundy()

        if event.type==pygame.QUIT:
            exit()


        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            model.object_3.color="красный"

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            model.object_3.color = "синий"

        if event.type==pygame.MOUSEBUTTONDOWN:
            model.chet_monet()
            # model.object_3.color="синий



# pygame.time.set_timer(free_type,3000,0)
#
#
#
# def controller():
#
#     event=pygame.event.get()
#
#
#     for cobitie in event:
#
#         if cobitie.type==free_type:
#             random_bool=random.randint(int(False),int(True))