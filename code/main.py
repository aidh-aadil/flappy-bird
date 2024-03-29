from settings import *

pygame.init()

running = True
game_over = False

def draw_pipes(obst, y_pos, player):
    global game_over
    global game_over_sound_played
    for i in range(len(obst)):
        y_coord = y_pos[i]
        top_rect = pygame.draw.rect(screen, colors["green"], [obst[i], 0, 60, y_coord], 0, 5)
        bottom_rect = pygame.draw.rect(screen, colors["green"], [obst[i], y_coord + 200, 60, HEIGHT -(y_coord - 70)], 0, 5)
        if top_rect.colliderect(player) or bottom_rect.colliderect(player):
            game_over = True
            if not game_over_sound_played:
                game_over_sound.play()
                game_over_sound_played = True

while running:
    timer.tick(FPS)
    screen.fill(colors["black"])
    screen.blit(bg, (0,0))
    screen.blit(flappybird, (player_x, player_y))

    if generate_places:
        for i in range(len(pipes)):
            y_positions.append(random.randint(0, 400))
        
        generate_places = False

    draw_pipes(pipes, y_positions, flappybird_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE:
                y_change = -jump_height
                jump_sound.play()

    if player_y + y_change < HEIGHT - PLAYER_HEIGHT:
        player_y += y_change
        y_change += gravity
        flappybird_rect.center = [player_x, player_y]

    else: 
        player_y = HEIGHT - PLAYER_HEIGHT 
        flappybird_rect.center = [player_x, player_y]


    for i in range(len(pipes)):
        if not game_over:
            pipes[i] -= speed
            if pipes[i] < - 30:
                pipes.remove(pipes[i])
                y_positions.remove(y_positions[i])
                pipes.append(random.randint(pipes[-1] + 280, pipes[-1] + 320))
                y_positions.append(random.randint(0, 400))
                score += 1

    if game_over:
        game_over_text = game_over_font.render('Game over!', True, colors['black'])
        screen.blit(game_over_text, (WIDTH / 2 - 130, HEIGHT / 2 - 20))

    score_text = font.render('Score: ' + str(score), True, colors['black'])
    screen.blit(score_text, (20, 30))

    pygame.display.flip()      

pygame.quit() 
sys.exit() 