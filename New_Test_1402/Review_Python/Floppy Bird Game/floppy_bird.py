# From Nabegheha.com/ https://github.com/nabeghehacom

import pygame
import sys

# All Variable
display_width = 900  # get yourself which number of pixel
display_hight = 680
floor_x = 0
#background_image = pygame.image.load('assets/img/bg2.png')
#floor_image = pygame.image.load('assets/img/floor.png')
background_image = pygame.transform.scale2x(pygame.image.load('assets/img/bg2.png'))
floor_image = pygame.transform.scale2x(pygame.image.load('assets/img/floor.png'))

# Game Display
main_screen = pygame.display.set_mode((display_width, display_hight))

# Start pygame Modules; All modules please be ready!:
pygame.init() 


# Game Timer
clock = pygame.time.Clock()

# Logic game:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # End pygame module
            pygame.quit()
            # Terminate Program
            sys.exit()
    # display background image
    main_screen.blit(background_image, (0, 0))
    # display floor image
    main_screen.blit(floor_image, (floor_x, 630))
    floor_x -= 1
    main_screen.blit(floor_image, (floor_x + 900, 630))
    if floor_x <= -900:
        floor_x = 0

    pygame.display.update()
    # Set Game Speed; 90
    clock.tick(90)   