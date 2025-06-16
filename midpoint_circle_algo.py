import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint circle ALgorithm")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Implementation of midpoint Circle algorithm 
def point (xc,yc,x,y):
    screen.set_at((round (x+xc),round (y+yc)),WHITE)
    screen.set_at((round (x+xc),round (-y+yc)),WHITE)
    screen.set_at((round (-x+xc),round (y+yc)),WHITE)
    screen.set_at((round (-x+xc),round (-y+yc)),WHITE)
    screen.set_at((round (y+xc),round (x+yc)),WHITE)
    screen.set_at((round (y+xc),round (-x+yc)),WHITE)
    screen.set_at((round (-y+xc),round (x+yc)),WHITE)
    screen.set_at((round (-y+xc),round (-x+yc)),WHITE)

def midpoint_circle (xc,yc,r):
    d=1-r
    x=0
    y=r
    point(xc,yc,x,y)
    while(x<=y):
        if (d<0):
            x=x+1
            y=y
            d=d+2*x+1
        else:
            x=x+1
            y=y-1
            d=d+2*x-2*y+1
        point(xc,yc,x,y)
        


def main():
    while True :
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            screen.fill(BLACK)
            midpoint_circle (300,200,80)
            midpoint_circle (300,200,70)
            midpoint_circle (300,200,60)
            midpoint_circle (300,200,50)
            midpoint_circle (300,200,40)
            midpoint_circle (300,200,30)
            midpoint_circle (300,200,20)
            midpoint_circle (300,200,10)

            pygame.display.update()
            
if __name__ == "__main__":
    main()
        
    