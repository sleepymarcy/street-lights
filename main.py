from microbit import *
from lib import set_lights, countdown


def main():
    while True:
        # red light
        set_lights(red=True)
        countdown(5)

        # red and yellow light
        set_lights(red=True, yellow=True)
        sleep(1000)

        # green light
        set_lights(green=True)
        countdown(5)

        # yellow light
        set_lights(yellow=True)
        sleep(3000)


main()
