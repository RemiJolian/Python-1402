# Quera quiz: Terminale Grafic
import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Python Test Window')

blue = (0, 0, 255)
red = (255, 0, 0)

turn = 0
while True:
    pygame.event.pump()

    if turn == 0:
        screen.fill(red)
    else:
        screen.fill(blue)
    turn = 1 - turn
    pygame.display.update()
    pygame.time.delay(550)
    