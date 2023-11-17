# Review of pygame, and a make game project; Quera

import pygame
from math import pi

pygame.init()
screen = pygame.display.set_mode((800, 600))

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
gray = (128, 128, 128)
purple = (128, 0, 128)
white = (255, 255, 255)

pygame.font.Font(None, 240)

# BACKGROUND COLOR OF SCREEN
screen.fill(gray)
# DRAW A LINE
pygame.draw.line(screen, green, (300, 300), (600, 400))
# DRAW A CIRCLE
pygame.draw.circle(screen, red, (50, 50), 25, 6) # NUM 6 IS THICKNESS OF CIRCLE(OR FONT)
# DRAW AN ELLIPSE
pygame.draw.ellipse(screen, purple, (455, 455, 100, 50))
#DRAW A RECTANGLE
pygame.draw.rect(screen, blue, (400, 400, 30, 60))
# DRAW A POLYGON
pygame.draw.polygon(screen, green, [(700, 500), (600, 500), (550, 450), (650, 440)])
# DRAW LINES, IF "TRUE" 2 END OF LINES WILL CONNECT
pygame.draw.lines(screen, red, True, [(500, 200), (400, 200), (350, 150), (450, 140)]) 
pygame.draw.lines(screen, green, False, [(350, 250), (250, 250), (200, 200), (300, 190)])
# DRAW AN ARC;
# when you draw a arc, you need draw it on a assumptive rectangle
pygame.draw.rect(screen, green, (65, 80, 85, 120)) # this line not need.IT IS  for test.
pygame.draw.arc(screen, red, (65, 80, 85, 120), 3*pi/2, 2*pi)

pygame.display.update()

while True:
    pygame.event.pump()








# AFTER RUN THE FILE, IN CMD, CLOSE IT BY CTL+C

