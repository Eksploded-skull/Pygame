import pygame as pg
import random

STANDING1 = pg.image.load("images/STANDING1.png")
STANDING1 = pg.transform.scale(STANDING1, (30,30))
STANDING2 = pg.image.load("images/STANDING2.png")
STANDING2 = pg.transform.scale(STANDING2, (30,30))
STANDING3 = pg.image.load("images/STANDING3.png")
STANDING3 = pg.transform.scale(STANDING3, (30,30))



#from Pygame import enemies_group



player_image = pg.image.load("images/player.png")
player_image = pg.transform.scale(player_image, (30,30))
enemy_image = pg.image.load("images/enemy.png")
enemy_image = pg.transform.scale(enemy_image, (30,30))

ranged_image = pg.image.load("images/ranged_img.png")
ranged_image = pg.transform.scale(ranged_image, (30,30))
Block_image = pg.image.load("images/Block.png")
Block_image = pg.transform.scale(Block_image, (30,30))


class Enemy(pg.sprite.Sprite):
    def __init__(self, all_sprites, enemies_group): # denne funksjonen kjører når vi lager enemy
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image 
        self.rect = self.image.get_rect()#at hitboxen til Enemy er imaget
        self.pos_x = 2560
        self.pos_y = random.randint(0,1440)
        self.speed = random.randint(1,10)
        self.all_sprites = all_sprites
        self.enemies_group = enemies_group

        self.all_sprites.add(self)
        self.enemies_group.add(self)

        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        enemy_hp = 100
        
    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        self.pos_x -= self.speed

        if self.pos_x < 0:
            self.kill()
        
class Block(pg.sprite.Sprite):
    def __init__(self, all_sprites, enemies_group, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = Block_image
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        self.pos_x = x
        self.pos_y = y
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.enemies_group = enemies_group
        all_sprites.add(self)
        self.hp = 100
    
    def take_dmg(self, dmg):
        self.hp-= dmg
        if self.hp  <= 0:
            self.kill()

    
    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        hits = pg.sprite.spritecollide(self, self.enemies_group, False)
        if hits:
            self.take_dmg(10)
            for enemy in hits:
                pass





class Player(pg.sprite.Sprite):
    def __init__(self, all_sprites, enemies_group): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.current_frame = 0
        self.last_update = 0

        self.standing = True
        self.running = False
        self.jumping = False
        
        self.standing_frames = [STANDING1, STANDING2, STANDING3]
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = 300
        self.pos_y = 500
        self.speed = 5
        self.hp = 100
        self.all_sprites = all_sprites
        self.enemies_group = enemies_group



    def take_dmg(self, dmg):
        self.hp-=dmg
        if self.hp  <= 0:
            self.kill()

    def attack(self):
        projectile = Ranged_attack(self.pos_x,self.pos_y, self.enemies_group)
        print("attacked")
        self.all_sprites.add(projectile)

    def place_block(self):
        block_projectile = Block(self.all_sprites, self.enemies_group, self.pos_x,self.pos_y)
        print("plasserte block")
        self.all_sprites.add(block_projectile)
    
    def update(self):
        self.animate()
    
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

        self.standing = True
      
    def animate(self):
        now = pg.time.get_ticks()

        if self.standing:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1)% len(self.standing_frames)
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()



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

        if keys[pg.K_SPACE]:
            self.attack()
            print("You attacked")
        
        if keys[pg.K_y]:
            for sprite in (self.enemies_group):
                sprite.kill()
        
        elif keys[pg.K_f]:
            self.place_block()
            print("Du plasserte en block")
        
    








class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, x, y, enemies_group) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image = ranged_image
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        self.pos_x = x
        self.pos_y = y
        self.speed = 10
        self.enemies_group = enemies_group
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        

        self.pos_x += self.speed
        hits = pg.sprite.spritecollide(self, self.enemies_group, True)
        if self.pos_x > 3000:
            self.kill()
    
        

 