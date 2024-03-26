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

class Hero(GameSprite):
    def update_l(self):
        # Движение перса левого
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and self.rect.y > top_border:
            self.rect.y -= self.speed
        elif keys_pressed[pygame.K_s] and self.rect.y < bottom_border:
            self.rect.y += self.speed

    def update_r(self):
        # Движение перса правого
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] and self.rect.y > top_border:
            self.rect.y -= self.speed
        elif keys_pressed[pygame.K_DOWN] and self.rect.y < bottom_border:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global scores
        if self.rect.y > -10:
            self.rect.y -= self.speed
        else:
            self.kill()

#_________________________________________________________________________

rocket1 = Hero(50, 350, 3,15,60)
rocket2 = Hero(650, 150, 3,15,60)

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


    text_scores = font1.render('Счет - ' + str(scores_r)+' : ' + str(scores_l), 1, (0, 0, 0))
    window.blit(text_scores, (100, 25))

    pygame.display.update()
    clock.tick(fps)