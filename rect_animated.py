from sense_hat import SenseHat
import time
import random


sense = SenseHat()


O = [0, 0, 0]  # empty
c = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

all = [ [
c, c, O, O, O, O, O, O,
c, c, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
], [
c, c, c, O, O, O, O, O,
c, O, c, O, O, O, O, O,
c, c, c, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
],[
c, c, c, c, c, O, O, O,
c, O, O, O, c, O, O, O,
c, O, O, O, c, O, O, O,
c, O, O, O, c, O, O, O,
c, c, c, c, c, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
], [
c, c, c, c, c, c, O, O,
c, O, O, O, O, c, O, O,
c, O, O, O, O, c, O, O,
c, O, O, O, O, c, O, O,
c, O, O, O, O, c, O, O,
c, c, c, c, c, c, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
] ]

while True:
  for i in range(0,4):
    
    sense.set_pixels(all[i])
    time.sleep(0.3)
    sense.clear(0,0,0)
    
  for i in reversed(range(0,4)):

    sense.set_pixels(all[i])
    time.sleep(0.3)
    sense.clear(0,0,0)