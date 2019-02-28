from sense_hat import SenseHat
import sys
import time

sense = SenseHat()

w = (250, 250, 250)
blank = (0, 0, 0)
r = (250, 0, 0)
fa = (240, 100, 75)
bl = (0, 0, 255)
br = (100, 50, 30)

normalPose = [
    blank, blank, r, r, r, blank, blank, blank,
    blank, r, r, r, r, r, r, blank,
    blank, blank, br, fa, fa, fa, blank, blank,
    blank, blank, fa, fa, br, br, blank, blank,
    blank, r, bl, r, r, bl, r, blank,
    blank, fa, bl, bl, bl, bl, fa, blank,
    blank, blank, bl, bl, bl, bl, blank, blank,
    blank, blank, br, blank, blank, br, blank, blank
    ]

jumpPose = [
    blank, blank, r, r, r, blank, blank, blank,
    blank, r, r, r, r, r, r, blank,
    blank, blank, br, fa, fa, fa, blank, fa,
    blank, blank, fa, fa, br, br, r, blank,
    blank, r, bl, r, r, bl, blank, blank,
    fa, blank, bl, bl, bl, bl, br, blank,
    blank, blank, bl, bl, bl, bl, br, blank,
    blank, br, blank, blank, blank, blank, blank, blank
    ]

def normal ():
    sense.set_pixels(normalPose)

def jump ():
    sense.set_pixels(jumpPose)

while True:
    try:
        normal()
        sense.stick.direction_up = jump
        time.sleep(1)
    except KeyboardInterrupt:
        sense.clear()
        sys.exit()