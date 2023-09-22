import pygame as pg

pg.init() #Starter game
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

#spillvindu
screen = pg.display.set_mode((800, 600)) #lager spillvindu 800x600)
clock = pg.time.Clock()

pos_x = 100
pos_y = 100

i = 0
playing = True
while playing: #game loop
    clock.tick(60)
    print("FPS", i,)
    i += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        pos_y -=5
    if keys[pg.K_s]:
        pos_y +=5
    if keys[pg.K_a]:
        pos_x -=5
    if keys[pg.K_d]:
        pos_x +=5
    screen.fill(YELLOW)
    player_box = pg.Rect((pos_x, pos_y, 100,100)) # to første er posisjon, to siste er size
    pg.draw.rect(screen, RED, player_box)
    if pos_x > 800:
        pos_x = 800
    if pos_y > 800:
        pos_y = 800
        

    pg.display.update()

    
    
