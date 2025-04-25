from pygame import*
from const import*
from game_sprite import GameSprite


class Player(GameSprite):
    def __init__(self, img, x, y, size, speed=9):
        super().__init__(img, x, y, size)
        self.speed = speed

    def update(self, up, down):
        keys_pressed = key.get_pressed()
        if keys_pressed[up] and self.rect.y > 7:
            self.rect.y -= self.speed
        if keys_pressed[down] and self.rect.y < WIN_H - self.rect.width - 133:
            self.rect.y += self.speed