from microbit import *
from lib import set_lights, countdown, warning, default


def main():
    is_ledmatrix_active = True
    is_default = False

    while True:
        if button_a.was_pressed():
            is_default = not is_default
        if button_b.was_pressed():
            is_ledmatrix_active = not is_ledmatrix_active

        if is_default:
            default(is_ledmatrix_active)
        else:
            warning(is_ledmatrix_active)


main()
