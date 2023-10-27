import pygame as pg
import random

player_image = pg.image.load("images/player.png")
enemy_image = pg.image.load("images/enemy.png")

class Player(pg.sprite.Sprite):
    def __init__(self): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = 50
        self.pos_y = 400
        self.speed = 5

    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

        if self.pos_x > 900:
            self.kill()

        # player input
        keys = pg.key.get_pressed()
        if keys[pg.K_w]: # oppover
            self.pos_y -= self.speed
        if keys[pg.K_s]: # nedover
            self.pos_y += self.speed
        if keys[pg.K_a]: # venstre
            self.pos_x -= self.speed
        if keys[pg.K_d]: # høyre
            self.pos_x += self.speed 

    

class Enemy(pg.sprite.Sprite):
    def __init__(self): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = 900
        self.pos_y = random.randint(0,600)
        self.speed = random.randint(1,10)

    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y