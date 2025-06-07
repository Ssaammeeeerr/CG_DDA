import pygame
import sys 
pygame.init()
width,height =800,600
screen= pygame.display.set_mode((width,height))
pygame.display.set_caption("DDA Algorithm")
white=(255,255,255)
black=(0,0,0)
def ds(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if dx>dy:
        step=dx
    else :
        step=dy
    xin=dx/step
    yin=dy/step
    x=x1
    y=y1
    for x in range(step):
        x=x+xin
        y=y+yin
        screen.set_at((round(x),round(y)),white)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.fill(black)
        ds(200,300,200,230)
        pygame.display.update()

if __name__=="__main""__":
    main()