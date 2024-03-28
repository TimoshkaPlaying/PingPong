import pygame
import random
import sys

scores_l = 0
scores_r = 0
window = pygame.display.set_mode((700, 500))
fps = 120
clock = pygame.time.Clock()

top_border = 65
bottom_border = 391

bg = pygame.image.load('fon.png')
bg = pygame.transform.scale(bg, (700, 500))

window.blit(bg, (0,0))

pygame.font.init()
font1 = pygame.font.SysFont('Ariel',36)


#Clases________________________________________
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, width, height):
        super().__init__()
        self.speed = speed
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.x, self.rect.y = x, y

    def reset(self):
        pygame.draw.rect(window, (0,0,0), self.rect)


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        super().__init__()
        self.img = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = x, y

    def reset(self):
        window.blit(self.img, (self.rect.x, self.rect.y))


class Hero(GameSprite):
    def update_l(self):
        # Движение перса левого
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and self.rect.y > top_border:
            self.rect.y -= self.speed
        elif keys_pressed[pygame.K_s] and (self.rect.y + 40) < bottom_border:
            self.rect.y += self.speed

    def update_r(self):
        # Движение перса правого
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] and self.rect.y > top_border:
            self.rect.y -= self.speed
        elif keys_pressed[pygame.K_DOWN] and (self.rect.y + 40) < bottom_border:
            self.rect.y += self.speed

#_________________________________________________________________________

ball = Ball(315, 230, 75, 50, 'ball.png')

rocket1 = Hero(50, 260, 3,15,100)
rocket2 = Hero(650, 150, 3,15,100)

ball_update = True

time = 50
time_border = 50

speed_x = random.choice([-3, 3])
speed_y = -3

game = True
while game:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()

    window.blit(bg, (0, 0))

    rocket1.reset()
    rocket1.update_l()

    rocket2.reset()
    rocket2.update_r()

    if ball_update:
        ball.reset()

        #ball update ____________________________________________________
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if pygame.sprite.collide_rect(ball, rocket1) and time >= 50 or pygame.sprite.collide_rect(ball, rocket2) and time >= 50:
            time = 0
            speed_x *= -1
            if speed_x > 0:
                speed_x += 0.1
            else:
                speed_x -= 0.1
            if speed_y > 0:
                speed_y += 0.1
            else:
                speed_y -= 0.1
        if ball.rect.y <= top_border and time_border >= 50 or ball.rect.y >= bottom_border and time_border >= 50:
            time_border = 0
            speed_y *= -1
        if ball.rect.x <= 0:
            scores_r += 1
            ball.rect.x = 315
            ball.rect.y = 230
            speed_x = random.choice([-3, 3])
            speed_y = -3
        elif ball.rect.x >= 700:
            scores_l += 1
            ball.rect.x = 315
            ball.rect.y = 230
            speed_x = random.choice([-3, 3])
            speed_y = -3
        #________________________________________________________________

    text_scores = font1.render('Счет - ' + str(scores_l)+' : ' + str(scores_r), 1, (0, 0, 0))
    window.blit(text_scores, (100, 25))

    if scores_l >= 10:
        ball_update = False
        text_win = font1.render('Выиграл Игрок WASD',3, (255, 255, 255))
        window.blit(text_win, (200, 230))
    elif scores_r >= 10:
        ball_update = False
        text_win = font1.render('Выиграл Игрок Стрелочка', 3, (255, 255, 255))
        window.blit(text_win, (165, 230))

    pygame.display.update()
    clock.tick(fps)

    time += 1
    time_border += 1