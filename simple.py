import time
import pyautogui as pg


def point_color(delta_x):
    pos = pg.position()
    rb, gb, bb = pg.mouseinfo.getPixel(pos.x + 50, pos.y + 50)
    monob = 0.2125 * rb + 0.7154 * gb + 0.0721 * bb

    for point in range(4):
        r, g, b = pg.mouseinfo.getPixel(pos.x + point + delta_x, pos.y)
        mono = 0.2125 * r + 0.7154 * g + 0.0721 * b

        if monob > 150:
            if mono<200:
                return True
        else:
            if mono>50:
                return True

        return False


evil = []
while True:
    active = pg.getActiveWindowTitle()
    if active and active.endswith('Google Chrome'):
        if point_color(100):
            pg.keyDown('space')
            pg.keyUp('space')

    else:
        time.sleep(0.1)
