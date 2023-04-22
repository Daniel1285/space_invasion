import pygame
import random
import time
from models.players import *
from models.EnemyShip import *
from database import *

pygame.font.init()
pygame.display.set_caption("Space invasion")

KILL = 0
LEVEL = 0

main_player = Player(535,600) # first location

def main():
    player = Player(535,600)

    run = True
    FPS = 60 # fram per sconde
    clock = pygame.time.Clock()
    count_down = 3

    # variable of player 
    killd = 0
    level = 0
    lives = 5  
    lost = False
    lost_count = 0
    
    movment = 7 # pixel of move player (left, rigth, up, down)
    pixel_health_bar = 20
    bonus = 0.1* player.health
    #font
    main_font = pygame.font.SysFont("comicsans", 50)
    local_font = pygame.font.SysFont("comicsans", 20)
    lost_font = pygame.font.SysFont("comicsans", 100)


    # variable of player 
    enemies = []
    wave_length = 1 # num of enemy ship evry wave
    enemy_val = 1 # speed of enemy
    leser_val = 5 # speed of laser

# ---------------------------------------------------------------------------------
    def redraw_window():
        WIN.blit(BG, (0,0))

        lives_label = main_font.render(f"lives: {lives}", 1, (255,255,255))
        level_lavel = main_font.render(f"level: {level}", 1, (255,255,255))
        kill_lavel = local_font.render(f"killd: {killd}", 1, (255,255,255))

        WIN.blit(lives_label, (10,10))
        WIN.blit(level_lavel, (WIDTH - level_lavel.get_width() -10 , 10))
        WIN.blit(kill_lavel, (WIDTH - kill_lavel.get_width() -10 , 50))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You lost!!", 1 , (255,0,0))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2 , 350))
        pygame.display.update()
# ---------------------------------------------------------------------------------


    
    while run:
        clock.tick(FPS)
        
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count+= 1
            

        if lost:
            if lost_count >= FPS*3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            player.level += 1
            if player.health + bonus < player.max_health:
                player.health +=  bonus
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - movment > 0: # left
            player.x -= movment
        if keys[pygame.K_RIGHT] and player.x + movment + player.get_width() < WIDTH: # riget
            player.x += movment
        if keys[pygame.K_UP] and player.y - movment > 0:   # up
            player.y -= movment
        if keys[pygame.K_DOWN] and player.y + movment + player.get_height() + pixel_health_bar < HEIGET : # down
            player.y += movment
        if keys[pygame.K_SPACE]:
            player.shoot()


        for enemy in enemies[:]:
            enemy.move(enemy_val)
            enemy.move_lasers(leser_val, player)

            if random.randrange(0,5*60) == 1:
                enemy.shoot()

            if  collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            elif enemy.y + enemy.get_height() > HEIGET:
                lives -= 1
                enemies.remove(enemy)


        player.move_lasers(-leser_val, enemies)

        killd = player.kill
        level = player.level

        main_player.kill = killd
        main_player.level = player.level


signup_button_rect = pygame.Rect(WIDTH/2 - 140 , 350, 120, 30)
signup_button_hover = False
signup_button_click = False  
login_button_hover = False
login_button_click = False

