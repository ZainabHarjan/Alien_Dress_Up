import pygame
import sys
import os

pygame.init()

#window stuffs
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

#character stuffs
character = pygame.image.load('randomguy.png')
character_rect = character.get_rect()
window_halfw = window.width/2
window_halfh = window.height/2
character_rect.center = (window_halfw, window_halfh)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False       
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    window.fill('white')
    window.blit(character, character_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()
