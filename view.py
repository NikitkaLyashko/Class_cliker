import pygame,round

import knopka
import model,text as text_mod,picture
pygame.init()
text=pygame.font.SysFont("Arial",50)
wind=pygame.display.set_mode([1500,700])
city=picture.Picture("sprites/place/place1.jpg",[1500,700],0,0)
woker=picture.Picture("sprites/worker/worker1.png",[160,160],150,500)
button_up=picture.Picture("sprites/controls/up_green.png",[70,70],model.rect_green_button.x,model.rect_green_button.y)
woker2=picture.Picture("sprites/worker/worker2_inv.png",[160,180],250,380)










def view():
    city.draw(wind)
    woker.draw(wind)
    button_up.draw(wind)
    woker2.draw(wind)
    model.put_2.draw((wind))
    model.button_2.draw(wind)






    model.chislo_monet.draw_text(wind)
    model.object_levl.draw_text(wind)
    model.upgrade.draw_text(wind)
    model.ceichas_mony.draw_text(wind)
    model.uvel_mony.draw_text((wind))
    model.level_2.draw_text(wind)
    # model.object_3.drow_round(wind)



    pygame.display.flip()
