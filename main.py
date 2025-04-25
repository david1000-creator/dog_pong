from pygame import *
from const import*
from game_sprite import GameSprite
from player import Player
from ball import*


# вынесем размер окна в константы для удобства
# W - width, ширина
# H - height, высота
dog_left = Player(DOGLEFT_IMG, 5, (WIN_H - DOG_H) / 2, (DOG_W, DOG_H))
dog_right = Player(DOGRIGHT_IMG, WIN_W - DOG_W - 5, (WIN_H - DOG_H) / 2, (DOG_W, DOG_H))

# создание окна размером 700 на 500
window = display.set_mode((WIN_W, WIN_H))
# создание таймера
clock = time.Clock()
mixer.init()
# mixer.music.load('src/crunch.mp3')
# mixer.music.play(-1)
# mixer.music.set_volume(0.5)

crunch = mixer.Sound('src/crunch.mp3')

font.init()
title_font = font.SysFont('comic sans', 41)
lost_left = title_font.render('Левый пёс потерял пельмень, Лошара', True, RED)
lost_right = title_font.render('Правый пёс потерял пельмень, Лошара', True, RED)

label_font = font.SysFont('comic sans', 29)
count_txt = label_font.render('Счёт:', True, WHITE)


# название окна
display.set_caption("dog_pong")

# задать картинку фона такого же размера, как размер окна
background = GameSprite(BG_IMG, 0, 0,  (WIN_W, WIN_H))
dumpling = Ball(DUMPLING_IMG, (WIN_W - DUMPLING_W) / 2, (WIN_H - DUMPLING_H) / 2, (DUMPLING_W, DUMPLING_H))

left_lost = 0
right_lost = 0
# игровой цикл
game = True
finish = False
while game:
    if not finish:

        background.draw(window)
        points = label_font.render(f'{left_lost}:{right_lost}', True, WHITE)
        window.blit(count_txt, (21,41))
        window.blit(points, (101, 41))

        dog_left.draw(window)
        dog_right.draw(window)
        dumpling.draw(window)
        dog_left.update(K_w, K_s)
        dog_right.update(K_UP, K_DOWN)
        dumpling.update()
        count_txt

        if sprite.collide_rect(dumpling, dog_right) or sprite.collide_rect(dumpling, dog_left):
            dumpling.speedx *= -1
            crunch.play()

        if dumpling.rect.x >= WIN_W - DUMPLING_W:
            left_lost += 1
            dumpling.rect.x = (WIN_W - DUMPLING_W) / 2
            dumpling.rect.y = (WIN_H - DUMPLING_H) / 2

        if dumpling.rect.x <= 0:
            right_lost += 1
            dumpling.rect.x = (WIN_W - DUMPLING_W) / 2
            dumpling.rect.y = (WIN_H - DUMPLING_H) / 2

        if right_lost >= WIN_SCORE:
            window.blit(lost_right, (100, 201))
            display.update()
            finish = True

        if left_lost >= WIN_SCORE:
            window.blit(lost_left, (100, 201))
            display.update()
            finish = True
    else:
        time.delay(2500)
        left_lost = 0
        right_lost = 0
        dumpling = Ball(DUMPLING_IMG, (WIN_W - DUMPLING_W) / 2, (WIN_H - DUMPLING_H) / 2, (DUMPLING_W, DUMPLING_H))
        dog_left = Player(DOGLEFT_IMG, 5, (WIN_H - DOG_H) / 2, (DOG_W, DOG_H))
        dog_right = Player(DOGRIGHT_IMG, WIN_W - DOG_W - 5, (WIN_H - DOG_H) / 2, (DOG_W, DOG_H))
        finish = False
    # слушать события и обрабатывать
    for e in event.get():
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    display.update()
    clock.tick(FPS)