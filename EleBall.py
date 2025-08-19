import pygame
from pygame import*
import sys
import random

init()
window = display.set_mode((700,650))
clock = time.Clock()

bg_img = image.load("forest.png").convert()
bg_img = transform.scale(bg_img, (700, 650))

name_img = image.load("name.png").convert_alpha()
name_img = transform.scale(name_img,(280,230))
name_rect = name_img.get_rect(topleft=(170, 30))

ball_img = image.load("ball.png").convert_alpha()
ball_img = transform.scale(ball_img,(320,360))
ball_rect = ball_img.get_rect(topleft=(0, 200))

start_img = image.load("start.png").convert_alpha()
start_img = transform.scale(start_img,(240,240))

enemyf_img = image.load("enemyf.png").convert_alpha()
enemyf_img = transform.scale(enemyf_img,(210,310))

enemya_img = image.load("enemya.png").convert_alpha()
enemya_img = transform.scale(enemya_img,(210,210))


chose_img = image.load("chose.png").convert_alpha()
chose_img = transform.scale(chose_img,(480,140))

btn_img = image.load("voda.png").convert_alpha()
btn_img = transform.scale(btn_img, (220, 140))

sea_img =  image.load("sea.png").convert()
sea_img = transform.scale(sea_img, (700, 650))

playersea_img = image.load("ball.png").convert_alpha()
playersea_img = transform.scale(playersea_img, (200, 240))
playersea_rect  = playersea_img.get_rect(center=(350, 695))

rock_img = image.load("rock.png").convert_alpha()
rock_img = transform.scale(rock_img,(150,70))
rocks = []

btn1_img = image.load("fire.png").convert_alpha()
btn1_img = transform.scale(btn1_img,(220,140))



start_btn = Rect(150,200,100,80)
start_btn.x = 230
start_btn.y = 250

voda_btn = Rect(150, 200, 100, 60)
voda_btn.x = 240
voda_btn.y = 100

fire_btn = Rect(150,200,200,60)
fire_btn.x = 240
fire_btn.y = 250

game_started = False
current_location = "menu"

ball_y_offset = 0
ball_direction = 1

enemy_y_offset = 0
enemy_direction = 1

enemy1_x_offset = 0
enemy1_direction = 1

chose_y_offset = 0
chose_direction = 1

playersea_speed = 5
playersea_gravity = 0
on_ground = True
scroll_x = 0

while True:
    mouse_pos = mouse.get_pos()
    for e in event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
        if not game_started:
            if e.type == MOUSEBUTTONDOWN and start_btn.collidepoint(e.pos):
                print("Гра почалась!")
                game_started = True
        else:
            if e.type == MOUSEBUTTONDOWN and voda_btn.collidepoint(e.pos):
                print("Вибрана вода!")
                current_location = "sea"
            if e.type == MOUSEBUTTONDOWN and fire_btn.collidepoint(e.pos):
                print("Вибраний вогонь")
                current_location = "fire"

    ball_y_offset += ball_direction
    if ball_y_offset > 15 or ball_y_offset < -20:
        ball_direction *= -1

    enemy_y_offset += enemy_direction
    if enemy_y_offset > 5 or enemy_y_offset < -5:
        enemy_direction *= -1

    enemy1_x_offset += enemy1_direction
    if enemy1_x_offset > 25 or enemy1_x_offset < -30:
        enemy1_direction *= -1

    chose_y_offset += chose_direction
    if chose_y_offset > 5 or chose_y_offset < -10:
        chose_direction *= -1


    if current_location == "sea":
        keys = pygame.key.get_pressed()


        if keys[K_LEFT]:
            playersea_rect.x -= playersea_speed
        if keys[K_RIGHT]:
            playersea_rect.x += playersea_speed
        if on_ground and keys[K_SPACE]:
            playersea_gravity = -25
            on_ground = False

        # --- Гравитация ---
        playersea_rect.y += playersea_gravity
        playersea_gravity += 1

        # Не падаем ниже "земли"
        if playersea_rect.bottom >= 695:
            playersea_rect.bottom = 695
            playersea_gravity = 0
            on_ground = True


        scroll_x -= playersea_speed // 2
        rel_x = scroll_x % sea_img.get_width()
        window.blit(sea_img, (rel_x - sea_img.get_width(), 0))
        window.blit(sea_img, (rel_x, 0))
        if rel_x < 700:
            window.blit(sea_img, (rel_x + sea_img.get_width(), 0))


        if random.randint(1, 60) == 1:
            rock_rect = rock_img.get_rect(midbottom=(800, 665))
            rocks.append(rock_rect)
        for rock in rocks[:]:
            rock.x -= playersea_speed
            window.blit(rock_img, rock)
            if playersea_rect.colliderect(rock):
                if playersea_rect.bottom <= rock.top + 5 and playersea_gravity >= 0:
                    playersea_rect.bottom = rock.top
                    on_ground = True
                    playersea_gravity = 0
                elif playersea_rect.right > rock.left and playersea_rect.left < rock.left:
                    playersea_rect.right = rock.left
                elif playersea_rect.left < rock.right and playersea_rect.right > rock.right:
                    playersea_rect.left = rock.right
            if rock.right < 0:
                rocks.remove(rock)

        window.blit(playersea_img, playersea_rect)

    if not game_started:
            window.blit(bg_img, (0, 0))
            window.blit(name_img, (210, 50))
            window.blit(ball_img,(5, 340 + ball_y_offset))
            window.blit(enemyf_img,(460,320 + enemy_y_offset))
            window.blit(enemya_img, (5 + enemy1_x_offset , 5))
            if start_btn.collidepoint(mouse_pos):
                window.blit(transform.scale(start_img, (240, 240)), (start_btn.x - 5, start_btn.y - 5))
            else:
                window.blit(start_img, (start_btn.x, start_btn.y))
    else:
            if current_location == "menu":
                window.blit(bg_img, (0, 0))
                window.blit(chose_img, (120, 5 + chose_y_offset))
                if voda_btn.collidepoint(mouse_pos):
                    window.blit(transform.scale(btn_img, (210, 130)), (voda_btn.x - 5, voda_btn.y - 4))
                else:
                    window.blit(btn_img, (voda_btn.x, voda_btn.y))

                if fire_btn.collidepoint(mouse_pos):
                    window.blit(transform.scale(btn1_img, (210, 130)), (fire_btn.x - 5, fire_btn.y - 4))
                else:
                    window.blit(btn1_img, (fire_btn.x, fire_btn.y))

    display.update()
    clock.tick(60)
