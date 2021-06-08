import pygame as pg
import numpy as np
from math import *
import Logic
import time
from numba import jit

display = (800, 600)
angles = (4 * pi / 9, pi / 3)
player_x, player_y, player_z = 0, 0, -.6

@jit
def draw(xp, yp, zp, dx, dy):
    array = np.zeros((dx, dy, 3), np.int32)
    length = dx / 2 * sqrt(3)
    for y in range(dy):
        for x in range(dx):
            hit = Logic.Ray(xp, yp, zp, atan((x - dx / 2) / length), atan((y - dy / 2) / length), 0, 0)
            array[x, y] = (hit, hit, hit)

    return array

def main():
    global player_x, player_y, player_z
    pg.init()
    screen = pg.display.set_mode(display)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        tik = time.time()
        screen.blit(pg.surfarray.make_surface(draw(player_x, player_y, player_z, display[0], display[1])), (0, 0))
        # player_x -= .01
        # print(time.time() - tik)
        pg.display.flip()


main()
