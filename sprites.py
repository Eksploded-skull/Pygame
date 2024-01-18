import pygame as pg
import random
from pygame import mixer

pg.init()


STANDING1 = pg.image.load("images/STANDING1.png")
STANDING1 = pg.transform.scale(STANDING1, (30,30))
STANDING2 = pg.image.load("images/STANDING2.png")
STANDING2 = pg.transform.scale(STANDING2, (30,30))
STANDING3 = pg.image.load("images/STANDING3.png")
STANDING3 = pg.transform.scale(STANDING3, (30,30))
Shooting1 = pg.image.load("images/Shooting1.png")
Shooting2 = pg.image.load("images\Shooting2.png")
Shooting3 = pg.image.load("images\Shooting3.png")



#from Pygame import enemies_group



player_image = pg.image.load("images/player.png")
player_image = pg.transform.scale(player_image, (30,30))
enemy_image = pg.image.load("images/enemy.png")
enemy_image = pg.transform.scale(enemy_image, (30,30))

ranged_image = pg.image.load("images/ranged_img.png")
ranged_image = pg.transform.scale(ranged_image, (50,50))
Block_image = pg.image.load("images/Block.png")
Block_image = pg.transform.scale(Block_image, (30,30))

small_attack_sound = pg.mixer.Sound("sound_effects/shooting.mp3")
small_attack_sound.set_volume(5)


class Enemy(pg.sprite.Sprite):
    def __init__(self, all_sprites, enemies_group,   ): # denne funksjonen kjører når vi lager enemy
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image 
        self.rect = self.image.get_rect()#at hitboxen til Enemy er imaget
        
        self.all_sprites = all_sprites
        self.enemies_group = enemies_group

        self.speed = random.randint(1,10)
        self.direction = random.choice(["left","right", "up", "down"])
        print(self.direction)
        #self.block = block



        if self.direction == "left":
            self.pos_x = 0
            self.pos_y = random.randint(0,1440)
            self.pos_x += self.speed
        else:
                self.pos_x = 2560
                self.pos_y = random.randint(0,1440)
            


        self.all_sprites.add(self)
        self.enemies_group.add(self)

        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        #self.enemy_hp = enemy_hp
        #enemy_hp = 100


        
        
    def update(self):

        #self.enemy_hp = 100
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        if self.direction == "left":
            self.pos_x += self.speed
        self.pos_x -= self.speed
        #hits = pg.sprite.spritecollide(self, self.enemies_group, self.block, False)
        #if hits:
        #    self.enemy_hp -= 10
        #    self.speed == 0

        if self.pos_x < -100:
            self.kill()
       # if self.enemy_hp <= 0:
        #    self.kill()
        
    

        


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
            self.kill()





class Player(pg.sprite.Sprite):
    def __init__(self, all_sprites, enemies_group): # denne funksjonen kjører når vi lager player
        pg.sprite.Sprite.__init__(self)
        self.current_frame = 0
        self.last_update = 0

        self.last_attack = 0
        self.attack_interval = 500

        self.standing = True
        self.running = False
        self.jumping = False
        self.shooting = False
        
        self.standing_frames = [STANDING1, STANDING2, STANDING3]
        self.shooting_frames = [Shooting1, Shooting2, Shooting3]
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = 300
        self.pos_y = 500
        self.speed = 5
        self.hp = 100
        self.all_sprites = all_sprites
        self.enemies_group = enemies_group
        self.cash = 0


    def take_dmg(self, dmg):
        self.hp-=dmg
        if self.hp  <= 0:
            self.kill()

    def attack(self):
        now = pg.time.get_ticks()
        if now - self.last_attack > self.attack_interval:
            self.standing = False
            self.shooting = True
            self.last_attack = now
            print("attacked")
            projectile = Ranged_attack(self.pos_x,self.pos_y, self.enemies_group, self)
            self.all_sprites.add(projectile)
            pg.mixer.Sound.play(small_attack_sound)





    def place_block(self):
        if self.cash > 100:
            self.cash -= 100
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
            if self.cash > 100:
                self.cash -=100
                for sprite in (self.enemies_group):
                    sprite.kill()
        
        elif keys[pg.K_f]:
            self.place_block()
            print("Du plasserte en block")
        
    





class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, x, y, enemies_group, player, speed_x=0, speed_y=0) -> None:
        
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
        self.player = player 
        
        self.hit_enemy = False
        self.hp = 2
        projectile_hp = 99
        self.projectile_hp = projectile_hp

    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y - 15
        
        self.player
        self.pos_x += self.speed
        hits = pg.sprite.spritecollide(self, self.enemies_group, True)

        if hits:
            self.player.cash += 1
            print("Du har", self.player.cash, "cash")
            self.hit_enemy = True
            self.projectile_hp -= 33
        if self.pos_x > 3000:
            self.kill()
        if self.projectile_hp <= 0:
            self.kill()
