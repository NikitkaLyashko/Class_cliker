import pygame


import model,picture
pygame.init()
text=pygame.font.SysFont("Arial",50)
wind=pygame.display.set_mode([1500,700])
city=picture.Picture("sprites/place/place1.jpg",[1500,700],0,0)
woker=picture.Picture("sprites/worker/worker1.png",[160,160],150,500)












def view():
    city.draw(wind)
    woker.draw(wind)

    model.put_2.draw(wind)


    model.worker2.draw_worker(wind)


    model.chislo_monet.draw_text(wind)
    model.object_levl.draw_text(wind)
    model.upgrade.draw_text(wind)
    model.ceichas_mony.draw_text(wind)
    model.uvel_mony.draw_text((wind))
    model.doxod.draw_text(wind)





    pygame.display.flip()
