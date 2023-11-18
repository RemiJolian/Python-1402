# events in pygame

# Run every block separately

# -----------------------------------------------------#

## QUIT EVENT

# import pygame
# pygame.init()

# screen = pygame.display.set_mode((800, 600))

# blue = (0, 0, 255)
# pink = (255, 0, 255)
# is_blue = True

# screen.fill(blue)
# pygame.display.update()

# while True:
#     event = pygame.event.wait() # wait until an event happen, then export it
#     if event.type == pygame.QUIT:
#         if is_blue == True:
#             screen.fill(pink)
#             is_blue = False

#         else:
#             screen.fill(blue)
#             is_blue = True

#         pygame.display.update()
#         print('Quit Event!')


# -----------------------------------------------------#

# # KEYDOWN EVENT

# import pygame

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# blue = (0, 255, 255)
# pink = (255, 0, 255)
# is_blue = True
# screen.fill(blue)
# pygame.display.update()
# while True:
#     event = pygame.event.wait()
#     if event.type == pygame.KEYDOWN:
#         if is_blue is True:
#             screen.fill(pink)
#             is_blue = False
#         else:
#             screen.fill(blue)
#             is_blue = True
#         pygame.display.update()
#         print('Key Down Event!')
#         print(f"Key Code is : {event.key}")
#         print(f"Key Unicode is : {event.unicode}")
#     if event.type == pygame.QUIT:
#         pygame.quit()
#         break

# --------------------------------------------------- #

# KEYUP EVENT


# import pygame
# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))

# blue = (0, 255, 255)
# pink = (255, 0, 255)
# is_blue = True

# screen.fill(blue)

# pygame.display.update()

# while True:
#     event = pygame.event.wait()
#     if event.type == pygame.KEYUP:
#         if is_blue is True:
#             screen.fill(pink)
#             is_blue = False
#         else:
#             screen.fill(blue)
#             is_blue = True
#         pygame.display.update()
#         print('Key Up Event!')
#         print(f"Key Code is : {event.key}")
#         print(f"Key Unicode is : {event.unicode}")

#     if event.type == pygame.QUIT:
#         pygame.quit()
#         break


# -------------------------------------------------------#

# MOUSEBOTTONDOWN and MOUSEBOTTONUP EVENTs

# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))

# blue = (0, 255, 255)
# pink = (255, 0, 255)
# is_blue = True

# screen.fill(blue)

# pygame.display.update()

# while True:
#     event = pygame.event.wait()
#     if event.type == pygame.MOUSEBUTTONDOWN: # or .MOUSEBOTTONDOWN
#         if is_blue is True:
#             screen.fill(pink)
#             is_blue = False
#         else:
#             screen.fill(blue)
#             is_blue = True
#         pygame.display.update()
#         print('Mouse Button Down Event!')
#         print(f"Key Position is : {event.pos}")
#         print(f"Key Button is : {event.button}")

#     if event.type == pygame.QUIT:
#         pygame.quit()
#         break


# ------------------------------------------------------------------ #\

# MOUSEMOTION EVENT

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

blue = (0, 255, 255)
red = (255, 0, 0)
is_blue = True
screen.fill(blue)
pygame.display.update()
while True:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEMOTION:
        if is_blue is True:
            screen.fill(red)
            is_blue = False
        else:
            screen.fill(blue)
            is_blue = True
        pygame.display.update()
        print('Mouse Motion Event!')
        print(f"Key Position is : {event.pos}")
        print(f"Key Button is : {event.rel}")

    if event.type == pygame.QUIT:
        pygame.quit()
        break