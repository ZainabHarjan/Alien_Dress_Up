import pygame
import sys
import os

pygame.init()

#window stuffs
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

#way to move on
current_level = 0;


#character stuffs
character = pygame.image.load('randomguy.png')
character_rect = character.get_rect()
window_halfw = window.width/2
window_halfh = window.height/2
character_rect.center = (window_halfw, window_halfh)

#clothes stuffs
sweater = pygame.image.load('sweater.png')
sweater = pygame.transform.scale(sweater, (130, 140))
sweater_rect = sweater.get_rect()
sweater_rect.right = (window_halfw)
pants = pygame.image.load('pants.png')
pants = pygame.transform.scale(pants, (130, 140))
pants_rect = pants.get_rect()

#next button stuff
next = pygame.image.load('next.png')
next = pygame.transform.scale(next, (200, 150))
next_rect = next.get_rect()
next_rect.center = (window_halfw + 200, window_halfh)

def add_clothing(cloth_rect):
   if event.type == pygame.MOUSEBUTTONDOWN:
           if cloth_rect.collidepoint(event.pos):
            cloth_rect.center = (window_halfw - 5, window_halfh - 80)

def next_function(next_button, current_level):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if next_button.collidepoint(event.pos):
            current_level = current_level + 1
            print(current_level)
            

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False       
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        next_function(next_rect, current_level)
        if current_level == 0:
            add_clothing(sweater_rect)
        if current_level == 1:
            add_clothing(pants_rect)

    

    window.fill('white')
    window.blit(character, character_rect)
    window.blit(pants, pants_rect)
    window.blit(sweater, sweater_rect)
    window.blit(next, next_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()
