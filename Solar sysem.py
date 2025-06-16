import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 1200, 1300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint circle ALgorithm")
WHITE = (255, 255, 25)
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
               # Neptune
        midpoint_circle(600, 500, 450)
        midpoint_circle(800, 90, 30)

        # Uranus
        midpoint_circle(600, 500, 400)
        midpoint_circle(500, 120, 30)

        # Saturn
        midpoint_circle(600, 500, 350)
        midpoint_circle(800, 210, 30)

        # Jupiter
        midpoint_circle(600, 500, 300)
        midpoint_circle(400, 280, 30)

        # Mars
        midpoint_circle(600, 500, 250)
        midpoint_circle(700, 270, 30)

        # Earth
        midpoint_circle(600, 500, 200)
        midpoint_circle(500, 320, 30)

        # Venus
        midpoint_circle(600, 500, 150)
        midpoint_circle(500, 600, 30)

        # Mercury
        midpoint_circle(600, 500, 100)
        midpoint_circle(600, 600, 30)
        pygame.display.update()
            
if __name__ == "__main__":
    main()
        
    