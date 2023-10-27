import pygame as pg
from sprites import *
import random
pg.init() # starter pygame modul

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

screen = pg.display.set_mode((800,600)) # lager spill vindu, 800x600
clock = pg.time.Clock()

player = Player() # lager 1 kopi av Player class
player2 = Player()
player3 = Player()

all_sprites = pg.sprite.Group()
all_sprites.add(player) # legg til player i gruppen
all_sprites.add(player2) # legg til player i gruppen
all_sprites.add(player3) # legg til player i gruppen


playing = True
while playing: # game loop
    clock.tick(120)
    #print("FPS: ", i)
    for event in pg.event.get():
        if event.type == pg.QUIT: # hvis vi trykker pÃ¥ krysset i spillvinduet
            playing = False
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_e:
                new_player = Player()
                all_sprites.add(new_player)
    # spawning av flere players
    if len(all_sprites) < 100:
        new_player = Player()
        all_sprites.add(new_player)
    if len(all_sprites) < 1:
        new_kreft = kreft()
        all_sprites.add(kreft)

   
    

    # oppdater alle sprites i all_sprites gruppen
    all_sprites.update()

    # tegn bakgrunn og alle sprites
    screen.fill(YELLOW)
    all_sprites.draw(screen)

    pg.display.update()