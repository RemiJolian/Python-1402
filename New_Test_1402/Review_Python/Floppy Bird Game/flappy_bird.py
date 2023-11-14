# From Nabegheha.com/ https://github.com/nabeghehacom

import pygame
import sys
import random
# Start pygame Modules; All modules please be ready!:
pygame.init() 

def generate_pipe_rect():
    random_pipe = random.randrange(150, 350)
    pipe_rect_top = pipe_image.get_rect(midbottom=(700, random_pipe - 200))
    pipe_rect_bottom = pipe_image.get_rect(midtop=(700, random_pipe)) 
    return pipe_rect_top, pipe_rect_bottom

def move_pipe_rect(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    inside_pipes = [pipe for pipe in pipes if pipe.right > -50 ]
    return inside_pipes

def display_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 500:
            main_screen.blit(pipe_image, pipe)
        else:
            reversed_pipes = pygame.transform.flip(pipe_image, False, True)
            main_screen.blit(reversed_pipes, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_image_rect.colliderect(pipe):
            return False
        if bird_image_rect.top < -50 or bird_image_rect.bottom >= 400:
            return False
    return True
def bird_animition()   :
    new_bird = bird_list[bird_list_index]
    new_bird_rect = new_bird.get_rect(center=(50, bird_image_rect.centery  ))
    return new_bird, new_bird_rect

def display_score():
    text1 = game_font.render(str(score), False, (255, 255, 255))
    text1_rect = text1.get_rect(center=(288, 100))
    main_screen.blit(text1, text1_rect)

# All Variable
display_width = 500  # get yourself which number of pixel
display_hight = 500
floor_x = 0
gravity = 0.25
bird_movement = 0
pipe_list = []
game_status = True
bird_list_index = 0
game_font = pygame.font.Font('assets/font/Flappy.TTF', 40)
score = 0
# ----------------#
create_pipe = pygame.USEREVENT
create_flap = pygame.USEREVENT + 1
pygame.time.set_timer(create_pipe, 1200) # 1200 mili secend
pygame.time.set_timer(create_flap, 200) 
#------------------#
background_image = pygame.transform.scale2x(pygame.image.load('assets/img/bg2.png'))
floor_image = pygame.transform.scale2x(pygame.image.load('assets/img/floor.png'))

bird_image_down = pygame.transform.scale2x(pygame.image.load('assets/img/red_bird_down_flap.png'))
bird_image_mid = pygame.transform.scale2x(pygame.image.load('assets/img/red_bird_mid_flap.png'))
bird_image_up = pygame.transform.scale2x(pygame.image.load('assets/img/red_bird_up_flap.png'))

bird_list = [bird_image_up, bird_image_mid, bird_image_down]

bird_image = bird_list[bird_list_index]
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
            if event.key == pygame.K_r and game_status == False:
                game_status = True
                pipe_list.clear()
                bird_image_rect.center = (50, 250)
                bird_movement = 0

        if event.type == create_pipe:
            pipe_list.extend(generate_pipe_rect())
        if event.type == create_flap:
            if bird_list_index < 2:
                bird_list_index += 1
            else:
                bird_list_index = 0

            bird_image, bird_image_rect = bird_animition()
    # Display background image
    main_screen.blit(background_image, (0, 0))

    if game_status:
        # Display Bird Image
        main_screen.blit(bird_image, bird_image_rect)
        # check for collision
        game_status = check_collision(pipe_list)
        # move pipes
        pipe_list = move_pipe_rect(pipe_list)
        display_pipes(pipe_list)
        #floor gravity and bird movement
        bird_movement += gravity
        bird_image_rect.centery += bird_movement
        #show score
        display_score()

    # display floor image
    floor_x -= 1
    main_screen.blit(floor_image, (floor_x, 450))
    main_screen.blit(floor_image, (floor_x + 500, 450))
    if floor_x <= -500:
        floor_x = 0

    pygame.display.update()
    # Set Game Speed; 90
    clock.tick(90)   