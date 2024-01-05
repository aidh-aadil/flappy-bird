import pygame
import random

pygame.font.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 40

player_x = 150
player_y = 300

y_change = 0
jump_height = 10
gravity = 1

pipes = [400, 700, 1000, 1300, 1600]
generate_places = True
y_positions = []

bg = pygame.image.load('graphics/bg.png')  
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT)) 

flappybird = pygame.image.load('graphics/flappybird.png')  
flappybird = pygame.transform.scale(flappybird, (PLAYER_WIDTH, PLAYER_HEIGHT)) 
flappybird_rect = flappybird.get_rect()
flappybird_rect.center = [player_x, player_y]

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
pygame.display.set_caption('Flappy bird')

game_over = False
speed = 3
score = 0
font = pygame.font.SysFont('Josefin Sans', 20)

def draw_pipes(obst, y_pos, player):
    global game_over
    for i in range(len(obst)):
        y_coord = y_pos[i]
        top_rect = pygame.draw.rect(screen, colors["green"], [obst[i], 0, 60, y_coord], 0, 5)
        bottom_rect = pygame.draw.rect(screen, colors["green"], [obst[i], y_coord + 200, 60, HEIGHT -(y_coord - 70)], 0, 5)
        if top_rect.colliderect(player) or bottom_rect.colliderect(player):
            game_over = True

colors = {
    "black": "#000000",
    "white": "#ffffff",
    "green": "#00cc00",
    "light_blue": "#6699ff",
    "yellow": "#ffff00",
    "orange": "#ff6600"
}