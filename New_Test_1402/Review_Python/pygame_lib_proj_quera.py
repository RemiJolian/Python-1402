# Queiz Quera: Terminale Grafic

import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

screen.fill(white)

# CHANGE COLOR OF PEN
# .....
# CHANGE FONT SIZE
pygame.font.Font(None, 11)
# DRAW LINE
pygame.draw.line(screen, green, (300, 300), (600, 400), 10)
# DRAW A CIRCLE
pygame.draw.circle(screen, red, (200, 200), 5, 7)
# DRAW A POLYGON
pygame.draw.line(screen, green, (300, 300), (600, 400))
# SAVE THE FILE 

while True:
    pygame.event.pump()  
    pygame.image.save(screen, 'draw.png')
    break
# END THE PROGRAM
pygame.quit()