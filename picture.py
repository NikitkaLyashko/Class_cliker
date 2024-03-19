import pygame
class Picture():
    def  __init__(self,put_k_file,size,x,y):
        self.put=put_k_file
        self.size2=size
        self.x=x
        self.y=y



    def draw(self,place:pygame.Surface):
        self.pict=pygame.image.load(self.put)

        self.object1=pygame.transform.scale(self.pict,self.size2)

        place.blit(self.object1,[self.x,self.y])


