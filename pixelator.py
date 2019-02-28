from sense_hat import SenseHat
import time
import random

sense = SenseHat()


for i in range(0,8):
  for n in range(0,8):
    c = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    sense.set_pixel(n,i,c)
    time.sleep(0.1)
    sense.clear(0,0,0)
    
