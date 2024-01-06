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


def countdown(seconds: int) -> None:
    for i in range(seconds, 0, -1):
        display.show(i)
        sleep(1000)
    display.clear()
