from random import randint
from sense_hat import SenseHat
import sys

sense = SenseHat()
text = 'Hello! We are New Media Development:)'

while True:
    try:
        sense.show_message(text, back_colour = [randint(15, 90), randint(15, 90), randint(15, 90)], text_colour = [randint(200, 255), randint(200, 255), randint(200, 255)])
    except KeyboardInterrupt:
        sense.clear()
        sys.exit()
        