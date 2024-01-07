from microbit import *

lights = {
    "R": False,
    "Y": False,
    "G": False,
}


def set_lights(red: bool = False, yellow: bool = False, green: bool = False) -> None:
    lights['R'] = red
    lights['Y'] = yellow
    lights['G'] = green
    update_display()


# in python:
#    True equals 1
#    False equals 0
def update_display() -> None:
    pin2.write_digital(lights['R'])
    pin1.write_digital(lights['Y'])
    pin0.write_digital(lights['G'])


def countdown(seconds: int, show: bool = False) -> None:
    if show:
        for i in range(seconds, 0, -1):
            display.show(i)
            sleep(1000)
        display.clear()
    else:
        sleep(seconds*1000)


def warning(matrix_active: bool = True) -> None:
    set_lights()
    if matrix_active:
        show_exclamation_mark()
    countdown(1)

    set_lights(yellow=True)
    if matrix_active:
        display.clear()
    countdown(1)


def default(matrix_active: bool = True) -> None:
    # red light
    set_lights(red=True)
    countdown(5, show=matrix_active)

    # red and yellow light
    set_lights(red=True, yellow=True)
    countdown(1)

    # green light
    set_lights(green=True)
    countdown(5, show=matrix_active)

    # yellow light
    set_lights(yellow=True)
    countdown(3)


def show_exclamation_mark() -> None:
    display.set_pixel(2, 0, 9)
    display.set_pixel(2, 1, 9)
    display.set_pixel(2, 2, 9)
    display.set_pixel(2, 4, 9)
