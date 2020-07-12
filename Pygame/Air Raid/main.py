# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:26:49 2020

@author: Rollie
"""

import pygame
import sys
import math
import random
from pygame import mixer

# initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("landscape.jpg")
mixer.music.load("background.wav")
mixer.music.play(-1)
pygame.display.set_caption("Air Raid!")
icon = pygame.image.load("missile.png")
pygame.display.set_icon(icon)
font = pygame.font.Font("animeace2_reg.ttf", 32)
over_font = pygame.font.Font("animeace2_reg.ttf", 64)
textX = 10
textY = 10

# Cannon
playerImg = pygame.image.load("cannon.png")
player_angle = 0
angle_change = 0
bullet_angle = "unknown"

# Bullet
bulletImg = pygame.image.load("circle.png")
bulletX = 400
bulletY = 480
bulletX_change = 0
bulletY_change = 0
bullet_state = "ready"

# Enemy
enemyImg = pygame.image.load("jet.png")
enemy_speed = 2
enemy_bullet_y_change = 4
enemy_bullet_x = 0
enemy_bullet_y = -50
enemy_bullet_state = "ready"


def randomize_enemy():
    enemy_dir = random.choice(["from_left", "from_right"])
    enemy_y = random.randrange(10, 400)
    if enemy_dir == "from_left":
        enemy_x = 0
        enemy_x_change = enemy_speed
    if enemy_dir == "from_right":
        enemy_x = 800
        enemy_x_change = enemy_speed * -1
    return enemy_x, enemy_y, enemy_x_change, enemy_dir


enemy_X, enemy_Y, enemyX_change, enemy_direction = randomize_enemy()


# TODO корректное вращение пушки
# def rot_center(image, angle):
#
#     center = image.get_rect().center
#     rotated_image = pygame.transform.rotate(image, angle)
#     new_rect = rotated_image.get_rect(center = center)
#
#     return rotated_image, new_rect
# https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame/54714144

def player(x: int):
    screen.blit(pygame.transform.rotate(playerImg, x), (370, 480))  # drop on screen


def enemy(x, y, dirn):
    if dirn == "from_left":
        screen.blit(enemyImg, (x, y))
    if dirn == "from_right":
        screen.blit(pygame.transform.flip(enemyImg, True, False), (x, y))


def place_bullet(x: int, y: int):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x - 7, y - 10))


def enemy_bullet(x: int, y: int):
    screen.blit(bulletImg, (x - 7, y - 10))


def bullet_coords(angle):
    # https://usercontent2.hubstatic.com/14421077.jpg
    # math.sin считает в радианах, поэтому сначала переводим градусы по формуле radian = degree * pi / 180
    bullet_speed = 7  # гипотенуза
    math_angle = 90 - abs(angle)  # угол от горизонтали в градусах
    math_angle = math_angle * math.pi / 180  # угол в радианах
    y = math.sin(math_angle) * bullet_speed
    if angle == 0:  # стреляем вверх yolo
        x = 0
    elif angle < 0:  # стреляем вправо
        x = math.cos(math_angle) * bullet_speed
    elif angle > 0:  # стреляем влево
        x = math.cos(math_angle) * bullet_speed * -1
    return x, y


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX + 30 - bulletX, 2)) + (math.pow(enemyY + 30 - bulletY, 2)))
    if distance < 35:
        return True
    else:
        return False


def gameover_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


# Main Loop
running = True
while running:
    screen.fill((0, 0, 0))  # RGB
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        # Quitting
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        # Key Presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle_change = 1
            if event.key == pygame.K_RIGHT:
                angle_change = -1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_angle = player_angle
                    bullet_Sound = mixer.Sound("laser.wav")
                    bullet_Sound.play()
                place_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                angle_change = 0

    # Rotating cannon with limits
    player_angle += angle_change
    if player_angle > 90:
        player_angle = 90
    if player_angle < -90:
        player_angle = -90

    # Bullet keeps moving
    if bullet_state == "fire":
        bulletX_change, bulletY_change = bullet_coords(bullet_angle)
        place_bullet(bulletX, bulletY)
        bulletX += bulletX_change
        bulletY -= bulletY_change

    # Bullet leaves screen and resets
    if bulletY <= 0 or bulletX > 800 or bulletX < 0:
        bulletY = 480
        bulletX = 400
        bullet_state = "ready"

    # enemy keeps moving
    enemy_X += enemyX_change

    # enemy shoots
    if enemy_bullet_state == "ready":
        dice = random.randrange(0, 800)
        if dice > 795:
            bullet_Sound = mixer.Sound("laser.wav")
            bullet_Sound.play()
            enemy_bullet_x = enemy_X + 20
            enemy_bullet_y = enemy_Y + 20
            enemy_bullet_state = "fire"
    if enemy_bullet_state == "fire":
        enemy_bullet_y += enemy_bullet_y_change

    # enemy leaves screen and re-randomizes
    if enemy_X < -64 or enemy_X > 800:
        enemy_X, enemy_Y, enemyX_change, enemy_direction = randomize_enemy()

    # enemy bullet reaches bottom 600 and resets
    if enemy_bullet_y > 600:
        enemy_bullet_y = -50
        enemy_bullet_state = "ready"

    # bullet/target collision
    collision = isCollision(enemy_X, enemy_Y, bulletX, bulletY)
    if collision:
        explosion_Sound = mixer.Sound("explosion.wav")
        explosion_Sound.play()
        bulletX = 400
        bulletY = 480
        bullet_state = "ready"
        enemy_X, enemy_Y, enemyX_change, enemy_direction = randomize_enemy()

    # enemy bullet / cannon collision:
    destroyed = isCollision(370, 480, enemy_bullet_x, enemy_bullet_y)
    if destroyed:
        explosion_Sound = mixer.Sound("explosion.wav")
        explosion_Sound.play()
        pygame.mixer.fadeout(3)
        gameover_text()
        enemy_bullet_y_change = 0
        enemy_X = 0
        enemy_Y = 0

    enemy(enemy_X, enemy_Y, enemy_direction)
    enemy_bullet(enemy_bullet_x, enemy_bullet_y)
    player(player_angle)
    pygame.display.update()
