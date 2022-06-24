import pygame

pygame.init() 
background=pygame.image.load("backgound.2.png")
icon=pygame.image.load("icon.png")

screen =pygame.display.set_mode((800,600))
pygame.display.set_caption('spaceinvader')
while True:
    
    screen.blit(background,(0 ,0))
    pygame.display.update()

 #this part runs the whole program

if __name__=='__main__':
    pass
