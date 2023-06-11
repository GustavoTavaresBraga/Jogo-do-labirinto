import pygame
import random
from config import WIDTH, HEIGHT, INITIAL, PLAYING, END
from init_screen import init_screen
from game_screen import game_screen

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')

state = INITIAL
while state != END:
    if state == INITIAL:
        state = init_screen(window)
    elif state == PLAYING:
        state = game_screen(window)
    else:
        state = END

pygame.quit() 