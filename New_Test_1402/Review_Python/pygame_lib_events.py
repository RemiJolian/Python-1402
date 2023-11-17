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
#     event = pygame.event.wait()
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


import pygame
