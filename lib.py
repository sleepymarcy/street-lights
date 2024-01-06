from microbit import *

lights = {
    "R": "OFF",
    "Y": "OFF",
    "G": "OFF",
}


def toggle_light(color: str) -> None:
    if lights[color] == "ON":
        lights[color] = "OFF"
    else:
        lights[color] = "ON"


def update_display():
    if lights.get("R") == "ON":
        display.set_pixel(4, 0, 9)
        pin2.write_digital(1)
    else:
        display.set_pixel(4, 0, 0)
        pin2.write_digital(0)

    if lights.get("Y") == "ON":
        display.set_pixel(4, 2, 9)
        pin1.write_digital(1)
    else:
        display.set_pixel(4, 2, 0)
        pin1.write_digital(0)

    if lights.get("G") == "ON":
        display.set_pixel(4, 4, 9)
        pin0.write_digital(1)
    else:
        display.set_pixel(4, 4, 0)
        pin0.write_digital(0)


def handle_input():
    if button_a.was_pressed():
        lights["R"] = toggle_light(lights["R"])
    elif button_b.was_pressed():
        lights["G"] = toggle_light(lights["G"])
    elif pin_logo.is_touched():
        lights["Y"] = toggle_light(lights["Y"])
        sleep(200)
