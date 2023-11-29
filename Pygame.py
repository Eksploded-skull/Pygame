import pygame as pg
from sprites import *

import random
# ha enemies som slår på vegger.
# ha dem prøve å finne en vei inn  
# add health til enemies
# add turrets  
# gjør som at æ kan snu rundt og skyt
# sov i timen
#ha enemy følge etter player, Add hp til enemy, Add waves, add endring i størrelse på skudd om man trykker en knapp
#add flere animations
#wall breakers
pg.init() # starter pygame modul

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

screen = pg.display.set_mode((2560, 1440)) # lager spill vindu, 800x600
clock = pg.time.Clock()

font_cs30 = pg.font.SysFont("Comic Sans", 30)
font_times40 = pg.font.SysFont("Times New Roman", 40)

all_sprites = pg.sprite.Group()
enemies_group = pg.sprite.Group() 
block = pg.sprite.Group()
block = Block(all_sprites, enemies_group, 800, 300)
player = Player(all_sprites, enemies_group)
all_sprites.add(player)






playing = True
while playing: # game loop
    clock.tick(12000)
    #print("FPS: ", i)
    for event in pg.event.get():
        if event.type == pg.QUIT: # hvis vi trykker pÃ¥ krysset i spillvinduet
            playing = False
            pg.quit()
        if event.type == pg.KEYDOWN: 
            if event.key == pg.K_e:
                player = Player(all_sprites)
                all_sprites.add(player)


    if len(enemies_group) < 10000:
        new_enemy = Enemy(all_sprites, enemies_group) #lager 1 kopi av fiende
   
    # oppdater alle sprites i all_sprites gruppen
    all_sprites.update()

    hits = pg.sprite.spritecollide(player, enemies_group, True)
    if hits:
        player.take_dmg(10)
        print("Du tok skade")
   
        


    hp_text = font_times40.render(f"HP:{player.hp}", False, (RED))
    cash_text = font_times40.render(f"Cash:{player.cash}", False, ((RED)))

 
    # tegn bakgrunn og alle sprites
    screen.fill(YELLOW)
    all_sprites.draw(screen)

    screen.blit(hp_text, (10,10))
    screen.blit(cash_text, (10,50))

    pg.display.update()
    