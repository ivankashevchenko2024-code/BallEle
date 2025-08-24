from pygame import *

init()
window = display.set_mode((700,650))
clock = time.Clock()

bg_img = image.load("img/backgrounds/forest.png").convert()
bg_img = transform.scale(bg_img, (700, 650))

name_img = image.load("img/ui/name.png").convert_alpha()
name_img = transform.scale(name_img,(280,230))
name_rect = name_img.get_rect(topleft=(170, 30))

ball_img = image.load("img/elements/ball.png").convert_alpha()
ball_img = transform.scale(ball_img,(320,360))
ball_rect = ball_img.get_rect(topleft=(0, 200))

start_img = image.load("img/ui/start.png").convert_alpha()
start_img = transform.scale(start_img,(240,240))

enemyf_img = image.load("img/enemies/enemyf.png").convert_alpha()
enemyf_img = transform.scale(enemyf_img,(210,310))

enemya_img = image.load("img/enemies/enemya.png").convert_alpha()
enemya_img = transform.scale(enemya_img,(210,210))


chose_img = image.load("img/ui/chose.png").convert_alpha()
chose_img = transform.scale(chose_img,(480,140))

btn_img = image.load("img/ui/voda.png").convert_alpha()
btn_img = transform.scale(btn_img, (220, 140))

sea_img =  image.load("img/backgrounds/sea.png").convert()
sea_img = transform.scale(sea_img, (700, 650))

playersea_img = image.load("img/elements/ball.png").convert_alpha()
playersea_img = transform.scale(playersea_img, (200, 240))
playersea_rect  = playersea_img.get_rect(center=(350, 695))

rock_img = image.load("img/elements/rock.png").convert_alpha()
rock_img = transform.scale(rock_img,(150,70))
rocks = []

btn1_img = image.load("img/ui/fire.png").convert_alpha()
btn1_img = transform.scale(btn1_img,(220,140))