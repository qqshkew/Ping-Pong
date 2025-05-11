from pygame import *
from random import randint
from time import time as timer

font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.SysFont('Arial', 36)

run = True
finish = False
img_back = 'Background.png'
img_ball = 'Ball.png'
img_racket = 'Racket.png'

speed_x = 3
speed_y = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
 
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < win_width - 200:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.y += self.speed

 
class Ball(GameSprite):
    pass


win_width = 700
win_height = 500
display.set_caption("Ping Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
racketl = Player(img_racket, 5, win_height - 100, 80, 100, 10)
racketr = Player(img_racket, 600, win_height - 100, 80, 100, 10)
ball = Ball(img_ball, 300, win_height - 200, 80, 80, 2)

while run:
    run = True

    for e in event.get():
        if e.type == QUIT:
            run = False
            
    if not finish:

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racketl, ball) or sprite.collide_rect(racketr, ball):
                speed_x *= -1

        racketl.update_l()
        racketr.update_r()

        display.update()
        window.blit(background,(0,0))
        racketl.reset()
        racketr.reset()
        ball.reset()
