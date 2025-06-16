import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line ALgorithm")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def plot(x, y, xc, yc):
    screen.set_at((round(xc + x), round(yc + y)), WHITE)
    screen.set_at((round(xc + x), round(yc - y)), WHITE)
    screen.set_at((round(xc - x), round(yc + y)), WHITE)
    screen.set_at((round(xc - x), round(yc - y)), WHITE)

def midpoint_ellipse(rx, ry, xc, yc):
    x = 0
    y = ry

    # Initial decision parameter for region 1
    p1 = (ry**2) - (rx**2 * ry) + (0.25 * rx**2)
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y

    plot(x, y, xc, yc)

    # Region 1
    while dx < dy:
        x += 1
        dx = 2 * ry**2 * x

        if p1 < 0:
            p1 += dx + ry**2
        else:
            y -= 1
            dy = 2 * rx**2 * y
            p1 += dx - dy + ry**2

        plot(x, y, xc, yc)

    # Initial decision parameter for region 2
    p2 = (ry**2) * (x + 0.5)**2 + (rx**2) * (y - 1)**2 - (rx**2 * ry**2)

    # Region 2
    while y > 0:
        y -= 1
        dy = 2 * rx**2 * y

        if p2 > 0:
            p2 += rx**2 - dy
        else:
            x += 1
            dx = 2 * ry**2 * x
            p2 += dx - dy + rx**2

        plot(x, y, xc, yc)

def main():
    # rx = int(input("Enter major axis (rx): "))
    # ry = int(input("Enter minor axis (ry): "))
    # xc = int(input("Enter x-coordinate of center: "))
    # yc = int(input("Enter y-coordinate of center: "))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        midpoint_ellipse(100, 50, WIDTH/2, HEIGHT/2)
        pygame.display.flip()

if __name__ == "__main__":
    main()