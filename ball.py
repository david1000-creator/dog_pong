from pygame import*
from game_sprite import*
from const import*


class Ball (GameSprite):
    def __init__(self, img, x, y, size, speed=3):
        super().__init__(img, x, y, size)
        self.speedx = speed
        self.speedy = speed

    def update(self):
        if self.rect.x <= 0 or self.rect.right >= WIN_W:
            self.speedx *= -1
        if self.rect.y <= 0 or self.rect.bottom >= WIN_H:
            self.speedy *= -1

        self.rect.x += self.speedx
        self.rect.y += self.speedy
