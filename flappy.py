import pygame

pygame.init()

screen = pygame.display.set_mode((288,512))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
