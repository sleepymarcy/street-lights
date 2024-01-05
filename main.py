from microbit import *


def main():
    while True:
        handle_input()
        update_display()


def update_display():
    if signal_state.get("R") == "ON":
        display.set_pixel(4, 0, 9)
    else:
        display.set_pixel(4, 0, 0)

    if signal_state.get("Y") == "ON":
        display.set_pixel(4, 2, 9)
    else:
        display.set_pixel(4, 2, 0)

    if signal_state.get("G") == "ON":
        display.set_pixel(4, 4, 9)
    else:
        display.set_pixel(4, 4, 0)


def handle_input():
    if button_a.was_pressed():
        signal_state["R"] = toggle_light(signal_state["R"])
    elif button_b.was_pressed():
        signal_state["G"] = toggle_light(signal_state["G"])
    elif pin_logo.is_touched():
        signal_state["Y"] = toggle_light(signal_state["Y"])
        sleep(200)


def toggle_light(light):
    if light == "ON":
        light = "OFF"
    else:
        light = "ON"
    return light


signal_state = {
    "R": "OFF",
    "Y": "OFF",
    "G": "OFF",
}


main()

# mamy 4 opcje sygnalizacji świateł
# 1. za pomocą literek na display'u
# 2. za pomocą pojedyńczych ledów na display'u
# 3. za pomocą ustawionych wcześniej obrazków
#    (tablica która określa które ledy mają świecić i w jakim natężeniu)
# 4. na płytce stykowej używając ledów
