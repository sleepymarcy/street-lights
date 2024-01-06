from microbit import *

lights = {
    "R": False,
    "Y": False,
    "G": False,
}


def set_lights(red: bool = False, yellow: bool = False, green: bool = False) -> None:
    if red:
        lights['R'] = True
    else:
        lights['R'] = False

    if yellow:
        lights['Y'] = True
    else:
        lights['Y'] = False

    if green:
        lights['G'] = True
    else:
        lights['G'] = False

    update_display()


def update_display():
    if lights['R']:
        # display.set_pixel(4, 0, 9)
        pin2.write_digital(1)
    else:
        # display.set_pixel(4, 0, 0)
        pin2.write_digital(0)

    if lights['Y']:
        # display.set_pixel(4, 2, 9)
        pin1.write_digital(1)
    else:
        # display.set_pixel(4, 2, 0)
        pin1.write_digital(0)

    if lights['G']:
        # display.set_pixel(4, 4, 9)
        pin0.write_digital(1)
    else:
        # display.set_pixel(4, 4, 0)
        pin0.write_digital(0)


def countdown(seconds: int) -> None:
    for i in range(seconds, 0, -1):
        display.show(i)
        sleep(1000)
    display.clear()
