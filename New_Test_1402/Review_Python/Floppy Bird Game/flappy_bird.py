# From Nabegheha.com/ https://github.com/nabeghehacom

import pygame
import sys
import random
# Start pygame Modules; All modules please be ready!:
pygame.init() 

def generate_pipe_rect():
    random_pipe = random.randrange(200, 350)
    pipe_rect = pipe_image.get_rect(midtop=(700, random_pipe))
    return pipe_rect

def move_pipe_rect(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    inside_pipes = [pipe for pipe in pipes if pipe.right > -50 ]
    return inside_pipes

def display_pipes(pipes):
    for pipe in pipes:
        main_screen.blit(pipe_image, pipe)

# All Variable
display_width = 500  # get yourself which number of pixel
display_hight = 500
floor_x = 0
gravity = 0.25
bird_movement = 0
pipe_list = []

# ----------------#
create_pipe = pygame.USEREVENT
pygame.time.set_timer(create_pipe, 1200) # 1200 mili secend
#------------------#
background_image = pygame.transform.scale2x(pygame.image.load('assets/img/bg2.png'))
floor_image = pygame.transform.scale2x(pygame.image.load('assets/img/floor.png'))
bird_image = pygame.transform.scale2x(pygame.image.load('assets/img/red_bird_mid_flap.png'))
pipe_image = pygame.transform.scale2x(pygame.image.load('assets/img/pipe_red.png'))

# -------------------------------------------#
bird_image_rect = bird_image.get_rect(center=(50, 250))
# Game Display
main_screen = pygame.display.set_mode((display_width, display_hight))



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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 8
        if event.type == create_pipe:
            pipe_list.append(generate_pipe_rect())
    # display background image
    main_screen.blit(background_image, (0, 0))
    # Display Bird Image
    main_screen.blit(bird_image, bird_image_rect)
    # move pipes
    pipe_list = move_pipe_rect(pipe_list)
    display_pipes(pipe_list)
    #floor gravity and bird movement
    bird_movement += gravity
    bird_image_rect.centery += bird_movement
    # display floor image
    floor_x -= 1
    main_screen.blit(floor_image, (floor_x, 450))
    main_screen.blit(floor_image, (floor_x + 500, 450))
    if floor_x <= -500:
        floor_x = 0

    pygame.display.update()
    # Set Game Speed; 90
    clock.tick(90)   