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

bg = pygame.image.load('graphics/background.png')  
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT)) 

flappybird = pygame.image.load('graphics/bird.png')  
flappybird = pygame.transform.scale(flappybird, (PLAYER_WIDTH, PLAYER_HEIGHT)) 
flappybird_rect = flappybird.get_rect()
flappybird_rect.width = PLAYER_WIDTH - 10
flappybird_rect.height = PLAYER_HEIGHT - 10
flappybird_rect.center = [player_x, player_y]

screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
pygame.display.set_caption('Flappy bird')

speed = 3
score = 0
font = pygame.font.SysFont('Josefin Sans', 20)

colors = {
    "black": "#000000",
    "white": "#ffffff",
    "green": "#00cc00",
    "light_blue": "#6699ff",
    "yellow": "#ffff00",
    "orange": "#ff6600"
}