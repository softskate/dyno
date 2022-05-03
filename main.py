from threading import Thread
import time
import pyautogui as pg

pg.FAILSAFE = False
class Evil:
    def __init__(self) -> None:
        self.first_time = time.time()
     
    def run(self):
        Thread(target=self.jump).start()

    def jump(self):
        speed = time.time() - self.first_time
        print(speed)
        time.sleep(speed)
        pg.keyDown('space')
        pg.keyUp('space')


def point_color(delta_x):
    pos = pg.position()
    r, g, b = pg.mouseinfo.getPixel(pos.x + delta_x, pos.y)
    r1, g1, b1 = pg.mouseinfo.getPixel(pos.x + 1 + delta_x, pos.y)
    r2, g2, b2 = pg.mouseinfo.getPixel(pos.x + 2 + delta_x, pos.y)
    mono1 = 0.2125 * r + 0.7154 * g + 0.0721 * b
    mono2 = 0.2125 * r1 + 0.7154 * g1 + 0.0721 * b1
    mono3 = 0.2125 * r2 + 0.7154 * g2 + 0.0721 * b2
    if mono1<200 or mono2<200 or mono3<200:
        return True

    return False


evil = []
while True:
    if pg.getActiveWindowTitle() and pg.getActiveWindowTitle().endswith('Google Chrome'):
        # if point_color(250):
        #     evil.append(Evil())

        if point_color(100):
            # near = evil.pop(-1)
            # near.run()
            pg.keyDown('space')
            pg.keyUp('space')

    else:
        time.sleep(0.1)
