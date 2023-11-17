import pygame

print(type(pygame.image))
img = pygame.image.load('nature.png')
print(type(img))

screen = pygame.display.set_mode((650, 500))
white = (255, 255, 255)
screen.fill(white)

x, y = (0, 0)

while True:
    screen.fill(white)
    screen.blit(img, (x, y))
    x, y = x + 1, y + 1
    pygame.display .update()
    pygame.time.delay(10)
    pygame.event.pump()


